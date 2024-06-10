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
      

  