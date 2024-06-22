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