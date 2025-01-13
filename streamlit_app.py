import streamlit as st

st.title("Please fill the form below")

name = st.text_input("Name")
email = st.text_input("Email")
address = st.text_input("Address")
phone_number = st.text_input("Phone Number")


col1 ,col2=st.columns(2)

    
with col1:
    st.radio(
        'Set selectbox label visibility',
        key='visibility',
        options=['red','blue','yellow']
        )
with col2:
    option = st.selectbox(
        "Gender: ",
        ("Male", "Female", "Other"),
        index=0,
        placeholder="Select what you like to be called...",
        )

if st.button('Submit'):
    if not name or not email or not address or not phone_number:
        st.error("Please fill the form")
    else:
        st.success("Form Submitted")