# Star Wars Mandalorian: NLP Classifier
## Autor
* Nombre: Alberto Becerra Tomé

## Misión

Agente Kallus,

Si está leyendo este mensaje es que ha alcanzado el piso franco que El Imperio 
tiene instalado cerca de la base Rebelde en la ciudad de Norg Bral. Bien hecho, 
aunque su trabajo aquí no ha hecho más que empezar.Como sabe, el planeta 
Mandalore es de una gran importancia estratégica para nosotros y tenemos que 
estar preparados ante cualquier movimiento de los comandos Rebeldes que se 
encuentran estacionados allí. Para anticiparnos a ellos, hemos estado 
desarrollando en los últimos meses un sistema de interceptación de 
comunicaciones que estamos cerca de poner en marcha y que se encuentra instalado
en su localización. El último módulo que queda por desarrollar es elsubsistema 
de clasificación de transmisiones. Aquí es donde entra usted.

**Detalles de la misión**

Nuestro departamento de inteligencia ha clasificado todas las comunicaciones 
interceptadas durante las últimas semanas en 7 categorías distintas, atendiendo 
a las divisiones Rebeldes a las que pertenecen. La misión es conseguir que el 
sistema de clasificación sea capaz de 
**clasificar una nueva transmisión de manera automática** para que el 
departamento de operaciones pueda evaluarlas amenazas más rápido.

## Descripción
En este proyecto se construye un subsistema de clasificación de transmisiones como parte del sistema de interceptación de comunicaciones. Para ello se usarán herramientas de NLP.

## Requisitos de instalación
- Python Version: 3.8.0
- Virtual Env:
    - Entorno virtual en la carpeta *./venv*
    - Librerías en *./requirements.txt*
    - Para este entorno se está usando un kernel de Jupyter específico (```python -m ipykernel install --name=venv```)
    - Si estuviéramos en GitHub, la carpeta *./venv* estaría ignorada por Git, ya que es posible reconstruir el entorno con *requirements.txt*

## Contenido del Proyecto
- Notebook *ANALYSIS.ipynb* con la información del proyecto y el análisis
- Carpeta *dataset* con los datos para el clasificador
- Carpeta *venv* con la información del entorno
- Fichero *requirements.txt* para restaurar el entorno
- Funciones auxiliares en *utils.py*
- JSON *target_encoder.json* con el mapeo número - nombre del target
- Modelo serializado de Python en *trained_model.pkl*
- Scripts de entrenamiento de modelo:
    - Python: train.py
    - Ejecutable PowerShell: train.ps1 (llama a train.py)
- Scripts del clasificador:
    - Python: classify.py
    - Ejecutable PowerShell: classify.ps1 (llama a classify.py)
- Fichero de log de la última ejecución de *train.ps1* en *lastrun.log*

## Pasos para la correcta ejecución

1. Activación del entorno (```>venv/Scripts/activate```) o reconstrucción del mismo con ayuda de ```>virtual venv``` y ```>venv/Scripts/activate```
2. Instalación de las librerías en el entorno activado ```(venv)>pip install-r requirements.txt```
3. Llamada al ejecutable de entrenamiento ```>.\train.ps1 dataset``` donde dataset es la fuente de los datos en la estructura dataset/categoria/fichero.
4. Una vez está entrenado el modelo, se escriben los ficheros .json, .log y .pkl citados previamente
5. Para obtener las predicciones una vez entrenado el modelo ```>.\classify.ps1 model file1 file2 ...```
