import streamlit as st

st.title("Contact Me  💌 🚀")

st.markdown("""
**Enter your email, subject, and email body then hit send to receive an email from `hmama8989@gmail.com`!**
""")

# Taking inputs
email_sender = st.text_input('From', 'hmama8989@gmail.com', disabled=True)
email_receiver = st.text_input('To')
subject = st.text_input('Subject')
body = st.text_area('Body')

# Hide the password input
password = st.text_input('password', type="password", disabled=True)  

import smtplib
from email.mime.text import MIMEText

if st.button("Send Email"):
    try:
        msg = MIMEText(body)
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(st.secrets["email"]["gmail"], st.secrets["email"]["password"])
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()

        st.success('Email sent successfully! 🚀')
    except Exception as e:
        st.error(f"Failed to send email: {e}")