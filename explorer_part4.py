#It initializes chat history, displays previous messages, manages initial startup messages, captures user input, and processes responses from the generative model.
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
    
    with st.chat_message("model"): #Prepares a message block in Streamlit with the role labeled as "model". This is where the model's response will be displayed.
        st.markdown(output)
        
    #Adds the user's query and the model's response to the messages list stored in Streamlit's session state. Each message is stored as a dictionary.
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

    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# For Intialize message startup
if len(st.session_state.messages) == 0:
    initial_message = "Welcome to Gemini Explorer! How can I assist you today?"

    st.session_state.messages.append({"role": "model", "content": initial_message})
    
    with st.chat_message("model"): #This line creates a message block in the Streamlit app.

        st.markdown(initial_message) #will format and display content as if it's coming from the model #this line displays the initial_message using Markdown formatting. Markdown is a lightweight markup language with plain-text formatting syntax.
          
# For capture user input
query = st.chat_input("Gemini")
    
if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query) #Calls llm to interact with the chat model, sending the user's query and displaying the model's response.
