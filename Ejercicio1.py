# Inicializar lista vacía para almacenar notas
notas = []

# Pedir notas de parciales al usuario
for i in range(3):
 nota = float(input(f"Ingrese la nota del parcial {i+1}: "))
 notas.append(nota)

# Mostrar las notas ingresadas
print("\nNotas de parciales:")
for i, nota in enumerate(notas, start=1):
 print(f"Parcial {i}: {nota}")

# Calcular el promedio de las notas
promedio = sum(notas) / len(notas)
print(f"\nPromedio de notas: {promedio:.2f}")