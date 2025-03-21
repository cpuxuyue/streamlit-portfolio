import streamlit as st

def get_education_section():
    # st.header("Education")
    # header_underline()
    st.markdown("""
        ### PRiME-UHN Postdoc Fellow
        <span class="education_location">University of Toronto, Leslie Dan Faculty of Pharmacy</span>

        2022-Present

        - Supervisor: Profs. Bowen Li
        - Co-Supervisor: Gang Zheng
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("""
        ### Ph.D., Pharmaceutical Engineering
        <span class="education_location">China Pharmaceutical University, College of Engineering</span>

        2017-2022

        - Supervisor: Prof. Haiyan Chen
        - Co-supervisor: Yueqing Gu
    """, unsafe_allow_html=True)
