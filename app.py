import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Dữ liệu 10 sinh viên
data = {
    "Ho_ten": [
        "Nguyễn Văn An",
        "Trần Thị Bích",
        "Lê Hoàng Cường",
        "Phạm Thị Dung",
        "Hoàng Văn Em",
        "Đỗ Thị Phương",
        "Bùi Văn Giang",
        "Vũ Thị Hương",
        "Ngô Văn Khải",
        "Phan Thị Lan",
    ],
    "Chuyen_can": [9.0, 8.0, 7.5, 6.0, 8.5, 9.5, 4.0, 7.0, 8.0, 5.5],
    "Giua_ky": [8.0, 7.5, 6.5, 5.0, 7.0, 9.0, 4.5, 6.5, 8.5, 6.0],
    "Cuoi_ky": [8.5, 8.0, 7.0, 5.5, 7.5, 8.5, 3.5, 6.5, 9.0, 5.0],
}
df = pd.DataFrame(data)

# Tính điểm tổng kết
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"] + 0.3 * df["Giua_ky"] + 0.5 * df["Cuoi_ky"]
).round(2)


# Xếp loại
def xep_loai(diem):
  if diem >= 8.5:
    return "Giỏi"
  elif diem >= 7.0:
    return "Khá"
  elif diem >= 5.0:
    return "Trung bình"
  else:
    return "Yếu"


df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Thống kê
dtb_lop = df["Tong_ket"].mean()
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_sinh_vien_dat = (df["Tong_ket"] >= 5.0).sum()

# Giao diện Streamlit Web App
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df, use_container_width=True)

st.subheader("Thống kê kết quả học tập của lớp")
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label="Điểm TB Lớp", value=f"{dtb_lop:.2f}")
with col2:
  st.metric(label="Số sinh viên Đạt", value=so_sinh_vien_dat)
with col3:
  st.metric(label="Tổng số sinh viên", value=len(df))

st.write(
    f"- **Sinh viên có điểm cao nhất:** {sv_max['Ho_ten']} ({sv_max['Tong_ket']}"
    " điểm)"
)
st.write(
    f"- **Sinh viên có điểm thấp nhất:** {sv_min['Ho_ten']} ({sv_min['Tong_ket']}"
    " điểm)"
)

st.subheader("Tra cứu thông tin cá nhân sinh viên")
selected_student = st.selectbox(
    "Chọn tên sinh viên để xem chi tiết:", df["Ho_ten"]
)
student_info = df[df["Ho_ten"] == selected_student].iloc[0]

st.info(f"Thông tin chi tiết của: **{selected_student}**")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Chuyên cần", student_info["Chuyen_can"])
c2.metric("Giữa kỳ", student_info["Giua_ky"])
c3.metric("Cuối kỳ", student_info["Cuoi_ky"])
c4.metric("Tổng kết", student_info["Tong_ket"])
c5.metric("Xếp loại", student_info["Xep_loai"])

st.subheader("Biểu đồ cột điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"], color="skyblue", edgecolor="black")
ax.set_xlabel("Họ và tên sinh viên", fontsize=11)
ax.set_ylabel("Điểm tổng kết", fontsize=11)
ax.set_title("Biểu đồ điểm tổng kết lớp học", fontsize=13, fontweight="bold")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
st.pyplot(fig)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 11px;'>Họ tên: Đặng"
    " Thanh Khoa | MSSV: [Điền MSSV của bạn]</p>",
    unsafe_allow_html=True,
)