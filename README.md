# Documentación del proyecto

![](app/static/resources/tierramedia.webp)

## Objetivo

Aplicación web funcional donde los usuarios, al autenticarse en el sistema, pueden simular batallas con personajes de la época medieval, ambientada en el universo de *El Señor de los Anillos*.

## Estructura del proyecto

- **README.md:** Documentación oficial del proyecto.
- **manage.py:** Archivo que permite ejecutar comandos como iniciar el servidor (`runserver`), aplicar migraciones (`migrate`), crear usuarios (`createsuperuser`), entre otros. Es esencial para la administración y desarrollo de la aplicación Django.
- **tierramedia/:** Directorio que almacena los archivos esenciales para la configuración y gestión global del proyecto, incluyendo ajustes, rutas y puntos de entrada para el servidor.
- **app/:** Directorio que contiene las funcionalidades principales de la aplicación web, como las URLs, vistas, modelos de datos, etc.
- **api/:** Directorio donde se alamacenan los serializadores y vistas de las apis del proyecto.

## Tecnologías utilizadas

1. **Python** - Lenguaje de programación de alto nivel utilizado para desarrollar la lógica del lado del servidor en aplicaciones web. Python es conocido por su simplicidad y versatilidad, permitiendo escribir código limpio y eficiente.
2. **Django** - Framework web de alto nivel para Python que facilita la creación de aplicaciones web rápidas y seguras. Django se utiliza para estructurar la aplicación web, manejar la base de datos, rutas y vistas, entre otras tareas.
3. **Bootstrap 5** - Framework de diseño que facilita la creación de interfaces web atractivas y funcionales. Bootstrap se utiliza para el diseño y estilo de las páginas del proyecto, asegurando que la interfaz sea responsiva y adaptada a distintos dispositivos.
4. **Cascading Style Sheets (CSS)** - Lenguaje de diseño utilizado para describir la presentación de las páginas web. CSS se usa para aplicar estilos visuales y definir la apariencia de los elementos dentro del proyecto.
5. **HyperText Markup Language (HTML)** - Lenguaje de marcado utilizado para estructurar el contenido de las páginas web. HTML permite organizar y mostrar texto, imágenes, enlaces y otros elementos dentro del navegador, creando la base de cada página web mediante el uso de etiquetas, que indican cómo debe organizarse y presentarse el contenido al usuario.

## Comandos a utilizar para ejecutar el proyecto

- docker rm -f $(docker ps -aq) (para borrar todos los contenedores que tengas y no haya problemas, también muestra los contenedores borrados)
- docker compose up -d --build (ejecutar la primera vez que se ejecute el programa o cada vez que se borran los volúmenes)
- docker compose run web python manage.py makemigrations
- docker compose run web python manage.py migrate (aplica las migraciones de datos iniciales)
- docker compose run web python manage.py createsuperuser (crear un superusuario y poder ingresar en la aplicación)
- docker ps (verifica que el servicio está ejecutándose)
- firefox localhost:8000 

## Consideraciones importantes

1. El proyecto guarda una lista de armas, facciones y ubicaciones ya creadas por defecto. El usuario no puede modificar ni añadir nuevos objetos de dichas clases. Sin embargo, el usuario sí podrá a través de un formulario añadir nuevos personajes, a parte de los dos creados ya (Aragorn y Legolas). La foto que suba el usuario en el formulario se guardará en el directorio *media/*.

2. Hemos diferenciado el videojuego de la api, separándolos por aplicaciones diferentes. Esto lo hemos hecho así para que sea más cómodo trabajar en el código y haya más reutilización. 

3. El middleware añadido en el proyecto se utiliza para ver los tiempos de respuesta del servidor. 

4. El template tag utilizado se usa para cambiar el color de un texto; en nuestro caso lo hemos usado para modificar el color del nombre del usuario en la página principal. 

5. Importante crear un superusuario para poder hacer login en la aplicación web. 

6. Hemos creado el mayor número de tests posibles pero por falta de tiempo y desarrollo no hemos podido terminarlos. Asumimos las consecuencias. 

7. A disfrutar del juego 😉

## Desarrolladores del proyecto
1. Carlos Chacón Atienza - https://github.com/Carlos5Noob
2. Álvaro Fernández de la Calle - https://github.com/Alvarokstar
3. Jonatan García Luna - https://github.com/JonatanGarLun