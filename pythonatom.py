import pandas as pd
import ydata_profiling as pp
from streamlit_pandas_profiling import st_profile_report
import streamlit as st
import sweetviz as sv

st.write("# INSIGHT company")
q=st.text_input("Enter your Name")
w=st.text_input("Enter your Phone Number")
no=st.number_input("Enter your age",min_value=0,max_value=120)
a=open('hello1.txt','a')
write=q+"\n"+w+"\n"+str(no)+"\n\n"
a.write(write)
if no>0:
    st.markdown(" Now this app is to give you the detailed analysis of the CSV file which is uploaded. We are gonna analysis and provide you the insights of the file ")
    ft=st.file_uploader("Enter your CSV file",type=('csv','xlsx'))
    st.divider()
    if ft is not None:
        tab1,tab2=st.tabs(["Data","Only Analysis"])
        df=pd.read_csv(ft)
        tab1.write(df)
        report=pp.ProfileReport(df,dark_mode=True)
        tab2.write("Now let us see the detailed analysis of the CSV file")
        tab2.info("You can download the Overview in the reproduction column")
        tab2.write(st_profile_report(report))
        if st.button("Click me for more info"):
            my_report = sv.analyze(df)
            my_report.show_html()
    else:
            st.warning("Please upload the file")
