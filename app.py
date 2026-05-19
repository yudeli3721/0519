import streamlit as st
st.set_page_config(page_title="微型 TimeTree", layout="wide")

with st.sidebar:
    st.write("###  行事曆群組")
    st.radio("選擇群組", ["工作", "家庭", "朋友"])

col_left, col_right = st.columns([1, 3], gap="large")


with col_left: 
    st.write("###  新增區") 
    st.button("按鈕放左邊")

with col_right: 
    st.write("###  設定區") 
    st.button("控制項放右邊")
    with st.container(border=True): 
        tab1, tab2 = st.tabs(["本月行程", "已封存行程"])

st.write("上面是大標題")
st.divider()
st.write("下面是內容區塊")

with st.popover("快速進階篩選"):
    st.checkbox("隱藏已過期行程")

st.columns(2)
    my_color = st.color_picker(
     "挑選辨識顏色",
     "#1A73E8"
    )
    
    meeting_time = st.time_input(
      "選擇時間"
    )
    
    import datetime
    today = st.date_input(
      "選擇日期",
      datetime.date.today()
    )
    
    title = st.text_input(
      "行程主旨",
      placeholder="請填寫會議名稱..."
    )
