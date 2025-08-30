# Enunciado:

# Estás en un bosque representado por un arreglo de enteros llamado forest. Cada elemento del arreglo puede ser:

# 0: una posición vacía.
# Un número entero positivo: representa una rama de longitud igual a ese número.
# Un cuervo se encuentra en una posición específica del arreglo, indicada por el índice crow. El cuervo puede:

# Moverse hasta 2 pasos a la izquierda y revisar si hay ramas.
# Luego moverse hasta 2 pasos a la derecha y revisar si hay ramas.
# El cuervo recolecta todas las ramas que encuentra en esas posiciones (si hay alguna). La suma de las longitudes de las ramas recolectadas se acumula.

# El proceso se repite: el cuervo sigue moviéndose 2 pasos a la izquierda y luego 2 pasos a la derecha, recolectando ramas, hasta que la suma total de las longitudes de las ramas recolectadas sea al menos 100.

# Tu tarea es devolver una lista con los índices de las posiciones donde el cuervo recolectó ramas hasta alcanzar o superar una longitud total de 100.

forest = [0, 5, 0 , 10, 0, 20, 0, 0, 15, 0, 30, 0, 25]
crow = 3

def collect_branches(forest, crow):
    collected_indices = []  # Lista para almacenar los índices donde se recolectaron ramas
    total_length = 0  # Suma total de las longitudes de las ramas recolectadas

    while crow < len(forest) and total_length <= 100:
        # Revisar hasta 2 posiciones a la izquierda
        for i in range(1, 3):
            left_index = crow - i
            if left_index >= 0 and forest[left_index] > 0:
                total_length += forest[left_index]
                collected_indices.append(left_index)
                forest[left_index] = 0  # Marcar como recolectado

        # Revisar hasta 2 posiciones a la derecha
        for i in range(1, 3):
            right_index = crow + i
            if right_index < len(forest) and forest[right_index] > 0:
                total_length += forest[right_index]
                collected_indices.append(right_index)
                forest[right_index] = 0  # Marcar como recolectado
        if total_length == 100:
            print(total_length)
            break
        # Avanzar una posición hacia la derecha
        crow += 1

    return collected_indices, total_length


if __name__ == '__main__':
    try:
    # 🧪 Ejemplo de entrada:
        forest = [0, 5, 0, 10, 0, 20, 0, 0, 15, 0, 30, 0, 25]
        crow = 2
    # Llamar a la función y mostrar el resultado
        result = collect_branches(forest, crow)
        print(result)  # Salida esperada: [1, 3, 5, 8, 10]
    except Exception as e:
        print(e)