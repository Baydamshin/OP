def code(t, t1):
    global key
    global string
    global symbol
    enter_text = True
    enter = False
    while (not enter):
        print("\nТеперь тебе нужно будет ввести ключ\n       Вот пример: (3 0 1 2)")
        key = input('\nВведи ключ: ').split()
        enter = Proverka()
    if (enter_text):
        match t:
            case "1":
                stroka = []
                string = input('\nВведи текст: ')
                for i in string:
                    stroka.append(i)
                enter_text = False
                return stroka
            case "2":
                stroka = []
                string = input('\nВведи текст: ')
                string = string.replace('\\x00', '\0')
                enter_text = False
                symbol = int(input('\nВведи количество символов: '))
                for i in range(0, len(string), symbol):
                    stroka.append(string[i:i + symbol])
                return stroka
            case "3":
                stroka = []
                string = input('\nВведи текст: ')
                enter_text = False
                stroka = string.split()
                return stroka


def Proverka():
    k = [int(item) for item in key]
    for i in range(max(k) + 1):
        if (k.count(i) > 1 or k.count(i) < 1):
            print("Упс, ключ неверный")
            return False
    else:
        return True


def Shifrovanie(s, k):
    if (len(s) % len(k) != 0):
        for i in range(len(k) - (len(s) % len(k))):
            s.append("\0")
    str_new = [0] * len(s)
    p = 0
    for i in range(len(s)):
        str_new[int(k[i % len(k)]) + (p)] = s[i]
        if ((i + 1) % len(k) == 0):
            p += len(k)
    return str_new


def Reverse(k):
    rs = [0] * len(k)
    for i in range(len(k)):
        rs[int(k[i])] = i
    return rs


def Razshifrovanie(s, k):
    p = True
    n = len(k) - (len(s) % len(k))
    new_str = ["0"] * (len(s) + n)
    for i in range(n):
        a = int(k[-i - 1]) + (len(k) * (len(s) // len(k)))
        new_str[int(k[-i - 1]) + (len(k) * (len(s) // len(k)))] = "\0"
    for item in s:
        p = True
        for i in range(len(new_str)):
            if (new_str[i] == "0" and p):
                new_str[i] = item
                p = False
    return new_str


def outgroup(str):
    print("\nПолученный результат: ")
    s = "".join(str)
    print(s)


def prt(str):
    print("\nПолученный результат: ")
    print("".join(str))


def group(str):
    print("\nПолученный результат: ")
    for i in range(str.count("\0")):
        str.remove("\0")
    print("".join(str))


def word(str):
    print("Полученный результат:")
    print(" ".join(str))

print("_"*71)
print("Привет, я робот шифровальщик! Мой хозяин сказал, что тебе нужна помощь!")
print("Вот что я могу:\n     1 - Зашифровать\n     2 - Расшифровать")
s = int(input("Пожалуйста, выбери нужное действие: "))
key = []
string = ""
symbol = 0

match s:
    case 1:
        print('\nСпособы шифровки: ')
        print('     1 - Посимвольное шифрование\n     2 - Шифрование группы\n     3 - Шифрование слов')
        start = input("Пожалуйста, выбери нужный способ шифровки: ")

        match start:
            case "1":
                str1 = code(start, s)
                str2 = Shifrovanie(str1, key)
                prt(str2)

            case "2":
                str1 = code(start, s)
                str1[-1] = str1[-1] + ("\0" * (symbol - len(string) % symbol))
                str2 = Shifrovanie(str1, key)
                group(str2)
            case "3":
                str1 = code(start, s)
                str2 = Shifrovanie(str1, key)
                word(str2)
    case 2:
        print('\nСпособы расшифровки: ')
        print('     1 - Посимвольное расшифрование\n     2 - Расшифрование группы\n     3 - Расшифрование слов')
        start = input("Пожалуйста, выбери нужный способ расшифровки: ")

        match start:
            case "1":
                str1 = code(start, s)
                str_new = Razshifrovanie(str1, key)
                rev = Reverse(key)
                str2 = Shifrovanie(str_new, rev)
                prt(str2)

            case "2":
                str1 = code(start, s)
                str_new = Razshifrovanie(str1, key)
                rev = Reverse(key)
                str2 = Shifrovanie(str_new, rev)
                outgroup(str2)

            case "3":
                str1 = code(start, s)
                str_new = Razshifrovanie(str1, key)
                rev = Reverse(key)
                str2 = Shifrovanie(str_new, rev)
                word(str2)