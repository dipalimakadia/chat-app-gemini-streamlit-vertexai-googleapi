import os
from dotenv import load_dotenv
import vertexai
import streamlit as st;
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

load_dotenv()

# Ensure the environment variables are set
assert 'GOOGLE_API_KEY' in os.environ, "GOOGLE_API_KEY not found in environment variables"
assert 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ, "GOOGLE_APPLICATION_CREDENTIALS not found in environment variables"

project= "sample-gemini-427119"
vertexai.init(project=project)

config = generative_models.GenerationConfig(temperature=0.4)

#load model with config
model = GenerativeModel("gemini-1.5-flash", generation_config=config)

chat = model.start_chat();

#Helper function to display and send streamlit messages
def llm_function(chat: ChatSession, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text
    
    with st.chat_message("model"):
        st.markdown(output)
    
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    
    st.session_state.messages.append(
        {
            "role": "model",
            "content": output
        }
    )

st.title("Gemini Explorer")

# Initialize chat History
if "messages" not in st.session_state:
    st.session_state.messages = []
    
#Display and Load chat history
for index, message in enumerate(st.session_state.messages):
    # content = Content(
    #     role = message["role"],
    #     parts = [Part.from_text(message["content"])]
    # )
    
    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # chat.history.append(content)

# For Intialize message startup
#Rex
if len(st.session_state.messages) == 0:
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive"
    llm_function(chat, initial_prompt) #llm_function to interact with the chat model, passing initial_prompt as the user query to start the conversation

    
# For capture user input
query = st.chat_input("Gemini")
    
if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)