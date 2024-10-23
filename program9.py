import streamlit as st
from num2words import num2words
import base64


annualSalary = lambda monthlySalary: monthlySalary * 12
bonusCalculation = lambda monthlySalary, bonusPercentage: monthlySalary * (bonusPercentage / 100)
overtimePay = lambda hourlyRate, overtimeHours: hourlyRate * overtimeHours * 1.5

def amountInWords(amount):
    return num2words(amount, lang='en_IN').replace(",", "")

def setBackgroundImage(imageFile):
    with open(imageFile, "rb") as file:
        data = base64.b64encode(file.read()).decode()
    pageBg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{data}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(pageBg, unsafe_allow_html=True)

def applyBackground():
    st.markdown(
         """
         <style>
          [data-testid="stSidebar"] > div:first-child {
        background-image: url('https://w0.peakpx.com/wallpaper/13/889/HD-wallpaper-space-light-dark-deep-galaxy-thumbnail.jpg');
        background-size: cover;
    }
         .stApp {
             background-image: url("https://www.shutterstock.com/image-vector/abstract-halftone-blue-background-shapes-600nw-2074348912.jpg");
             background-size: cover;
         }
         </style>
         """,
         unsafe_allow_html=True
     )

applyBackground()  
def employeeManagementCalculator():
   
    st.title("Employee Management Calculator")
    st.subheader("Calculate Annual Salary, Bonus, and Overtime Pay Easily")

    
    option = st.sidebar.selectbox(
        "Choose a Calculation",
        ("Annual Salary", "Bonus Calculation", "Overtime Pay")
    )

    if option == "Annual Salary":
        st.header("Annual Salary Calculator")
        monthlySalary = st.number_input("Enter the Monthly Salary:", min_value=0.0, format="%.2f")
        
        if st.button("Calculate Annual Salary"):
            annualSalaryResult = annualSalary(monthlySalary)
            st.success(f"The annual salary is: ₹{annualSalaryResult:.2f} ({amountInWords(annualSalaryResult)})")

    elif option == "Bonus Calculation":
        st.header("Bonus Calculation")
        monthlySalary = st.number_input("Enter the Monthly Salary:", min_value=0.0, format="%.2f")
        bonusPercentage = st.slider("Enter the Bonus Percentage:", 0, 100)
        
        if st.button("Calculate Bonus"):
            bonusResult = bonusCalculation(monthlySalary, bonusPercentage)
            st.success(f"The bonus amount is: ₹{bonusResult:.2f} ({amountInWords(bonusResult)})")

    elif option == "Overtime Pay":
        st.header("Overtime Pay Calculator")
        hourlyRate = st.number_input("Enter the Hourly Rate:", min_value=0.0, format="%.2f")
        overtimeHours = st.number_input("Enter the Number of Overtime Hours:", min_value=0.0, format="%.2f")
        
        if st.button("Calculate Overtime Pay"):
            overtimePayResult = overtimePay(hourlyRate, overtimeHours)
            st.success(f"The overtime pay is: ₹{overtimePayResult:.2f} ({amountInWords(overtimePayResult)})")

if __name__ == "__main__":
    employeeManagementCalculator()
