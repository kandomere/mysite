import random

countries = {'Абхазия': 'Сухум',
             'Австралия': 'Канберра',
             'Австрия': 'Вена',
             'Азербайджан': 'Баку',
             'Албания': 'Тирана',
             'Алжир': 'Алжир',
             }

s = ['A', 'B', 'C', 'D']
ck = [k for k, v in countries.items()]
cv = [v for k, v in countries.items()]
random.shuffle(ck)

for count in range(1, 6):
    fquest = open(f'Билет {count}', 'w')
    fanswer = open(f'Ответ для билета {count}', 'w')
    for i, k in enumerate(ck, 1):
        rs = random.shuffle(cv)
        fquest.write(f'{i}. Выберите столицу {k}\n')
        answer = countries[k]
        list_coustion = cv[:3]
        list_coustion.append(answer)
        random.shuffle(list_coustion)
        for j in range(0, 4):
            fquest.write(f'\t{s[j]}. {list_coustion[j]}\n')
            if countries[k] == list_coustion[j]:
                fanswer.write(f'{str(i)} {s[j]}\n')
                break
    fanswer.close()
    fquest.close()