import vertexai
import streamlit as st;
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession


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
if len(st.session_state.messages) == 0:
    initial_message = "Welcome to Gemini Explorer! How can I assist you today?"
    # initial_content = Content(
        
    #     role = "model",
    #     parts = [Part.from_text(initial_message)]
        
    # )
    st.session_state.messages.append({"role": "model", "content": initial_message})
    
    with st.chat_message("model"):
        st.markdown(initial_message)
    
    # chat.history.append(initial_content)
      
# For capture user input
query = st.chat_input("Gemini")
    
if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)