Las instancias son 30 archivos separados por comas, 15 con estrés al inicio
y 15 con estrés al final, el nombre del archivo se conforma de los siguiente:

	Ejemplo:	f_1_2
	posicionEstres_numInstancia_cantRequerimiento

Cada instancia se conforman de 10 columnas y 88 renglones. Las instancias con
actividades de precedencia tiene solo el 30% de las actividades con precedencias.

Las columnas significan lo siguiente:
1.- Materia             (Toma el valor de 1 o 2, solo hay dos materias)
2.- Tema                (Toma el valor de 1,2,3 o 4, solo existen 4 temas)
3.- Subtema             (Toma el valor entre 1-8, solo existen 8 subtemas
4.- Número de Actividad (Toma el valor entre 1-88, solo existen 88 actividades)
5.- Duración            (Toma valores entre 3-15)
6.- Valor               (Toma valores entre 9-15)
7.- Estrés              (Toma valores entre XX, esta columna no la utilizamos para este modelo)
8.- Obligatoria         (Toma el valor de 1 si la actividad es obligatoria)
9.- Requerimiento 1     (Toma el valor del num de la actividad que la precede, cero en otro caso)
10.-Requerimiento 2     (Toma el valor del num de la actividad que la precede, cero en otro caso)

----------------------------------------------------------------------------

El archivo estudiantes_AGRUPAMIENTO contiene los 45 perfiles de estrés
de estudiantes simulando diferentes niveles de estrés en cada uno. Cada columna
representa a un estudiante y puede presentar niveles bajos, medios o altos de estrés.

Los perfiles de estrés son los siguientes:

1.- Alto				(valores entre .35  - .5)
2.- Medio				(valores entre .16  - .34
3.- Bajo				(valores entre .001 - .15)
4.- Medio - Alto			(La mitad valores medios, el resto valores altos)
5.- Medio - Bajo			(La mitad valores medios, el resto valores bajos)
6.- Estrés Agudo 20%			(El 20% de las actividades tiene un valor alto de estrés)
7.- Alto - Medio Bajo			(La primer tercera parte tiene valores altos, la segunda valores medios y la última tercera parte valores bajos)
8.- Medio Bajo - alto - Medio Bajo	(La primer tercera parte y la última tiene valores medios y bajos, la tercera parte central son valores altos)
9.- Bajo - Medio - Alto			(La primer tercera parte tiene valores bajos, la segunda valores medios y la última tercera parte valores altos)

Cada perfil tiene 5 instancias, es decir el primer perfil tiene 5 columnas, el 
segundo las siguiente 5 y así sucesivamente hasta las 45 columnas.