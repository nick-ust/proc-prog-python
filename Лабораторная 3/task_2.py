# TODO Напишите функцию find_common_participants
def find_common_participants(participants_1, participants_2, split_char=','):
    p1_set = set(participants_1.split(split_char))
    p2_set = set(participants_2.split(split_char))
    participant_intersection = list(p1_set.intersection(p2_set))
    participant_intersection.sort()
    return participant_intersection


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
