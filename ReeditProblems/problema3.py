# CHECKED
# Question: Write a Python function that takes a list of integers 
# and returns a new list containing only the prime numbers from the original list.
def es_primo_simple(n):
    """Versión simple: verifica todos los divisores hasta n-1"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_numbers(numbers):
    list_prime_numbers = []
    for number in numbers:
        if es_primo_simple(number):
            list_prime_numbers.append(number)
    print(list_prime_numbers)
        

if __name__ == "__main__":
    try:
        numbers = [10, 15, 3, 7, 13, 19, 21, 23]
        prime_numbers(numbers)
    except Exception as e:
        print(e)