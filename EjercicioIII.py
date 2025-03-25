# Programa Ejercicio III

#Variables y Codigos de Descuento
descuento = 0
codigos_validos = ["DESC5", "OFERTA5", "BONO5"]

#Entradas
monto = float(input("Ingrese el monto de la compra: $"))
es_vip = input("¿El cliente es VIP? (si/no): ") == "si"
codigo_descuento = input("Ingrese el código de descuento (si tiene): ")


#Proceso
tiene_codigo_descuento = codigo_descuento in codigos_validos

#Condiciones
if monto > 100 and es_vip and tiene_codigo_descuento:
    descuento = 0.20 + 0.10 + 0.05
elif monto > 100 and es_vip:
    descuento = 0.20 + 0.10
elif monto > 100 and tiene_codigo_descuento:
    descuento = 0.20 + 0.05
elif es_vip and tiene_codigo_descuento:
    descuento = 0.10 + 0.05
elif monto > 100:
    descuento = 0.20
elif es_vip:
    descuento = 0.10
elif tiene_codigo_descuento:
    descuento = 0.05
else:
    descuento = 0

#Salida
monto_final = monto * (1 - descuento)
porcentaje_descuento = descuento * 100

print("\nDescuento total aplicado:", porcentaje_descuento, "%")
print("Monto final a pagar: $", monto_final)
