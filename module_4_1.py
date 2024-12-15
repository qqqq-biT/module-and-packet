from fake_math import divide as fake_dv
from true_math import divide as true_dv

error = fake_dv(59, 3)
error_1 = fake_dv(9, 0)
infinity = true_dv(69, 3)
infinity_1 = true_dv(9, 0)

print(f"Ответ №1: {error}\nОтвет №1.2: {error_1}")
print(f"Ответ №2: {infinity}\nОтвет №2.2: {infinity_1}")
