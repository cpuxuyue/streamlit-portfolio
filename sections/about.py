import streamlit as st
from social_media_icons import SocialMediaIcons


def get_about_section():
    # render_about_information()
    # st.header("About me")
    # header_underline()
    st.markdown("""
        I am a third-year UHN-PRiME postdoctoral fellow at the Leslie Dan Faculty of Pharmacy, University of Toronto, 
        with a Ph.D. from China Pharmaceutical University. My research focuses on medicinal and lipid chemistry, 
        with particular interest in developing AI-guided high-throughput screening platforms for lipid nanoparticle 
        (LNP) delivery systems. I have published high-impact research and filed patents in the field, and I'm 
        currently working on mRNA delivery strategies for cancer immunotherapy and intranasal vaccines. My 
        long-term goal is to lead interdisciplinary drug discovery efforts as a senior scientist in biotech or 
        as a principal investigator in academia.
    """)
    get_contact_section()
    st.info("Want to learn more about me? Feel free to explore other sections of this website using the tabs above.")


def get_contact_section():
    social_media_links = [
        "mailto:cpuxuyue@gmail.com",
        "https://www.linkedin.com/in/yuexu1995/",
        "https://www.github.com/cpuxuyue/",
    ]
    social_media_icons = SocialMediaIcons(social_media_links)
    # st.header("Contact")
    # header_underline()
    st.write("Feel free to contact me via email, connect with me on LinkedIn or follow me on GitHub:")
    # st.divider()
    social_media_icons.render()