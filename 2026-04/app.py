import streamlit as st
import pandas as pd
import requests

# --- CẤU HÌNH HỆ THỐNG ---
# Thay 'TEN_USER' và 'TEN_REPO' bằng tên thật của bạn trên GitHub
GITHUB_USER = "TEN_USER_CUA_BAN"
REPO_NAME = "Content-Bank-Toeic-MrMinh"
FOLDER = "2026-04"

st.set_page_config(page_title="Quant System - Toeic Mr. Minh", layout="wide")

# Giao diện Sidebar
with st.sidebar:
    st.title("🛡️ Quant System")
    st.write("---")
    st.success("Trạng thái: Đang kết nối Real-time")
    refresh = st.button("🔄 CẬP NHẬT DỮ LIỆU MỚI")

# Tiêu đề chính giống ảnh mẫu
st.title("📊 Master Advisor & Real-Flow Engine")
st.info("Hệ thống tự động đồng bộ dữ liệu từ Kho lưu trữ GitHub")

# --- HÀM TỰ ĐỘNG LẤY DỮ LIỆU TỪ GITHUB ---
def get_all_reports():
    url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{FOLDER}"
    response = requests.get(url)
    if response.status_code == 200:
        return [file['name'] for file in response.json() if file['name'].endswith('.md')]
    return []

# --- HIỂN THỊ DỮ LIỆU ---
tabs = st.tabs(["🚀 BÁO CÁO MỚI NHẤT", "📅 LỊCH SỬ SĂN TIN", "⚙️ CẤU HÌNH"])

with tabs[0]:
    files = get_all_reports()
    if files:
        latest_file = sorted(files)[-1] # Lấy file mới nhất theo tên
        st.subheader(f"📍 Bản tin mới nhất: {latest_file}")
        
        # Đọc nội dung file từ GitHub và hiển thị
        raw_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/{FOLDER}/{latest_file}"
        content = requests.get(raw_url).text
        st.markdown(content) # Hiển thị bảng Markdown ngay tại đây
    else:
        st.warning("Chưa có dữ liệu nào trong kho lưu trữ.")

with tabs[1]:
    st.subheader("Toàn bộ lịch sử thu thập")
    if files:
        selected_file = st.selectbox("Chọn ngày để xem lại:", sorted(files, reverse=True))
        raw_url_hist = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/{FOLDER}/{selected_file}"
        st.markdown(requests.get(raw_url_hist).text)

with tabs[2]:
    st.write("Cấu hình API và kết nối Gem.")
