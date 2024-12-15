import streamlit as st

import pandas as pd
import numpy as np


# st.title : 웹 페이지의 타이틀 설정
st.title('steamlit Example app')

# st.header : 웹페이지의 헤더 텍스트 설정
st.header('steamlit Example')

# ============================================
# st.button : 버튼 위젯을 표시
st.subheader('st.button') # st.subheader : 서브헤더 텍스트 설정
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

# ============================================
# st.dataframe : dataframe 의 테이블 추가
st.subheader('st.dataframe') # st.subheader : 서브헤더 텍스트 설정
df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},    
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
st.dataframe(df, use_container_width=True)

# ============================================
# st.slider : 슬라이더 입력 위젯을 표시
st.subheader('st.slider') # st.subheader : 서브헤더 텍스트 설정
age = st.slider('당신의 나이는?', 0, 130, 25)
st.write("나는 ", age, '살입니다')

# ============================================
# st.line_chart : 라인 차트를 표시
st.subheader('st.line_chart') # st.subheader : 서브헤더 텍스트 설정
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# ============================================
# st.selectbox : 선택 위젯을 표시
st.subheader('st.selectbox') # st.subheader : 서브헤더 텍스트 설정
option = st.selectbox(
     '가장 좋아하는 색상은 무엇인가요?',
     ('파랑', '빨강', '초록'))

st.write('당신이 좋아하는 색상은 ', option)

# ============================================
# st.multiselect : 여러 항목을 선택할 수 있는 위젯을 표시
st.subheader('st.multiselect') # st.subheader : 서브헤더 텍스트 설정
options = st.multiselect(
     '가장 좋아하는 색상은 무엇인가요',
     ['초록', '노랑', '빨강', '파랑'],
     ['노랑', '빨강'])

st.write('당신이 선택한 색상:', options)

# ============================================
# st.checkbox : 체크박스 위젯을 표시
st.subheader('st.checkbox') # st.subheader : 서브헤더 텍스트 설정
st.write ('주문하고 싶은 것이 무엇인가요?')

icecream = st.checkbox('아이스크림')
coffee = st.checkbox('커피')
cola = st.checkbox('콜라')

if icecream:
     st.write("좋아요! 여기 더 많은 🍦")

if coffee: 
     st.write("알겠습니다, 여기 커피 있어요 ☕")

if cola:
     st.write("여기 있어요 🥤")
    
    
