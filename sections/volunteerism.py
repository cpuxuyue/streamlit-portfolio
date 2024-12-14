import streamlit as st

def get_volunteerism_section():

    @st.cache_data(ttl=3600)  # Cache images for 1 hour (=3600 seconds)
    def get_images():
        images = {}
        images['open_discussion_1'] = "assets/images/Vasileios Papastergios - DAR YE Camp 1.png"
        images['open_discussion_2'] = "assets/images/Vasileios Papastergios - DAR YE Camp 2.png"
        images['farewell_1'] = "assets/images/Vasileios Papastergios - Farewell comments 1.jpg"
        images['farewell_2'] = "assets/images/Vasileios Papastergios - Farewell comments 2.jpg"
        images['outdoor_cooking'] = "assets/images/Vasileios Papastergios - DAR YE Camp 3.png"
        images['love_nature'] = "assets/images/Vasileios Papastergios - DAR YE Camp 4.png"
        images['endurance'] = "assets/images/Vasileios Papastergios - DAR YE Camp 5.png"
        images['bill_builder'] = "assets/images/Vasileios Papastergios - DAR YE Camp 6.png"
        images['skouras_group_photo'] = "assets/images/Vasileios Papastergios - Skouras Camp 1.jpg"
        images['skouras_instructor'] = "assets/images/Vasileios Papastergios - Skouras Camp 2.JPG"
        return images

    images = get_images()
    st.markdown("""
            ### Leader of Youth Community
            <span class="education_location">DAR YE Camp Erasmus+ Program, Novi Becej, Serbia</span>

            Aug 2023""", unsafe_allow_html=True)
    dar_ye_left, dar_ye_right = st.columns(2)
    with dar_ye_left:
        st.image(images['open_discussion_1'], caption="Open-discussion activity (photo 1)")
    with dar_ye_right:
        st.image(images['open_discussion_2'], caption="Open-discussion activity (photo 2)")

    st.markdown("""
            "DAR YE Camp" is an Erasmus+ European program I proudly participated during summer 2023. The program was a <u>**Y**</u>outh <u>**E**</u>xchange (YE) about <u>**D**</u>iscovering the <u>**A**</u>bundance of <u>**N**</u>ature (DAR). For a time period of 14 days, 35 young people (aged 18-30) from 5 different EU countries were brought together in a camp site, away from the urban way of living. Sleeping in tents for the whole duration of the program, performing rural occupations and reconnecting with mother nature were just a few of the deeply motivational activities we accomplished together. Some of these activities are depicted in the photos below! If you, guys, are reading this, I would like you to know that I miss you all! I always fail to hold back tears every time I read again your farewell personal comments (photos below)!""", unsafe_allow_html=True)

    dar_ye_left, dar_ye_right = st.columns(2)
    with dar_ye_left:
        st.image(images['farewell_1'], caption="Farewell comments (page 1)")
    with dar_ye_right:
        st.image(images['farewell_2'], caption="Farewell comments (page 2)")


    st.markdown("""        
            Some of my responsibilities as a coordinator of the program & Leader of the Greek group (consisting of 6 members) were the following:
            - actively participated in the Advance Planning Visit (APV) among group leaders of the 5 involved countries to co-organize scheduling and administrative details for the main event.
            - coordinated & led 12 non-formal learning activities with 35 participants each, in English language. An open-discussion activity about expectations, fears and contributions to the program is depicted in the photos above! 
        """, unsafe_allow_html=True)
    dar_ye_left, dar_ye_right = st.columns(2)
    with dar_ye_left:
        st.image(images['outdoor_cooking'], caption="Outdoor cooking activity with home-grown ingredients")
        st.image(images['endurance'], caption="Endurance (not attention) is all you need (Sorry AI guys)")
    with dar_ye_right:
        st.image(images['love_nature'], caption="Returning love to mother nature :)")
        st.image(images['bill_builder'], caption="Building a home-made outdoor oven to cook yummy home-made pizza!")
    st.divider()

    st.markdown("""
                ### Tennis Instructor
                <span class="education_location">Skouras Sports & Language Camp, Nea Fokaia, Greece</span>

                Summer 2018 & 2019""", unsafe_allow_html=True)
    skouras_left, skouras_right = st.columns(2)
    with skouras_left:
        st.image(images['skouras_instructor'], caption="Demystifying the forehand movement with young campers")
    with skouras_right:
        st.image(images['skouras_group_photo'], caption="Group photo with the quarter-finalists of the first ever \"Skouras Open\" camp tournament")

    st.markdown("""
                [Skouras Sports & Language Camp](https://skourascamp.com/en/) is the largest summer camp in the Balkans, with more than 4'000 children from 10+ EU countries simultaneously on site every summer. During the summers of 2018 and 2019 I had the opportunity to volunteer as a tennis instructor. Recollecting knowledge and experiences from my 10-year journey as an athlete and exploring ways to encourage 2000+ children to actively adopt a healthier lifestyle are things that make me most proud of, when thinking back to those summers. I will never forget the large queues of campers waiting to register for the first ever tournament, the so-called \"Skouras Open\". Giving birth to a tournament we envisioned with coach Kostas and receiving such a warm interest from young campers with little or even no prior engagement with tennis was the greatest reward we received!""",
                unsafe_allow_html=True)
    st.divider()