import streamlit as st

# 设置页面配置
st.set_page_config(page_title="羊羊简历生成器", page_icon="📄", layout="wide")

# 应用标题
st.title("羊羊简历生成器")
st.subheader("使用Streamlit创建的个性化简历")

# 创建两列布局
col1, col2 = st.columns(2)

with col1:
    st.header("羊羊信息表单")
    
    # 基本信息
    st.subheader("基本信息")
    name = st.text_input("姓名", "喜羊羊")
    position = st.text_input("职位", "软件测试")
    phone = st.text_input("电话", "17874527896")
    email = st.text_input("邮箱", "2297173294@qq.com")
    birth_date = st.text_input("出生日期", "2003/06/07")
    
    col1_1, col1_2 = st.columns(2)
    with col1_1:
        gender = st.selectbox("性别", ["男", "女"], index=0)
        education = st.selectbox("学历", ["高中", "专科", "本科", "硕士", "博士"], index=2)
    
    with col1_2:
        experience = st.selectbox("工作经验", ["无经验", "1年", "2年", "3年", "4年", "5年", "6年", "7年", "8年", "9年", "10年以上"], index=6)
        expected_salary = st.text_input("期望薪资", "5540-8450元")
    
    # 语言能力
    st.subheader("语言能力")
    languages = st.multiselect(
        "选择语言能力",
        ["中文", "英语", "日语", "韩语", "法语", "德语", "羊文"],
        default=["中文", "羊文"]
    )
    
    # 专业技能
    st.subheader("专业技能")
    skills = st.multiselect(
        "选择专业技能",
        ["Java", "HTML/CSS", "机器学习", "Python", "JavaScript", "C++", "数据库管理", "网络工程"],
        default=["Java", "HTML/CSS", "机器学习", "Python"]
    )
    
    # 最佳联系时间
    best_time = st.text_input("最佳联系时间", "12：00")
    
    # 个人简介
    st.subheader("羊羊简介")
    introduction = st.text_area(
        "羊羊简介",
        "喜羊羊，中国动画片《喜羊羊与灰太狼》及其衍生作品的主角之一，居住在羊村里的绵羊，大肥羊学校的学生，“草原三剑客”之一，后来考上航天学校，是天才少年。是村长慢羊羊的得力助手，同时也是小羊们重要的伙伴。喜羊羊是羊村中的主心骨，机智聪明，善良勇敢。同时也是羊村里跑得最快的羊。曾为灰太狼宿敌，现成为其挚友。",
        height=150
    )
    
    # 座右铭
    motto = st.text_input("座右铭", "羊羊法的世界里，你是最优解")
    
    # 上传照片
    st.subheader("上传个人照片")
    uploaded_file = st.file_uploader("选择图片文件", type=['png', 'jpg', 'jpeg'])
    
    # 下载按钮
    if st.button("生成并下载简历"):
        st.success("简历已生成！下载功能将在后续版本中实现。")

with col2:
    st.header("简历实时预览")
    
    # 简历预览区域
    with st.container():
        st.markdown("---")
        
        # 简历头部信息
        col2_1, col2_2 = st.columns([1, 3])
        with col2_1:
            if uploaded_file is not None:
                st.image(uploaded_file, width=150)
            else:
                st.markdown("<div style='width:150px; height:150px; border-radius:50%; background-color:#f0f0f0; display:flex; align-items:center; justify-content:center; font-size:48px;'>👤</div>", unsafe_allow_html=True)
        
        with col2_2:
            st.markdown(f"### {name}")
            st.markdown(f"**{position}**")
            st.markdown(f"📱 {phone} | 📧 {email}")
        
        st.markdown("---")
        
        # 个人信息详情
        st.subheader("个人详情")
        col2_3, col2_4 = st.columns(2)
        with col2_3:
            st.markdown(f"**出生日期**: {birth_date}")
            st.markdown(f"**性别**: {gender}")
            st.markdown(f"**工作经验**: {experience}")
        
        with col2_4:
            st.markdown(f"**学历**: {education}")
            st.markdown(f"**期望薪资**: {expected_salary}")
            st.markdown(f"**最佳联系时间**: {best_time}")
        
        if languages:
            st.markdown(f"**语言能力**: {', '.join(languages)}")
        
        st.markdown("---")
        
        # 个人简介
        st.subheader("个人简介")
        st.write(introduction)
        
        # 专业技能
        st.subheader("专业技能")
        for skill in skills:
            st.markdown(f"- {skill}")
        
        # 座右铭
        if motto:
            st.markdown("---")
            st.markdown(f"> *{motto}*")

# 添加页脚说明
st.markdown("---")
st.caption("简历生成器 - 数据会实时更新，左侧表单修改后右侧预览将自动变化")
