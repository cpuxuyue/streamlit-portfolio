import streamlit as st
from social_media_icons import SocialMediaIcons

social_media_links = [
    "mailto:bilpapster@gmail.com",
    "https://www.linkedin.com/in/bilpapster/",
    "https://www.github.com/bilpapster/",
]
social_media_icons = SocialMediaIcons(social_media_links)

def get_contact_section():
    # st.header("Contact")
    # header_underline()
    st.write("Feel free to contact me via email, connect with me on LinkedIn or follow me on GitHub!")
    # st.divider()
    social_media_icons.render()