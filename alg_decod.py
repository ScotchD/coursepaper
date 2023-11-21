def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
def summator(x, y):
    for i in range(len(SR)):
        rs = []
        for j in range(len(SR[i])):
            rs.append(y[SR[i][j]])
        l = 0
        for k in range(len(rs)):
            if rs[k] == 1:
                l += 1
        if l % 2 == 0:
            l = 0
        else:
            l = 1
        x.append(l)

file_name = "C:\\Users\\Дмитрий\\OneDrive\\Рабочий стол\\4 курс, 2 семестр\\Курсовая работа\\Открытый текст и ключи.txt"
with open(file_name, 'r', encoding='utf8') as file:
    n = int(file.readline()[4:])
    d = int(file.readline()[4:])
    ST1 = file.readline()[5:]
ST1 = ST1.replace('[', '')
ST1 = ST1.replace(']', '')
ST1 = ST1.replace("'", '')
ST1 = ST1.split(', ')
print(f'n = {n}')
print(f'd = {d}')
print(f'ST1 = {ST1}')

#d = 476418619515067823588714793638656202201857139291083867959899955667653856265612022291529050965698956954980403301461703015038614868574193962397485499515664041394986281501470694218497988307090612350614568889981811581986638138356992766991125087684991039263797693265785104917948470363624188015370806861100688624248678603221354110605494242806696770917600281683633644108236805349374738136918815731368582599191891954042154031640578510234055103862187476613117399488481460317825611407737894256555037882572203580919569719825554820635703945122525655142867259335210893272327056051927519150227161849803955583483422130016277366149645187225958439976324236745223185422914992006460893085523949518747052097319358193378697931652326752042142239336421790958496682974373076635520836784028919211864805605377
#n = 3953
#ST1 = ['2e5', 'e83', 'aee', '300', '47b', '7ea', 'd6a', '834', 'e44', 'b5a', '83', 'd52', 'e14', '19f', 'eb4', '297', '83', '300', '22b', '90c', 'd6a', '324', 'afd', 'e14', 'd5f', '4a7', '732', 'b6d', '7de', 'e83', '524', '7ea', 'e63', '7c1', 'd52', '698', 'e50', 'd52', 'e14', '80', '4a3', '90c', 'd5f', 'd7a', '475', '297', '83', '300', '475', 'e44', '7ea', 'd58', '7c1', '146', '4ca', '80', '4a3', '361', 'b6e', 'd6a', '324', 'afd', '475', '361', '4a7', 'ef3', '582', 'd7a', 'f06']

ST = []
for i in range(len(ST1)):
    ST.append(int(ST1[i], 16))
print("ШТ:", ST)

RST = []
for i in range(len(ST)):
    RST.append(pow(int(ST[i]), d, n))
print("RST:", RST)

OT1 = []
for i in range(len(RST)):
    OT1.append(format(RST[i], "b"))
print("OT1:", OT1)

OT = []
for i in range(len(OT1)):
    OT.append(chr(int(OT1[i], 2)))
OT = ''.join(OT)
print("OT:", OT)

st1 = ''.join(format(ord(x),'b') for x in OT)
print("decipher_ text:", st1)

codsl = ""
for i in range(0, len(st1), 8):
    codsl += st1[i + 1 : i + 8]
print("cipher_text1:", codsl)

#codsl = input("cipher_text: ")

sd1 = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]
for i in range(len(codsl)):
    if i in sd1:
        codsl = codsl[:i] + " " + codsl[i + 1:]
codsl = codsl.replace(" ", "")

kreg = 3
kreg1 = kreg
reg = [0] * kreg
sumat = 2
SR = [[0, 1], [1, 2]]

INFSL = []
while len(codsl) != 0:
    ck = ""
    for i in range(sumat):
        ck += codsl[0]
        codsl = codsl.replace(codsl[0], "", 1)

    reg1 = []
    for i in range(len(reg)):
        reg1.append(reg[i])
    reg1.insert(0, 0)
    del reg1[-1]
    rez1 = []
    summator(rez1, reg1)

    REZ1 = ""
    for i in range(len(rez1)):
        REZ1 += str(rez1[i])

    reg2 = []
    for i in range(len(reg)):
        reg2.append(reg[i])
    reg2.insert(0, 1)
    del reg2[-1]
    rez2 = []
    summator(rez2, reg2)

    REZ2 = ""
    for i in range(len(rez2)):
        REZ2 += str(rez2[i])

    if REZ1 == ck and REZ2 != ck:
        INFSL.append(0)
        reg = []
        for i in range(len(reg1)):
            reg.append(reg1[i])
    elif REZ1 != ck and REZ2 == ck:
        INFSL.append(1)
        reg = []
        for i in range(len(reg2)):
            reg.append(reg2[i])
    elif len(codsl) == 0:
        INFSL.append(0)
    elif REZ1 == ck and REZ2 == ck:
        reg4 = []
        for i in range(len(reg2)):
            reg4.append(reg2[i])
        reg.insert(0, 0)
        del reg[-1]

        ck = ""
        for i in range(sumat):
            ck += codsl[i]

        reg1 = []
        for i in range(len(reg)):
            reg1.append(reg[i])
        reg1.insert(0, 0)
        del reg1[-1]
        rez1 = []
        summator(rez1, reg1)

        REZ1 = ""
        for i in range(len(rez1)):
            REZ1 += str(rez1[i])

        reg2 = []
        for i in range(len(reg)):
            reg2.append(reg[i])
        reg2.insert(0, 1)
        del reg2[-1]
        rez2 = []
        summator(rez2, reg2)

        REZ2 = ""
        for i in range(len(rez2)):
            REZ2 += str(rez2[i])

        if REZ1 == ck or REZ2 == ck:
            INFSL.append(0)

        else:
            reg = []
            for i in range(len(reg4)):
                reg.append(reg4[i])
            INFSL.append(1)

IS = ""
for i in range(len(INFSL)):
    IS += str(INFSL[i])
IS = IS[:-kreg1]

ISS = text_from_bits(IS)

print("Расшифрованный текст: ", ISS)