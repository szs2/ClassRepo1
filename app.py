import pandas as pd
import altair as alt
import streamlit as st

# Set up the title and a brief description for the Streamlit app
st.title("Class Demo for Streamlit")
st.write("Submitted by: Senuri Kahandugoda")

# Load the penguins dataset from the raw GitHub URL
data = pd.read_csv('https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/main/data/penguins.csv')

# Create a scatter plot using Altair, where flipper length is on the x-axis and body mass is on the y-axis
scatter_plot = alt.Chart(penguins).mark_circle(size=60).encode(
    x='flipper_length_mm',
    y='body_mass_g',
    color='species',
    tooltip=['species', 'flipper_length_mm', 'body_mass_g']
).properties(
    title='Penguins: Flipper Length vs Body Mass',
    width=600,
    height=400
)


st.altair_chart(scatter_plot, use_container_width=True)

st.write("-------------------------------------------------------------------------------")
st.write("Chart 2")

cars = pd.read_csv('https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/main/data/cars.csv')

cars.columns = cars.columns.str.strip()

bar_chart = alt.Chart(cars).mark_bar().encode(
 y=alt.Y('Name:N', title='Car Model'),
 x=alt.X('Horsepower:Q', title='Horsepower'),
 color=alt.Color('Origin:N', title='Origin'),
 tooltip=['Name', 'Horsepower', 'Origin']
).properties(
    title='Car Horsepower by Model',
    width=600,
    height=400
)


st.altair_chart(bar_chart, use_container_width=True)