money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0
while True:
    money_capital += salary
    if months != 0:
        spend += spend * increase
    money_capital -= spend
    if money_capital > 0:
        months += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months)
