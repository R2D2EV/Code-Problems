sequence = "LRLRLLR"

start_position = 0
for movement in sequence:
    if movement == "L":
        start_position -= 1
    if movement == "R":
        start_position += 1

end_position = start_position

if end_position == -1:
    print("L")
if end_position == 1:
    print("R")
if end_position == 0:
    print("Origin")
