import pandas as pd
import ydata_profiling as pp
import base64  # Add this import
from streamlit_pandas_profiling import st_profile_report
import streamlit as st

st.write("# INSIGHT company")
q = st.text_input("Enter your Name")
w = st.text_input("Enter your Phone Number")
no = st.number_input("Enter your age", min_value=0, max_value=120)
a = open('database.txt', 'a')
write = q + "\n" + w + "\n" + str(no) + "\n\n"
a.write(write)
def get_html_download_link(html_content, text, filename):
    b64 = base64.b64encode(html_content.encode()).decode()
    href = f'<a href="data:text/html;base64,{b64}" download="{filename}">{text}</a>'
    return href

if no > 0:
    st.markdown("Now this app is to give you a detailed analysis of the CSV file that is uploaded. We are going to analyze and provide you with the insights of the file")
    ft = st.file_uploader("Enter your CSV file", type=('csv', 'xlsx'))
    st.divider()
    if ft is not None:
        tab1, tab2 = st.tabs(["Data", "Only Analysis"])
        df = pd.read_csv(ft)
        tab1.write(df)
        report = pp.ProfileReport(df, dark_mode=True)
        tab2.write("Now let us see the detailed analysis of the CSV file")
        tab2.info("You can download the Overview in the reproduction column")
        tab2.write(st_profile_report(report))         
else:
    st.warning("Please upload the file")

