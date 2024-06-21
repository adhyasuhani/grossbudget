import streamlit as st
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('Final.csv')

# Function to calculate gross income based on budget, genre, rating, and country
def calculate_gross_income(budget, genre, rating, country):
    # Filter the dataset based on the provided genre, rating, and country
    filtered_df = df[(df['genre'].str.lower() == genre.lower()) &
                     (df['rating'].str.lower() == rating.lower()) &
                     (df['country'].str.lower() == country.lower())]
    
    if not filtered_df.empty:
        # Calculate average gross income for the filtered data
        average_gross_per_budget = filtered_df['gross'].sum() / filtered_df['budget'].sum()
    else:
        # If no matching data found, use the overall average
        average_gross_per_budget = df['gross'].sum() / df['budget'].sum()
    
    # Predict gross income based on the budget
    gross_income = budget * average_gross_per_budget
    return gross_income

# Streamlit app
st.title('Movie Gross Income Predictor')

# Input for movie budget
budget = st.number_input('Enter movie budget:', min_value=0)

# Input for genre
genre = st.selectbox('Select genre:', df['genre'].unique())

# Input for rating
rating = st.selectbox('Select rating:', df['rating'].unique())

# Input for country
country = st.selectbox('Select country:', df['country'].unique())

if st.button('Calculate Gross Income'):
    if budget and genre and rating and country:
        gross_income = calculate_gross_income(budget, genre, rating, country)
        st.write(f'The estimated gross income for a movie with:')
        st.write(f'**Budget:** ${budget:,}')
        st.write(f'**Genre:** {genre}')
        st.write(f'**Rating:** {rating}')
        st.write(f'**Country:** {country}')
        st.write(f'is **${gross_income:,.2f}**')
    else:
        st.write('Please enter all inputs.')
