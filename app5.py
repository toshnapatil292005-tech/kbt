import streamlit as st

st.title("chatbot")

Question=st.text_input("ask anything..")

if st.button("send"):
    st.write("you ask",Question)
    st.write("chatbot is on the process reply soon")