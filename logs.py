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


def generate_tone(db_level, duration=1.0, freq=440, sample_rate=44100):
    """
    Generuje dźwięk sinusoidalny o głośności proporcjonalnej do db_level (dB).
    Zakładamy poziom referencyjny 0 dB jako maksymalną amplitudę.
    """
    # Przelicz decybele na liniową amplitudę (zakładamy 0 dB jako amplituda 1.0)
    amplitude = 10 ** (db_level / 20)  # 20 bo amplituda (ciśnienie), a nie moc
    # Skalujemy, by nie przekroczyć maksymalnej wartości 1.0 (normalizacja)
    max_amplitude = 1.0
    norm_amplitude = min(amplitude / (10 ** (120 / 20)), max_amplitude)

    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = norm_amplitude * np.sin(2 * np.pi * freq * t)

    # Konwertujemy na 16-bitowe wartości całkowite
    audio = np.int16(tone * 32767)

    # Zapis do bufora bytes
    buf = io.BytesIO()
    wavfile.write(buf, sample_rate, audio)
    return buf.getvalue()

# W sekcji porównania dźwięków:

if I1 > 0 and I2 > 0:
    L1 = 10 * math.log10(I1 / I0)
    L2 = 10 * math.log10(I2 / I0)
    diff = L1 - L2

    # ... (poprzedni kod wyświetlania wyników i pasków)

    st.markdown("### Odtwarzanie dźwięków")

    audio1 = generate_tone(L1)
    audio2 = generate_tone(L2)

    st.audio(audio1, format="audio/wav", start_time=0, sample_rate=44100)
    st.write("Odtwarzanie dźwięku I₁")

    st.audio(audio2, format="audio/wav", start_time=0, sample_rate=44100)
    st.write("Odtwarzanie dźwięku I₂")

