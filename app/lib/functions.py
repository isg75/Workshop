import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import folium
from streamlit_folium import st_folium


def map_plot(df):

	df_cat = df.select_dtypes(object)
	st.subheader('Avistamientos')  

	m = folium.Map(location=[40.781781, -73.966787], zoom_start=14)

	colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']

	var_cat = st.sidebar.selectbox("Colorear según la variable categórica: ",df_cat.columns.insert(0,None))

	if (var_cat == None):
		for i in range(len(df)):
			folium.CircleMarker(
    		location=[df.iloc[i,1],df.iloc[i,0]],
    		radius=2,
    		icon=folium.Icon(icon="cloud")).add_to(m)

	elif ( (var_cat != None) and (df_cat[var_cat].nunique() <= len(colors)) ):

		cmap = dict(zip(list(df[var_cat].unique()), colors[:df[var_cat].nunique()]))

		for i in range(len(df)):
			folium.CircleMarker(
        	location=[df.iloc[i,1],df.iloc[i,0]],
        	radius=2,
        	color=cmap[df.loc[i,var_cat]],
        	icon=folium.Icon(icon="cloud")).add_to(m)    

	st_data = st_folium(m, width=725)


def frequency_plot(df, column_count_plot, hue_opt):
        
	fig = sns.countplot(x=column_count_plot,data=df,hue=hue_opt)
	st.pyplot()


def boxplot_plot(df, column_box_plot_X, column_box_plot_Y):

	fig = sns.boxplot(x=column_box_plot_X, y=column_box_plot_Y,data=df,palette="Set3")
	st.pyplot()


def distribution_plot(df, column_dist_plot, hue_opt=None):

	if (hue_opt == None):
		fig = sns.displot(data=df, x=column_dist_plot,kde=True)
	else:
		fig = sns.displot(data=df, x=column_dist_plot, hue=hue_opt,kde=True)
	st.pyplot()

