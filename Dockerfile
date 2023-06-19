FROM python:3.10.9
  
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .
#COPY known_hosts /root/.ssh/
# Instala las dependencias
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update && apt-get -y upgrade && apt-get -y install openssh-client unixodbc
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18 mssql-tools
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

RUN mkdir /BGENTE

# Cambiar el el openssl para acepte TLSv1.0 por problemas de compatibilidad
RUN sed -i 's/SECLEVEL=2/SECLEVEL=1/g' /etc/ssl/openssl.cnf

# Ejecuta el comando python index.py 
CMD ["python", "index.py"]
# Ejecuta el comando python index.py 
#@CMD ["python", "indexWithDate.py"]

# docker build -t lote_bangente .   

# docker stop $(docker ps -aq)
# docker rm $(docker ps -aq)

#remove
# docker rmi --force lote_bangente
# docker ps -a  
# docker stop
# docker rm
# docker build -t lote_bangente .   

# docker stop $(docker ps -aq)
# docker rm $(docker ps -aq)

#remove
# docker rmi --force lote_bangente
# docker ps -a  
# docker stop
# docker rm
