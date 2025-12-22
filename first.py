import streamlit as st
import pandas as pd

st.title("广西职业示范学院食堂人流量统计")

data = {
    '隆江猪脚饭':[568, 868, 670, 884, 144],
    '早点来早餐':[820, 884, 768, 524, 709],
    '砂锅米线':[577, 532, 996, 929, 694]
}

df=pd.DataFrame(data)

st.dataframe(df)

st.table(df)


