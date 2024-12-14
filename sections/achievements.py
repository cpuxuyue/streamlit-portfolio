import streamlit as st

def get_achievements_section():
    st.markdown("""
            ### Graduation Valedictorian
            <span class="education_location">Aristotle University, Thessaloniki, Greece</span>

            July 2024

            Graduated with the highest grade point average (9.57 / 10.0) among 83 alumni from the Computer Science B.Sc. School of Informatics.
        """, unsafe_allow_html=True)
    st.image("assets/images/Vasileios Papastergios - Graduation Valedictorian - July 2024.jpeg", caption="Giving the valediction at the graduation ceremony commencement")
    st.divider()

    st.markdown("""
                ### Training Platoon Commander
                <span class="education_location">Heraklion & Evros, Greece</span>

                March 2022

                Admitted in 2nd & graduated 1st out of 26 from the Specialized Training Wing of the Reserve Officer Infantry School. Executed Staff Sergeant Duties and served as Training Platoon Commander among trainees. Successfully completed 1 international & 10+ national tactical exercises.
            """, unsafe_allow_html=True)
    left_image, right_image = st.columns(2)
    with left_image:
        st.image("assets/images/Vasileios Papastergios - Military Parade - May 2022.JPG", caption="Marching as part of a Special Forces Platoon")
    with right_image:
        st.image("assets/images/Vasileios Papastergios - Army Officer Graduation - March 2022.png", caption="Receiving the rank of 2nd Lieutenant")
    st.divider()

    st.markdown("""
                ### Euroscola Representative
                <span class="education_location">European Parliament, Strasbourg, France</span>

                March 2018

                Represented Greece as a member of the Youth [EU Parliament](https://www.europeana.eu/en/exhibitions/louise-weiss-a-committed-european/louise-weiss-in-strasbourg) in Strasbourg, France. Ranked
                in top 5% of applicants to get selected based on various criteria, including writing - intellectual assessments and personal interviews.
            """, unsafe_allow_html=True)
    st.image("assets/images/Vasileios Papastergios - Euroscola Representative - March 2018.JPG", caption="Posing in front of the entrance of the EU Parliament in Strasbourg, named after Louise Weiss")