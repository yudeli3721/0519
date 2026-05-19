import streamlit as st
import datetime

st.set_page_config(page_title="微型 TimeTree", layout="wide")

with st.sidebar:
    st.write("###  行事曆群組")
    st.radio("選擇群組", ["工作", "家庭", "朋友"])

view = st.segmented_control(
  "檢視模式",
  ["月視角", "週視角"],
  default="月視角"
)

col_left, col_right = st.columns(2)

with col_left: 
    st.write("###  行程主旨") 
    my_color = st.color_picker(
        "挑選辨識顏色",
        "#1A73E8"
    )

with col_right: 
    st.write("###  日期+時間") 
    today = st.date_input(
        "選擇日期",
        datetime.date.today()
    )
    meeting_time = st.time_input(
        "選擇時間"
    )

st.write("上面是大標題")
st.divider()
st.write("下面是內容區塊")

with st.popover("快速進階篩選"):
    st.checkbox("隱藏已過期行程")

