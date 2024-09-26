import streamlit as st
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

if not st.session_state.loggedIn:
    st.subheader("Login")

    if st.session_state.lockedOutUntil and datetime.now() < st.session_state.lockedOutUntil:
        timeRemaining = (st.session_state.lockedOutUntil - datetime.now()).total_seconds() / 60
        st.error(f"Login is currently disabled. Please wait until {st.session_state.lockedOutUntil.strftime('%Y-%m-%d %H:%M:%S')}. Approximately {timeRemaining:.1f} minutes remaining.")
    else:
        enteredUsername = st.text_input("Username")
        enteredPassword = st.text_input("Password", type="password")

        if st.button("Login"):
            if checkLogin(enteredUsername, enteredPassword):
                st.session_state.loggedIn = True
                st.session_state.loginAttempts = 0
                st.success("You are now logged in!")
            else:
                st.session_state.loginAttempts += 1
                attemptsRemaining = 5 - st.session_state.loginAttempts
                st.error(f"Username or password is incorrect. {attemptsRemaining} attempts remaining.")
                if st.session_state.loginAttempts >= 5:
                    st.session_state.lockedOutUntil = datetime.now() + timedelta(minutes=30)
                    st.error("Too many incorrect attempts. Login will be disabled for 30 minutes.")

        st.write(f"Attempt {st.session_state.loginAttempts} of 5")

if st.session_state.loggedIn:
    if 'studentMarks' not in st.session_state:
        st.session_state.studentMarks = {}

    def calculateMarks(DSA, JAVA, Python):
        return DSA + JAVA + Python

    def updateStudentMarks(name, DSA, JAVA, Python):
        st.session_state.studentMarks[name] = calculateMarks(DSA, JAVA, Python)

    def displayMarks():
        for name, marks in st.session_state.studentMarks.items():
            st.write(f"{name}: {marks}")

    st.subheader("Student Marks Manager")
    studentName = st.text_input("Student Name")
    DSAMarks = st.number_input("DSA Marks", 0, 100, key="DSA")
    JAVAMarks = st.number_input("JAVA Marks", 0, 100, key="JAVA")
    PythonMarks = st.number_input("Python Marks", 0, 100, key="Python")

    if st.button("Update Marks"):
        updateStudentMarks(studentName, DSAMarks, JAVAMarks, PythonMarks)
        st.success("Student marks have been successfully updated.")

    if st.button("Show All Marks"):
        displayMarks()
