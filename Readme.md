# Evaluador de Requisitos

Este proyecto es una herramienta diseñada para evaluar la calidad de requisitos de software mediante frases descriptivas. Su objetivo principal es proporcionar retroalimentación cualitativa que permita mejorar la redacción de requisitos y alinearlos con criterios predefinidos.

---

## Introducción

Escribir requisitos claros y bien estructurados es crucial para el éxito de proyectos de desarrollo de software. Sin embargo, esta tarea puede ser difícil debido a la ambigüedad y la subjetividad en la redacción. Este proyecto ofrece una herramienta automatizada que evalúa la calidad de los requisitos, proporcionando retroalimentación inmediata y específica para mejorarlos.

---

## Motivación  

Este proyecto surge de la necesidad de desarrollar un evaluador de requisitos que, aunque básico en un primer momento, ofrezca un nivel de precisión aceptable en gran parte de los casos y requiera un uso mínimo de recursos. 

---

## Características

- **Clasificación cualitativa**: Los requisitos se evalúan en base a descripciones como "Mal estructurado", "Aceptable", "Bueno" o "Excelente".
- **Análisis contextual**: Evalúa profesionalismo, claridad, verificabilidad, completitud y consistencia.
- **Retroalimentación personalizada**: Proporciona mensajes específicos sobre cómo mejorar los requisitos.
- **Integración con ejemplos ideales y no ideales**: Calcula similitudes con plantillas predefinidas para identificar la calidad del requisito.

Nota: Si el requisito es demasiado corto, también se indicará que no puede ser evaluado.

---

## Limitaciones Actuales

- La herramienta no evalúa requisitos escritos en idiomas diferentes al español.
- Los resultados dependen de la calidad de los criterios y ejemplos ideales proporcionados.
- No realiza evaluaciones contextuales complejas (e.g., interpretación de dominios específicos).
- Necesita de modelos LLM de HuggingFace para poder funcionar.
---

## Requisitos del Sistema

- **Python** 3.8 o superior
- Librerías necesarias (ver `requirements.txt`):
  - `numpy`
  - `scipy`
  - `sentence-transformers`
  - `transformers`
  - `streamlit`

---

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tcosma/evaluador-requisitos.git
   cd evaluador-requisitos
   ```

2. **Crea un entorno virtual** (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   .\venv\Scripts\activate  # Windows
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
---

## Uso

1. Ejecuta el archivo principal del proyecto:
   ```bash
   streamlit run main.py
   ```

2. Ingresa un requisito en el área de texto proporcionada.

3. Recibirás una evaluación cualitativa del requisito, acompañada de recomendaciones para mejorarlo.

---

## Estructura del Proyecto

```
evaluador-requisitos/
│
├── criterios/
│   └── criterios_requisitos.json   # Archivo de criterios predefinidos
│
├── utils/
│   ├── __init__.py                 # Archivo para inicializar el paquete utils
│   ├── criteria.py                 # Carga y validación de criterios
│   ├── models.py                   # Carga de modelos de embeddings
│   └── scoring.py                  # Cálculo de similitud y evaluación
│
├── __init__.py                     # Archivo para inicializar el paquete app
├── .gitignore                      # Aplicación principal
├── main.py                         # Aplicación principal
├── evaluation.py                   # Lógica principal de evaluación
├── LICENSE                         # Licencia del proyecto
├── requirements.txt                # Dependencias del proyecto
└── README.md                       # Documentación del proyecto
```

---

## Ejemplos de Evaluación de Requisitos

A continuación, se presentan ejemplos de cómo la herramienta evalúa diferentes tipos de requisitos, con su entrada y salida:

### **Requisitos No Evaluables Por Longitud**
**El sistema debe ser rápido**  
   _El requisito no puede ser evaluado._

### **Requisitos Mal Estructurados**
**Hacer que todo funcione bien y rápido.**  
   _El requisito tiene fallos graves, necesita mejoras importantes._

### **Requisitos Aceptables**
**El sistema debe ser el más rápido del mercado.**  
   _El requisito es aceptable, pero necesita varias mejoras._

### **Requisitos Buenos**
**El sistema debe garantizar un tiempo de actividad del 99.9% durante horarios laborales (8:00 a 18:00).**  
   _El requisito es bueno, pero hay algunos detalles que podrían optimizarse._

### **Requisitos Excelentes**
**La aplicación debe ser capaz de procesar y responder a solicitudes de búsqueda con un tiempo de respuesta promedio inferior a 1 segundo para un volumen de hasta 1 millón de usuarios concurrentes, garantizando una tasa de éxito del 99,99%, y deberá implementarse antes del 30 de junio de 2025.**  
   _El requisito es excelente. Cumple con los criterios establecidos._

---

## Contribuciones

1. Haz un fork del repositorio.
2. Crea una rama para tus cambios:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Envía un pull request para revisión.

---
## Referencias

1. **[Leveraging LLMs for the Quality Assurance of Software Requirements](https://arxiv.org/html/2408.10886v1)**  
   Uso de LLMs para mejorar la calidad de requisitos de software.

2. **[Using LLMs in Software Requirements Specifications: An Empirical Evaluation](https://arxiv.org/html/2404.17842v1)**  
   Evaluación del uso de LLMs en especificaciones de requisitos.

3. **[Plataforma de Contratación del Sector Público](https://contrataciondelestado.es/)**  
   Portal oficial para consultar requisitos en licitaciones públicas.

--- 

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

