import streamlit as st
import joblib
import numpy as np

# Cargar el modelo entrenado
model = joblib.load("primermillon.joblib")

# Configuración de la página
st.set_page_config(page_title="Predictor de Éxito Académico", page_icon="🎓", layout="centered")

# Título
st.title("🎓 Predictor de Éxito Académico")
st.write("**Autor:** Brayan León")

# Imagen debajo del autor
st.image(
    "https://buscacarrera.com.co/public/content/articulos/la-clave-del-exito-academico-como-crear-un-plan-de-estudio-efectivo.jpg",
    caption="La clave del éxito académico"
)

# Introducción
st.markdown("""
Esta aplicación te permite predecir si un estudiante se graduará con éxito en la universidad a partir de dos variables:
- **Nota IA**: Desempeño en inteligencia artificial (0.0 a 1.0)
- **GPA**: Promedio general acumulado (0.0 a 1.0)

Usa los controles deslizantes para ingresar los valores y presiona el botón para obtener la predicción.
""")

# Sliders para las variables de entrada
nota_ia = st.slider("Nota IA", 0.0, 1.0, 0.5, 0.1)
gpa = st.slider("GPA", 0.0, 1.0, 0.5, 0.1)

# Botón de predicción
if st.button("🔮 Predecir"):
    features = np.array([[nota_ia, gpa]])
    prediction = model.predict(features)[0]

    if prediction == 0:
        st.markdown(
            "<h2 style='color:red;'>❌ No se graduará</h2>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<h2 style='color:green;'>🎉 Felicitaciones, te vas a graduar con honores</h2>",
            unsafe_allow_html=True
        )

# Footer con derechos de autor
st.markdown("""
---
© 2025 UNAB
""")
