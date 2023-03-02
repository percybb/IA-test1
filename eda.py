import pandas as pd
import numpy as np
import matplotlib as plt
import streamlit as st
import seaborn as sb


def eda_fun(df):
    st.subheader("Exploratory data analisys")
    st.write("EDA")
    if st.checkbox("show raw Data"):
        st.write(df)
    if st.checkbox("Show missng values"):
        st.write(df.isna().sum())

    if st.checkbox("show Descriptive statistics"):
        st.write(df.describe())

    if st.checkbox("Show Scatter plot"):
        st.write("")
