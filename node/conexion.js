const slqlite = require('sqlite3')

const conexion = new slqlite.Database('cita.db', (err) => {
    if (err) {
        console.log('Error en la conexion', err)
    } else {
        console.log('Conexion exitosa')
    }
})

const sql = `CREATE TABLE IF NOT EXISTS cita (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente TEXT NOT NULL,
    detalle TEXT NOT NULL,
    dia date NOT NULL,
    hora time NOT NULL,
    estado TEXT NOT NULL
)`

conexion.run(sql)

module.exports = conexion