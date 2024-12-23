import streamlit as st
import pandas as pd
import sqlalchemy
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터베이스 연결 설정
# DB_URL = "postgresql+psycopg2://username:password@localhost/dbname"
DB_URL = "postgresql+psycopg2://postgres:1111@localhost/postgres"

engine = sqlalchemy.create_engine(DB_URL)

# 데이터 가져오는 함수
@st.cache_data
def fetch_data():
    query = "SELECT * FROM reports ORDER BY report_date"
    return pd.read_sql(query, con=engine)

# Streamlit 애플리케이션
st.title("📊 레포트 프로그램")


# 데이터 로드
st.sidebar.header("필터")
data = fetch_data()

# 데이터 필터링
st.sidebar.subheader("날짜 필터")
date_range = st.sidebar.date_input("날짜 범위 선택", [])
if date_range:
    data = data[
        (data["report_date"] >= pd.to_datetime(date_range[0])) &
        (data["report_date"] <= pd.to_datetime(date_range[1]))
    ]

st.sidebar.subheader("카테고리 필터")
category_filter = st.sidebar.multiselect("카테고리 선택", 
                                         data["category"].unique(), 
                                         default=data["category"].unique())
if category_filter:
    data = data[data["category"].isin(category_filter)]

# 데이터 미리보기
st.subheader("📋 데이터 미리보기")
st.dataframe(data)

# 요약 레포트
st.subheader("📄 요약 레포트")
if not data.empty:
    summary = data.groupby("category")["sales_amount"].sum().reset_index()
    st.write(summary)
else:
    st.write("선택된 데이터가 없습니다.")

# 그래프 시각화
st.subheader("📈 매출 그래프")
if not data.empty:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=data, x="report_date", 
                y="sales_amount", 
                hue="category", ax=ax)
    ax.set_title("날짜별 카테고리 매출")
    st.pyplot(fig)
else:
    st.write("그래프를 표시할 데이터가 없습니다.")

# 다운로드 버튼 추가
st.sidebar.subheader("📥 다운로드")
if not data.empty:
    csv = data.to_csv(index=False)
    st.sidebar.download_button(label="CSV 다운로드", 
                               data=csv, file_name="report.csv", 
                               mime="text/csv")
else:
    st.sidebar.write("다운로드할 데이터가 없습니다.")
