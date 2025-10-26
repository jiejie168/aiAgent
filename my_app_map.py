#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Title for the app
st.title("Simple Streamlit App with a map")
# Create a sample DataFrame
city_data = {
'City': ['Palermo', 'Syracuse', 'Catania', 'Agrigento'],
'latitude': [38.1157, 37.0757, 37.5079, 37.2982],
'longitude': [13.3615, 15.2867, 15.0830, 13.5763]
}
city_data = pd.DataFrame(city_data)

# Display the DataFrame
st.write("Here is the sample DataFrame:")
st.dataframe(city_data)
# Create a map
st.map(city_data)
# Display the plot in Streamlit
#st.pyplot(fig)

