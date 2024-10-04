import streamlit as st


def custom_text(text, color, fsize, weight):
    st.sidebar.markdown(f"<p style='text-align: left; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{text}</p>", unsafe_allow_html=True)

def custom_text_main(text, color, fsize, weight):
    st.markdown(f"<p style='text-align: left; color : {color}; font-size:{fsize}px; font-weight:{weight}'>{text}</p>", unsafe_allow_html=True)

def set_openai_api_key(api_key: str):
   st.session_state["OPENAI_API_KEY"] = api_key

def sidebar():
    with st.sidebar:
        st.markdown("## How to use\n"
                    "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"
                    "2. Ask a question to get to know our products. \n")
        API_KEY = st.text_input("OpenAI API Key",
                                            placeholder="Paste your OpenAI API key here (sk-...)",
                                            type="password")
        
        st.markdown("---")
        st.markdown("# About")
               
        txt1= "GPT Customer Assistant allows you to get to know more about the products being sold."
        txt2= "Allow customers to gain quick information and faster checkout."
        txt3= "Note: This app showcasing the usage of GPT. It simulates a chatbot usecase."
        txt4= "Work in progress by Pete Chisamba."
        custom_text(txt1,'orange',14,'normal')
        custom_text(txt2,'orange',14,'normal')    
        custom_text(txt3,'orange',14,'normal') 
        custom_text(txt4,'red',12,'normal')       
        st.markdown("---")
        st.markdown("Privacy")
        st.markdown(
            "Your conversation and API key will not saved at all."
        )
        
        if API_KEY:
            set_openai_api_key(API_KEY)
        
