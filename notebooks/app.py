
import pandas as pd
import streamlit as st
import plotly.express
from matplotlib import pyplot as plt
import seaborn as sns


panic_attack_df = pd.read_csv('panic_attack_dataset.csv')

st.header('Analysis of Panic Attacks')
st.write(panic_attack_df)

# Plot Panic Attack triggers 
trigger_counts = panic_attack_df['Trigger'].value_counts()

st.write('Freqency of Panic Attack Triggers')

fig, ax = plt.subplots()
sns.barplot(x=trigger_counts.index, y=trigger_counts.values, ax=ax)
ax.set_title("Panic Attack Triggers Frequency")
ax.set_xlabel("Triggers")
ax.set_ylabel("Frequency")

st.pyplot(fig)


st.write("Histogram of Panic Attack Frequency by Age")

# Filter by Gender
gender_options = list(panic_attack_df["Gender"].unique())
selected_gender = st.selectbox("Select Gender", ["All"] + gender_options)

if selected_gender != "All":
    filtered_df = panic_attack_df[panic_attack_df["Gender"] == selected_gender]
else:
    filtered_df = panic_attack_df

# Plot histogram for Panic Attack Frequency by Gender and Age
fig, ax = plt.subplots(figsize=(12, 6))
sns.histplot(filtered_df, x="Age", weights="Panic_Attack_Frequency", bins=10, kde=True, ax=ax)

ax.set_title("Distribution of Panic Attack Frequency by Age")
ax.set_xlabel("Age")
ax.set_ylabel("Frequency")

st.pyplot(fig)
