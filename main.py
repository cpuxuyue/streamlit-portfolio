import streamlit as st
# from st_social_media_links import SocialMediaIcons
import streamlit.components.v1 as components
import base64
import textwrap




with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def header_underline():
    return components.html("""
        <hr style="
            position: absolute;
            left: 0px;
            top: 0px;
            border-radius: 25px;
            height:3px;
            border: none;
            color:#333;
            background: rgb(2,0,36);
            background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(84,74,125,1) 0%, rgba(147,125,109,1) 30%, rgba(255,212,82,1) 100%);
            width:99%;
            padding:0px;
            margin:0;
        " /> 
    """, height=3)

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

def email_svg():
    email_svg = """
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M256 64C150 64 64 150 64 256s86 192 192 192c17.7 0 32 14.3 32 32s-14.3 32-32 32C114.6 512 0 397.4 0 256S114.6 0 256 0S512 114.6 512 256l0 32c0 53-43 96-96 96c-29.3 0-55.6-13.2-73.2-33.9C320 371.1 289.5 384 256 384c-70.7 0-128-57.3-128-128s57.3-128 128-128c27.9 0 53.7 8.9 74.7 24.1c5.7-5 13.1-8.1 21.3-8.1c17.7 0 32 14.3 32 32l0 80 0 32c0 17.7 14.3 32 32 32s32-14.3 32-32l0-32c0-106-86-192-192-192zm64 192a64 64 0 1 0 -128 0 64 64 0 1 0 128 0z"/></svg>
        """
    render_svg(email_svg)
    return


left, right = st.columns([4, 1])

with left:
    st.write("Hello traveller,")
    st.title("I'm Vasileios Papastergios,")
    st.write("a Computer Science graduate with a passion for data-centric, impactful solutions.")
with right:
    st.image("Vasileios Papastergios.png")

about, education, achievements, experience, projects, volunteerism, contact = st.tabs(["About", "Education", "Achievements", "Experience", "Projects", "Volunteerism", "Contact"])

with about:
    from sections.about import get_about_section
    get_about_section()

with education:
    from sections.education import get_education_section
    get_education_section()

with achievements:
    from sections.achievements import get_achievements_section
    get_achievements_section()

with experience:
    from sections.experiences import get_experiences_section
    get_experiences_section()

with projects:
    from sections.projects import get_projects_section
    get_projects_section()

with volunteerism:
    st.header("Volunteerism & Community")
    header_underline()

with contact:
    from sections.contact import get_contact_section
    get_contact_section()


