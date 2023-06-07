FROM python:3.10.9

WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Ejecuta el comando python index.py con parámetros
CMD ["python", "index.py"]
