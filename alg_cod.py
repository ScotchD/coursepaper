import random
import sympy

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'): #Функция перевода текста в 0 и 1
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
def summator(x, y): #Функция вывода результата работы сумматора с определенным содержимым регистра.
    for i in range(len(SR)):
        rs = [] #Список. Сюда будут записываться значения из регистра, которые подобраны сумматором.
        for j in range(len(SR[i])):
            rs.append(y[SR[i][j]]) #Запись значений в список
        l = 0
        for k in range(len(rs)):
            if rs[k] == 1:
                l += 1
        if l % 2 == 0:
            l = 0
        else:
            l = 1
        x.append(l)
def summa(x): #Функция суммы по модулю 2
    if x % 2 == 0:
        x = 0
    else:
        x = 1
    return x

infsl = input("Открытый текст: ")

kreg = 3
reg = [0] * kreg #Список. Образ регистра. Сюда будут записываться значения информационного слова.
SR = [[0, 1], [1, 2]] #Список. Образ сумматора. Здесь отмечены позиции суммирования значений в регистре.

infsl = text_to_bits(infsl) #Строка. Переводит текст в 0 и 1.

rez = [] #Список. Здесь будет записываться результат работы сумматора.

while len(infsl) != 0 or kreg != 0:
    if len(infsl) != 0:
        reg.insert(0, int(infsl[0])) #Добавление значений в регистр.
        del reg[-1]
        infsl = infsl.replace(infsl[0], '', 1) #Удаление позиции из информационного слова.
        summator(rez, reg) #Подсчет сумматоров.
    else:
        reg.insert(0, 0) #Обнуление регистра.
        del reg[-1]
        summator(rez, reg) #Подсчет сумматоров.
        kreg -= 1
REZ = "" #Строка. Сюда будет записываться результат из списка rez
for i in range(len(rez)):
    REZ += str(rez[i]) #Запись результата

infsl = REZ #Строка. Сюза записывается результат кодирования из алгоритма выше.

spinf = [] #Список. Сюда запишутся значение из infsl
for i in range(len(infsl)):
    spinf.append(int(infsl[i])) #Запись значений.

sd = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768] #Список. Это изначально пустые позиции, которые будут задаваться в списке spinf, которые впоследсвии будут заполняться значениями.
for i in range(len(sd)):
    spinf.insert(sd[i] - 1, "") #Список. Добавляет пустую строку на конкретную позицию.

sd1 = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767] #Список. Будет использоваться для подсчета значений в списке spinf.

for i in range(len(spinf)):
    if spinf[-1 - i] == "":
        spinf[-1 - i] = " "
    else:
        break
while " " in spinf:
    spinf.remove(" ") #Список. Удаляет ненужные пустые строки.

for i in range(len(spinf)):
    if spinf[i] == '':
        spinf[i] = 0
        for z in range(len(sd1)):
            if i == sd1[z]:
                for j in range(i, len(spinf), sd1[z] * 2 + 2):
                    for k in range(0, i + 1):
                        try:
                            spinf[i] += spinf[j + k] #Запись в пустую строку результата относительно данного алгоритма.
                        except:
                            break
                spinf[i] = summa(spinf[i]) #Итоговое число переводит либо в 0, либо в 1, в зависимости от четности числа.

spp = "" # Строка. Сюда записывается результат.
for i in range(len(spinf)):
    spp += str(spinf[i])
print("cipher_text:", spp)

# Генерация ключей
n = 0
p = None
q = None
while not(sympy.isprime(p)):
    p = random.randint(32, 100)
while not(sympy.isprime(q)):
    q = random.randint(32, 100)
n = p * q
print("p =", p)
print("q =", q)
print("n =", n)

m = (p - 1) * (q - 1)
print("m =", m)

pr = True
while pr:
    d = random.randint(2 ** 2600, 2 ** 2605)
    if sympy.isprime(d):
        pr = False
print("d =", d)

for i in range(2 ** 2500, 2 ** 10000):
    e = i
    if (e * d - 1) % m == 0:
        pr = False
        break
print("e =", e)
#e = 375828023454801203683362418972386504867736551759258677056523839782231681498337708535732725752658844333702457749526057760309227891351617765651907310968780236464694043316236562146724416478591131832593729111221580180531749232777515579969899075142213969117994877343802049421624954402214529390781647563339535024772584901607666862982567918622849636160208877365834950163790188523026247440507390382032188892386109905869706753143243921198482212075444022433366554786856559389689585638126582377224037721702239991441466026185752651502936472280911018500320375496336749951569521541850441747925844066295279671872605285792552660130702047998218334749356321677469529682551765858267502715894007887727250070780350262952377214028842297486263597879792176338220932619489510721

# Перевод битовой строки в символы
st = ""
for i in range(0, len(spp), 7):
    st += chr(int("1" + spp[i:i+7], 2))
print("cipher_text1:", st)

# Перевод символов в битовую строку
OT = st
OT = ''.join(format(ord(x),'b') for x in OT)
print("cipher_ text2:", OT)

# Перевод битовой строки в десятичную
OT1 = []
for i in range(0, len(OT), 8):
    OT1.append(int(OT[i : i + 8], 2))
print("OT1:", OT1)

# Шифрование
ST = []
for i in range(len(OT1)):
    ST.append(pow(int(OT1[i]), e, n))
print("ST:", ST)

# Зашифрованный текст в шеснадцатиричном виде
ST1 = []
for i in range(len(ST)):
    ST1.append(hex(ST[i])[2:])
print("Шифртекст:", ST1)

file_name = "C:\\Users\\Дмитрий\\OneDrive\\Рабочий стол\\4 курс, 2 семестр\\Курсовая работа\\Открытый текст и ключи.txt"
with open(file_name, 'w', encoding='utf8') as file:
    file.write(f'n = {str(n)}\n')
    file.write(f'd = {str(d)}\n')
    file.write(f'ОТ = {str(ST1)}')