const conexion = require('../conexion');

const todas = (req, res) => {
    const sql = 'SELECT * FROM cita'
    conexion.all(sql, (err, result) => {
        if (err){
            res.send('Error en la consulta', err)
        }else{
            res.send(result)
        }
    })

}

const buscar = (req, res) => {
    const dia = req.body.dia
    const sql = `SELECT * FROM cita WHERE dia='${dia}' AND estado='Agendada'`
    conexion.all(sql, (err, result) => {
        if (err){
            res.send('Error en la consulta', err)
        }else{
            res.send(result)
        }
    })

}

const registar = (req, res) => {
    const {paciente, detalle, dia, hora, estado} = req.body
    const sql = `INSERT INTO cita (paciente, detalle, dia, hora, estado) VALUES('${paciente}', '${detalle}', '${dia}', '${hora}', '${estado}')`
    conexion.run(sql, (err) => {
        if (err){
            res.send('Error en la consulta', err)
        }else{
            res.send('Registro exitoso')
        }
    })
}

const modificar = (req, res) => {
    const {id} = req.params
    const {estado} = req.body
    const sql = `UPDATE cita SET estado='${estado}' WHERE id=${id}`
    conexion.run(sql, (err) => {
        if (err){
            res.send('Error en la consulta', err)
        }else{
            res.send('Modificacion exitosa')
        }
    })
}

const eliminar = (req, res) => {
    const {id} = req.params
    const sql = `DELETE FROM cita WHERE id=${id}`
    conexion.run(sql, (err) => {
        if (err){
            res.send('Error en la eliminacion', err)
        }else{
            res.send('Se ha eliminado correctamente')
        }
    })
}

module.exports = { todas, buscar, registar, modificar, eliminar}