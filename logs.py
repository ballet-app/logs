import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

# Suwak do wyboru wartości a w zakresie 2 do 10
a = st.slider('Wybierz wartość a', 2, 10, 2)

# Definicja funkcji y = a^x
def f(x, a):
    return a ** x

# Przygotowanie danych do wykresu
x = np.linspace(0, 6, 100)
y = f(x, a)

# Wyróżnione punkty dla argumentów naturalnych od 0 do 6
x_points = np.arange(0, 7)
y_points = f(x_points, a)

# Rysowanie wykresu
fig, ax = plt.subplots()
ax.plot(x, y, label=f'y = {a}^x')
ax.scatter(x_points, y_points, color='red', zorder=5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)

st.pyplot(fig)

# Losowy wybór punktu do pytania
index = random.randint(0, len(x_points) - 1)
selected_x = x_points[index]
selected_y = y_points[index]

# Pytanie do użytkownika
st.write(f"Dla jakiego x wartość y wynosi {selected_y:.2f}?")

# Pole do wpisania odpowiedzi
user_answer = st.text_input('Wpisz wartość x:')

# Sprawdzenie odpowiedzi
if user_answer:
    try:
        user_x = float(user_answer)
        if abs(user_x - selected_x) < 1e-6:
            st.success(f"Poprawna odpowiedź! Z podanej zależności wynika, że logarytm przy podstawie {a} z wartości {selected_y:.2f} równa się {selected_x}.")
        else:
            st.error("Niepoprawna odpowiedź, spróbuj ponownie.")
    except ValueError:
        st.error("Proszę wpisać poprawną liczbę.")
