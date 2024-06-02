from random import shuffle, choices
import os

clear = lambda: os.system('cls')
clear()

questions = {
  'Что из этого является списоком?': ['[5]', '(х, 1, "х")', '{1: "waa"}', '{1, 2, 3, 4}'],
  'Что из этого является словарем?': ['{1: "waa"}', '[5]', '(х, 1, "х")', '{1, 2, 3, 4}'],
  'Что из этого является множеством?': ['{1, 2, 3, 4}', '[5]', '(х, 1, "х")', '{1: "waa"}'],
  'Что из этого является кортежем?': ['(х, 1, "х")', '[5]', '{1: "waa"}', '{1, 2, 3, 4}'],
  'Каким будет результат: 1 is \'1\'?': ['False', 'True', '1', '0'],
  'Каким будет результат: 1 and \'1\'?': ['1', 'False', 'True', '0'],
  'Каким будет результат: 1 and \'1\'?': ['1', 'False', 'True', '0'],
  'Каким будет результат: 1 or 0?': ['True', '1', '0', 'False'],
  '2%2 = ?': ['0', 'True', '1', 'False'],
  '2+2*2 = ?': ['6', '4', '2', '16'],
}


print('Привет, сыграем в "Кто хочет стать миллионером"? Введи "Да" или "Нет"')
decision = str(input('')).lower()
counter_fifty = 1
counter_callfriend = 1
end_game = False
score = 0
level = 1
level_score = 0
clear()

while decision == 'да' and end_game == False:
    if len(questions) == 0:
        print(f'ВЫ ВЫИГРАЛИ! ВЫ ЗАРАБОТАЛИ: {score}')
        end_game =True
        break
    qstn, answrs = questions.popitem()
    right_answer = answrs[0]
    shuffle(answrs)
    answrs = dict(zip(['a)', 'b)', 'c)', 'd)'], answrs))
    print_answrs = [f'{x} {y}' for x, y in answrs.items()]

    fifty_fifty = []
    remain = []
    for x, y in answrs.items():
        if y == right_answer:
            fifty_fifty += [f'{x} {y}']
        else:
            remain += [f'{x} {y}']
    second_fifty = choices(remain)
    fifty_fifty += second_fifty

    print(f'Вопрос: {qstn}\n\n{"; ".join(print_answrs)}')
    print(
      '\nПодсказки: {}{}{}{}\n{}'.format(
      "Закончились" if counter_callfriend == 0 and counter_fifty == 0 else "",
      '50/50. Стоимость 5000 очков - Напиши "F"' if counter_fifty != 0 else '',
      ', ' if counter_callfriend and counter_fifty != 0 else "",
      'Звонок другу. Стоимость 1000 очков - Напиши "Z"' if counter_callfriend != 0 else '',
      'Нельзя использовать две подсказки к одному вопросу.' if counter_callfriend
      and counter_fifty != 0 else ""
      )
    )
    print(f'\nТвои очки: {score}')
    clients_answer = str(input('\nНапиши просто букву:')).lower()

    while clients_answer:
        clear()
        if clients_answer == 'f' and counter_fifty != 0:
            counter_fifty -= 1
            score -=5000
            print(f'Вопрос: {qstn}\n\n{"; ".join(sorted(fifty_fifty))}')
            print(f'\nТвои очки: {score}')
            clients_answer = str(input('\nНапиши просто букву:'))
            continue

        elif clients_answer == 'z' and counter_callfriend != 0:
            counter_callfriend -= 1
            score -= 1000
            print(f'Вопрос: {qstn}\n\n{"; ".join(print_answrs)}')
            print(f'Друг говорит ответ: {"; ".join(choices(print_answrs))}')
            print(f'\nТвои очки: {score}')
            clients_answer = str(input('\nНапиши просто букву:'))
            continue
        elif (clients_answer+')') in answrs.keys() and\
        right_answer == answrs[clients_answer+')']:
            level += 1
            level_score += (((level**2)+level)/2)*50
            score += level_score
            break
        else:
            print(f"Нет, ты проиграл. Ты заработал {score} очков")
            end_game = True
            break
