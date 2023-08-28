import pandas as pd
import streamlit as st
from datatypes import datatypes
from tab_q import tab_q
from vis_q import vis_q
from vis_null import vis_null
st.set_page_config(layout='wide')

def main():
    options = ["Main","Data Types Quiz","Quantitative Variablen (Tabelle)",
    "Quantitative Variablen (Diagramm)","Null-Values (Diagramm)"]
    choice = st.sidebar.selectbox("Menu",options, key = '1')
    if choice == "Main":
        st.markdown('<div style="text-align: center;"><h1><em>--- Data Analytics Quiz ---</em></h1></div>', unsafe_allow_html=True)
        a01, a02, a03 = st.columns (3)
        with a03: 
            st.image("./logo_70.jpeg")
        st.write("   ")
        st.subheader("Inhalte:")
        # a11,a12 = st.columns(2)
        # with a11:
    elif choice == "Data Types Quiz":
        datatypes()
    elif choice == "Quantitative Variablen (Tabelle)":
        tab_q()
    elif choice == "Quantitative Variablen (Diagramm)":
        vis_q()
    elif choice == "Null-Values (Diagramm)":
        vis_null()
main()

