import streamlit as st
import pandas as pd
import os
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
from query import *

st.set_page_config(page_title="UB-Beauty", layout='wide')


tab1, tab2 = st.tabs(["micro-persona-analytics", "brand-analytics"])

with tab1:
	with st.sidebar:
		st.set_option('deprecation.showPyplotGlobalUse', False)
		st.sidebar.header("UB Beauty")
		st.title('UB_BEAUTY DATA')
	# get data
	get_tbl_master = view_all_data();
	# convert data to dataframe
	df_all_data=pd.DataFrame(get_tbl_master)
	
	#switcher
	st.sidebar.header("Please filter the table")
	skin_type=st.sidebar.multiselect("Select Skin Type", options=df_all_data["skin_type"].unique(), default=df_all_data["skin_type"].unique())
	product_type=st.sidebar.multiselect("Select Product Type", options=df_all_data["product_type"].unique(), default=df_all_data["product_type"].unique())
	gender=st.sidebar.multiselect("Select Gender", options=df_all_data["gender"].unique(), default=df_all_data["gender"].unique())

	df_all_data_selection=df_all_data.query("skin_type==@skin_type & product_type==@product_type & gender==@gender")
	st.dataframe(df_all_data_selection)




	
