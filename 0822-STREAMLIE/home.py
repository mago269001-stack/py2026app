import streamlit as st

# st.title('首頁')
# st.write('hello world')
# st.markdown("""
# ## title
#
# - test
# - test
#
# """)
with open("0822-STREAMLIE/type.md","r",encoding="utf-8")as f:
    st.markdown(f.read())
st.title("Hello~~")
# ("0822-STREAMLIE/type.md"打開的資料夾路徑,"r"閱讀,encoding="utf-8"中文字形)