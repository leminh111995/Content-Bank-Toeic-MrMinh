import streamlit as st
import google.generativeai as genai
import pandas as pd
from datetime import datetime

# --- 1. CẤU HÌNH HỆ THỐNG & API ---
# Đây là mã API bạn đã cung cấp
API_KEY = "AQ.Ab8RN6KbAuD58J-PEQR8vFVNlevhf1cd2cxlbxWoBIH1V4IFPg"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Lỗi cấu hình AI ban đầu: {e}")

# --- 2. GIAO DIỆN PHONG CÁCH QUANT SYSTEM ---
st.set_page_config(page_title="Quant System V14.1 - Toeic Mr. Minh", layout="wide", page_icon="🛡️")

# CSS làm đẹp giao diện
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background-color: #1e40af; color: white; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #1e3a8a; border: 1px solid #3b82f6; }
    .status-bar { padding: 15px; border-radius: 10px; background-color: white; border-left: 6px solid #1e40af; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .report-card { padding: 20px; background-color: #ffffff; border-radius: 10px; border: 1px solid #e2e8f0; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TIÊU ĐỀ CHÍNH ---
st.markdown('<h1 style="color: #1e3a8a; font-family: sans-serif;">🛡️ Master Advisor & Real-Flow Engine</h1>', unsafe_allow_html=True)
st.markdown('<div class="status-bar">🎯 Trạng thái: Đang kết nối trực tiếp với Hệ sinh thái AI Gemini 2026</div>', unsafe_allow_html=True)
st.write("")

# --- 4. SIDEBAR (BẢNG ĐIỀU KHIỂN BÊN TRÁI) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/10061/10061834.png", width=100)
    st.title("TRUNG TÂM ĐIỀU KHIỂN")
    st.write("---")
    
    # NÚT BẤM QUAN TRỌNG NHẤT
    if st.button("🚀 KÍCH HOẠT MÁY QUÉT", type="primary"):
        with st.spinner("Hệ thống đang quét Threads, TikTok và các Social Signals..."):
            # Prompt Ver 2026 Pro của bạn
            prompt = """Kích hoạt máy quét xu hướng cho Toeic Mr. Minh. 
            Yêu cầu: Thực hiện quy trình quét tin Ver 2026 Pro. 
            Tập trung vào Threads/TikTok, xác thực nguồn. 
            Chất xuất dữ liệu dưới dạng BẢNG MARKDOWN gồm 7 cột: 
            Trend, Từ khóa, Bằng chứng, Ngòi nổ, Hook TOEIC, Định dạng & Đối tượng, Độ nóng."""
            
            try:
                response = model.generate_content(prompt)
                # Lưu kết quả vào bộ nhớ tạm của trang web
                st.session_state.data_output = response.text
                st.success("Dữ liệu đã được thu thập thành công!")
            except Exception as e:
                # HIỂN THỊ LỖI CHI TIẾT ĐỂ CHÚNG TA CÙNG SỬA
                st.error(f"⚠️ LỖI HỆ THỐNG TRẢ VỀ: {e}")
                st.info("Mẹo: Nếu lỗi báo 'API Key not found', hãy kiểm tra lại mã API trong code.")

# --- 5. KHU VỰC HIỂN THỊ CHÍNH (TABS) ---
tab1, tab2, tab3 = st.tabs(["🚀 BÁO CÁO MỚI NHẤT", "📅 LỊCH SỬ SĂN TIN", "⚙️ CẤU HÌNH"])

with tab1:
    if 'data_output' in st.session_state:
        st.markdown('<div class="report-card">', unsafe_allow_html=True)
        st.subheader("Bản phân tích xu hướng 12h qua")
        st.markdown(st.session_state.data_output)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.write("---")
        st.caption("Gợi ý: Bạn có thể copy bảng này để đăng trực tiếp lên Fanpage Toeic Mr. Minh.")
    else:
        st.warning("Hàng chưa về! Hãy nhấn nút '🚀 KÍCH HOẠT MÁY QUÉT' ở menu bên trái để bắt đầu.")

with tab2:
    st.info("Chưa có tệp tin lịch sử. Khi bạn lưu dữ liệu vào GitHub, chúng sẽ xuất hiện ở đây.")

with tab3:
    st.write("Hệ thống đang chạy trên Model: **Gemini-1.5-Flash**")
    st.write(f"API Key hiện tại: `{API_KEY[:5]}...{API_KEY[-5:]}`")
