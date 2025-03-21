import streamlit as st
from social_media_icons import SocialMediaIcons

def get_contact_section():
    social_media_links = [
        "https://x.com/YueXu1995",
        "mailto:cpuxuyue@gmail.com",
        "https://www.linkedin.com/in/yuexu1995/",
        "https://www.github.com/cpuxuyue/",
        "https://orcid.org/0000-0001-7672-9170",
        "https://scholar.google.com.hk/citations?user=xJDpDu4AAAAJ&hl",
        "assets/Yue Xu CV.pdf",
    ]
    social_media_icons = SocialMediaIcons(social_media_links)
    st.write(
        "Feel free to contact me via email, connect with me on LinkedIn, follow me on GitHub, or check my academic profiles on ORCID and Google Scholar:")
    social_media_icons.render() 