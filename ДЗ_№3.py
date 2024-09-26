while True:
    command = input('Enter "yes" or "no": ')
    if command == 'yes':
        word = input('Слово: ')
        counter = 0
        count_vowels = 0
        count_consonants = 0
        sign = 'ьъ'
        vowels = 'AEUIOYaeioyuАОЫЭИУЕЁЮЯаоуыиэеёюя'

        for letter in word:
            if letter.isalpha():
                counter += 1
                if letter in vowels:
                    count_vowels += 1
                elif letter not in sign:
                    count_consonants += 1
        print(f'Количество букв: {counter}')
        print(f'Гласных букв: {count_vowels}')
        print(f'Согласных букв:  {count_consonants}')

        vowel_percent = round((count_vowels / counter) * 100, 1)
        consonant_percent = round(100 - vowel_percent, 1)
        print(f'Гласные/Согласные:: {vowel_percent}% / {consonant_percent}%')
    elif command == 'no':
        print('Stop')
        break
    else:
        print('Try again!')
