from string import ascii_lowercase

def _encry(text):
    from random import randint

    alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", 
            "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " ", "1"]

    alphabet = ascii_lowercase

    publisher = text # исходный текст
    res = '' # блок в шестнадцатиричной системе
    block = '' # строка блоков
    key_dec = '' # строка ключей в dec
    key = '' # ключ 
    chain = '' # это итоговая цепочка
    count = 0 # первый счетчик для перебора букв и их намеров
    method = 0.00 # переменная для превращения каждого элемената в ирацианально число
    spam = 0 # блок в восьмеричной/десятичной системе
    rand1 = 0 # случайное число
    temp = [] # список для записи чисел после деления на π
    subsequence = [] # список с исходными намерами букв домноженый на 1000
    randl1 = [] # список ключей
    aelist = [] # список блоков
    pi = 3.141592653589793 # π

    #Перевод чисел в числовую последовательность по афавиту с коофициентом 1000
    def translation(count, subsequence):
        for i in publisher:
            while i != alphabet[count]:
                count +=1
            if i == alphabet[count]:
                subsequence.append((count+1)*1000)
                subsequence.append(0)
                count = 0

    # деление на π и округление до целого числа с кооффициентом 100
    def irationality(subsequence, method, temp):
        for y in subsequence:
            if y != 0:
                method = y/pi
                temp.append(round(method*100))
                #temp.append(0)

    # шифрование блоков и генерация ключей        
    def rationality(temp, rand1, randl1, spam, res, aelist):
        for u in temp: # u это один блок
            rand1 = randint(3,9) # рандомное число
            randl1.append(rand1) # добавляем это число в список 
            spam = int(oct(u)[2:]) # переводим u в восьмеричную систему
            spam = spam*rand1 # домнажаем на это то рандомное число
            spam = int(oct(spam)[2:]) # переводим это обратно в восьмеричную систему
            res = f'{spam:x}' # и теперь как десятичеую переводим в шестнадцатиричную
            aelist.append(res) # добавляем этот блок в список
    

    # Запуск системы

    def start():     
        translation(count=count, subsequence=subsequence)
        irationality(subsequence=subsequence, method=method, temp=temp)
        rationality(temp=temp, rand1=rand1, randl1=randl1, spam=spam, res=res, aelist=aelist)
        

    start()
    # генерация цепи              
    for t in randl1:
        key_dec += str(t)

    for z in aelist:
        block += str(z)
                    
    key = f'{int(key_dec):x}'
    chain = str(block) + ':' + str(key)
    return chain

def _decry(crypted, text):
    encryption = crypted

    # alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", 
    #             "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]

    alphabet = ascii_lowercase

    publisher = text # исходный текст
    res = '' # блок в шестнадцатиричной системе
    block = '' # строка блоков
    spam = 0 # блок в восьмеричной/десятичной системе
    count = 0 # первый счетчик для перебора букв и их намеров
    count1 = 0 # второй счетчик для домножения temp
    method = 0.00 # переменная для превращения каждого элемената в ирацианально число
    temp = [] # список для записи чисел после деления на π
    subsequence = [] # список с исходными намерами букв домноженый на 1000
    keyl = [] # строка ключей в шестнадцатиричной сисетме
    trash = [] # строка блоков в шестнадцатиричной системе
    aelist = [] # список всех блоков домноженых на коофициенты
    key_dec_l = [] # список ключей в десятичной сисеме
    conf = 0 # в какой их списков пойдет символ
    pi = 3.141592653589793 # π

    #Перевод чисел в числовую последовательность по афавиту с коофициентом 1000
    try:
        for i in publisher:
            while i != alphabet[count]:
                count +=1
            if i == alphabet[count]:
                subsequence.append((count+1)*1000)
                subsequence.append(0)
                count = 0
    except Exception:
        return 'Можно юзать только маленькие рус буквы'

    # деление на π и округление до целого числа с кооффициентом 100

    for y in subsequence:
        if y != 0:
            method = y/pi
            temp.append(round(method*100))
            #temp.append(0)
            
            
    # тут мы разделяем эдементы до двоеточия и после
    for z in encryption:
        if conf == 0:
            trash.append(z) # до
            if z == ':':
                conf = 1
        elif conf == 1:
            keyl.append(z) # после
            
    key_hex = (''.join(keyl))
    key_dec = int(key_hex, 16)

    # переводим десятичные ключи в список 
    for c in str(key_dec):
        key_dec_l.append(c)
        
    # генерируем блоки из добытых ключей
    for u in temp:
        spam = int(oct(u)[2:])
        spam = int(spam) * int(key_dec_l[count1])
        count1 += 1
        spam = int(oct(spam)[2:])
        res = f'{spam:x}'
        aelist.append(res)
        
    # переводим блоки в строку
    for p in aelist:
        block += str(p)
        
    # создаем цепочку   
    chain = str(block) + ':' + str(key_hex)

    if chain == encryption:
        return True
    else:
        return False

#  Заброшено =============================================

def force(decrypted=0):
    print(f'Начало брутфорса для {decrypted}')

    # symbols = 'abcdefghijklmnopqrstuvwxyz'
    symbols = 'qwe'
    lenth = 4
    # crypted = '160832e170232fdb06c944e9e0f6c99e:b2d2'
    crypted = '78c00d4160832e2772a5732919b3:2507'

    password = [i for i in symbols]
    for y in range(lenth - 1):
        for x in password:
            for i in symbols:
                password = [x+i]
                print(password)
    if _decry(crypted, password):
        print(f"{password}")

# ==============================================

def newforce(lenth:int, lenth_max=None, is_print=True, show_process=False):
    """
    Брутфорсит шифр от Kiebe
    Параметры:
    lenth: предпологаемая длинна шифра
    lenth_max: максимальная длинна шифра, тогда параметр lenth означает минимальную длинну (включительно)
    is_print: выводить текст, или только вернуть расшифрованый текст
    show_process: показывать процесс подбора (Очень сильно увеличивает время на расшифровку)
    """
    from itertools import product

    charset = ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    crypted = '160832e170232fdb06c944e9e0f6c99e:b2d2'

    def printuwu(txt):
        if is_print:
            print(txt)

    def solve_password(maxrange):
        if not show_process:
            for attempt in product(charset, repeat=maxrange):
                if _decry(crypted, ''.join(attempt)):
                    return ''.join(attempt)
        
        else:
            for attempt in product(charset, repeat=maxrange):
                s = ''.join(attempt)
                print(attempt, end='')
                print('\r', end='')
                if _decry(crypted, s):
                    return ''.join(attempt)

    
    
    if lenth_max:
        for lenthNow in range(lenth, lenth_max+1):
            printuwu(f'Проверка при длинне {lenthNow}')
            password = solve_password(lenthNow)
            if password:
                return password

print(newforce(3, 6, True))
    
