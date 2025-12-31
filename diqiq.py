import streamlit as st
import pandas as pd
import random
import os
import time

# 设置页面配置
st.set_page_config(
    page_title="多功能应用整合",
    page_icon="🚀",
    layout="wide"
)

# 自定义样式：优化顶部导航栏外观
st.markdown("""
    <style>
        /* 顶部导航栏容器 */
        .top-nav {
            display: flex;
            justify-content: center;
            background-color: #f8f9fa;
            padding: 10px 0;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        /* 导航按钮样式 */
        .nav-button {
            border: none;
            padding: 0.8rem 1.5rem;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 500;
            transition: all 0.3s ease;
            margin: 0 5px;
            min-width: 120px;
            text-align: center;
        }
        .nav-button-selected {
            background-color: #0EA5E9;
            color: white;
            box-shadow: 0 2px 8px rgba(14, 165, 233, 0.3);
        }
        .nav-button-unselected {
            background-color: #ffffff;
            color: #333;
            border: 1px solid #e0e2e5;
        }
        .nav-button-unselected:hover {
            background-color: #f0f2f6;
            transform: translateY(-2px);
        }
        /* 主标题样式 */
        .main-title {
            text-align: center;
            color: #1E3A8A;
            font-size: 2.5rem;
            margin: 20px 0;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# 初始化会话状态：记录当前选中的页面
if "current_page" not in st.session_state:
    st.session_state.current_page = "音乐播放器"

# 定义所有功能页面名称
page_names = ["音乐播放器", "图片相册", "小组档案", "动漫视频", "美食仪表盘", "简历生成器"]

# 创建顶部导航栏
st.markdown('<h1 class="main-title">多功能应用整合平台</h1>', unsafe_allow_html=True)

# 创建导航栏容器
st.markdown('<div class="top-nav">', unsafe_allow_html=True)

# 创建与页面数量匹配的列
cols = st.columns(len(page_names))

for idx, col in enumerate(cols):
    page_name = page_names[idx]
    # 判断当前按钮是否为选中状态，应用不同样式
    if st.session_state.current_page == page_name:
        button_style = "nav-button nav-button-selected"
    else:
        button_style = "nav-button nav-button-unselected"
    
    # 渲染按钮并处理点击事件
    with col:
        if st.button(
            page_name,
            key=f"nav_{idx}",
            use_container_width=True
        ):
            st.session_state.current_page = page_name
            st.rerun()  # 重新运行应用以切换页面

st.markdown('</div>', unsafe_allow_html=True)

# 音乐播放器页面
def music_player():
    st.title("🎵 简易音乐播放器")
    
    # 初始化会话状态
    if "current_idx" not in st.session_state:
        st.session_state.current_idx = 0
    if "is_playing" not in st.session_state:
        st.session_state.is_playing = False
    if "progress" not in st.session_state:
        st.session_state.progress = 0
    
    # 歌曲数据
    songs = [
        {
            "title": "起风了",
            "artist": "冯沁苑",
            "duration": "5:25",
            "cover": "http://p2.music.126.net/diGAyEmpymX8G7JcnElncQ==/109951163699673355.jpg?param=130y130",
            "audio": "https://music.163.com/song/media/outer/url?id=1330348068"
        },
        {
            "title": "碎碎念",
            "artist": "队长", 
            "duration": "2:12",
            "cover": "http://p1.music.126.net/RYIrCEYzgeAD85DJ0rgOQA==/109951169256300966.jpg?param=130y130",
            "audio": "https://music.163.com/song/media/outer/url?id=2097443876"
        },
        {
            "title": "于是",
            "artist": "郑润泽",
            "duration": "3:52", 
            "cover": "http://p2.music.126.net/BtXjoRNLCZjoSV-3Ag3M0Q==/109951164458656122.jpg?param=640y300",
            "audio": "https://music.163.com/song/media/outer/url?id=1303464858"
        }
    ]
    
    # 切换函数
    def prev_song():
        st.session_state.current_idx = (st.session_state.current_idx - 1) % len(songs)
        st.session_state.progress = 0
    
    def next_song():
        st.session_state.current_idx = (st.session_state.current_idx + 1) % len(songs)
        st.session_state.progress = 0
    
    # 播放控制
    def toggle_play():
        st.session_state.is_playing = not st.session_state.is_playing
    
    # 获取当前歌曲
    current_song = songs[st.session_state.current_idx]
    
    # 显示专辑封面和歌曲信息
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.image(current_song["cover"], caption="专辑封面", width=250)
    
    with col2:
        st.markdown(f"## {current_song['title']}")
        st.markdown(f"**歌手**: {current_song['artist']}")
        st.markdown(f"**时长**: {current_song['duration']}")
    
    # 控制按钮
    col3, col4, col5 = st.columns([1, 1, 2])
    with col3:
        st.button("⏮️ 上一首", on_click=prev_song, use_container_width=True)
    with col4:
        play_text = "⏸️ 暂停" if st.session_state.is_playing else "▶️ 播放"
        st.button(play_text, on_click=toggle_play, use_container_width=True)
    with col5:
        st.button("⏭️ 下一首", on_click=next_song, use_container_width=True)
    
    # 进度条
    st.progress(st.session_state.progress / 100)
    
    # 时间显示
    st.markdown(f"0:00 / {current_song['duration']}")
    
    # 音频播放器
    st.audio(current_song["audio"])

# 图片相册页面
def image_gallery():
    st.title("🖼️ 我的图片相册")
    
    # 准备图片数据：列表中每个元素是(图片路径, 图注)
    image_data = [
         ("cat1.png", "橘白相间的猫咪，正慵懒地晒太阳"),
    ("dog.png", "活泼的小狗在草地上奔跑"),
    ("flower.png", "盛放的向日葵，充满生机")
    ]
    
    # 初始化会话状态，记录当前显示的图片索引
    if "img_current_idx" not in st.session_state:
        st.session_state.img_current_idx = 0
    
    # 定义切换图片的函数
    def prev_image():
        st.session_state.img_current_idx = (st.session_state.img_current_idx - 1) % len(image_data)
    
    def next_image():
        st.session_state.img_current_idx = (st.session_state.img_current_idx + 1) % len(image_data)
    
    # 显示当前图片和图注
    current_img, current_caption = image_data[st.session_state.img_current_idx]
    st.image(current_img, caption=current_caption, use_column_width=True)
    
    # 按钮布局：上一张 + 下一张
    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ 上一张", on_click=prev_image, use_container_width=True)
    with col2:
        st.button("➡️ 下一张", on_click=next_image, use_container_width=True)

# 小组档案页面
def group_profile():
