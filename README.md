# Proyecto SIEM con Docker 
## Configuración de siem_app, Logstash, Elasticsearch y Kibana

Este proyecto configura un sistema `SIEM` (Security Information and Event Management) utilizando contenedores Docker para siem_app (una aplicación Python), Logstash, Elasticsearch y Kibana.

# Tabla de contenidos

1. Requisitos

2. Clonación y Configuración del Proyecto

3. Configuración de Docker Compose

4. Construcción y Levantado de Contenedores

5. Configuración de Contenedores Docker

6. Verificación de Conexiones y Logs

7. Solución de Problemas

8. Acceso a Kibana y Visualización de Logs

# 1. Requisitos

Requisitos para ejecutar el proyecto:

* `Docker`
* `Docker Compose`
* `curl` (para verificar las conexiones)

---

# 2. Clonación y Configuración del Proyecto

1. Clona el repositorio del proyecto en tu máquina local:

```bash
git clone https://github.com/carmona-fugaz/SIEM.git

cd SIEM
```

2. Dentro del proyecto, deberás tener el archivo docker-compose.yml con la configuración de los contenedores.


---

# 3. Configuración de Docker Compose

El archivo docker-compose.yml configura los servicios que componen el proyecto: siem_app, logstash, elasticsearch y kibana. Además, se establece una red de tipo bridge para facilitar la comunicación entre los contenedores.


---

# 4. Construcción y Levantado de Contenedores

Después de configurar tu archivo `docker-compose.yml`, ejecuta el siguiente comando para construir las imágenes y levantar los contenedores

```bash
docker-compose up -d --build
```
Verifica que todos los contenedores estén funcionando:

```bash
docker ps -a
```

Esto debería mostrarte los contenedores en ejecución, incluyendo `siem_app`, `logstash`, `elasticsearch` y `kibana`.


---

# 5. Configuración de Contenedores Docker

### Contenedor siem_app:

* siem_app es una aplicación Python que se conecta a Logstash para enviar logs.

* Dentro del Dockerfile, se asegura de instalar todas las dependencias necesarias y  el código fuente de la aplicación.

### Contenedor logstash:

* Configurado para escuchar en el puerto 5000 y recibir los logs en formato JSON.

* El archivo de configuración logstash.conf debe estar correctamente montado para que Logstash procese los datos recibidos.

### Contenedor elasticsearch:

* Configurado para correr en un único nodo y exponer el puerto 9200 para acceder a Elasticsearch.

### Contenedor kibana:

* Accede a Elasticsearch para visualizar los logs procesados y ofrece una interfaz web en el puerto 5601.


---

# 6. Verificación de Conexiones y Logs

1. Verifica las conexiones entre contenedores con el siguiente comando:

```bash
docker exec -it <nombre del contenedor> ping <nombre del contenedor de destino>
```

2. Verifica los logs de `siem_app`; 
Si `siem_app` no se conecta correctamente a `logstash`, revisa los logs del contenedor con el siguiente comando:

```bash
docker logs siem_app
```

Revisa si hay algún error de conexión, como `ConnectionRefusedError`, y asegúrate de que `logstash` esté en funcionamiento.

3. Verifica los logs de logstash: Para revisar si logstash está escuchando correctamente, usa este comando:

```bash
docker logs logstash | grep "Listening"
```

Si todo está correcto, deberías ver algo como Listening on port 5000.


---

# 7. Solución de Problemas

Si experimentas problemas al levantar los contenedores o la comunicación entre ellos, aquí hay algunos pasos de solución:

* Verifica si los contenedores están corriendo: Si alguno de los contenedores no se está iniciando correctamente, verifica sus logs para obtener más información sobre el problema.

* Reinicia los contenedores: Si un contenedor no está funcionando correctamente, puedes intentar reiniciarlo con el siguiente comando:

```bash
docker restart siem_app
```

* Revisa la configuración de la red: Si la red no está configurada correctamente, puede que los contenedores no puedan comunicarse entre sí. Asegúrate de que todos los contenedores estén en la misma red (bridge en este caso).

* Verifica las dependencias: Si siem_app depende de logstash, asegúrate de que logstash esté completamente levantado antes de iniciar siem_app. Puedes verificar si un contenedor está listo usando docker logs.


---

# 8. Acceso a Kibana y Visualización de Logs

Una vez que todos los contenedores estén funcionando correctamente, puedes acceder a Kibana para visualizar los logs.

* Accede a Kibana usando la dirección `http://<ip>:5601`.

* Configura las visualizaciones en Kibana: En Kibana, configura los índices y visualizaciones para que puedas empezar a analizar los logs enviados desde `siem_app` a través de Logstash.


---

# Notas adicionales

1. Configuración de siem_app:

* Asegúrate de que `LOGSTASH_URL` en las variables de entorno de `siem_app` esté correctamente configurado para apuntar a la URL de tu contenedor Logstash.

2. Conexiones de red: 

* En este proyecto, la red Docker utilizada es de tipo `bridge`, lo que significa que todos los contenedores están en la misma red local de Docker y pueden comunicarse entre sí.

3. Monitorización y Escalabilidad: 

* Si deseas escalar este proyecto para procesar más logs, puedes agregar más instancias de `siem_app` o usar herramientas adicionales de monitorización.


---

# Conclusión
Este proyecto te permite configurar un sistema básico de SIEM utilizando Docker y herramientas como siem_app, Logstash, Elasticsearch y Kibana. Siguiendo los pasos anteriores, deberías poder levantar los contenedores y comenzar a procesar y visualizar logs de seguridad en tiempo real.

---
---

# SIEM project with Docker 
## Configuration of siem_app, Logstash, Elasticsearch and Kibana

This project configures a `SIEM` (Security Information and Event Management) system using Docker containers for siem_app (a Python application), Logstash, Elasticsearch and Kibana.

# Table of Contents

1. Requirements

2. Cloning and Project Configuration

3. Docker Compose Configuration

4. Building and Lifting Containers

5. Configuring Docker Containers

6. Verifying Connections and Logs

7. Troubleshooting

8. Accessing Kibana and Viewing Logs

# 1. Requirements

Requirements to run the project:

* `Docker`
* `Docker Compose`
* `curl` (for checking connections)

---

# 2. Cloning and Configuring the Project

1. Clone the project repository on your local machine:

```bash
git clone https://github.com/carmona-fugaz/SIEM.git

cd SIEM
```

2. Inside the project, you should have the docker-compose.yml file with the container configuration.


---

# 3. Configuring Docker Compose

The docker-compose.yml file configures the services that make up the project: siem_app, logstash, elasticsearch and kibana. In addition, a bridge network is set up to facilitate communication between the containers.


---

# 4. Building and Pulling Up Containers

After setting up your `docker-compose.yml` file, run the following command to build the images and lift the containers

```bash
docker-compose up -d --build
```
Verify that all containers are up and running:

```bash
docker ps -a
```

This should show you the running containers, including `siem_app`, `logstash`, `elasticsearch` and `kibana`.


---

# 5. Docker Container Configuration

### siem_app container:

* siem_app is a Python application that connects to Logstash to send logs.

* Inside the Dockerfile, it makes sure to install all the necessary dependencies and source code for the application.

### Logstash container:

* Configured to listen on port 5000 and receive logs in JSON format.

* The logstash.conf configuration file must be correctly mounted for Logstash to process the received data.

### Elasticsearch container:

* Configured to run on a single node and expose port 9200 to access Elasticsearch.

### kibana container:

* Accesses Elasticsearch to display processed logs and provides a web interface on port 5601.


---

# 6. Verifying Connections and Logs

1. Verify connections between containers with the following command:

```bash
docker exec -it <container name> ping <destination container name>.
```

2. Check the `siem_app` logs; 
If `siem_app` does not connect to `logstash` correctly, check the container logs with the following command:

```bash
docker logs siem_app
```

Check for any connection errors, such as `ConnectionRefusedError`, and make sure `logstash` is up and running.

3. Check the logstash logs: To check if logstash is listening correctly, use this command:

```bash
docker logs logstash | grep ‘Listening
```

If everything is correct, you should see something like Listening on port 5000.

---


# 7. Troubleshooting

If you experience problems getting the containers up or communicating between them, here are some troubleshooting steps:

* Check if the containers are running: If any of the containers are not starting correctly, check their logs for more information about the problem.

* Restart the containers: If a container is not running correctly, you can try restarting it with the following command:

```bash
docker restart siem_app
```

* Check the network configuration: If the network is not configured correctly, containers may not be able to communicate with each other. Make sure all containers are on the same network (bridge in this case).

* Check dependencies: If siem_app depends on logstash, make sure that logstash is fully up before starting siem_app. You can check if a container is ready using docker logs.


---

# 8. Accessing Kibana and Viewing Logs

Once all the containers are working properly, you can access Kibana to view the logs.

* Log in to Kibana using the address `http://<ip>:5601`.

* Configure the visualisations in Kibana: In Kibana, configure the indexes and visualisations so that you can start analysing the logs sent from `siem_app` via Logstash.


---

# Additional notes

1. siem_app configuration:

* Make sure `LOGSTASH_URL` in the `siem_app` environment variables is correctly set to point to the URL of your Logstash container.

2. Network connections: 

* In this project, the Docker network used is of type `bridge`, which means that all containers are on the same local Docker network and can communicate with each other.

3. Monitoring and Scalability: 

* If you want to scale this project to process more logs, you can add more `siem_app` instances or use additional monitoring tools.


---

# Conclusion
This project allows you to set up a basic SIEM system using Docker and tools such as siem_app, Logstash, Elasticsearch and Kibana. By following the steps above, you should be able to pull up the containers and start processing and visualising security logs in real time.