import streamlit as st
import numpy as np

st.title("Zrozum definicję logarytmu")

# Wybór trybu zmiany parametru
mode = st.radio(
    "Który parametr chcesz zmieniać?",
    ("Podstawa logarytmu (a)", "Argument logarytmu (b)")
)

# Ustawienia domyślne
default_a = 2
default_b = 8

if mode == "Podstawa logarytmu (a)":
    a = st.slider("Wybierz podstawę logarytmu (a)", 2, 10, default_a)
    b = st.number_input("Podaj argument logarytmu (b)", min_value=1.0, value=float(default_b), step=1.0)
    # c = log_a(b)
    c = np.log(b) / np.log(a)
elif mode == "Argument logarytmu (b)":
    a = st.slider("Wybierz podstawę logarytmu (a)", 2, 10, default_a)
    c = st.number_input("Podaj wartość logarytmu (c)", min_value=0.0, value=3.0, step=1.0)
    # b = a^c
    b = a ** c

st.markdown(f"### log<sub>{a}</sub>({b:.4g}) = {c:.4g}")

st.info(f"Ponieważ {a} do potęgi {c:.4g} równa się {b:.4g}.")

# Dodatkowe wyjaśnienie
st.write("""
Definicja logarytmu:
> logarytm przy podstawie **a** z liczby **b** to taka liczba **c**, że **a<sup>c</sup> = b**.
""")

