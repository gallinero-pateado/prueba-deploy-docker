import express from 'express'

const app = express();

app.get('/', async (req, res) => {
	res.send("<h1>Todo OK<h1>")
});

app.listen(3000, () => console.log('servidor escuchando en el puerto 3000...'))
