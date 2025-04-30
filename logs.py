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

# Dane do wykresu funkcji logarytmicznej y = log_a(x)
x_log = np.linspace(1, a**6, 100)
y_log = np.log(x_log) / np.log(a)
x_points_log = a ** np.arange(0, 7)
y_points_log = np.log(x_points_log) / np.log(a)

# Rysowanie wykresów
fig, ax = plt.subplots()

# Wykres funkcji wykładniczej
ax.plot(x_exp, y_exp, label=f'y = {a}^x', color='blue')
ax.scatter(x_points_exp, y_points_exp, color='blue', zorder=5, label='Punkty y=a^x dla x=0..6')

# Wykres funkcji logarytmicznej
ax.plot(x_log, y_log, label=f'y = log_{a}(x)', color='green')
ax.scatter(x_points_log, y_points_log, color='green', zorder=5, label='Punkty y=log_a(x) dla x=1,a^1,...,a^6')

# Opisy osi i legenda
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)

st.pyplot(fig)
