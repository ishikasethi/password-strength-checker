import streamlit as st
from modules.methods import password_strength

st.title("Password Strength checker")

password = st.text_input("Enter password:")

result = password_strength(password)

if all(result.values()):
    st.info("Strong Password")
elif password == "":
    st.warning("Enter password to check!")
else:
    st.error("Weak Password")

st.subheader("Instruction to generate a strong password:")
caption = """
1. Password should contain at-least one UpperCase and one LowerCase alphabet.
2. Password should contain at-least one special character [@_!#$%^&*()<>?/\|}{~:]. 
3. Password should contain at-least one digit [0-9].
4. Password should be at-least 8 character long."""
st.caption(caption)
