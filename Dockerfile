# Usa una imagen base de Python
FROM python:3

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el código y el archivo de configuración al directorio de trabajo del contenedor
COPY . /app

# Instala las dependencias
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade requests beautifulsoup4 lxml jproperties cx_Oracle

# Establece la hora y la zona horaria
RUN ln -fs /usr/share/zoneinfo/Europe/Paris /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

# Descarga e instala diferentes paquetes
RUN apt-get update && apt-get -y upgrade && apt-get -y install libaio1 unzip cron

# Descarga el cliente Oracle Instant Client ZIP desde una ubicación en línea o copia desde una ubicación local
COPY ./instant_client_linux/instantclient-basic-linux.x64-21.11.0.0.0dbru.zip /tmp/
RUN unzip /tmp/instantclient-basic-linux.x64-21.11.0.0.0dbru.zip -d /opt/oracle/
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_11
ENV ORACLE_HOME=/opt/oracle/instantclient_21_11
ENV PATH=$PATH:$ORACLE_HOME

# Agrega la tarea cron al archivo cron dentro del contenedor
RUN echo "0 15 * * * /app/cron_script.sh" | crontab -

# Define an environment variable for the Python interpreter to use
ENV PYTHONUNBUFFERED=1

# Inicia cron como proceso principal en segundo plano
CMD ["cron", "-f", "-L", "/dev/stdout"]