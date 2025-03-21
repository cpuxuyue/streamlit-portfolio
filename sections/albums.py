import streamlit as st
from PIL import Image
import os

def get_albums_section():
    st.markdown("### 📸 Albums")
    
    # 创建图片目录
    images_dir = os.path.join('assets', 'images')
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    
    # Research Life 部分
    st.markdown("#### Research Life")
    # 研究生活图片
    graduation1_path = os.path.join(images_dir, 'Research Life_Haotian_Graduation1.JPG')
    if os.path.exists(graduation1_path):
        image = Image.open(graduation1_path)
        st.image(image, caption="Graduation ceremony for Haotian (2023)", use_column_width=True)
        
    graduation2_path = os.path.join(images_dir, 'Research Life_Haotian_Graduation2.JPG')
    if os.path.exists(graduation2_path):
        image = Image.open(graduation2_path)
        st.image(image, caption="Celebrating Haotian's graduation (2023)", use_column_width=True)
    
    # Conference & Travel 部分
    st.markdown("#### Conference & Travel")
    # 会议和旅行图片
    changsha_path = os.path.join(images_dir, 'Conference_Changsha 2022.jpg')
    if os.path.exists(changsha_path):
        image = Image.open(changsha_path)
        st.image(image, caption="Presenting at the Conference in Changsha (2022)", use_column_width=True)
        
    cambridge_path = os.path.join(images_dir, 'Travel_UK cambridge University.JPG')
    if os.path.exists(cambridge_path):
        image = Image.open(cambridge_path)
        st.image(image, caption="Visiting the University of Cambridge (2023)", use_column_width=True)
    