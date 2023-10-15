list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
num_of_players = len(list_players)
team_A = list_players[:num_of_players // 2]
team_B = list_players[num_of_players // 2:]
print(team_A)
print(team_B)