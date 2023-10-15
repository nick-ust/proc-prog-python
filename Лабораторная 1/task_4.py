users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
info = dict.fromkeys(["Общее количество", "Уникальные посещения"], 0)
info["Общее количество"] = len(users)
info["Уникальные посещения"] = len(set(users))
print(info)