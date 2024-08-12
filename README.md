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
    * Input OpenAI API key and slack user token
    * upload pdf file
    * enter one or multiple questions and post the results on slack

## Sample Output
1. App output:<img width="1266" alt="Screenshot 2024-08-13 at 12 02 51 AM" src="https://github.com/user-attachments/assets/76ca6850-2e00-4e0a-9a07-c26cac90d9c9">
   Slack output: ![Screenshot 2024-08-13 at 12 03 19 AM](https://github.com/user-attachments/assets/9cb74724-c4d7-4809-94e2-9a699ad7dae2)
2. App Output:  <img width="1272" alt="Screenshot 2024-08-13 at 12 06 35 AM" src="https://github.com/user-attachments/assets/a4e00410-639e-4e40-a120-75969c4f6c35">
   Slack Output: ![Screenshot 2024-08-13 at 12 06 13 AM](https://github.com/user-attachments/assets/4d3243dd-7810-4bc3-96e9-dc7afd7a9dbd)
