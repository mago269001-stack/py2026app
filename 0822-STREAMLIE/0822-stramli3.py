import streamlit as st
from openpyxl.styles.builtins import currency

st.title('Hello World!!! NEWS　World')
st.header('今日外匯新聞')
st.subheader('幣別外匯兌換')
st.write('美元兌換')
name=st.text_input("請輸入查詢幣別 :")
currency=st.selectbox("選項",[ "USD","JPY","EUR"])
if st.button("輸入"):
    st.write(name)
    st.write(currency)