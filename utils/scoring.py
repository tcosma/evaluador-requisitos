from sentence_transformers import SentenceTransformer, util

# Load the model
modelo_embeddings = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def calcular_similitud(requisito, ejemplos_ideales, modelo_embeddings):
    emb_req = modelo_embeddings.encode(requisito, convert_to_tensor=True)
    emb_ej = modelo_embeddings.encode(ejemplos_ideales, convert_to_tensor=True)
    sims = util.cos_sim(emb_req, emb_ej)
    return float(sims.max())

def evaluar_requisito(requisito, criterios):
    sub_profesionalismo = 2
    sub_claridad = 2
    sub_verificabilidad = 2.0
    sub_completitud = 2.0
    sub_consistencia = 2.0

    req_lower = requisito.lower()

    criterios_ambigüedades = criterios["criterios"]["ambigüedades"]
    conectores_validos = criterios["conectores_validos"]
    prefijos_validos = criterios["prefijos_validos"]
    criterios_métricas = criterios["criterios"]["métricas"]
    criterios_palabras_informales = criterios["criterios"]["palabras_informales"]

    if any(a in req_lower for a in criterios_ambigüedades):
        sub_claridad -= 1.0

    if not any(c in req_lower for c in conectores_validos):
        sub_verificabilidad -= 1.0

    if not any(m in req_lower for m in criterios_métricas):
        sub_verificabilidad -= 1.0

    if len(requisito.split()) < 6:
        sub_completitud = 0.0

    if not any(req_lower.startswith(prefijo.lower()) for prefijo in prefijos_validos):
        sub_profesionalismo -= 2.0

    if any(a in req_lower for a in criterios_palabras_informales):
        sub_profesionalismo -= 2.0

    if len(requisito) > 300:
        sub_profesionalismo -= 1.0


    sub_profesionalismo = max(sub_profesionalismo, 0.0)
    sub_claridad = max(sub_claridad, 0.0)
    sub_verificabilidad = max(sub_verificabilidad, 0.0)
    sub_completitud = max(sub_completitud, 0.0)
    sub_consistencia = max(sub_consistencia, 0.0)

    pr = sub_profesionalismo + sub_claridad + sub_verificabilidad + sub_completitud + sub_consistencia
    pr = max(1.0, min(pr, 10.0))  

    aspectos = []
    if sub_profesionalismo < 2.0:
        aspectos.append("La redacción del requisito podría ser más profesional.")
    if sub_claridad < 2.0:
        aspectos.append("El requisito contiene términos ambiguos o imprecisos.")
    if sub_verificabilidad < 2.0:
        aspectos.append("El requisito no es totalmente verificable. Añade métricas o condiciones claras.")
    if sub_completitud < 2.0:
        aspectos.append("El requisito no incluye suficiente información para ser implementado.")
    if sub_consistencia < 2.0:
        aspectos.append("Revisa la consistencia del requisito para evitar contradicciones.")
    if len(requisito) > 300:
        aspectos.append("El requisito es demasiado extenso. Considera simplificarlo para mejorar su claridad.")

    return pr, aspectos