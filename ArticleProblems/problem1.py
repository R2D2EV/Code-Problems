# **Dado un arreglo `a`, tu tarea es generar un arreglo `b` del mismo tamaño aplicando la siguiente transformación:**

# - Para cada índice `i` desde `0` hasta `a.length - 1` inclusive,  
#   $$b[i] = a[i - 1] + a[i] + a[i + 1]$$
# - Si algún elemento en la suma `a[i - 1] + a[i] + a[i + 1]` no existe, usa `0` en su lugar.
# - Por ejemplo,  
#   $$b[0] = 0 + a[0] + a[1]$$

# **Ejemplo:**

# Para `a = [4, 0, 1, -2, 3]`:

# - `b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4`
# - `b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5`
# - `b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1`
# - `b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2`
# - `b[4] = a[3] + a[4] + 0 = -2 + 3 + 0 = 1`