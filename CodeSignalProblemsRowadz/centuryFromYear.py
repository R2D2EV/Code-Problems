# CHECKED
import math

def century_from_year(year):
    abs_year = abs(year)
    century = math.ceil(abs_year / 100)

    if year > 0:
        print(f'{century} A.C')
    else:
        print(f'{century} B.C')


if __name__ == "__main__":
    try:
        century_from_year(1900)
    except Exception as e:
        print(e)
