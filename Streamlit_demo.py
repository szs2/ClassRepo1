import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("More Charts and Utilities")
st.write("Submitted by: Senuri Kahandugoda")

data = pd.read_csv('https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/main/data/penguins.csv')

st.sidebar.header('Select Options')
selected_category = st.sidebar.selectbox("Select Species", options=['All', 'Adelie', 'Gentoo', 'Chinstrap'])

# Filter data based on user selection
if selected_category != 'All':
    filtered_data = data[data['species'] == selected_category]
else:
    filtered_data = data

# Seaborn density plot
st.write("### Seaborn Density Plot")
fig, ax = plt.subplots()
sns.kdeplot(data=filtered_data, x='culmen_depth_mm', color="black", fill=True, ax=ax)
ax.set_title("Seaborn Density Plot for Culmen Depths")
ax.set_xlabel("Value")
ax.set_ylabel("Density")
st.pyplot(fig)  # use streamlit to display the pyplot object

# Altair scatter plot
st.write("### Altair Scatter Plot")
scatter_plot = alt.Chart(filtered_data).mark_circle().encode(
    x='flipper_length_mm',
    y='body_mass_g',
    tooltip=['island', 'species'],
    color=alt.Color('island', scale=alt.Scale(scheme='tableau10')),  # Updated to 'tableau10'
    size='body_mass_g'
).properties(
    title='Scatter Plot of Penguins Data',
    width=600,
    height=400
).interactive()  # Allows zooming and panning
st.altair_chart(scatter_plot, use_container_width=True)  # Display the chart