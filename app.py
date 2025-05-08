import streamlit as st
from PIL import Image
import os

# 设置页面配置
st.set_page_config(
    page_title="辅助生殖预测平台",
    page_icon="🏥",
    layout="wide"
)

# 自定义CSS样式
st.markdown("""
<style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #007BFF;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .sub-text {
        font-size: 18px;
        text-align: center;
        margin-bottom: 30px;
    }
    .card-style {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 40px;
    }
    .img-container {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    .img-container img {
        max-width: 100%;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# 主标题
st.markdown('<div class="main-title">辅助生殖活产率预测列线图</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">基于多因素回归的可视化工具，为医生和患者提供精准的妊娠预后评估</div>', unsafe_allow_html=True)

# 创建选项卡
tab1, tab2 = st.tabs(["预测图展示", "项目简介"])

with tab1:
    st.markdown('<div class="card-style">', unsafe_allow_html=True)
    st.write("此列线图用于根据多个临床变量（如年龄、BMI、子宫内膜厚度等）预测活产率。通过对各项指标的综合评估，可以为患者提供个性化的预测结果。")
    
    # 显示图片
    image_path = "ab5c9664600fe024393b44e6825794c.png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.markdown('<div class="img-container">', unsafe_allow_html=True)
        st.image(image, caption="辅助生殖活产率预测列线图")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("图片文件未找到，请确认路径是否正确。")
    
    st.write("使用方法：根据患者的各项指标，在每个变量轴上找到对应的点，然后垂直连接到'Points'轴获取分数。将所有分数相加得到总分，再从'Total Points'轴垂直向下找到对应的活产率预测值。")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="card-style">', unsafe_allow_html=True)
    st.subheader("模型原理与变量解释")
    
    st.write("该预测模型基于回归分析建模，用于评估辅助生殖中各变量对活产率的影响。通过大量临床数据分析，我们确定了以下关键变量：")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**年龄**")
        st.write("年龄是影响生育能力的重要因素。一般而言，年龄越小，活产率越高。35岁以上女性的生育能力开始明显下降。")
        
        st.markdown("**BMI (体质指数)**")
        st.write("正常范围（18.5–23.9）的BMI对妊娠结局最为有利。过低或过高的BMI都可能对辅助生殖结果产生负面影响。")
        
        st.markdown("**子宫内膜厚度**")
        st.write("子宫内膜厚度≥8mm更利于胚胎着床。内膜厚度不足可能导致胚胎着床困难。")
    
    with col2:
        st.markdown("**胚胎类型**")
        st.write("囊胚移植通常比卵裂期胚胎移植具有更高的着床率和活产率，因为囊胚已经经过了更多的发育筛选。")
        
        st.markdown("**生化妊娠经历**")
        st.write("曾有生化妊娠经历的患者，表明子宫具有一定的接受能力，这可能是预后良好的指标。")
        
        st.markdown("**RIF时间(反复种植失败)**")
        st.write("种植失败时间越短，活产率通常越高。长期反复种植失败可能提示存在更复杂的不孕因素。")
    
    st.write("此预测工具旨在为医生提供临床决策支持，同时帮助患者更好地了解自身情况和治疗预期。需要注意的是，预测结果仅供参考，实际妊娠结局受多种因素影响。")
    st.markdown('</div>', unsafe_allow_html=True)

# 添加页脚
st.markdown("---")
st.markdown("© 2023 辅助生殖预测平台 | 仅供医学研究和临床参考")
