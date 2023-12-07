document.addEventListener("DOMContentLoaded", function(){

const formulario = document.querySelector('form')

formulario.addEventListener('submit', function(event){
    event.preventDefault();
// Obtener los valores del formulario
const nombre = document.querySelector('input[name="nombre"]').value;
const apellido = document.querySelector('input[name="apellido"]').value;
const correo = document.querySelector('input[type="email"]').value;
const edad = document.querySelector('input[type="number"]').value;
const fechaNacimiento = document.querySelector('input [name="fechaNacimiento"]')
const color = document.querySelector('input[type="color"]').value;
const lista = document.querySelector('select').value;

const mensaje = `
    Nombre = ${nombre}
    Apellido = ${apellido}
    Correo = ${correo}
    Edad = ${edad}
    Fecha de Nacimiento = ${fechaNacimiento}
    Color Favorito = ${color}
    Comida Preferida = ${lista}
    `

    // MUESTRO MENSAJE
    alert(mensaje)
})


})


