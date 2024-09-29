# prueba-docker

Prueba de creación de contenedor para devops

## Que hace?

Para que funcione, primero se deben descargar las dependencias (solo express):

```
npm install
```

Luego, se inicia con:

```
node index.js
```

Al correr esta aplicación con node, debe mostrar en la consola `servidor escuchando en el puerto 3000...`, luego, al entrar a `localhost:3000` en el navegador debe mostrar una pantalla con el texto `Todo OK`.

## Objetivo

El objetivo es crear una imagen de docker con un archivo `Dockerfile` a partir de este repositorio, y que docker corra la aplicación correctamente.
