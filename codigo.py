def multiplicacion(a,b):
    return a * b

def resta(a,b):
    return a-b

def mensaje_bienvenida(nombre="Usuario"):
    return f"!Hola, {nombre}! Bienvenido a la aplicación."

if __name__ == "__main__":
    print(mensaje_bienvenida("DevOps Team"))

    resultado_multiplicacion=multiplicacion(10,100)
    resultado_resta=resta(10,3)

    print(f"Resultado Multiplicación (10*10): {resultado_multiplicacion}")
    print(f"Resultado Resta (10-3): {resultado_resta}")
