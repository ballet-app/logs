import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

st.title("Wizualizacja funkcji wykładniczej i quiz")

# Suwak do wyboru wartości a
a = st.slider('Wybierz wartość a', 2, 10, 2)

# Przygotowanie punktów do wyróżnienia
x_points = np.arange(0, 7)
y_points = a ** x_points

# Jeśli zmieniono wartość a, resetuj pytanie
if 'last_a' not in st.session_state or st.session_state.last_a != a:
    st.session_state.selected_index = random.randint(0, len(x_points) - 1)
    st.session_state.last_a = a
    st.session_state.answered = False

selected_x = x_points[st.session_state.selected_index]
selected_y = y_points[st.session_state.selected_index]

# Wykres funkcji
fig, ax = plt.subplots()
x = np.linspace(0, 6, 100)
y = a ** x
ax.plot(x, y, label=f'y = {a}^x')
ax.scatter(x_points, y_points, color='red', zorder=5)
for i, (xp, yp) in enumerate(zip(x_points, y_points)):
    ax.annotate(f"({xp},{int(yp)})", (xp, yp), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Pytanie quizowe
st.write(f"Dla jakiego x wartość y wynosi {selected_y:.2f}?")

user_answer = st.text_input('Wpisz wartość x:', disabled=st.session_state.get("answered", False))

if user_answer and not st.session_state.get("answered", False):
    try:
        user_x = float(user_answer.strip())
        if abs(user_x - selected_x) < 1e-6:
            st.success(
                f"Poprawna odpowiedź! Z podanej zależności wynika, że logarytm przy podstawie {a} z wartości {selected_y:.2f} równa się {selected_x}."
            )
            st.session_state.answered = True
        else:
            st.error("Niepoprawna odpowiedź, spróbuj ponownie.")
    except ValueError:
        st.error("Proszę wpisać poprawną liczbę.")

# Przycisk do wylosowania nowego pytania
if st.button("Nowe pytanie"):
    st.session_state.selected_index = random.randint(0, len(x_points) - 1)
    st.session_state.answered = False
    st.experimental_rerun()
