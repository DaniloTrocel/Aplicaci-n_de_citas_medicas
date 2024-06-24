const express = require('express');
const app = express();
const citaRouter = require('./router/cita')
require('./conexion')

app.use(express.urlencoded({ extended: false }))
app.use(express.json())

app.use('/citas-medicas', citaRouter)

app.listen(3000, () => {
    console.log('Servidor iniciado en el puerto 3000')
})