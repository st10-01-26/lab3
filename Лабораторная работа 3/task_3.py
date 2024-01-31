# TODO  Напишите функцию count_letters
def count_letters(text):
    lowercase_text = text.lower()
    dictionary_of_letters = {}
    for letter in lowercase_text:
        if letter.isalpha():
            if letter in dictionary_of_letters:
                dictionary_of_letters[letter] += 1
            else:
                dictionary_of_letters[letter] = 1
    return dictionary_of_letters

# TODO Напишите функцию calculate_frequency
def calculate_frequency(dictionary_of_letters):
    sum_of_letters = sum(dictionary_of_letters.values())
    list_of_values = list(dictionary_of_letters.values())
    for i in range(len(list_of_values)):
        list_of_values[i] = '{:.2f}'.format(round(list_of_values[i]/sum_of_letters, 2))
    letters = list(dictionary_of_letters.keys())
    dictionary_with_frequency = {}
    for letter, count in dictionary_of_letters.items():
        dictionary_with_frequency[letter] = '{:.2f}'.format(round(count/sum_of_letters, 2))
    return dictionary_with_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dictionary = count_letters(main_str)
for key, value in calculate_frequency(dictionary).items():
    print(f"{key}: {value}")

