import streamlit as st

st.markdown("""
<style>
            .stButton > button
            {
            background-color:green;
            color:white;
            border-radius:50%;
            }
</style>
















""", unsafe_allow_html=True)

st.title("welcome to basic streamlit app")

age=st.slider("select your age", 1,100)
city=st.selectbox("select your city",["delhi","mumbai","nashik","pune"])

if st.button("show details"):
    st.write("age",age)
    st.write("city",city)