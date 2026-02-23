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

st.title("welcome to form")


name=st.text_input("enter first name")
name2=st.text_input("enter last name")
age=st.slider("select your age", 1,100)
city=st.selectbox("select your city",["delhi","mumbai","nashik","pune"])

if st.button("show details"):
    st.write("first name",name)
    st.write("last name",name2)
    st.write("age",age)
    st.write("city",city)