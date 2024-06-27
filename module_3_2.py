def send_email(message, recipient, *, sender="university.help@gmail.com"):
    list_end = ['.com', '.ru', '.net']
    sender_sub = sender[(sender.rfind('.')):] #вытаскиваем доменные имена
    recipient_sub = recipient[(recipient.rfind('.')):]
    if '@' in sender and '@' in recipient:
        if sender_sub and recipient_sub not in list_end:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

        elif recipient == sender:
            print('Нельзя отправить письмо самому себе!')

        elif sender == "university.help@gmail.com":
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vas137@gmail.com')
send_email('Все ок', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.uk', sender='urban.teacher@mail.uk')
send_email('Сам себе о вебинаре', 'urban.teacher@mail.com', sender='urban.teacher@mail.com')
