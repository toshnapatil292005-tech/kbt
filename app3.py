import streamlit as st

st.title("basic calculator")

num1=int(st.number_input("enter first number"))
num2=int(st.number_input("enter second number"))
operation=st.selectbox("choose op",["add","sub","mul","div"])

if st.button("calculate"):
    if operation == "add":
        st.write(num1+num2)
    elif operation =="sub":
        st.write(num1-num2)
    elif operation =="mul":
        st.write(num1*num2)
    else:
      st.write("cannot display output")
