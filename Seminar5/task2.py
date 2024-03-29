"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процента вида "10.25%".
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
"""

names: list[str] = ['Vas', 'Das']
salary: list[int] = [100, 100]
bonus: list[str] = ['10.25%', '5.0%']

# a: dict[str, float] = {z[0]: z[1] * float(z[2].strip('%')) / 100 for z in zip(names, salary, bonus)}


result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
print(result)
