# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
# больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним, только если треугольник существует .




a = 4
b = 4
c = 4

# Введите ваше решение ниже

# a = int(input('Введите первую сторону треугольника'))
# b = int(input('Введите вторую сторону треугольника'))
# c = int(input('Введите третью сторону треугольника'))

if (a < b + c) and (b < a + c) and (c < a + b):
    print(f'Треугольник существует')
    if a == b == c:
        print('Треугольник равносторонний')
    elif (a == b) or (a == c) or (b == c):
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print(f'Треугольник не существует')