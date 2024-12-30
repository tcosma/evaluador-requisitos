from utils.scoring import calcular_similitud, evaluar_requisito

def combinar_reglas_y_modelo(requisito, criterios, modelo_embeddings):
    if len(requisito.split()) < 7:
        return "El requisito no puede ser evaluado.", ["El requisito es demasiado corto para ser evaluado."]

    pr, aspectos = evaluar_requisito(requisito, criterios)

    pm_ideal = calcular_similitud(requisito, criterios["ejemplos_ideales"], modelo_embeddings) * 10
    pm_ideal = min(pm_ideal, 10.0)  

    pm_no_ideal = calcular_similitud(requisito, criterios["requisitos_no_ideales"], modelo_embeddings) * 10
    pm_no_ideal *= 0.75 if pm_ideal > 7 else 1.25 

    pf = 0.85 * pr + 0.7 * pm_ideal - 0.55 * pm_no_ideal
    pf = max(1.0, min(pf, 10.0))

    if pf < 5:
        mensaje = "El requisito no tiene sentido, necesita mejoras importantes."
    elif 5 <= pf <= 7:
        mensaje = "El requisito es aceptable, pero necesita varias mejoras."
    elif 8 <= pf < 9:
        mensaje = "El requisito es bueno, pero hay algunos detalles que podrían optimizarse."
    elif pf >= 9:
        mensaje = "El requisito es excelente. Cumple con los criterios establecidos."

    return mensaje, aspectos
