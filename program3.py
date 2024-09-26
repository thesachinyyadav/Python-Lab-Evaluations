import streamlit as st
import pandas as pd
from datetime import datetime, timedelta


st.set_page_config(page_title="Virtual Lab Assistant")
st.title("Virtual Lab Assistant")

validUsers = {
    "sachin": "yadav",
    "surya": "vamshi",
    "arjun": "ramesh"
}

def checkLogin(username, password):
    return username in validUsers and validUsers[username] == password

if 'loginAttempts' not in st.session_state:
    st.session_state.loginAttempts = 0
if 'lockedOutUntil' not in st.session_state:
    st.session_state.lockedOutUntil = None
if 'loggedIn' not in st.session_state:
    st.session_state.loggedIn = False
if 'studentName' not in st.session_state:
    st.session_state.studentName = {}

def loginPage():
    if st.session_state.lockedOutUntil and datetime.now() < st.session_state.lockedOutUntil:
        st.error("Login is currently disabled. Please try again later.")
    else:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if checkLogin(username, password):
                st.session_state.loggedIn = True
                st.session_state.loginAttempts = 0
            else:
                st.session_state.loginAttempts += 1
                if st.session_state.loginAttempts >= 5:
                    st.session_state.lockedOutUntil = datetime.now() + timedelta(minutes=30)
                    st.error("Too many incorrect attempts. Login disabled for 30 minutes.")
                else:
                    st.error(f"Incorrect username or password. {5 - st.session_state.loginAttempts} attempts remaining.")

def mainApp():
    menu = ["Add Update Student Marks", "View All Student Marks", "Remove Student Marks", "Search Student Marks", "Count Students", "Exit"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Update Student Marks":
        st.subheader("Add or Update Student Marks")
        studentName = st.text_input("Enter student name:")
        DSAMarks = st.number_input("Enter DSA marks for the selected student:", min_value=0, max_value=100)
        JavaMarks = st.number_input("Enter Java marks for the selected student:", min_value=0, max_value=100)
        PythonMarks = st.number_input("Enter Python marks for the selected student:", min_value=0, max_value=100)
        if st.button("Add Update"):
            if studentName:
                addOrUpdateStudentMarks(studentName, DSAMarks, JavaMarks, PythonMarks)
            else:
                st.error("Student name cannot be empty")

    elif choice == "View All Student Marks":
        st.subheader("View All Student Marks")
        viewAllStudentMarks()

    elif choice == "Remove Student Marks":
        st.subheader("Remove Student Marks")
        studentName = st.text_input("Enter student name to remove:")
        if st.button("Remove"):
            if studentName:
                removeStudentMarks(studentName)
            else:
                st.error("Student name cannot be empty")

    elif choice == "Search Student Marks":
        st.subheader("Search Student Marks")
        keyword = st.text_input("Enter the keyword to search for:")
        if st.button("Search"):
            if keyword:
                searchStudentMarks(keyword)
            else:
                st.error("Keyword cannot be empty")

    elif choice == "Count Students":
        st.subheader("Count Students")
        countStudents()

    elif choice == "Exit":
        st.write("Thank you for using the Virtual Lab Assistant!")

#functions here-----

def addOrUpdateStudentMarks(name, DSA, Java, Python):
    st.session_state.studentName[name] = {
        "DSA": DSA,
        "Java": Java,
        "Python": Python,
        "Total": DSA + Java + Python
    }
    st.success("Marks updated successfully!")

def viewAllStudentMarks():
    if st.session_state.studentName:
        df = pd.DataFrame(st.session_state.studentName).T
        st.table(df)
    else:
        st.write("No student marks available.")

def removeStudentMarks(name):
    if name in st.session_state.studentName:
        del st.session_state.studentName[name]
        st.success("Student marks removed successfully!")
    else:
        st.error("Student not found!")

def searchStudentMarks(keyword):
    matchedStudents = {name: marks for name, marks in st.session_state.studentName.items() if keyword.lower() in name.lower()}
    if matchedStudents:
        df = pd.DataFrame(matchedStudents).T
        st.table(df)
    else:
        st.write("No matching students found.")

def countStudents():
    studentCount = len(st.session_state.studentName)
    st.write(f"Total number of students: {studentCount}")

if not st.session_state.loggedIn:
    loginPage()
else:
    mainApp()
