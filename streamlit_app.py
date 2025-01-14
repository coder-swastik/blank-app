import streamlit as st
import sqlite3

st.title("Please fill the form below")

name = st.text_input("Name")
email = st.text_input("Email")
address = st.text_input("Address")
phone_number = st.text_input("Phone Number")


col1 ,col2=st.columns(2)

    
with col1:
   course = st.radio(
        'Course: ',
        key='visibility',
        options=['BE. Computer' ,'Bsc CSIT','BCA','BIM','BE. ICT','BCIS' ]
        )
with col2:
    gender = st.selectbox(
        "Gender: ",
        ("Male", "Female", "Other"),
        index=0,
        placeholder="Select what you like to be called...",
        )


def insert_data(name, email, address, phone_number, course, gender):
    conn = sqlite3.connect("form_data.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO form_entries (name, email, address, phone_number, course, gender)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (name, email, address, phone_number, course, gender),
    )
    conn.commit()
    conn.close()

if st.button('Submit'):
    if not name or not email or not address or not phone_number:
        st.error("Please fill the form")
    else:
        insert_data(name, email, address, phone_number, course, gender)
        st.success("Form Submitted")