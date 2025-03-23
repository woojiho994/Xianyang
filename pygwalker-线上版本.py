import streamlit as st
import pandas as pd
import os
from pygwalker.api.streamlit import StreamlitRenderer

# 设置页面配置
st.set_page_config(page_title="数据可视化平台", layout="wide")

# 主页面
st.title("数据可视化平台")

# 获取当前文件夹中的所有Excel文件
excel_files = [f for f in os.listdir('.') if f.endswith(('.xlsx', '.xls'))]

# 如果没有Excel文件，显示提示
if not excel_files:
    st.error("当前文件夹中没有找到Excel文件(.xlsx或.xls)")
else:
    # 从文件列表中选择一个
    selected_file = st.selectbox("选择要分析的Excel文件", excel_files)
    
    # 加载数据
    df = None
    
    if selected_file:
        try:
            with st.spinner(f"正在加载Excel文件 {selected_file}..."):
                df = pd.read_excel(selected_file)
            st.success("文件加载成功！")
        except Exception as e:
            st.error(f"加载文件时出错: {e}")
    
    # 如果有数据，显示可视化
    if df is not None:
        # 数据预览选项卡
        tab1, tab2 = st.tabs(["数据预览", "数据可视化"])
        
        with tab1:
            st.subheader("数据预览")
            st.dataframe(df)
            
            # 显示数据统计信息
            st.subheader("数据统计")
            st.write(df.describe())
            
        with tab2:
            st.subheader("数据可视化")
            # 创建PyGWalker应用
            pyg_app = StreamlitRenderer(df)
            pyg_app.explorer()
            

    else:
        st.info("请选择一个Excel文件以开始可视化") 
