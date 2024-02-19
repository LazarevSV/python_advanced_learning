# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
#
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
#
# # Для проверки своего кода используйте модуль fractions.


frac1 = "1/2"
frac2 = "1/3"

# Введите ваше решение ниже
def process_fractions(frac1, frac2):
    # Преобразуем дроби из строк в числа
    num1, denom1 = map(int, frac1.split("/"))
    num2, denom2 = map(int, frac2.split("/"))

    # Вычисляем сумму дробей
    sum_frac_num = num1 * denom2 + num2 * denom1
    sum_frac_denom = denom1 * denom2
    sum_frac = (sum_frac_num, sum_frac_denom)

    # Вычисляем произведение дробей
    prod_frac_num = num1 * num2
    prod_frac_denom = denom1 * denom2
    prod_frac = (prod_frac_num, prod_frac_denom)

    return sum_frac, prod_frac

# Пример использования функции
# frac1_str = "3/4"
# frac2_str = "2/3"

sum_frac, prod_frac = process_fractions(frac1, frac2)

print(f"Сумма дробей: {sum_frac[0]}/{sum_frac[1]}")
print(f"Произведение дробей: {prod_frac[0]}/{prod_frac[1]}")