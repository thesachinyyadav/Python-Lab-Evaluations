import streamlit as st
import pandas as pd

# Data Setup
employees = pd.DataFrame([
    (2341501, "Sachin Yadav", "Engineering", 50000),
    (2341502, "Surya Vamshi", "Marketing", 60000),
    (2341503, "Dinesh J", "Human Resources", 55000),
    (2341504, "Arjun Ramesh", "Engineering", 62000),
    (2341505, "Suyash Maskara", "Marketing", 50000),
    (2341506, "Priya Singh", "Finance", 58000),
    (2341507, "Rahul Sharma", "Engineering", 65000),
    (2341508, "Neha Gupta", "Human Resources", 52000),
    (2341509, "Amit Patel", "Marketing", 60000),
    (2341510, "Anjali Rao", "Finance", 55000)
], columns=['ID', 'Name', 'Department', 'Salary'])

# sets for emp;oyee managment
departments = set(employees['Department']) 
highSalary = set(employees[employees['Salary'] > 55000]['Name']) 
lowSalary = set(employees[employees['Salary'] <= 55000]['Name']) 
jobLevels = set(["Junior", "Senior"]) //imaginary scenario

# functions
def getUnion(firstSet, secondSet):
    return firstSet.union(secondSet)

def getIntersection(firstSet, secondSet):
    return firstSet.intersection(secondSet)

def getDifference(firstSet, secondSet):
    return firstSet.difference(secondSet)

def getSymmetricDifference(firstSet, secondSet):
    return firstSet.symmetric_difference(secondSet)

def isSubset(smallSet, bigSet):
    return smallSet.issubset(bigSet)

def isSuperset(bigSet, smallSet):
    return bigSet.issuperset(smallSet)

#bg image
def applyBackground():
    st.markdown(
         """
         <style>
         .stApp {
             background-image: url("https://img.freepik.com/free-photo/online-school-equipment-home_23-2149041150.jpg?w=996&t=st=1728969729~exp=1728970329~hmac=e8dd7d484cfbad043df3de6bc79f3ad3862e6e8a9c71932f638c174692bb36f0");
             background-size: cover;
         }
         </style>
         """,
         unsafe_allow_html=True
     )

# streamlit interfce
applyBackground()  

st.title("Employee Management System")

menu = ["Manage Employees", "Set Operations", "Exit"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Manage Employees":
    st.subheader("Employee List")
    st.table(employees)

elif choice == "Set Operations":
    st.subheader("Perform Set Operations")

    # results using expanders 
    with st.expander("Union Operation"):
        st.write("Union of Departments and Job Levels:")
        unionResult = getUnion(departments, jobLevels)
        st.write(", ".join(sorted(unionResult)))  

    with st.expander("Intersection Operation"):
        st.write("Intersection of High and Low Salary Employees:")
        intersectionResult = getIntersection(highSalary, lowSalary)
        st.write(", ".join(sorted(intersectionResult)) if intersectionResult else "No common elements")

    with st.expander("Difference Operation"):
        st.write("Employees earning above 55,000 (Difference):")
        differenceResult = getDifference(highSalary, lowSalary)
        st.write(", ".join(sorted(differenceResult)))

    with st.expander("Symmetric Difference Operation"):
        st.write("Symmetric Difference between High and Low Salary Employees:")
        symmetricDifferenceResult = getSymmetricDifference(highSalary, lowSalary)
        st.write(", ".join(sorted(symmetricDifferenceResult)))

    with st.expander("Subset and Superset Operations"):
        st.write("Is Low Salary Set a subset of High Salary Set?")
        subsetResult = isSubset(lowSalary, highSalary)
        st.write("Yes" if subsetResult else "No")
        
        st.write("Is High Salary Set a superset of Low Salary Set?")
        supersetResult = isSuperset(highSalary, lowSalary)
        st.write("Yes" if supersetResult else "No")

elif choice == "Exit":
    st.write("Thank you for using the Employee Management System!")
