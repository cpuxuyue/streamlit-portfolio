import streamlit as st
# from st_social_media_links import SocialMediaIcons
import streamlit.components.v1 as components
import base64
import textwrap
from social_media_icons import SocialMediaIcons

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

social_media_links = [
    "mailto:bilpapster@gmail.com",
    "https://www.linkedin.com/in/bilpapster/",
    "https://www.github.com/bilpapster/",
]
social_media_icons = SocialMediaIcons(social_media_links)

with left:
    st.write("Hello traveller,")
    st.title("I'm Vasileios Papastergios,")
    st.write("a Computer Science graduate with an avid passion for sports.")
with right:
    st.image("Vasileios Papastergios.png")

about, education, achievements, experience, projects, volunteerism, contact = st.tabs(["About", "Education", "Achievements", "Experience", "Projects", "Volunteerism", "Contact"])

with about:
    # st.header("About")
    # header_underline()
    st.markdown("""Computer Science graduate with expertise in Data Quality, Artificial Intelligence, and Big Data Management. Passionate about leveraging technology to drive innovative, impactful solutions to real-life problems. Skilled in analytical problem-solving, and cross-functional collaboration. Currently serving as a Research Assistant at [Datalab AUTh](https://datalab.csd.auth.gr/), under the supervision of [Prof. Anastasios Gounaris](https://datalab-old.csd.auth.gr/~gounaris/).
    """)

with education:
    # st.header("Education")
    # header_underline()
    st.markdown("""
    ### Computer Science BSc. School of Informatics
    Aristotle University - Thessaloniki, Greece
    
    Oct 2019 - Jul 2024
    
    - Grade: 9.57 / 10.0 - **top 1%** and Graduation Valedictorian
    - Thesis: Data Quality Assessment for Static & Streaming Data
    - Degree specializations: Artificial Intelligence, Data & Web Management
    - TODO transcript of records
    """)
    st.button("Transcript of records")
    st.divider()
    st.markdown("""
    ### Army ROTC, Military Science and Operations
    Reserve Officer Infantry School & Specialized Training Wing - Heraklion, Greece

    Oct 2021 – Mar 2022

    - Graduated 5th among 56 from the Reserve Officer Infantry School, **top-seeded** in age group 18 – 21 and top 7% overall.
    - Admitted in 2nd & graduated **1st among 26** from the Specialized Training Wing.
    - Executed Staff Sergeant Duties and served as Training Platoon Commander among trainees.
    - TODO SEAP certificate
    """)
    st.button("Military Cerificate")
    st.divider()
    st.markdown("""
        ### Upper Secondary National Apolytirion
        4th Regional Senior High School - Kozani, Greece

        Sep 2016 – Jun 2019

        - GPA: 20/20, Science & IT Branch, Economics & IT Elective
        - Represented my country as a member of the Youth EU Parliament in Strasbourg, France (March 2018). Ranked in top 5% of applicants to get selected, based on various criteria.
        - TODO add Apolytirion
    """)
    st.button("High School Degree")

with achievements:
    st.header("Achievements & Distinctions")
    header_underline()

with experience:
    st.header("Work Experience")
    header_underline()

with projects:
    st.header("Projects & Technologies")
    header_underline()

with volunteerism:
    st.header("Volunteerism & Community")
    header_underline()

with contact:
    # st.header("Contact")
    # header_underline()
    st.write("Contact me via email, reach me on LinkedIn or follow me on GitHub!")
    # st.divider()
    social_media_icons.render()


