# ENTRADA DE DATOS
dias_laborales = int(input("Escriba los días laborales: "))


# PROCESOS
pago_bruto = 250 * dias_laborales
iva_trasladado = pago_bruto * 0.16
subtotal = pago_bruto + iva_trasladado 
iva_retenido = (2/3) * iva_trasladado
isr_retenido = pago_bruto * .10
pago_neto = subtotal - iva_retenido - isr_retenido

# SALIDA DE DATOS
print(f"Pago bruto= {round(pago_bruto, 2)}")
print(f"Pago neto= {round(pago_neto, 2)}")
