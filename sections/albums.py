import streamlit as st
from PIL import Image
import os

def get_albums_section():
    st.markdown("### 📸 Albums")
    
    # 创建图片目录
    if not os.path.exists('assets/images'):
        os.makedirs('assets/images')
    
    # Research Life 部分
    st.markdown("#### Research Life")
    # 研究生活图片
    if os.path.exists('assets/images/Research Life_Haotian_Graduation1.JPG'):
        image = Image.open('assets/images/Research Life_Haotian_Graduation1.JPG')
        st.image(image, caption="Graduation ceremony for Haotian (2023)", use_column_width=True)
        
    if os.path.exists('assets/images/Research Life_Haotian_Graduation2.JPG'):
        image = Image.open('assets/images/Research Life_Haotian_Graduation2.JPG')
        st.image(image, caption="Celebrating Haotian's graduation (2023)", use_column_width=True)
    
    # Conference & Travel 部分
    st.markdown("#### Conference & Travel")
    # 会议和旅行图片
    if os.path.exists('assets/images/Conference_Changsha 2022.jpg'):
        image = Image.open('assets/images/Conference_Changsha 2022.jpg')
        st.image(image, caption="Presenting at the Conference in Changsha (2022)", use_column_width=True)
        
    if os.path.exists('assets/images/Travel_UK cambridge University.JPG'):
        image = Image.open('assets/images/Travel_UK cambridge University.JPG')
        st.image(image, caption="Visiting the University of Cambridge (2023)", use_column_width=True)
    