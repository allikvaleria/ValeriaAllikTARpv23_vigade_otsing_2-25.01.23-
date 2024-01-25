print("*** Mängud numbritega ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1: 
    try:
        a = abs(int(input("Sisesta täisarv => "))) #убрать доп скобка перед abs
        break
    except ValueError:
         print("See pole täisarv.")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi teha.")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju on paaris- ja mitu paaritut numbrit")
    print()
    c=b=a #убать 2 =
    paaris = 0 #убать 2 =
    paaritu = 0 #убать 2 =
    while b > 0: #вместо ; надо :
            if b % 2 == 0: #2 равно
                    paaris =+ 1
            else:
                    paaritu =+ 1
            b = b // 10 #передвинуть в лево
    
    print("Numbrite arv:"+str(paaris)) #добавить +str и )
    print("Paaritu arv:"+str(paaritu)) #добавить +str и )
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake ümber* sisestatud arv")
    print()
    b=0
    while a > 0 : #не хватает :
        number = a % 10
        a = a // 10
        b = b * 10+ number
    print("*Pööratud* arv"+str(b))
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Uurime Syracuse hüpoteesi") #лишняя скобка
    print()
    if c % 2 == 0: #добавить второе равно и :
        print("c - paarisarv. Jagame 2.")
    else:
        print("c - paaritu arv. Korrutame 3-ga, liidame 1 ja jagame 2-ga.")
    while c != 1:
            if c % 2 == 0: #2 равно
                    c == c / 2
            else:
                    c == (3*c + 1) / 2
            print(c, end=" ") #добавить " 
    print()
    print("Hüpotees on õige") #другия кавычки
