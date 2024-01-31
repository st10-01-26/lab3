# TODO Напишите функцию find_common_participants
def find_common_participants(first_team, second_team, separator=','):
    first_teammates = first_team.split(separator)
    first_teammates_set = set(first_teammates)

    second_teammates = second_team.split(separator)

    intersection_teammates = first_teammates_set.intersection(second_teammates)
    intersection_teammates_list = list(intersection_teammates)
    intersection_teammates_list.sort()

    return intersection_teammates_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, separator='|'))