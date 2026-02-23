import streamlit as st

st.title("Basic Calculator")

num1 = int(st.number_input("Enter first number"))
num2 = int(st.number_input("Enter second number"))

operation = st.selectbox("Choose operation", ["add", "sub", "mul", "div"])

if st.button("Calculate"):

    result = None

    if operation == "add":
        result = num1 + num2

    elif operation == "sub":
        result = num1 - num2

    elif operation == "mul":
        result = num1 * num2

    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero not allowed")

    if result is not None:
        st.success(f"Result = {round(result,2)}")