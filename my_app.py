import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Title for the app
st.title("Simple Streamlit App with Box Plot")
# Create a sample DataFrame
data = {
'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
'Values': [10, 20, 15, 25, 30, 20, 35, 40, 45]
}
df = pd.DataFrame(data)
# Display the DataFrame
st.write("Here is the sample DataFrame:")
st.dataframe(df)
# Create a box plot
fig, ax = plt.subplots()
df.boxplot(column='Values', by='Category', ax=ax, grid=False)
plt.title("Box Plot of Values by Category")
plt.suptitle("") # Remove the automatic subtitle
plt.xlabel("Category")
plt.ylabel("Values")
# Display the plot in Streamlit
st.pyplot(fig)