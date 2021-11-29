from decimal import Decimal

while True:
    try:
        am_bill = Decimal(input("Введите сумму счета:\n")).quantize(Decimal("1.00"))
        break
    except:
        print("Некорректный ввод")
while True:
    try:
        numb_part = Decimal(
            input("Введите количество участников:\n")).quantize(Decimal("1"))
        break
    except:
        print("Некорректный ввод")
while True:
    try:
        am_part = input(
            "Введите суммы участников через пробел, в виде: sum1 sum2 sum3 ...:\n").split()
        for i in range(len(am_part)):
            am_part[i] = Decimal(am_part[i]).quantize(Decimal("1.00"))
        if len(am_part) == numb_part and sum(am_part) == am_bill:
            break
        else:
            print("Некорректный ввод")
    except:
        print("Некорректный ввод")

def bill(am_bill, numb_part, am_part):
    aver = Decimal(am_bill/numb_part).quantize(Decimal("1.00"))
    am_part_dic = {}
    for i in range(len(am_part)):
        am_part_dic[i+1] = am_part[i]
    major = {}
    minor = {}
    for k, v in am_part_dic.items():
        if am_part_dic[k] == aver:
            print(f"Участник №{k} ничего не должен")
        if am_part_dic[k] > aver:
            major[k] = am_part_dic[k]-aver
        if am_part_dic[k] < aver:
            minor[k] = aver-am_part_dic[k]
    for major_k, major_v in major.items():
        for minor_k, minor_v in minor.items():
            if major_v >= minor_v:
                major_v = major_v-minor_v
                print(
                    f"Участник №{minor_k} должен участнику №{major_k} {minor_v}")
            elif major_v < minor_v:
                minor_v = minor_v-major_v
                minor[minor_k] = minor_v
                print(
                    f"Участник №{minor_k} должен участнику №{major_k} {major_v}")
                break

bill(am_bill, numb_part, am_part)
