FROM node:20

WORKDIR /app

COPY . .

EXPOSE 3000

# Instalar dependencias de Node (Expresss)
RUN npm install

# Ver si se creo la carpeta /node_modules con las dependencias
RUN ls -al

CMD ["node", "index.js"]
