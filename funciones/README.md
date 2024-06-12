# FUNCIONES
## CONCEPTO
matematicamente una funcion es una operacion
que toma uno o mas valores llamados
```argumentos``` y produce un valor denominado
`resultado`.
>[!NOTE]
> Todos los lenguaes de programacion tiene funciones incorporadas(`funciones internas`),y funciones creadas por el usuario (`funciones externas`)

En programacion una funcion es un subprograma, es una
estructura que nos permite agrupar codigo y sus principales  objetivoss son:
-`NO REPETIR` fragmentos de codigo
-`REUTILIZAR` el codigo en distintos escenarios
## Estructura de una funcion
Una funcion tiene por `definida` por un `nombre`, sus
 `parametros` y su valor de `retorno`.
 una vez creada la funcion podremos solicitar su ejecucion
 `invocando` la funcion por su `nombre`

## Definir una funcion en pyton
Para deinir una funcion en pyton primero utilizaremos
la palabra reservada `def` segida por el `nombre` de la 
funcion.A continuacion especificaremos sin parametos, `(a)` si es
una funcion con parametros, si se tuviera mas de un
parametros iran separados por `,`, finalizaremos la
linea con `:` , en la siguiente linea sin olvidar el
 identado , comenzara el `cuerpo` de la funcion (micro
 programa) que puede contener 1 a mas
  sentencias , finalmente devera `retornar` un resultado con la palabra
  reservada `return`.
  >[!NOTE]
  > como retorno tambien se puede utilizar la `funcion interna`, `print ()`
  ,para depuracion de codigo no es recomendable usarlo en produccion.
  [observacion]
  `print` dentro de una funcion es una herramienta que nos permite comprobar

  **ejemplo**


  def saludo():
      saludo="hola chivo"
      saludo_dos="como estas"
      return saludo+ saludo_dos # concatenacion
      ## tambien 
      return f"{saludo},{saludo_dos}"
      saludo()
      print(saludo())
      # saludo()
    
## Invocar una funcion
para invovar, (o llamar, ejecutar)una funcion solo tendremos que
escribir el `nombre` de la funcion seguido por `()` parentesis.


def saludo():
     print("hola")
#  invocando la funcion
saludo()

## Retornar un valor
Las funciones pueden retornar (o devolver )un valor

def uno ():
    return
    uno()

>[!WARNING]
> No confundir `print()` con `return`. el valor retornado por
`return` nos permite usarlo fuera de su contexto. y `print()` solo 
mostrara el literal por terminal.

**ejemplo**
* en el archivo `lecture.py`

## Retornando multiples valores
El secreto es hacerlo mediante un tipo de tado estructurado

def varios ():
     return 2,3,4
varios()
# retorna(2,3,4)
def lista():
    return ["hola",45]
# retorna["hola",45]
def dicc():
     return{"nombre":"jose","edad":45}


## parametros y argumentos
 si una funcion no disposiera de valores de entrada estaria limitada en su actuacion.
 Es por ello que los `parametros` no permiten variar los datos que consume una funcion para obtener distintos resultados
 **ejemplo**
 *crear una funcion que recibe un valor numerico y retorna su raiz cuadrada
 
def sqrt(valor):
    return valor**(1/2)
# NOTA: en este caso, el valor 4 es un argumento de la funcion
sqrt(4)

cuando llamamos a na funcion con `argumentos`, los valores de estos argumentos se copian en los correspondientes
`parametros` dentro de la funcion

def ejm(a,b,c):
    return a+b+c
ejm(4,5,6)

### Argumentos nominales
en esta aproximacion los argumentos no son copiados en un orden especifico sino que 
**se asignan por nombre a cada parametro**.ello nos permite evitar el problema de
conocer o recordar cual es el orden de los parametros en la definicion de la funcion.
para utilizarlo, basta con realizar una asignacion de cada argumento en la propia llamada a la funcion.
**ejemplo**

def build_cpu(familia,num_core,recuencia):
    print(f"""
        la cpu de la familia {familia},
        con {num_core} cores y con una
        frecuencia de {frecuencia}
    """)

# haciendo uso de argumentos nominales
los argumentos son copiados en orden especifico, en este  caso debemos conocer o recordar cual es el orden de los parametros
build_cpu(num_core=4,familia="intel",frecuencia=2.7)


### Argumentos posicionales
build_cpu("intel",4,2,7)

### Parametros por defecto

es posible especificar **valores por defecto** en los parametros de una funcion , en
el caso de que no se proporcione un valor al argumento en la llamada a la funcion , el
parametro correspondiente tomara el valor definido por defecto.
**ejemplo**

def alumnos(nom,app,estado="aprobado"):

alumnos("ruth","castillo")
alumno("antony","crucez","desaprobado")

## desempaquetado/Empaquetado de argumentos(tarea)
cada uno con su ejemplo




### FUNCIONES INTERNAS DE PYTON (tarea)



      

  