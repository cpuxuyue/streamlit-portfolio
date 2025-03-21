import streamlit as st
import base64
import sys
import os
from pathlib import Path

dir = Path(__file__).absolute()
sys.path.append(str(dir) + "/sections/")

st.set_page_config(
    page_title="Yue Xu's personal website",
    page_icon=":computer:",
)

# 添加 Academicons CDN
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/academicons@1.9.1/css/academicons.min.css">', unsafe_allow_html=True)

# 添加 Font Awesome 5 CDN
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">', unsafe_allow_html=True)

# 读取样式文件
style_path = os.path.join(os.path.dirname(__file__), 'style.css')
with open(style_path) as f:
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

def cv_svg():
    cv_svg = """
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M208 0H332.1c12.7 0 24.9 5.1 33.9 14.1l67.9 67.9c9 9 14.1 21.2 14.1 33.9V336c0 26.5-21.5 48-48 48H208c-26.5 0-48-21.5-48-48V48c0-26.5 21.5-48 48-48zM48 128H192v64H64V448H256V416h64v48c0 26.5-21.5 48-48 48H48c-26.5 0-48-21.5-48-48V176c0-26.5 21.5-48 48-48z"/></svg>
        """
    render_svg(cv_svg)
    return

from utilities import render_about_information
from sections.contact import get_contact_section

render_about_information()

about, education, academics, teaching, projects, activities, honors, albums, tools = st.tabs(["About", "Education", "Academics", "Teaching", "Projects", "Activities", "Honors", "Albums", "Tools"])

with about:
    def get_about_section():
        st.markdown(
            """I am a third-year UHN-PRiME postdoctoral fellow at the Leslie Dan Faculty of Pharmacy, University of Toronto, 
            with a Ph.D. from China Pharmaceutical University. My research focuses on medicinal and lipid chemistry, 
            with particular interest in developing AI-guided high-throughput screening platforms for lipid nanoparticle 
            (LNP) delivery systems. I have published high-impact research and filed patents in the field, and I'm 
            currently working on mRNA delivery strategies for cancer immunotherapy and intranasal vaccines. My 
            long-term goal is to lead interdisciplinary drug discovery efforts as a senior scientist in biotech or 
            as a principal investigator in academia.""")
        get_contact_section()
        st.info(
            "Want to learn more about me? Feel free to explore other sections of this website using the tabs above.")

    get_about_section()

with education:
    from sections.education import get_education_section
    get_education_section()

with academics:
    from sections.academics import get_academics_section
    get_academics_section()

with teaching:
    from sections.teaching import get_teaching_section
    get_teaching_section()

with projects:
    from sections.projects import get_projects_section
    get_projects_section()

with activities:
    from sections.activities import get_activities_section
    get_activities_section()

with honors:
    from sections.honors import get_honors_section
    get_honors_section()

with albums:
    from sections.albums import get_albums_section
    get_albums_section()

with tools:
    from sections.tools import get_tools_section
    get_tools_section()

st.divider()
st.markdown('[Back to Top](#i-m-yue-xu)')

