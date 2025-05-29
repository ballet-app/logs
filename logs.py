import streamlit as st
import math
import numpy as np
import io
from scipy.io import wavfile

st.title("Decybele i logarytmy — wizualizacja skali dźwięku")

st.markdown("""
Decybele (dB) to logarytmiczna skala do pomiaru natężenia dźwięku.  
Możesz podać natężenie dźwięku \(I\) i zobaczyć, jaki to poziom w decybelach względem progu słyszalności \(I_0 = 10^{-12} W/m^2\).
""")

I0 = 1e-12  # próg słyszalności

st.subheader("Pojedynczy poziom dźwięku")

I = st.number_input("Podaj natężenie dźwięku I [W/m²] (I > 0)", min_value=1e-15, value=1e-6, format="%.12f")

if I <= 0:
    st.error("Natężenie musi być większe od zera!")
else:
    L = 10 * ma*
