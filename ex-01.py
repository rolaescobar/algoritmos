# Sistema de descuentos para una tienda de videojuegos

precio = float(input("Ingresá el precio del videojuego: Q"))
vip = input("¿El cliente es miembro VIP? (Si/No): ").strip().lower()

precio_final = precio

# Primer descuento: 10% si el precio es mayor o igual a Q500
if precio >= 500:
    precio_final = precio_final * 0.90

# Segundo descuento: 15% adicional si es VIP
if vip == "si":
    precio_final = precio_final * 0.85

print(f"El precio final a pagar es: Q{precio_final:.2f}")

#diagrama: https://mermaid.live/view#pako:eNpVkt9umzAUxl_FOlLvSIRhJMTSOrX502ZSq1aZdjHIhYdPiCewI2O6tVEeac8wqXuxGTOaDXHBd_T7vvPJ-AiFFggMdpX-Xuy5seTTIlfEPVfZWslC6i0ZjS7JtVOlwYYbcjDoxkRgRZ6kQP2txVJve9O1h-dnuJEEG1JLrL8aTT6vHxjZSKLJ_eCYe8fi-Prroc-9fE8ekzD8cMpVTywcQTa_f3pwmV0dKlm4ZBpeuA7ubYoWlR3yPH2vPbzK5lo1aJ7OrbWRpVS82g7pS0_euP3LpuvX7e3mq34-YDf_lrg9l0guCBfdMfWZb-jfBuvsTjfWnPfv_lt-20O9WHvxMVtJtYUASiMFMGtaDKBGU_NOwrFjc7B7rDEH5j4F7nhb2RxydXK2A1dftK4Hp9FtuQe241XjVHsQ3OJC8tLwN4S3Vm-eVTFolwDsCD-AxTQehyl9F9FpOoloEgXwDGxE43QcTdJ0FifuR00nyfQUwItfSsfTkNJJHM3oLKbOEQeAQlpt7vp75q-bq4VKoJnrVllgyekPeXjENA