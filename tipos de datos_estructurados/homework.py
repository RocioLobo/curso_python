#crear una lista de 5 alumnos cada alumno almacenaremos su nombre apellido y edad

#insertar al final de la lista los datos de antony
# eliminar de la lista si existe los datos de abel
# buscar y mostrar el alumno en la pocicion 4 de la lista.

lista_alumnos=[
    {
        "nombre":"abel",
        "apellido":"castillo",
        "edad":20,
    },{
        "nombre":"ruth",
        "apellido":"morales",
        "edad":18,

    },{
        "nombre":"flor",
        "apellido":"lucana ",
        "edad":18,

    },{
        "nombre":"luz",
        "apellido":"jimenez",
        "edad":19,

    },{
        "nombre":"antony",
        "apellido":"quispe",
        "edad":25,
        
    }
]

lista_alumnos.remove("nombre":"abel",
        "apellido":"castillo",
        "edad":20,)
indice=lista_alumnos.index(""nombre":"luz",
        "apellido":"jimenez",
        "edad":19,")
print(lista_alumnos[indice]) 