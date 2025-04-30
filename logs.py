import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Wykresy: funkcja wykładnicza i logarytmiczna")

# Suwak do wyboru wartości a
a = st.slider('Wybierz wartość a', 2, 10, 2)

# Dane do wykresu funkcji wykładniczej y = a^x
x_exp = np.linspace(0, 6, 100)
y_exp = a ** x_exp
x_points_exp = np.arange(0, 7)
y_points_exp = a ** x_points_exp

# Dane do wykresu funkcji logarytmicznej y
