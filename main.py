import streamlit as st
from utils.criteria import load_criteria
from evaluation import combinar_reglas_y_modelo
from sentence_transformers import SentenceTransformer

def load_models():
    modelo_embeddings = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return modelo_embeddings

st.title("Evaluador de Requisitos")

criterios = load_criteria("criterios/criterios_requisitos.json")
modelo_embeddings = load_models()

requisito = st.text_area("Ingresa el requisito a evaluar:")

if st.button("Evaluar"):
    if requisito:
        puntuacion, mejoras = combinar_reglas_y_modelo(
            requisito,
            criterios,
            modelo_embeddings
        )
        
        st.subheader(f"{puntuacion}")
        if mejoras:
            st.write("**Aspectos a mejorar:**")
            for mejora in mejoras:
                st.write(f"- {mejora}")
    else:
        st.warning("Por favor, ingresa un requisito para evaluar.")
