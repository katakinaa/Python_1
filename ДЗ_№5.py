def get_discount(points_homework, points_test, attendance):
    if 50 <= points_homework <= 80 and 60 <= points_test <= 100 and 1 <= attendance <= 8:
        if points_test <= 80:
            if points_homework < 70:
                if attendance >= 6:
                    return 2000
                else:
                    return 1000
            else:
                if attendance == 8:
                    return 2500
                else:
                    return 3000
        else:
            if points_homework < 70:
                return 2000
            else:
                return 1000
    else:
        print('Вы не можете получить скидку!')
while True:
    command = input('Enter "yes" or "no": ')
    if command == 'yes':
        points_homework = int(input('Введите баллы за ДЗ: '))
        points_test = int(input('Введите баллы за тест: '))
        attendance = int(input('Введите количество посещений: '))
        # def get_discount(points_homework, points_test, attendance):
        #     if 50 <= points_homework <= 80 and 60 <= points_test <= 100 and 1 <= attendance <= 8:
        #         if points_test <= 80:
        #             if points_homework < 70:
        #                 if attendance >= 6:
        #                     return 2000
        #                 else:
        #                     return 1000
        #             else:
        #                 if attendance == 8:
        #                     return 2500
        #                 else:
        #                     return 3000
        #         else:
        #             if points_homework < 70:
        #                 return 2000
        #             else:
        #                 return 1000
        #     else:
        #         print('Вы не можете получить скидку!')
        discount = get_discount(points_homework, points_test, attendance)
        print('Ваша скидка: ', discount)
    elif command == 'no':
        print('Stop')
        break
    else:
        print('Try again!')