import streamlit as st
import matplotlib.pyplot as plt
echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)