import streamlit as st

# Function to calculate percentage returns
def percentage_return(previous, current):
    if previous == 0:
        return 0
    return ((current - previous) / previous) * 100

# Function to filter days with increasing odds
def get_increasing_days(betting_odds):
    return {day for day in range(1, len(betting_odds)) if betting_odds[day] > betting_odds[day - 1]}

# Function to calculate percentage returns using dictionary comprehension
def calculate_percentage_returns(betting_odds, increasing_days):
    return {day: percentage_return(betting_odds[day - 1], betting_odds[day]) for day in increasing_days}

# Streamlit application

def applyBackground():
    st.markdown(
         """
         <style>
          [data-testid="stSidebar"] > div:first-child {
        background-image: url('https://st3.depositphotos.com/1144687/19192/i/450/depositphotos_191922334-stock-photo-forex-chart-background.jpg');
        background-size: cover;
    }
         .stApp {
             background-image: url("https://bsmedia.business-standard.com/_media/bs/img/misc/2023-03/21/full/market-stocks-stock-market-trading-stock-market-1679390474-25992620.jpg?im=FeatureCrop,size=(826,465)");
             background-size: cover;
         }
         </style>
         """,
         unsafe_allow_html=True
     )

# streamlit interfce
applyBackground()  

def main():
    st.title("Sports Betting Analysis")
    
    # Sidebar menu
    st.sidebar.header("Menu")
    option = st.sidebar.selectbox("Choose an option", [
        "Enter Betting Odds",
        "Display List of Betting Odds",
        "Show Days with Increasing Odds",
        "Show Percentage Returns for Increasing Odds",
        "Exit"
    ])

    # Initialize session state variables
    if 'betting_odds' not in st.session_state:
        st.session_state.betting_odds = []
    if 'increasing_days' not in st.session_state:
        st.session_state.increasing_days = set()
    if 'percentage_returns' not in st.session_state:
        st.session_state.percentage_returns = {}

   
    if option == "Enter Betting Odds":
        st.header("Enter Betting Odds")
        betting_odds_input = st.text_area("Enter 10 betting odds, separated by commas:")
        
        if st.button("Submit"):
            try:
                odds = [float(x.strip()) for x in betting_odds_input.split(',')]
                if len(odds) != 10:
                    st.warning("Please enter exactly 10 odds.")
                else:
                    st.session_state.betting_odds = odds
                    st.session_state.increasing_days = get_increasing_days(odds)
                    st.session_state.percentage_returns = calculate_percentage_returns(odds, st.session_state.increasing_days)
                    st.success("Betting odds successfully entered.")
            except ValueError:
                st.error("Please enter valid numbers separated by commas.")
    
    #  displauy List of Betting Odds
    elif option == "Display List of Betting Odds":
        st.header("List of Betting Odds")
        if st.session_state.betting_odds:
            st.write(st.session_state.betting_odds)
        else:
            st.warning("No betting odds entered yet.")
    
    #  Show Days with Increasing Odds
    elif option == "Show Days with Increasing Odds":
        st.header("Days with Increasing Betting Odds")
        if st.session_state.increasing_days:
            st.write(st.session_state.increasing_days)
        else:
            st.warning("No betting odds entered yet or no days with increasing odds.")
    
    # show Percentage Returns for Increasing Odds
    elif option == "Show Percentage Returns for Increasing Odds":
        st.header("Percentage Returns on Increasing Days")
        if st.session_state.percentage_returns:
            for day, percentage in st.session_state.percentage_returns.items():
                st.write(f"Day {day}: {percentage:.2f}%")
        else:
            st.warning("No betting odds entered yet or no increasing days to calculate returns.")
    
    # Option 5: Exit
    elif option == "Exit":
        st.info("Thank you for using the Sports Betting Analysis app!")

if __name__ == "__main__":
    main()
