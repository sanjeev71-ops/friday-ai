import streamlit as st
import requests

st.title("FRIDAY")

user_input = st.text_input("Message")

if st.button("Send"):

    response = requests.post(
        "http://127.0.0.1:8000/api/v1/chat", json={"message": user_input}, stream=True
    )

    if response.status_code == 200:

        response_container = st.empty()

        full_text = ""

        for chunk in response.iter_content(chunk_size=None):

            if chunk:

                decoded_chunk = chunk.decode("utf-8")

                full_text += decoded_chunk

                response_container.markdown(full_text)

    else:
        st.error("Backend error")
