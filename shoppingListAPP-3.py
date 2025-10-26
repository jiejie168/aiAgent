import streamlit as st

# Set the page configuration to include a logo
st.set_page_config(page_title="Grocery List App",
                   page_icon="https://github.com/SalvatoreRa/tutorial/blob/main/images/vegetable_basket_logo.jpg?raw=true")

# Initialize session state for grocery_items if it doesn't exist yet
if 'grocery_items' not in st.session_state:
    st.session_state.grocery_items = ['Apple', 'Banana', 'Carrot',
    'Milk', 'Eggs']
# Streamlit app interface
st.title('Grocery List App :banana: :apple: :egg:') # Main title of the app
# Display a header for the section where the user can add items
st.header('Add new item')


# Display the title image
st.image("https://github.com/SalvatoreRa/tutorial/blob/main/images/vegetables.jpg?raw=true",
         use_column_width=True)
st.caption("Image from [here](https://unsplash.com/it/@randyfath)")
# Add logo to the sidebar
st.sidebar.image("https://github.com/SalvatoreRa/tutorial/blob/main/images/vegetable_basket_logo.jpg?raw=true",
                 use_column_width=True)


# Text input to add a new item to the list
new_item = st.text_input("Type an item to add to your grocery list:")
# Button to add the new item to the list
'''
st.session_state allows temporary storage of values during a user session—
gradually filling up as interactions occur—this data is lost upon a full page reload or app restart.
'''
if st.button('Add Item'):
    if new_item:
        # Append the new item to the list stored in session state
        st.session_state.grocery_items.append(new_item)
        st.success(f"'{new_item}' has been added to your list!")
    else:
        st.warning("Please enter an item to add.")
# Display a subheader for the current grocery list
st.subheader('Current Grocery List')
# Display the current list of grocery items
st.write("### Items to Buy:")
for item in st.session_state.grocery_items:
    st.write(f"- {item}")

#conn = st.connection("my_database_sql",type='sql') # not working now
#df = conn.query("select * from my_beautiful_table")
#st.dataframe(df)