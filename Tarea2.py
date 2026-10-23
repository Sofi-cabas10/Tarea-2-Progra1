# Nombre del estudiante: Sofía Cabas Madrigal

# Contexto seleccionado: Cajero automático

# Descripción: realizar retiros consecutivos, registrar las salidas de dinero.

# ---- CONSTANTES ----

SALDO_INICIAL = 250000
RETIRO_MINIMO = 5000
RETIRO_MAXIMO = 100000

# ---- Inicialización ----

saldo_actual = SALDO_INICIAL
total_retiros = 0
desea_retirar_mas = "s"

# ---- Ciclo principal ----

while desea_retirar_mas == "s" and saldo_actual >= RETIRO_MINIMO :
    
    monto_retirar = int(input("Ingrese el monto a retirar: "))

    if monto_retirar < RETIRO_MINIMO or monto_retirar > RETIRO_MAXIMO: 
       print("No puede ingresar esa cantidad. El monto debe estar entre 5000 y 100000 colones.")
       print("Saldo actualizado:", saldo_actual, "colones")

    elif monto_retirar > saldo_actual:
       print("Saldo insuficiente.")
       print("Saldo actualizado:", saldo_actual, "colones")
    
    else:
       saldo_actual = saldo_actual - monto_retirar
       total_retiros += 1
       print("Retiro realizado") 
       print("Saldo actualizado", saldo_actual, "colones")

       if saldo_actual < RETIRO_MINIMO:
          print("Saldo insuficiente, ya no puede hacer más retiros.")
          break

       else:
          desea_retirar_mas = input("¿Desea retirar más? (s/n): ").lower()

# ---- Ciclo secundario ----
        
          while desea_retirar_mas != "s" and desea_retirar_mas != "n":
           print("Respuesta no válida. Debe ser poner s o n.")
           desea_retirar_mas = input("¿Desea retirar más? (s/n): ")

# ---- Salida final ----
    
print("Su saldo final es de:" , saldo_actual, "colones")
print("El total de retiros exitosos es de:", total_retiros)
