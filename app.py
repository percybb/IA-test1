import pandas as pd
import numpy as np
import streamlit as st
import matplotlib as plt
from sklearn.datasets import load_iris
# from sklearn.neighbors import neighbors_class

import plotly.express as px
from eda import eda_fun
dataset = load_iris()
# print(dataset)


X = dataset.data
# print(data)

Y = dataset.target
# print(output)

targes_name = dataset.target_names
# print(targes_name)

feature_names = dataset.feature_names
# print(feature_names)


df = pd.DataFrame(data=X, columns=feature_names)
# print(df)

st.set_page_config(page_title="Eda page",
                   layout="centered",
                   initial_sidebar_state="auto"
                   )

st.title("EDA and Predictive Modeling")

option = ["EDA", "Predictive modelling"]

selected_option = st.sidebar.selectbox("Selected Option", option)

if selected_option == "EDA":
    eda_fun(df)


elif selected_option == "Predictive modelling":
    st.subheader("Predictive Modelling")
    st.write("Predictive modelling")
