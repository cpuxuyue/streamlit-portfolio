import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os

def make_lnp_formulation(rna_scale, rna_stock_concentration, ionizable_lipid_to_rna_ratio, aqueous_to_ethanol_ratio, ionizable_lipid_mw, helper_lipid_mw, cholesterol_mw, pegdmg2000_mw, ionizable_lipid_concentration, helper_lipid_concentration, cholesterol_concentration, pegdmg2000_concentration, ionizable_lipid_ratio, helper_lipid_ratio, cholesterol_ratio, pegdmg2000_ratio):
    """计算 LNP 配方组成"""
    ionizable_lipid_moles = (rna_scale * ionizable_lipid_to_rna_ratio) / ionizable_lipid_mw
    helper_lipid_moles = ionizable_lipid_moles * helper_lipid_ratio / ionizable_lipid_ratio
    cholesterol_moles = ionizable_lipid_moles * cholesterol_ratio / ionizable_lipid_ratio
    pegdmg2000_moles = ionizable_lipid_moles * pegdmg2000_ratio / ionizable_lipid_ratio

    ionizable_lipid_mass = ionizable_lipid_moles * ionizable_lipid_mw
    helper_lipid_mass = helper_lipid_moles * helper_lipid_mw
    cholesterol_mass = cholesterol_moles * cholesterol_mw
    pegdmg2000_mass = pegdmg2000_moles * pegdmg2000_mw

    final_lnp_volume = rna_scale / 0.1
    
    ionizable_lipid_volume = ionizable_lipid_mass / ionizable_lipid_concentration
    helper_lipid_volume = helper_lipid_mass / helper_lipid_concentration
    cholesterol_volume = cholesterol_moles * cholesterol_mw / cholesterol_concentration
    pegdmg2000_volume = pegdmg2000_moles * pegdmg2000_mw / pegdmg2000_concentration
    ethanol = final_lnp_volume / (aqueous_to_ethanol_ratio + 1) - ionizable_lipid_volume - helper_lipid_volume - cholesterol_volume - pegdmg2000_volume
    ethanol_phase_volume = ionizable_lipid_volume + helper_lipid_volume + cholesterol_volume + pegdmg2000_volume + ethanol

    aqueous_phase_volume = final_lnp_volume * (aqueous_to_ethanol_ratio / (aqueous_to_ethanol_ratio + 1))
    rna_volume = rna_scale / rna_stock_concentration
    citrate_volume = 0.1 * aqueous_phase_volume
    water_volume = aqueous_phase_volume - rna_volume - citrate_volume

    data = {
        'Component': ['Ionizable Lipid', 'Helper Lipid', 'Cholesterol', 'PEG-DMG2000', 'Ethanol', 'RNA', 'Citrate', 'Water'],
        'Volume (μL)': [ionizable_lipid_volume, helper_lipid_volume, cholesterol_volume, pegdmg2000_volume, ethanol, rna_volume, citrate_volume, water_volume]
    }

    df = pd.DataFrame(data)
    
    volumes = {
        "Ionizable Lipid": ionizable_lipid_volume,
        "helper_lipid_volume": helper_lipid_volume,
        "cholesterol_volume": cholesterol_volume,
        "pegdmg2000_volume": pegdmg2000_volume,
        "ethanol": ethanol,
        "ethanol_phase_volume": ethanol_phase_volume,
        "rna_volume": rna_volume,
        "citrate_volume": citrate_volume,
        "water_volume": water_volume,
        "aqueous_volume": aqueous_phase_volume
    }

    return df, volumes

def prepare_bulk_lnp_volumes(volumes, times):
    """计算批量制备的 LNP 体积"""
    bulk_volumes = {
        "Component": ['Ionizable Lipid', "Helper Lipid", "Cholesterol", "PEG-DMG2000", "Ethanol", "RNA", "Citrate", "Water"],
        "Volume (μL)": [
            volumes["Ionizable Lipid"] * times * 1.5,
            volumes["helper_lipid_volume"] * times * 1.5,
            volumes["cholesterol_volume"] * times * 1.5,
            volumes["pegdmg2000_volume"] * times * 1.5,
            volumes["ethanol"] * times * 1.5,
            volumes["rna_volume"] * times * 1.2,
            volumes["citrate_volume"] * times * 1.2,
            volumes["water_volume"] * times * 1.2,
        ]
    } 
    bulk_df = pd.DataFrame(bulk_volumes)
    return bulk_df

def get_tools_section():
    st.markdown("### 🛠️ Tools")
    
    # 创建两个标签页
    tab1, tab2 = st.tabs(["📊 Lilab-Spreadsheet", "🧪 LNP Formulation Calculator"])
    
    with tab1:
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
    
    with tab2:
        st.markdown("""
        ### LNP 配方计算器
        这个工具可以帮助您计算脂质纳米颗粒（LNP）的配方组成。
        """)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            rna_scale = st.number_input("RNA Scale (μg)", min_value=0.0, step=1.0, value=3.0)
        with col2:
            rna_stock_concentration = st.number_input("RNA Stock (μg/μL)", min_value=0.0, step=0.1, value=1.0)
        with col3:
            ionizable_lipid_to_rna_ratio = st.number_input("Ionizable Lipid to RNA Ratio", min_value=0.0, max_value=100.0, step=0.1, value=10.0)
        with col4:
            aqueous_to_ethanol_ratio = st.number_input("Aqueous to Ethanol Ratio", min_value=0.0, step=0.1, value=3.0)

        col5, col6, col7, col8 = st.columns(4)
        with col5:
            ionizable_lipid_mw = st.number_input("Ionizable Lipid Molecular Weight (μg/μmol)", min_value=0.0, step=1.0, value=1000.0)
        with col6:
            helper_lipid_mw = st.number_input("Helper Lipid Molecular Weight (μg/μmol)", min_value=0.0, step=1.0, value=744.034)
        with col7:
            cholesterol_mw = st.number_input("Cholesterol Molecular Weight (μg/μmol)", min_value=0.0, step=1.0, value=386.654)
        with col8:
            pegdmg2000_mw = st.number_input("PEG-DMG2000 Molecular Weight (μg/μmol)", min_value=0.0, step=1.0, value=2509.2)

        col9, col10, col11, col12 = st.columns(4)
        with col9:
            ionizable_lipid_concentration = st.number_input("Ionizable Lipid Concentration (μg/μL)", min_value=0.0, step=0.1, value=40.0)
        with col10:
            helper_lipid_concentration = st.number_input("Helper Lipid Concentration (μg/μL)", min_value=0.0, step=0.1, value=10.0)
        with col11:
            cholesterol_concentration = st.number_input("Cholesterol Concentration (μg/μL)", min_value=0.0, step=0.1, value=10.0)
        with col12:
            pegdmg2000_concentration = st.number_input("PEG-DMG2000 Concentration (μg/μL)", min_value=0.0, step=0.1, value=10.0)
        
        col13, col14, col15, col16 = st.columns(4)
        with col13:
            ionizable_lipid_ratio = st.number_input("Ionizable Lipid Molar Ratio", min_value=0.0, step=0.1, value=35.0)
        with col14:
            helper_lipid_ratio = st.number_input("Helper Lipid Molar Ratio", min_value=0.0, step=0.1, value=16.0)
        with col15:
            cholesterol_ratio = st.number_input("Cholesterol Molar Ratio", min_value=0.0, step=0.1, value=46.5)
        with col16:
            pegdmg2000_ratio = st.number_input("PEG-DMG2000 Molar Ratio", min_value=0.0, step=0.1, value=2.5)
        
        col17, col18 = st.columns(2)
        with col17:
            bulk_times = st.number_input("Bulk Preparation Times", min_value=1, step=1, value=1)
        
        if "result_df" not in st.session_state:
            st.session_state.result_df = None
            st.session_state.volumes = None
            st.session_state.checkboxes_col2 = {}
            st.session_state.checkboxes_col4 = {}

        if st.button("Calculate"):
            result_df, volumes = make_lnp_formulation(
                rna_scale, rna_stock_concentration, ionizable_lipid_to_rna_ratio, aqueous_to_ethanol_ratio,
                ionizable_lipid_mw, helper_lipid_mw, cholesterol_mw, pegdmg2000_mw, ionizable_lipid_concentration,
                helper_lipid_concentration, cholesterol_concentration, pegdmg2000_concentration, ionizable_lipid_ratio,
                helper_lipid_ratio, cholesterol_ratio, pegdmg2000_ratio
            )
            st.session_state.result_df = result_df
            st.session_state.volumes = volumes
            st.session_state.checkboxes_col2 = {index: False for index in result_df.index}
            st.session_state.checkboxes_col4 = {index: False for index in result_df.index}

        if st.session_state.result_df is not None:
            st.header('', divider='rainbow')
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown("Single LNP")
                st.dataframe(st.session_state.result_df)

            with col2:
                st.markdown("Checklist")
                for index, row in st.session_state.result_df.iterrows():
                    st.session_state.checkboxes_col2[index] = st.checkbox(
                        f"{row['Component']}", 
                        value=st.session_state.checkboxes_col2[index],
                        key=f"col2_{index}"
                    )               
            with col3:
                st.markdown("EtOH Phasex1.5, Aqueous Phasex1.2")
                if st.session_state.volumes is not None:
                    bulk_volumes = prepare_bulk_lnp_volumes(st.session_state.volumes, bulk_times)
                    st.dataframe(bulk_volumes)

            with col4:
                st.markdown("Checklist")
                for index, row in st.session_state.result_df.iterrows():
                    st.session_state.checkboxes_col4[index] = st.checkbox(
                        f"{row['Component']}", 
                        value=st.session_state.checkboxes_col4[index],
                        key=f"col4_{index}"
                    ) 