import streamlit as st
from openpyxl.styles.builtins import title

home=st.Page("home.py", title="首頁")
rate=st.Page("rate.py",title="取得匯率")
rss=st.Page("rss.py",title="取得rss")
weather = st.Page('weather.py', title='天氣資訊')
pg=st.navigation([home,rate,rss,weather])

pg.run()
#app.py 為主要分頁趨動入口 設立分頁 如 home.rate.rss 在app.py執行