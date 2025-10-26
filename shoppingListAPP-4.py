import streamlit as st
data = []
# Initialize session state for grocery_items if it doesn't exist yet
if 'grocery_items' not in st.session_state:
    st.session_state.grocery_items = ['Apple', 'Banana', 'Carrot',
    'Milk', 'Eggs']
    quantity_at_home = [3, 3, 5, 6, 7]
    quantity_to_take = [2, 3, 2, 4, 6]
    # Streamlit app interface
    st.title('Grocery List App :banana: :apple: :egg:') # Main title of the app
    # Display a header for the section where the user can add items
    st.header('Add new item')

# Text input to add a new item to the list
new_item = st.text_input("Type an item to add to your grocery list:")
num_home=st.text_input("Type the quantity you would like to buy at home:")
num_buy=st.text_input("Type the quantity you would like to buy:")
# Button to add the new item to the list
if st.button('Add Item'):
    if new_item:
        # Append the new item to the list stored in session state
        st.session_state.grocery_items.append(new_item)
        st.session_state.quantity_to_buy.append(num_home)
        st.session_state.quantity_to_take.append(num_buy)
        st.success(f"'{new_item}' has been added to your list!")
    else:
        st.warning("Please enter an item to add.")
# Display a subheader for the current grocery list
st.subheader('Current Grocery List')


col1, col2 = st.columns(2)
for i, item in enumerate(st.session_state.grocery_items):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"**{item}**")
        quantity_at_home = st.slider(f"Quantity at home", 0, 12,
                                     st.session_state.quantity_at_home[item], key=f"home_{item}")
        st.session_state.quantity_at_home[item] = quantity_at_home
        quantity_to_take = st.slider(f"Quantity to take", 0, 12,
                                     st.session_state.quantity_to_take[item], key=f"take_{item}")
st.session_state.quantity_to_take[item] = quantity_to_take
taken = st.checkbox(f"Taken", st.session_state.taken[item],key=f"taken_{item}")
st.session_state.taken[item] = taken
data.append([item, quantity_at_home, quantity_to_take, "Yes" if taken else "No"])