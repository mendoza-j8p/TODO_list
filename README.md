# TODO List

Este proyecto es una aplicación de lista de tareas donde puedes crear, mostrar, actualizar y eliminar tareas. Se utiliza para gestionar tus tareas diarias de forma sencilla.

## Requisitos

- Python 3.7
- Pylint para análisis estático de código
- colorama para la salida de texto con colores

## Configuración

Para configurar el entorno y ejecutar la aplicación, sigue los siguientes pasos:

### 1. Clona el repositorio

Clona este repositorio en tu máquina local:

```bash
git clone <URL_DEL_REPOSITORIO>
cd TODO_list
```

### 2. Crea un entorno virtual

```bash
python -m venv .venv
```

### 3. Activa el entorno virtual

```bash
.\.venv\Scripts\activate
```

### 4. Instala las dependencias necesarias

```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar la aplicación

```bash
python main.py
```

Una vez que la aplicación esté en ejecución, podrás interactuar con ella a través de un menú de opciones.

### Opciones disponibles y menu principal:

Ttitulo del proyecto + Python version.

1. Crear tarea: Ingresa el nombre de una nueva tarea.
2. Ver tareas actuales: Muestra todas las tareas existentes con su estado.
3. Actualizar tarea: Marca una tarea como completada.
4. Eliminar tarea: Elimina una tarea de la lista.
5. Salir: Finaliza la aplicación.

## Ejemplo de uso:

1. Elige la opción 1 para crear una tarea.

Te pedirá que ingreses el nombre de la tarea.
* Ejemplo: Ir al gimnasio.
- Se mostrará un mensaje de confirmación con el nombre de la tarea y la fecha de creación.

- __Si la tarea esta en blanco dará un mensaje avisandolo y la opcion de salir al menu anterior escribiendo 'exit'.__

2. Elige la opción 2 para ver las tareas actuales.

- Veras algo como:
```
Tareas:
1. Ir al gimnasio - Pendiente
```

3. Elige la opción 3 para actualizar una tarea a completada.

- Ingresa el nombre de la tarea que deseas marcar como completada.
- Se mostrará el mensaje: 
```
Tarea 'x' marcada como completada.
```

4. Elige la opción 4 para eliminar una tarea escribiendo su nombre o todas las tareas escribiendo 'ALL'.

- Ingresa el nombre de la tarea que deseas eliminar.
- Se mostrará el mensaje: 
```
¡Tarea 'x' eliminada con éxito!
```
- Si escribe ALL:
- Se mostrara un mensaje para confirmar si realmente quiere eliminarlas todas.
- Y finalmente un mensaje confirmando su elección.

5. Elige la opción 5 para salir de la aplicación.


__Opcionales creadas:__
- Opciones de volver al menu anterior.
- Visualizacion de las tareas creadas, antes de actualizar y borrar.
- Sin posiblidad de introducir tareas en blanco.



## Análisis estático de código

Desde la raiz del proyecto, introduciremos el siguiente comando:

(Ignora la carpeta .venv y graba la salida en un archivo llamado: pylint_report.txt)

```bash
pylint --ignore .venv . > pylint_report.txt
```

+ __.pylintrc__: Archivo de configuracion en la raiz del proyecto


## Autores
Jenifer Mendoza - Desarrollador principal - @mendoza-j8p

## Enlaces útiles:
- Documentacion __pylint__:
  https://pylint.pycqa.org/en/v2.10.2/