import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os

def get_tools_section():
    st.markdown("### 🛠️ Tools")
    
    # Lilab-Spreadsheet 工具
    st.markdown("#### 📊 Lilab-Spreadsheet")
    st.markdown("""
    这是一个用于处理和分析实验室数据的工具。您可以：
    - 上传 Excel 文件
    - 查看和编辑数据
    - 进行数据分析
    - 导出处理后的结果
    """)
    
    # 文件上传
    uploaded_file = st.file_uploader("上传 Excel 文件", type=['xlsx', 'xls'])
    
    if uploaded_file is not None:
        try:
            # 读取 Excel 文件
            df = pd.read_excel(uploaded_file)
            
            # 显示数据预览
            st.markdown("#### 数据预览")
            st.dataframe(df.head())
            
            # 数据分析选项
            st.markdown("#### 数据分析")
            analysis_type = st.selectbox(
                "选择分析类型",
                ["基本统计", "数据可视化", "数据筛选"]
            )
            
            if analysis_type == "基本统计":
                st.markdown("##### 基本统计信息")
                st.write(df.describe())
                
            elif analysis_type == "数据可视化":
                st.markdown("##### 数据可视化")
                # 选择要可视化的列
                numeric_columns = df.select_dtypes(include=[np.number]).columns
                if len(numeric_columns) > 0:
                    column_to_plot = st.selectbox("选择要可视化的列", numeric_columns)
                    st.line_chart(df[column_to_plot])
                else:
                    st.warning("没有找到数值类型的列用于可视化")
                    
            elif analysis_type == "数据筛选":
                st.markdown("##### 数据筛选")
                # 选择要筛选的列
                filter_column = st.selectbox("选择要筛选的列", df.columns)
                filter_value = st.text_input("输入筛选值")
                if filter_value:
                    filtered_df = df[df[filter_column].astype(str).str.contains(filter_value, case=False)]
                    st.dataframe(filtered_df)
            
            # 导出选项
            st.markdown("#### 导出数据")
            if st.button("导出为 Excel"):
                output = df.to_excel(index=False)
                st.download_button(
                    label="下载 Excel 文件",
                    data=output,
                    file_name="processed_data.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                
        except Exception as e:
            st.error(f"处理文件时出错: {str(e)}")
    
    # 使用说明
    with st.expander("使用说明"):
        st.markdown("""
        ### 使用说明
        
        1. **上传数据**
           - 点击"上传 Excel 文件"按钮
           - 选择您的 Excel 文件（.xlsx 或 .xls 格式）
        
        2. **查看数据**
           - 上传后会自动显示数据预览
           - 可以查看前几行数据
        
        3. **数据分析**
           - 选择分析类型
           - 根据提示进行操作
        
        4. **导出结果**
           - 点击"导出为 Excel"按钮
           - 下载处理后的数据
        """) 