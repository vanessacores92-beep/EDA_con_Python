# 📊 Bank Marketing EDA

## 🧾 Descripción del proyecto

Este proyecto consiste en un Análisis Exploratorio de Datos (EDA) aplicado a un dataset de marketing bancario. El objetivo principal es identificar los factores que influyen en la decisión de los clientes de suscribirse a un producto financiero.

El análisis abarca desde la limpieza y transformación de los datos hasta la extracción de insights relevantes que permitan entender el comportamiento de los clientes.

---

## 🎯 Objetivos

- Analizar la estructura y calidad de los datos
- Identificar patrones y relaciones entre variables
- Determinar qué factores influyen en la suscripción (`subscription`)
- Extraer conclusiones útiles para la toma de decisiones

---

## 🗂️ Estructura del proyecto

📦 proyecto/
┣ 📁 data_raw/
┃ ┣ bank-additional.csv
┃ ┗ archivo_excel.xlsx
┃
┣ 📁 data_processed/
┃ ┗ bank_final.csv
┃
┣ 📓 notebook.ipynb
┗ 📄 README.md


---

## 🧹 Procesamiento de datos

Se realizaron las siguientes tareas:

- eliminación de columnas irrelevantes o con alto porcentaje de valores nulos  
- tratamiento de valores faltantes  
- transformación de variables (fechas, categóricas, binarias)  
- unificación de múltiples datasets mediante `merge`  
- creación de nuevas variables (como grupos de edad)  

---

## 📊 Análisis realizado

### 🔹 Análisis univariado
- estudio de la distribución de variables numéricas y categóricas  
- detección de valores extremos  
- identificación de sesgos en los datos  

### 🔹 Análisis bivariado
Se analizaron las relaciones entre variables y la variable objetivo (`subscription`):

#### ✔ Variables relevantes:
- `job`
- `income`
- `age_group`
- `contact`

#### ❌ Variables no relevantes:
- `marital`
- `education`
- `housing`
- `loan`

---

## 📈 Principales conclusiones

- El perfil profesional (`job`) influye en la probabilidad de suscripción  
- El nivel de ingresos (`income`) muestra cierta relación con el comportamiento del cliente  
- La edad, agrupada en rangos (`age_group`), presenta diferencias en la tasa de suscripción  
- El tipo de contacto (`contact`) puede afectar al resultado  

Por el contrario:

- Variables como estado civil, educación o situación financiera básica no muestran impacto significativo  

---

## 💡 Recomendaciones

- segmentar campañas por perfil profesional  
- enfocar estrategias en determinados grupos de edad  
- priorizar canales de contacto más efectivos  
- considerar el nivel de ingresos en la toma de decisiones  

---

## 🛠️ Tecnologías utilizadas

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  

---

## 👤 Autor

Proyecto realizado por Vanesa Cores como práctica de análisis de datos.

