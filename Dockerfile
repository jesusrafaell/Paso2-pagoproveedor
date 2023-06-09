FROM python:3.10.9

# Descargar e instalar el controlador ODBC de Microsoft SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Instalar las dependencias necesarias
RUN apt-get update && apt-get install -y unixodbc-dev

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos del proyecto al contenedor
COPY . .

# Ejecutar el comando "python app.py" con los parámetros deseados
ENTRYPOINT ["python", "app.py"]



# docker build -t lote_bangente .   

# docker stop $(docker ps -aq)
# docker rm $(docker ps -aq)

#remove
# docker rmi --force lote_bangente
# docker ps -a  
# docker stop
# docker rm