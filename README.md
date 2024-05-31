

# Natural Language Data Analysis Tool

This Streamlit application allows users to upload CSV files and use natural language to query and analyze their data. It leverages the Gemini Pro API to translate natural language queries into SQL commands, enabling users to interact with their data without needing to write SQL queries directly.

NOTE: This application is not complete as it has bugs that needs to be resolved.

## Prerequisites

Before you run this application, ensure you have the following:
- Python 3.11 or higher
- Streamlit
- Pandas
- SQLite3
- dotenv
- Google GenerativeAI Python SDK

## Installation

1. **Clone the Repository**

   Begin by cloning the repository to your local machine:


2. **Set Up a Virtual Environment**

   Using a virtual environment is recommended to manage dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install all the necessary Python packages:

   ```bash
   pip install streamlit pandas sqlite3 python-dotenv google-generativeai
   ```

4. **Environment Variables**

   Create a `.env` file in the root of your project directory:

   ```plaintext
   GOOGLE_API_KEY='your_gemini_pro_api_key_here'
   ```

   Replace `'your_gemini_pro_api_key_here'` with your actual Gemini Pro API key.

## Running the Application

To run the application, use Streamlit:

```bash
streamlit run app.py
```

## How to Use

1. **Upload a CSV File**: Use the file uploader to select and upload a CSV file containing your data.
2. **Enter Metadata**: Input metadata for the CSV columns in the provided text area. This metadata should describe the column names and types or any other relevant information that will help in generating accurate SQL schemas.
3. **Ask Questions**: Enter natural language queries about your data in the provided input field. The application uses the Gemini Pro API to translate these queries into SQL commands and execute them to retrieve and display answers directly from your data.

## Troubleshooting

- Ensure your API key is correct.
- Verify that your CSV files are formatted correctly and match the metadata you provide.
- If you encounter dependency issues, make sure all packages are installed correctly, and consider checking their documentation for any additional setup requirements.
