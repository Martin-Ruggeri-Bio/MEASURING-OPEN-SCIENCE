# MEASURING-OPEN-SCIENCE
# Procesador de Papers ficticio

    El procesador de papers genera de forma Random los datos de autores, sus papers y sus citas
    
## Procesador de Papers Real
    La busqueda de los papers se deberia realizar con web scraping en los repositorios publicos de google scholar 
    El procesamiento de los papers se deberia realizar con PNL en python con la libreria Pandas, Scikit-learn, XGBoost, TextBlog, Keras entre otras para poder obtener de los pdf los parametros necesarios para enviarle a la class Paper para mapear dichos datos

# Papers

    La class Paper sirve para mapear los papers para que tengan los atributos necesarios para trabajar.
    Al cargar una cita en un papers, guarda una referencia de memoria del objeto paper que esta citando y a ese papers se le carga una referencia de memoria del objeto paper que lo cito, a traves de los atributos de country prodremos saber de que pais es el paper citado y el citador asi como tambien la categoria institucion y datos de contacto del author
# Servicio de carga de papers

	Este servicio hace 1000 llamadas al procesador de paper para generar los parametros para crear 1000 objetos de la clase paper.
	Luego a cada paper se le cargan las citas correspondientes proceso en el cual no solo se modifica el contenido del atributo que almacena las citas de dichos paper sino tambien que se modifica el atributo de citado del paper que se cito junto a otras medidas de cuantitativas y categoricas de dichas citas como la cantidad de citas nacionales e internacionales y la informacion del pais del paper que cito y fue citado.
    Luego genera un dataframe donde almacena todos los papers donde de enviara a distintas funciones que aplicaran ciencia de datos para filtrar, ordenar y procesar los datos para obtener ouput de valor
# Data Cience

	Aqui se aplican los distintos filtros y se crean las metricas de ciencia abierta con distintas funciones para crear distintos dataframes y guardarlos en archivos csv que se enviaran a software de data analist como data estudio para generar graficas para representar la informacion de forma amigable

# Data Analist
	Aqui se muestran graficas para representar algunas de las tablas creadas, se adjunta el link de data studio
	https://datastudio.google.com/reporting/c0b4b8df-5ac1-46fa-9aee-162b30a2d6fe
