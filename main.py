import random 

all_symbols = 'QWERTYIOPASDFGHJKLZXCVBNMqwertyiopasdfghjklzxcvbnm!?/_.@#-0123456789'

lenght = int(input('Введите кол-во символов для енерации пароля: '))

password = ''

for i in range (lenght):
    password += random.choice (all_symbols)

print (password)
