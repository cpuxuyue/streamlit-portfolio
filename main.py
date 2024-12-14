import streamlit as st
import base64
import sys
from pathlib import Path

dir = Path(__file__).absolute()
sys.path.append(str(dir))

st.set_page_config(
    page_title="Vasileios Papastergios' personal website",
    page_icon=":computer:",
)



with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

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


from utilities import render_about_information

render_about_information()
about, education, achievements, experience, projects, volunteerism = st.tabs(["About", "Education", "Achievements", "Experience", "Projects", "Volunteerism"])

with about:
    from social_media_icons import SocialMediaIcons
    def get_about_section():
        # render_about_information()
        # st.header("About me")
        # header_underline()
        st.markdown(
            """Computer Science graduate with expertise in Data Quality, Artificial Intelligence, and Big Data Management. Passionate about leveraging technology to drive innovative, impactful solutions to real-life problems. Skilled in analytical problem-solving, and cross-functional collaboration. Currently serving as a Research Data Engineer at [Datalab AUTh](https://datalab.csd.auth.gr/), under the supervision of [Prof. Anastasios Gounaris](https://datalab-old.csd.auth.gr/~gounaris/).""")
        get_contact_section()
        st.info(
            "Want to learn more about me? Feel free to explore other sections of this website using the tabs above.")


    def get_contact_section():
        social_media_links = [
            "mailto:bilpapster@gmail.com",
            "https://www.linkedin.com/in/bilpapster/",
            "https://www.github.com/bilpapster/",
        ]
        social_media_icons = SocialMediaIcons(social_media_links)
        # st.header("Contact")
        # header_underline()
        st.write(
            "Feel free to contact me via email, connect with me on LinkedIn or follow me on GitHub, by clicking on the icons below:")
        # st.divider()
        social_media_icons.render()
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
    from sections.volunteerism import get_volunteerism_section
    get_volunteerism_section()

st.divider()
st.markdown('[Back to Top](#i-m-vasileios-papastergios)')

