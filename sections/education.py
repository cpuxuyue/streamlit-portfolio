import streamlit as st

def get_education_section():
    # st.header("Education")
    # header_underline()
    st.markdown("""
        ### Computer Science BSc. School of Informatics
        <span class="education_location">Aristotle University - Thessaloniki, Greece</span>

        Oct 2019 - Jul 2024

        - Grade: 9.57 / 10.0 - **top 1%** and Graduation Valedictorian
        - Thesis: Investigation & Implementation of Data Quality Checks (supervised by Prof. A. Gounaris)
        - Degree specializations: Artificial Intelligence, Data & Web Management
        """, unsafe_allow_html=True)
    st.link_button("See transcript of records",
                   url="https://drive.google.com/file/d/1Jm-H1rnyRLoMjvrZwngEOnQojHQ8awCz/view?usp=sharing",
                   icon=":material/description:")
    st.link_button("See BSc Thesis (greek)",
                   url="https://ikee.lib.auth.gr/record/358513/?ln=en",
                   icon=":material/description:")
    st.divider()
    st.markdown("""
        ### Army ROTC, Military Science and Operations
        <span class="education_location">Reserve Officer Infantry School & Specialized Training Wing - Heraklion, Greece</span>

        Oct 2021 – Mar 2022

        - Graduated 5th among 56 from the Reserve Officer Infantry School, **top-seeded** in age group 18 – 21 and top 7% overall.
        - Admitted in 2nd & graduated **1st among 26** from the Specialized Training Wing.
        - Executed Staff Sergeant Duties and served as Training Platoon Commander among trainees.
        """, unsafe_allow_html=True)
    st.link_button("See certificates", icon=":material/description:",
                   url="https://drive.google.com/drive/folders/1II_90vrue4JDzDg7_Tt951LPWjWv1laZ?usp=sharing")
    st.divider()
    st.markdown("""
            ### Upper Secondary National Apolytirion
            <span class="education_location">4th Regional Senior High School - Kozani, Greece</span>

            Sep 2016 – Jun 2019

            - GPA: 20/20, Science & IT Branch, Economics & IT Elective
            - Represented my country as a member of the Youth EU Parliament in Strasbourg, France (March 2018). Ranked in top 5% of applicants to get selected, based on various criteria.
        """, unsafe_allow_html=True)
    st.link_button("See diploma", icon=":material/description:",
                   url="https://drive.google.com/file/d/1qPf6GVB9TV4mTX037tREMoGWo1Nnxeab/view?usp=sharing")
