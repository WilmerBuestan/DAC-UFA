# DAC-UFA

Aquí tienes un archivo `README.txt` con las instrucciones claras para que cualquier persona pueda ejecutar tu aplicación en su computadora. Este archivo incluye todos los pasos necesarios, desde crear el entorno virtual hasta ejecutar el servidor Flask.

---

### **Archivo `README.txt`**

```
# Analizador Militar de Documentos Word

Esta aplicación permite analizar documentos Word (.docx) para identificar problemas de formato como fuente, tamaño de letra, justificación, y contar palabras. Diseñada para propósitos militares, incluye un análisis sencillo y eficiente.

---

## Requisitos Previos

1. Tener Python 3.7 o superior instalado.
   - Descarga Python desde: https://www.python.org/downloads/
   - Durante la instalación, asegúrate de seleccionar "Add Python to PATH".

2. Un editor de texto o IDE como Visual Studio Code.

---

## Pasos para Configurar y Ejecutar

### 1. Clonar o Descargar el Proyecto
Descarga o clona este proyecto en una carpeta de tu elección.

### 2. Crear un Entorno Virtual
Abre una terminal o consola en la carpeta del proyecto y ejecuta:

```
python -m venv env
```

Esto creará un entorno virtual llamado `env`.

### 3. Activar el Entorno Virtual
- En **Windows**:
  ```
  .\env\Scripts\activate
  ```
- En **Mac/Linux**:
  ```
  source env/bin/activate
  ```

Verás `(env)` al inicio de tu terminal si el entorno virtual está activado.

### 4. Instalar las Bibliotecas Necesarias
Con el entorno virtual activado, instala las dependencias del proyecto:

```
pip install flask python-docx
```

### 5. Estructura del Proyecto
Asegúrate de que la estructura del proyecto sea la siguiente:

```
tu_carpeta/
├── env/                   # Entorno virtual
├── templates/
│   └── index.html         # Archivo HTML para la interfaz
├── app.py                 # Archivo principal de Flask
```

### 6. Ejecutar el Servidor
Con el entorno virtual activado, ejecuta el archivo principal:

```
python app.py
```

Deberías ver en la terminal un mensaje como este:

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### 7. Acceder a la Aplicación
Abre tu navegador web y visita la URL:

```
http://127.0.0.1:5000/
```

Desde ahí podrás subir documentos Word para analizarlos.

---

## Solución de Problemas

1. **Flask no está instalado:**
   - Verifica que el entorno virtual esté activado y ejecuta:
     ```
     pip install flask
     ```

2. **El archivo `index.html` no se encuentra:**
   - Asegúrate de que el archivo esté en la carpeta `templates` dentro del proyecto.

3. **Error de Puertos:**
   - Si el puerto 5000 está ocupado, cambia el puerto en el archivo `app.py`:
     ```python
     app.run(debug=True, port=8080)
     ```
   - Luego accede a: `http://127.0.0.1:8080/`.

---

## Créditos

Creado con Python, Flask y python-docx para análisis de documentos Word con propósitos militares.

```

---

