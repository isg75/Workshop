# Tutorial introductorio al análisis de datos en Python

¡Bienvenid@s a este tutorial introductorio de análisis de datos en Python.

El propósito de este tutorial es mostrar las posibilidades que permite el análisis de datos en Python.

## Diapositivas

Si estás interesado en una visión muy breve de las posibilidades que ofrece el análisis de datos, en el directorio *slides/* 
encontrarás una breve presentación para poder hacerte una idea.

## Datos

En este tutorial, analizaremos un dataset público de avistamientos de ardillas en Central Park que puedes descargar [aquí](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw). Si lo prefieres, podrás encontrar una copia de estos datos 
en el directorio *data/*.

## Instalación

Para poder tener una copia de todo el material en tu ordernador, abre una `Terminal` en Linux/MacOS ó bien un `Anaconda prompt` en Windows dentro del y escribe:

```shell
git clone https://github.com/isg75/Workshop
cd Workshop
```

## Creación de un entorno de trabajo

Es muy aconsejable que crees un *entorno de trabajo* para poder instalar las librerías que necesitarás para este tutorial sin que sea necesario reemplazar las que ya possees en tu ordenador. Para crear un entorno, abre una `Terminal` en Linux/MacOS ó bien un `Anaconda prompt` en Windows dentro del directorio del tutorial y escribe:

```shell
# En Linux/MacOS
python -m venv tutorial

# En Windows
python -m venv tutorial
```

de esta manera podrás tener distintas versiones de las librerías en el entorno *tutorial* a las que ya tengas instaladas en tu ordenador sin que se reemplacen las ya existentes.

## Activatión del entorno de trabajo

Verás que el comando anterior genera un directorio llamado `tutorial` que será el *entorno de trabajo*. Sin embargo, este *entorno* no estará `activo` y deberás activarlo. Para *activar* el *entorno*, en la `Terminal` de Linux/MacOS ó bien en el `Anaconda prompt` de Windows escribe:

```shell
# En Linux/MacOs
source tutorial/bin/activate

# En Windows
tutorial\scripts\activate.bat
```

Tras ello, deberías ver que al principio de la línea en la terminal aparece la palabra `tutorial` indicando que estás en el *entorno* `tutorial` en lugar del entorno por defecto.

## Notebook

Para este tutorial, utilizaré un `jupyter notebook` que puedes encontrar en el directorio *notebooks/* en donde trataremos de responder a distintas
preguntas que podemos hacernos sobre las ardillas de Central Park.

En el directorio *notebooks/* encontrarás un fichero llamado `requirements.txt` que contiene todas las librerías (y sus versiones) que son necesarias
para poder ejecutar el notebook. Para poder instalar las librerías necesarias en el *entorno* `tutorial`, en la `Terminal` de Linux/MacOS ó bien en el `Anaconda prompt` de Windows escribe:

```shell
cd notebooks
pip install -r requirements.txt
```

y espera a que termine el proceso (lleva tiempo).

Si no dispones de una instalación adecuada de `Python` y `jupyter` y no te quieres complicar, puedes ejecutar el *notebook* haciendo *click* en el botón inferior: 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/isg75/Workshop/HEAD?labpath=https%3A%2F%2Fgithub.com%2Fisg75%2FWorkshop%2Fblob%2Fmain%2Fnotebooks%2Fnotebook-ardillas.ipynb)

Si prefieres abrir el notebook en to ordenador,implemente en la `Terminal` de Linux/MacOS ó bien en el `Anaconda prompt` de Windows escribe:

```shell
jupyterlab notebook-ardillas.ipynb
```

esto abrirá una pestaña en tu navegador por defecto con el notebook abierto.

## Aplicación

Finalmente, también veremos cómo podemos crear una simple aplicación en Python para explorar los datos haciendo uso de la librería [streamlit](https://docs.streamlit.io/). 

En el directorio *app/* encontrarás otro fichero llamado `requirements.txt` que contiene todas las librerías (y sus versiones) que son necesarias
para poder ejecutar la aplicación. Para poder instalar las librerías necesarias en el *entorno* `tutorial` creado anteriormente abre una `Terminal` en Linux/MacOS ó bien un `Anaconda prompt` en Windows dentro del directorio `app` y escribe:

```shell
# En Linux/MacOS
cd ../app
pip install -r requirements.txt

# En Windows
cd ..\app
pip install -r requirements.txt
```

y espera a que termine el proceso (debería llevar algo menos de tiempo ya que ya tienes unas cuantas librerías instaladas).

Para poder ejecutar la aplicación, abre una `Terminal` en Linux/MacOS ó bien un `Anaconda prompt` en Windows dentro del directorio `app` y escribe:

```shell
streamlit run app.py
```

Tras unos segundos, se abrirá una nueva pestaña en tu navegador por defecto con la aplicación.

Espero que lo disfrutes y te motive a entrar en el interesante mundo del análisis de datos con Python.

## Desactivación del entorno de trabajo

Puedes `desactivar` el entorno de trabajo `tutorial` al terminar. Para ello, abre una `Terminal` en Linux/MacOS ó bien un `Anaconda prompt` en Windows dentro del directorio del proyecto y escribe:

```shell
deactivate
```

