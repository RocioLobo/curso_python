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

lista_alumnos.remove({
        "nombre":"abel",
        "apellido":"castillo",
        "edad":20,
        
})
indice=lista_alumnos.index({
    
        "nombre":"luz",
        "apellido":"jimenez",
        "edad":19,
    })
print(lista_alumnos[indice]) 



#2.Crear una lista con 4 diccionarios donde tendran los datos de sus mascotas (nombre ,edad ,sexo ,raza)

#Tareas
# mostrar la lista con los 4 diccionarios
# editar el tercer registro y cambiarle la edad sin modificar la lista original
# mostrar la lista original y luego la lista con el tercer registro modificado.

lista_mascotas=[

    {
        "nombre":"chocolate",
        "edad":2,
        "sexo":"macho",
        "raza":"pitbul"
    },{
        "nombre":"miel",
        "edad":4,
        "sexo":"hembra",
        "raza":"terries"
    },{
        "nombre":"pinina",
        "edad":3,
        "sexo":"hembra",
        "raza":""

    },{
        "nombre":"samuel",
        "edad":7,
        "sexo":"macho",
        "raza":"pastor"


        
    }
]

lista_mascotas[3]["edad"]=1
print(lista_mascotas)

# OTRA MANERA DE RESOLVER

lista_mascotas=[

    {
        "nombre":"chocolate",
        "edad":2,
        "sexo":"macho",
        "raza":"pitbul"
    },{
        "nombre":"miel",
        "edad":4,
        "sexo":"hembra",
        "raza":"terries"
    },{
        "nombre":"pinina",
        "edad":3,
        "sexo":"hembra",
        "raza":""

    },{
        "nombre":"samuel",
        "edad":7,
        "sexo":"macho",
        "raza":"pastor"


        
    }
]
print(lista_mascotas)
copia_lista=lista_mascotas.copy()
copia_lista[3]["edad"]=1
print(copia_lista)