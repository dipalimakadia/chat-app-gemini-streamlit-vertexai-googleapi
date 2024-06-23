# chat-app-streamlit-vertexai-gemini-googleapi

## Overview

This app initializes chat history, displays previous messages, manages initial startup messages, captures user input, and processes responses from the generative model.

This README provides detailed instructions on how the project is built, installing dependencies, configuring API keys, troubleshooting common errors, and adding custom code snippets to enhance the functionality.

## Installation

### Prerequisites

Following technologies are used while making this project:

- Python 3.6+
- Google Cloud SDK
- Google Cloud account
- streamlit
- google-cloud-aiplatform
- vertexai
- LLM
- Gemini

### Step-by-Step Project Guide

#### Task 1: Install GCD SDK

Begin by installing the Google Cloud SDK. For detailed installation instructions, refer to the official Google Cloud documentation [here](https://cloud.google.com/sdk/docs/install).

#### Task 2: Link GCD to App

Follow the documentation provided by Google Cloud to link GCD to your Python application. This typically involves setting up authentication credentials and configuring the necessary permissions.

#### Task 3: Set Up Python Environment

1. Create a virtual environment to isolate project dependencies:
   ```bash
   python -m venv env
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source env/bin/activate
     ```

3. Initialize Google Cloud SDK and authenticate:
   ```bash
   gcloud init
   ```

1. Install other required libraries listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

6. Create a Google API key by following the instructions at [Google Cloud Console](https://console.cloud.google.com/apis/credentials).

7. Create a `.env` file in the project root directory and add the Google API key:
   ```
   GOOGLE_API_KEY=YOUR_API_KEY
   ```

8. Install the `langchain-google-genai` library for language processing:
   ```bash
   pip install langchain-google-genai
   ```

9. Create a Python script file named `explorer.py` to interact with the Google Cloud API. (explorer.py - File Name as per your preference)

10. Follow the instructions provided in the project's documentation or video tutorials to set up the `explorer.py` file.

11. Run the application using Streamlit:
    ```bash
    streamlit run explorer.py
    ```

### Task 4: Initialize Chat History and Manage Messages

In Task 4, we implemented a script (`explorer.py`) to initialize the chat history, display previous messages, manage initial startup messages, capture user input, and process responses from the generative model. Here’s an overview of what the script does:

1. **Environment Setup**: 
   - Load environment variables from a `.env` file.
   - Ensure `GOOGLE_API_KEY` and `GOOGLE_APPLICATION_CREDENTIALS` are set.

2. **Google Cloud Initialization**:
   - Initialize the Google Cloud project using the provided project ID.
   - Configure the generative model with specific settings like temperature.

3. **Model Setup**:
   - Load the generative model and start a chat session.

4. **Helper Function**:
   - Define a helper function (`llm_function`) to handle the interaction between the user and the model, sending user queries to the model and displaying the responses.

5. **Streamlit Application**:
   - Set up the Streamlit interface to display the chat interface.
   - Initialize chat history if it does not exist.
   - Display previous chat messages.
   - Handle initial startup messages and user input, sending queries to the model and displaying the responses.


### Task 5: Replacing Code

Enhance the functionality of your application by adding custom code snippets. For example, you can integrate additional APIs, implement chatbot logic, or incorporate machine learning models for advanced NLP capabilities. Refer to the project's documentation and sample code for guidance on adding custom functionality.

```python
if len(st.session_state.messages) == 0:
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive"
    llm_function(chat, initial_prompt)
```
message.txt
5 KB
 
