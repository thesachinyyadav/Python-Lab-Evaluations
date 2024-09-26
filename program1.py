import streamlit as st

st.setpage(page_title="Virtual Lab Assistant")
st.title("Virtual Lab Assistant")

def calculatemarks(assignmentmarks, quizmark, projectmarks):
    totalmarks = assignmentmarks + quizmark + projectmarks
    return totalmarks


assignmentmarks = st.numberinput("Enter assignment marks:", min=0, max=100)
quizmark = st.numberinput("Enter quiz marks:", min=0, max=100)
projectmarks = st.numberinput("Enter project marks:", min=0, max=100)


if st.button("Calculate Lab Marks"):
    labmark = calculatemarks(assignmentmarks, quizmark, projectmarks)
    st.write("Your lab marks are:", labmark)