# %%
import pandas as pd
import streamlit as st
import plotly.express
from matplotlib import pyplot as plt
import seaborn as sns

# %%
panic_attack_df = pd.read_csv('panic_attack_dataset.csv')

st.header('Analysis of Panic Attacks')

st.write('Freqency of Panic Attack Triggers')

print('Hello')
# %%
st.write(panic_attack_df)
# %%
