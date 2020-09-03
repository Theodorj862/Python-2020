
bbase = 40
bmile = 0.25
dbase = 60
dmile = 0.25
print('Welcome to car rentals!')
while True:
    afram = input('Would you like to continue (y/n)? ')
    if afram == 'n':
        break
    val = input('Customer code (b or d): ')
    dagar = int(input('Number of days: '))
    maelirb = int(input('Odometer reading at the start: '))
    maelirl = int(input('Odometer reading at the end: '))
    milur = maelirl - maelirb
    print('Miles driven:', milur)
    if val == 'b':
        b =round((dagar * bbase + bmile * milur), 1)
        print('Amount due:', b)
    if val == 'd':
        if (milur / dagar) > 100:
            t = milur/dagar - 100
            d = round((dagar * dbase + dmile * t * dagar), 1)
            print('Amount due:', d)
    else:
        d = round((dagar * dbase ), 1)
