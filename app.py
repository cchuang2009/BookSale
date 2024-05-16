import streamlit as st
import pandas as pd
import os

# Create a CSV file for the book data
books = pd.DataFrame(columns=['book_name', 'year', 'publisher', 'ISBN', 'price', 'unit', 'seller_email'])

# Check if the book.csv file exists
if os.path.exists('book.csv'):
    # Read the book.csv file
    books = pd.read_csv('book.csv')

    # Display the books
    st.header('Books for Sale')
    st.table(books)

else:
    st.header('Create a new book')



# Create a Streamlit app
st.title('Bookstore')
st.header('Add a new book')

# Create input columns
book_name = st.text_input('Book Name:')
year = st.text_input('Year (YYYY):')
publisher = st.text_input('Publisher:')
ISBN = st.text_input('ISBN:')
price = st.number_input('Price:')
unit = st.selectbox('Unit:', ['US $', 'NT $', 'Other'])
seller_email = st.text_input('Seller Email:')

# Add the new book to the CSV file
if st.button('Add Book'):
    new_book = pd.DataFrame({'book_name': [book_name], 'year': [year], 'publisher': [publisher], 'ISBN': [ISBN], 'price': [price], 'unit': [unit], 'seller_email': [seller_email]})
    books = pd.concat([books, new_book])
    books.to_csv('book.csv', index=False)

# List the books for sale
st.header('Books for Sale')
st.table(books)

