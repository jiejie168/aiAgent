import pandas as pd
import streamlit as st
import requests
import os
from fpdf import FPDF
from geopy import Nominatim
import folium
import webbrowser
from IPython.display import display

st.set_page_config(page_title="Grocery List App",  layout= "wide")
global df
# function for the add of grocery list
def grocerylist():
    data = []
    # Initialize session state for grocery_items if it doesn't exist yet
    if 'grocery_items' not in st.session_state:
        st.session_state.grocery_items = ['Apple', 'Banana', 'Carrot', 'Milk', 'Eggs']
        st.session_state.quantity_at_home={'Apple':0, 'Banana':0, 'Carrot':0, 'Milk':0, 'Eggs':0}
        st.session_state.quantity_to_take = {'Apple': 0, 'Banana': 0, 'Carrot': 0, 'Milk': 0, 'Eggs': 0}
        st.session_state.taken={'Apple': 0, 'Banana': 0, 'Carrot': 0, 'Milk': 0, 'Eggs': 0}
    # Streamlit app interface
    st.title('Grocery List App :banana: :apple: :egg:') # Main title of the app
    # Display a header for the section where the user can add items
    st.header('Add new item')

    # Text input to add a new item to the list
    new_item = st.text_input("Type an item to add to your grocery list:")

    # Button to add the new item to the list
    if st.button('Add Item'):
        if new_item:
            # Append the new item to the list stored in session state
            st.session_state.grocery_items.append(new_item)
            st.session_state.quantity_at_home[new_item]=0
            st.session_state.quantity_to_take[new_item]=0
            st.session_state.taken[new_item]=0
            st.success(f"'{new_item}' has been added to your list!")
        else:
            st.warning("Please enter an item to add.")

    # Display a subheader for the current grocery list
    st.subheader('Current Grocery List')

    col1, col2 = st.columns(2)
    for i, item in enumerate(st.session_state.grocery_items):
        with col1 if i% 2 == 0 else col2:
            st.markdown(f"**{item}**")
            quantity_at_home=st.slider(f"Quantity at home",0,12,
                                       st.session_state.quantity_at_home[item],key=f"home_{item}")
            st.session_state.quantity_at_home[item]=quantity_at_home

            quantity_to_take=st.slider(f"Quantity to take",0,12,
                                       st.session_state.quantity_to_take[item],key=f"take_{item}")
            st.session_state.quantity_to_take[item]=quantity_to_take

            taken=st.checkbox(f"Take", st.session_state.taken[item], key=f"taken_{item}")
            st.session_state.taken[item]=taken
            data.append([item, quantity_at_home, quantity_to_take, "Yes" if taken else "No"])

    df=pd.DataFrame(data,columns=['Name', 'Quantity at Home', 'Quantity to Take', 'Taken'])
    st.table(df)
    # progress bar
    taken_count=sum(1 for item in st.session_state.taken.values() if item)
    total_items=len(st.session_state.grocery_items)
    progress=taken_count / total_items if total_items > 0 else 0
    st.subheader('Progress Bar of Current Grocery List')
    st.progress(progress)
    st.write(f"{taken_count} out of {total_items} items taken ({progress*100:.2f}%)")
    return df

# Function to generate PDF
def generate_pdf(df,note):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True,margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    logo_path="https://github.com/SalvatoreRa/tutorial/blob/main/images/vegetable_basket_logo.jpg?raw=true"
    logo_url="https://github.com/SalvatoreRa/tutorial/blob/main/images/vegetable_basket_logo.jpg?raw=true"
    response=requests.get(logo_url)
    with open('vegetable_basket_logo.jpg', 'wb') as f:
        f.write(response.content)
    pdf.image(logo_path, 10,10,30)
    pdf.cell(200,10,"Grocery List", ln=True,align="C")
    pdf.ln(20)
    for index, row in df.iterrows():
        pdf.cell(0,10,f"{row['Name']}- At home: {row['Quantity at Home']} "
                      f"- To take: {row['Quantity to Take']}-"
                      f"Taken: {row['Taken']}", ln=True,align="C")
    pdf.ln(20)
    pdf.cell(200, 10, note, ln=True, align="C")
    pdf_output=os.path.join(os.getcwd(),'grocery_list.pdf')
    pdf.output(pdf_output)
    return pdf_output

# Directly download the PDF when the button is clicked
# if st.sidebar.button('Download list as PDF'):
#     pdf_file=generate_pdf()
#     with open (pdf_file, 'rb') as f:
#         st.sidebar.download_button("Download Grocery List PDF", f,
#                                    file_name="grocery_list.pdf",
#                                    mime="application/pdf", key="download_pdf", on_click=None)

def main():
    # sidebar navigation
    with st.sidebar:
        st.title("Navigation")
        st.subheader("Go to")
        page=st.radio(label="Go to",options=["Grocery list","Notes","Find Supermarkets"],
                      index=0,label_visibility="collapsed")
    # main content by pages
    st.session_state.notes = ""
    if page=="Grocery list":
        df=grocerylist()
    elif page=="Notes":
        st.header("📝 Notes")
        st.session_state.notes=st.text_area("Write your notes here :",st.session_state.notes)
        if st.button("Save Notes"):
            st.subheader("Notes saved successfully!")
    else:
        st.title("🗺️ Find Nearby Supermarkets (OSM)")
        # get users location
        location_input=st.text_input("Enter your location (City, Address, or Coordinates):")
        if st.button("Find Supermarkets") and location_input:
            geolocator=Nominatim(user_agent="Mozilla/5.0")
            location=geolocator.geocode(location_input)
            if location:
                st.success(f"Location found: {location.address}")
                # create a map
                m=folium.Map(location=[location.latitude,location.longitude], zoom_start=14)
                folium.Marker(location=[location.latitude,location.longitude],tooltip="Your location",
                              icon=folium.Icon(color="blue")).add_to(m)
                # Display the map
                m.save("map.html")
                webbrowser.open("map.html")
                #display(m)
                #m.save(" my_map1.html ")

    if st.sidebar.button('Download list as PDF'):
        pdf_file = generate_pdf(df,st.session_state.notes)
        with open(pdf_file, 'rb') as f:
            st.sidebar.download_button("Download Grocery List PDF", f,
                                       file_name="grocery_list.pdf",
                                       mime="application/pdf", key="download_pdf", on_click=None)

if __name__=='__main__':
    main()