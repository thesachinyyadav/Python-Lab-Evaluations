import streamlit as st
import pandas as pd

# Data Setup
employees = pd.DataFrame([
    (2341501, "Sachin Yadav", "Engineering", 50000),
    (2341502, "Surya Vamshi", "Marketing", 60000),
    (2341503, "Dinesh J", "Human Resources", 55000),
    (2341504, "Arjun Ramesh", "Engineering", 62000),
    (2341505, "Suyash Maskara", "Marketing", 50000)
], columns=['ID', 'Name', 'Department', 'Salary'])

movieDB = pd.DataFrame({
    'Movie': ['Inception', 'The Matrix', 'Interstellar'],
    'Year': [2010, 1999, 2014]
}).set_index('Movie')

# Function to display tables
def display_table(dataframe):
    st.table(dataframe)

st.title("Data Management System")

# Background Images for sections
st.markdown("""
    <style>
    [data-testid="stSidebar"] > div:first-child {
        background-image: url('https://static.toiimg.com/photo/104701914/104701914.jpg');
        background-size: cover;
    }
    .block-container {
        background-image: url('https://img.freepik.com/free-photo/cracked-black-wooden-textured-background_53876-104673.jpg?w=996&t=st=1727453592~exp=1727454192~hmac=ee1b2e1387dd55cdcc8d95e4ca4a3014fc10a26bea29f092891a3a82aa228201');
        background-size: cover;
    }
    </style>
    """, unsafe_allow_html=True)

menu = ["Manage Employees", "Manage Movies", "Exit"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Manage Employees":
    st.subheader("Employee Management")
    display_table(employees)

    empId = st.number_input("Enter Employee ID", int(employees['ID'].min()), int(employees['ID'].max()))
    newSalary = st.number_input("Enter New Salary (in rupees)", min_value=0)
    
    if st.button("Update Salary"):
        if empId in employees['ID'].values:
            employees.loc[employees['ID'] == empId, 'Salary'] = newSalary
            st.success("Salary updated successfully!")
            display_table(employees[employees['ID'] == empId])
        else:
            st.error("Employee ID not found")

elif choice == "Manage Movies":
    st.subheader("Movie Management")
    display_table(movieDB.reset_index())

    movieMenu = st.radio("Choose action", ["View Movies", "Add Movie", "Update Movie", "Delete Movie"])
    
    if movieMenu == "View Movies":
        display_table(movieDB)
    
    elif movieMenu == "Add Movie":
        newMovie = st.text_input("Enter Movie Name")
        newYear = st.number_input("Enter Release Year", min_value=1900, max_value=2024)
        
        if st.button("Add Movie"):
            if newMovie not in movieDB.index:
                movieDB.loc[newMovie] = newYear
                st.success(f"Added {newMovie} released in {newYear}")
                display_table(movieDB.reset_index())
            else:
                st.error("Movie already exists in the database")

    elif movieMenu == "Update Movie":
        updateMovie = st.selectbox("Select a Movie to Update", movieDB.index.tolist())
        newYear = st.number_input("Enter New Release Year", value=movieDB.loc[updateMovie, 'Year'], min_value=1900, max_value=2024)
        
        if st.button("Update Movie"):
            movieDB.loc[updateMovie, 'Year'] = newYear
            st.success(f"Updated {updateMovie} to release year {newYear}")
            display_table(movieDB.reset_index())

    elif movieMenu == "Delete Movie":
        deleteMovie = st.selectbox("Select a Movie to Delete", movieDB.index.tolist())
        
        if st.button("Delete Movie"):
            movieDB.drop(deleteMovie, inplace=True)
            st.success(f"Deleted {deleteMovie}")
            display_table(movieDB.reset_index())

elif choice == "Exit":
    st.write("Thank you for using the Data Management System!")
