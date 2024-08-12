# Agentic-RAG
## An AI agent that leverages the capabilities of a large language model using Langchain. This agent extracts answers based on the content of a large PDF document and post the results on Slack using OpenAI LLMs

The code has been organized as:
1. Coding_test.ipynb: Development script to test the framework and all its components.
2. app.py: Contains code for deployment in Streamlit App
3. requirement.txt: contains all the libraries required to be installed before running any script.
* Code was developed using python 3.12.2

## How to run:
1. pip install -r requirements.txt to install all the libraries
2. git clone the repository
3. Run the command: streamlit run main.py
4. This will open the UI:
    * Input OpenAI API key
    * upload pdf file
    * enter one or multiple questions and post the results on slack

## Sample Output
1. App Result: <img width="1249" alt="Screenshot 2024-08-12 at 11 32 29 PM" src="https://github.com/user-attachments/assets/628cd993-f6f1-4b91-878a-bcac1a8b2472">
Slack Result: ![Screenshot 2024-08-12 at 11 33 56 PM](https://github.com/user-attachments/assets/92aa0c9e-d2a0-41d1-9ad3-f0cf1fb1cc81)
2. App Result: <img width="1227" alt="Screenshot 2024-08-12 at 11 41 17 PM" src="https://github.com/user-attachments/assets/0e3625f1-bf21-4240-a172-182ca7be653d">
Slack Result: ![Screenshot 2024-08-12 at 11 41 41 PM](https://github.com/user-attachments/assets/3a14c45f-9af8-4a22-a8a5-d82ebe2f8961)
