import streamlit as st
import math

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
    L = 10 * math.log10(I / I0)
    st.markdown(f"Poziom dźwięku:  \n**{L:.2f} dB**")

    st.latex(r"L = 10 \log_{10} \left(\frac{I}{I_0}\right)")

st.subheader("Porównanie dwóch poziomów dźwięku")

I1 = st.number_input("Natężenie dźwięku I₁ [W/m²]", min_value=1e-15, value=1e-6, format="%.12f", key="I1")
I2 = st.number_input("Natężenie dźwięku I₂ [W/m²]", min_value=1e-15, value=1e-9, format="%.12f", key="I2")

if I1 > 0 and I2 > 0:
    L1 = 10 * math.log10(I1 / I0)
    L2 = 10 * math.log10(I2 / I0)
    diff = L1 - L2
    st.markdown(f"Poziom dźwięku I₁: **{L1:.2f} dB**")
    st.markdown(f"Poziom dźwięku I₂: **{L2:.2f} dB**")
    st.markdown(f"Różnica poziomów: **{diff:.2f} dB**")
    st.markdown("""
    Różnica w decybelach pokazuje, o ile razy silniejszy jest dźwięk I₁ w porównaniu z I₂.  
    Przykładowo, różnica 10 dB oznacza, że natężenie I₁ jest 10 razy większe niż I₂.
    """)

    ratio = I1 / I2
    st.write(f"Natężenie I₁ jest {ratio:.1e} razy większe niż I₂.")

    # Wizualizacja poziomów dźwięku jako paski:
    max_db = 120  # maksymalna wartość na skali

    def bar(db_value):
        # Długość paska w procentach
        length_pct = max(0, min(db_value / max_db, 1)) * 100
        bar_html = f"""
        <div style="background-color:#ddd; width:100%; height:25px; border-radius:5px;">
            <div style="background-color:#4caf50; width:{length_pct}%; height:25px; border-radius:5px;"></div>
        </div>
        """
        return bar_html

    st.markdown("### Wizualizacja poziomów dźwięku")
    st.markdown("**I₁**")
    st.markdown(bar(L1), unsafe_allow_html=True)
    st.write(f"{L1:.2f} dB")

    st.markdown("**I₂**")
    st.markdown(bar(L2), unsafe_allow_html=True)
    st.write(f"{L2:.2f} dB")

else:
    st.error("Obie wartości natężenia muszą być większe od zera.")

