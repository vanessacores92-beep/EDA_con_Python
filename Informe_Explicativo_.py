# %% [markdown]
# 📊 ANÁLISIS EXPLORATORIO DE DATOS (EDA) – MARKETING BANCARIO

# %% [markdown]
# 🧾 1. INTRODUCCIÓN

# %% [markdown]
# El presente proyecto tiene como objetivo realizar un análisis exploratorio de datos (EDA) sobre un dataset de marketing bancario, con el fin de identificar los factores que influyen en la decisión de los clientes de suscribirse a un producto financiero.
# El análisis se centra en comprender el comportamiento de los clientes, detectar patrones relevantes y extraer conclusiones que puedan ser útiles para la toma de decisiones en estrategias de marketing.

# %% [markdown]
# 🎯 2. OBJETIVO DEL ANÁLISIS

# %% [markdown]
# Los principales objetivos del proyecto son:
# Analizar la estructura y calidad de los datos disponibles
# Identificar variables relevantes que influyen en la suscripción
# Detectar patrones y relaciones entre variables
# Evaluar la utilidad de las variables disponibles
# Extraer conclusiones y recomendaciones basadas en los datos

# %% [markdown]
# 📥 3. CARGA E INTEGRACIÓN DE LOS DATOS

# %% [markdown]
# El análisis parte de múltiples fuentes de datos:
# Un archivo principal en formato CSV con información general de clientes
# Un archivo en formato Excel con información adicional distribuida en varias hojas (correspondientes a distintos años)
# Las tablas del archivo Excel presentan la misma estructura, por lo que se han unificado en un único dataset. Posteriormente, se ha realizado un proceso de integración mediante operaciones de merge, utilizando el identificador único de cliente como clave.
# Como resultado, se obtiene un dataset consolidado (bank_final) que contiene toda la información relevante para el análisis.

# %% [markdown]
# 🧹 4. LIMPIEZA Y PREPARACIÓN DE LOS DATOS

# %% [markdown]
# Durante esta fase se han realizado diversas tareas para garantizar la calidad y consistencia de los datos:
# 🔹 Tratamiento de valores nulos
# Se ha llevado a cabo un análisis del porcentaje de valores faltantes en cada variable, adoptando distintas estrategias:
# Eliminación de variables con un alto porcentaje de valores nulos y baja relevancia analítica
# Imputación de valores en variables categóricas mediante la categoría "Unknown"
# Imputación de variables numéricas mediante medidas estadísticas como la mediana
# 🔹 Eliminación de variables irrelevantes
# Se han eliminado variables que no aportaban valor al análisis, bien por su alta proporción de valores nulos o por su escasa capacidad explicativa.
# 🔹 Transformación de variables
# Conversión de variables binarias de formato numérico (0/1) a categórico ("Yes"/"No") para mejorar la interpretabilidad
# Transformación de variables de fecha al formato adecuado
# Renombrado de variables para facilitar su comprensión (por ejemplo, y → subscription)
# 🔹 Creación de nuevas variables
# Se ha generado una nueva variable (age_group) agrupando la edad en rangos, con el objetivo de facilitar el análisis y mejorar la interpretabilidad de los resultados.

# %% [markdown]
# 📊 5. ANÁLISIS UNIVARIADO

# %% [markdown]
# En esta fase se ha realizado un análisis individual de cada variable con el objetivo de comprender su distribución y detectar posibles anomalías.
# 🔹 Variables numéricas
# Se analizaron variables como age e income, observándose:
# Distribuciones no uniformes, en algunos casos sesgadas
# Presencia de valores extremos (outliers), especialmente en la variable income
# Concentración de valores en determinados rangos
# Se utilizaron gráficos como boxplots y curvas de densidad (KDE) para visualizar estas características.
# 🔹 Variables categóricas
# Se analizaron variables como job, marital, education, housing y loan, observando:
# Distribución desigual entre categorías
# Presencia de categorías dominantes
# Aparición de valores "Unknown" tras el tratamiento de nulos
# Este análisis permitió comprender la composición del dataset antes de estudiar relaciones entre variables.

# %% [markdown]
# 🔗 6. ANÁLISIS BIVARIADO

# %% [markdown]
# El objetivo de esta fase es analizar la relación entre las variables independientes y la variable objetivo (subscription).
# 🔹 Variables con relación significativa
# ✔ Job (perfil profesional)
# Se observan diferencias en la tasa de suscripción entre distintos perfiles profesionales, lo que indica que el tipo de ocupación puede influir en la decisión del cliente.
# ✔ Income (nivel de ingresos)
# El nivel de ingresos muestra cierta relación con la suscripción, observándose que los clientes con mayores ingresos tienden, en algunos casos, a presentar una mayor probabilidad de contratación.
# ✔ Age_group (grupo de edad)
# El análisis por grupos de edad revela diferencias en el comportamiento de los clientes, lo que sugiere que la edad es un factor relevante en la toma de decisiones.
# ✔ Contact (tipo de contacto)
# El canal de contacto utilizado (teléfono móvil, fijo, etc.) muestra variaciones en los resultados, lo que puede indicar su influencia en la efectividad de la interacción.
# 
# 🔹 Variables sin relación significativa
# Las siguientes variables no presentan diferencias relevantes en relación con la suscripción:
# marital
# education
# housing
# loan
# Estas variables muestran distribuciones similares entre los grupos de clientes que suscriben y los que no, por lo que no parecen ser determinantes en el comportamiento observado.
# 
# 🔹 Consideraciones sobre variables específicas
# ⚠ Duration
# La variable duration (duración de la llamada) muestra una fuerte relación con la suscripción. Sin embargo, esta variable debe interpretarse con cautela, ya que puede estar influida por el propio resultado de la interacción, lo que podría generar sesgos en el análisis.

# %% [markdown]
# 🎯 7. CONCLUSIONES

# %% [markdown]
# El análisis realizado permite extraer las siguientes conclusiones principales:
# El comportamiento de los clientes está influido por variables relacionadas con su perfil profesional, edad y nivel de ingresos
# No todas las variables disponibles aportan valor explicativo, siendo necesario realizar una selección adecuada
# Factores relacionados con la interacción, como el tipo de contacto, pueden influir en el resultado final
# En conjunto, el dataset muestra patrones que permiten segmentar a los clientes y entender mejor su comportamiento.

# %% [markdown]
# 💡 8. RECOMENDACIONES

# %% [markdown]
# A partir de los resultados obtenidos, se proponen las siguientes recomendaciones:
# Diseñar estrategias de marketing segmentadas por perfil profesional
# Adaptar campañas en función de la edad de los clientes
# Priorizar los canales de contacto más efectivos
# Considerar el nivel de ingresos como variable relevante en la segmentación

# %% [markdown]
# 📌 10. CONCLUSIÓN FINAL

# %% [markdown]
# El análisis exploratorio realizado ha permitido comprender la estructura del dataset, identificar variables relevantes y extraer insights útiles sobre el comportamiento de los clientes.
# Este tipo de análisis constituye una base fundamental para posteriores fases de modelado y toma de decisiones basada en datos.


