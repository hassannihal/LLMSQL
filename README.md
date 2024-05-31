# LLMSQL
Utilize LLM to interact with SQL data


Natural Language Data Analysis Tool
This Streamlit application allows users to upload CSV files and use natural language to query and analyze their data. It leverages the Gemini Pro API to translate natural language queries into SQL commands, enabling users to interact with their data without needing to write SQL queries directly.

Prerequisites
Before you run this application, ensure you have the following:

Python 3.6 or higher
Streamlit
Pandas
SQLite3
dotenv
Google GenerativeAI Python SDK
Installation
Clone the Repository

Begin by cloning the repository to your local machine:

bash
Copy code
git clone https://your-repository-url
cd your-repository-directory
Set Up a Virtual Environment

Using a virtual environment is recommended to manage dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies

Install all the necessary Python packages:

bash
Copy code
pip install streamlit pandas sqlite3 python-dotenv google-generativeai
Note: The actual command to install google-generativeai might differ based on how it's made available. Ensure you have the correct package name or installation method from the API provider.

Environment Variables

Create a .env file in the root of your project directory:

plaintext
Copy code
GOOGLE_API_KEY='your_gemini_pro_api_key_here'
Replace 'your_gemini_pro_api_key_here' with your actual Gemini Pro API key.

Running the Application
To run the application, use Streamlit:

bash
Copy code
streamlit run app.py
Navigate to http://localhost:8501 in your web browser to see the application in action.

How to Use
Upload a CSV File: Use the file uploader to select and upload a CSV file containing your data.
Enter Metadata: Input metadata for the CSV columns in the provided text area. This metadata should describe the column names and types or any other relevant information that will help in generating accurate SQL schemas.
Ask Questions: Enter natural language queries about your data in the provided input field. The application uses the Gemini Pro API to translate these queries into SQL commands and execute them to retrieve and display answers directly from your data.
