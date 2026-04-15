import streamlit as st
import google.generativeai as genai
import pandas as pd
from datetime import datetime
import requests

# --- CẤU HÌNH HỆ THỐNG ---
API_KEY = "AQ.Ab8RN6KbAuD58J-PEQR8vFVNlevhf1cd2cxlbxWoBIH1V4IFPg"

# Kết nối AI
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Quant System V14.1", layout="wide", page_icon="🛡️")

# Làm đẹp giao diện
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #1e40af; color: white; font-weight: bold; }
    .status-box { padding: 15px; border-radius: 10px; background-color: #f0fdf4; border-left: 5px solid #22c55e; color: #166534; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: NƠI RA LỆNH ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/10061/10061834.png", width=80)
    st.title("TRUNG TÂM ĐIỀU KHIỂN")
    st.write("---")
    
    # ĐÂY LÀ CÁI NÚT BẠN CẦN BẤM
    if st.button("🚀 KÍCH HOẠT MÁY QUÉT", type="primary"):
        with st.spinner("Đang quét xu hướng toàn cầu..."):
            prompt = "Kích hoạt máy quét xu hướng cho Toeic Mr. Minh. Thực hiện quy trình Ver 2026 Pro. Xuất bảng Markdown 7 cột."
            try:
                response = model.generate_content(prompt)
                st.session_state.data = response.text
                st.success("Đã có dữ liệu mới!")
            except:
                st.error("Mã API có vấn đề hoặc chưa kích hoạt.")

# --- THÂN TRANG CHÍNH ---
st.markdown(f'<h1>🛡️ Master Advisor & Real-Flow Engine</h1>', unsafe_allow_html=True)
st.markdown('<div class="status-box">Trạng thái: Đang kết nối Real-time với AI Gemini</div>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🚀 BÁO CÁO MỚI NHẤT", "📅 LỊCH SỬ"])

with tab1:
    if 'data' in st.session_state:
        st.subheader("📍 Dữ liệu vừa quét được:")
        st.markdown(st.session_state.data) # BẢNG SẼ HIỆN Ở ĐÂY
        st.write("---")
        st.info("Để lưu bảng này vĩnh viễn vào GitHub, bạn hãy copy nó và dán vào file mới trên GitHub nhé!")
    else:
        st.warning("Hàng chưa về! Hãy nhấn nút '🚀 KÍCH HOẠT MÁY QUÉT' ở menu bên trái.")

with tab2:
    st.write("Khi nào bạn có file trên GitHub, chúng sẽ hiện ở đây.")
