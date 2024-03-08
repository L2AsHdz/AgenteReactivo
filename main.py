
reglas = {
        "sin-moneda": "pedir-moneda",
        "recibi-moneda": "pedir-codigo",
        "servido-c1": "servir-c1-esperar",
        "servido-c2": "servir-c2-esperar",
        "servido-c3": "servir-c3-esperar"
    }

acciones = {
    "pedir-moneda": "Pedir moneda",
    "pedir-codigo": "Pedir codigo",
    "servir-c2-esperar": "Sirviendo refresco 2 y esperar",
    "servir-c1-esperar": "Sirviendo refresco 1 y esperar",
    "servir-c3-esperar": "Sirviendo refresco 3 y esperar"
}

modelo = {
    ('sin-moneda', 'pedir-moneda', 'moneda'): 'recibi-moneda',
    ('recibi-moneda', 'pedir-codigo', 'c1'): 'servido-c1',
    ('recibi-moneda', 'pedir-codigo', 'c2'): 'servido-c2',
    ('recibi-moneda', 'pedir-codigo', 'c3'): 'servido-c3',
    ('servido-c1', 'servir-c1-esperar', 'servido'): 'sin-moneda',
    ('servido-c2', 'servir-c2-esperar', 'servido'): 'sin-moneda',
    ('servido-c3', 'servir-c3-esperar', 'servido'): 'sin-moneda',
    ('recibi-moneda', 'pedir-codigo', 'moneda'): 'recibi-moneda'
}


def actualizar_estado(estado, accion, percepcion):
    if (estado, accion, percepcion) in modelo:
        return modelo[(estado, accion, percepcion)]
    else:
        return 'sin-moneda'


estado = 'sin-moneda'
accion = 'pedir-moneda'

while True:
    percepcion = input("Ingresar percepcion: ")

    print(f"Estado: {estado}, Accion: {accion}, Percepcion: {percepcion}", end="")
    estado = actualizar_estado(estado, accion, percepcion)
    regla = reglas[estado]
    accion = regla
    texto_accion = acciones[accion]

    print(f" -> {estado}")
    print(f"{texto_accion}")

