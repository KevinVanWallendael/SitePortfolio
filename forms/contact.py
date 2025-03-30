import re
import streamlit as st
import requests

WEBHOOK_URL = "https://hooks.zapier.com/hooks/catch/22023960/2lypoz3/"

def is_valid_email(email):
    """Checks if an email address is valid using a regular expression."""
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email) is not None

def contact_form():
    """Creates a contact form and sends the data to a webhook."""

    with st.form("contact_form"):
        name = st.text_input("Name").strip()
        email = st.text_input("Email").strip()
        message = st.text_area("Message").strip()
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        errors = []  # List to store error messages

        if not name:
            errors.append("Please enter your name.")
        if not email:
            errors.append("Please enter your email address.")
        elif not is_valid_email(email):
            errors.append("Please enter a valid email address.")
        if not message:
            errors.append("Please enter a message.")

        if errors:
            for error in errors:
                st.error(error)
            return  # Stop execution if there are errors

        # Prepare the data to be sent to the webhook
        data = {"name": name, "email": email, "message": message}

        try:
            # Send the POST request to the webhook
            response = requests.post(WEBHOOK_URL, json=data, timeout=10) #added timeout

            # Check the response status code
            if response.status_code == 200:
                st.success("Message sent successfully!", icon="✅")
            else:
                st.error(f"Failed to send message. Status code: {response.status_code}. Response: {response.text}", icon="❌")

        except requests.exceptions.RequestException as e:
            # Handle any exceptions that may occur during the request
            st.error(f"An error occurred while sending the message: {e}", icon="⚠️")
        except Exception as generic_e:
            st.error(f"A generic error occurred: {generic_e}", icon="🚨")