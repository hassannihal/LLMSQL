from dotenv import load_dotenv
import os
import sqlite3
import pandas as pd
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Gemini Pro API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def clean_sql(sql):
    """Remove markdown code block syntax and extra spaces from SQL statement."""
    return sql.replace('```sql', '').replace('```', '').strip()

def get_gemini_response(metadata, sample_data):
    """Generate response from Gemini model with structured prompt for schema and transformations."""
    model = genai.GenerativeModel('gemini-pro')
    prompt = (f"Given the metadata: {metadata} and sample data:\n{sample_data}\n"
              "Please provide the SQL schema under the header 'schema' followed by any necessary data transformations "
              "under the header 'transformations'. Also, please do not include any comments from your side.")
    response = model.generate_content([prompt])
    return response.text


def parse_response(response_text):
    """Parse the response to extract SQL schema and transformation commands from structured sections."""
    try:
        schema_index = response_text.index("schema:") + 7
        transformations_index = response_text.index("transformations:") + 16
    except ValueError as e:
        st.error(f"Required section not found in the response: {e}")
        return None, None

    schema_sql = response_text[schema_index:transformations_index].strip()
    transformations = response_text[transformations_index:].strip()

    # Further cleaning if necessary
    schema_sql = clean_sql(schema_sql.split('```sql')[1].split('```')[0].strip())
    transformations = clean_sql(transformations.split('```sql')[1].split('```')[0].strip())

    return schema_sql, transformations

def apply_schema_and_transformations(df, db_file, schema_sql, transformations, table_name):
    """Apply schema creation and data transformations to the database."""
    try:
        conn = sqlite3.connect(db_file)
        execute_sql_commands(conn, schema_sql)  # Create schema
        execute_sql_commands(conn, transformations)  # Apply transformations
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Error in database operation: {e}")
    finally:
        conn.close()

def execute_sql_commands(conn, sql_commands):
    """Execute given SQL commands."""
    cursor = conn.cursor()
    for command in sql_commands.split(';'):
        if command.strip():
            cursor.execute(command)

def csv_to_df(uploaded_file):
    """Convert uploaded CSV file to DataFrame."""
    return pd.read_csv(uploaded_file)

# Streamlit UI setup
st.set_page_config(page_title="Data Schema and Transformation Generator")
st.header("Upload your data and define metadata for schema generation")
uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])
metadata = st.text_area("Enter metadata for the CSV columns:", height=300)
db_file = 'database.db'
table_name = 'data'

if st.button("Generate Schema and Transform Data") and uploaded_file and metadata:
    df = csv_to_df(uploaded_file)
    response_text = get_gemini_response(metadata, df.head(2).to_string(index=False))
    schema_sql, transformations = parse_response(response_text)
    if schema_sql and transformations:
        apply_schema_and_transformations(df, db_file, schema_sql, transformations, table_name)
        st.success("Schema generated and data transformed successfully!")
    else:
        st.error("Failed to generate or parse SQL commands.")
