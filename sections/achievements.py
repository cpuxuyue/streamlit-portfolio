import streamlit as st

def get_achievements_section():
    from streamlit_carousel import carousel
    army_photos_carousel_items = [
        dict(
            title="",
            text="",
            img="assets/images/Vasileios Papastergios - Military Parade - May 2022.jpg",
            # link="https://discuss.streamlit.io/t/new-component-react-bootstrap-carousel/46819",
        ),
        dict(
            title="",
            text="",
            img="assets/images/Vasileios Papastergios - Army Officer Graduation - March 2022.png",
            # link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel",
        )
    ]

    st.markdown("""
            ### Graduation Valedictorian
            <span class="education_location">Aristotle University, Thessaloniki, Greece</span>

            July 2024

            Graduated with the highest grade point average (9.57 / 10.0) among 83 alumni at the Computer Science B.Sc. School of Informatics AUTh.
        """, unsafe_allow_html=True)
    st.image("assets/images/Vasileios Papastergios - Graduation Valedictorian - July 2024.jpeg")
    st.divider()

    st.markdown("""
                ### Training Platoon Commander
                <span class="education_location">Heraklion & Evros, Greece</span>

                March 2022

                Admitted in 2nd & graduated 1st out of 26 from the Specialized Training Wing of the Reserve Officer Infantry School. Executed Staff Sergeant Duties and served as Training Platoon Commander among trainees. Successfully completed 1 international & 10+ national tactical exercises.
            """, unsafe_allow_html=True)
    # st.image("assets/images/Vasileios Papastergios - Graduation Valedictorian - July 2024.jpeg")
    carousel(items=army_photos_carousel_items)
    st.divider()

    st.markdown("""
                ### Euroscola Representative
                <span class="education_location">European Parliament, Strasbourg, France</span>

                March 2018

                Represented Greece as a member of the Youth EU Parliament in Strasbourg, France. Ranked
                in top 5% of applicants to get selected based on various criteria, including writing - intellectual assessments and personal interviews.
            """, unsafe_allow_html=True)
    st.image("assets/images/Vasileios Papastergios - Euroscola Representative - March 2018.JPG")