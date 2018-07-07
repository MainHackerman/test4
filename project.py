# rezervacni system

def nabidka(destinace, ceny):
    print('We can offer you the following destinations:')
    print('=' * 80)
    for i in range(len(destinace)):
        print('| ' + destinace[i] + ' | ' + str(ceny[i]))
    print('=' * 80)

def jejmeno(string):
    pss = 0
    valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
    for pismeno in string:
        if str(pismeno) in valid:
            pss += 1
    if pss == len(string):
        return True
    else:
        return False

def regvalid(udaje):
    passwd = False
    mail = False
    vek = False
    if len(udaje[2]) >= 8:
        passwd = True
    if '@' in udaje[3]:
        mail = True
    if udaje[4] > 15:
        vek = True
    if jejmeno(udaje[0]) and jejmeno(udaje[1]) and passwd and mail and vek:
        return True
    else:
        return False

def registrace():
    reg_udaje = []
    reg_udaje.append(input('Zadej krestni jmeno (bez diakritiky a mezer): '))
    reg_udaje.append(input('Zadej prijmeni (bez diakritiky a mezer): '))
    reg_udaje.append(input('Zadej heslo dlouhe alespon 8 znaku: '))
    reg_udaje.append(input('Zadej e-mail: '))
    reg_udaje.append(int(input('Zadej svuj vek: ')))
    if regvalid(reg_udaje):
        return reg_udaje
    else:
        return 'CHYBA'

def login():
    login_udaje = []
    login_udaje.append(input('Zadej email: '))
    login_udaje.append(input('Zadej heslo: '))
    return login_udaje

def auth(udaje, databaze):
    for zaznam in databaze:
        if zaznam[0] == udaje[0] and zaznam[1] == udaje[1]:
            return True
    return False


def nakup(destinace, ceny, vyber):
    cena = 0
    for i in range(len(destinace)):
        for vec in vyber:
            if destinace[i] == vec:
                cena += ceny[i]
    return cena

destinace = ['Olomouc','Brno']
ceny = [200,300]
prihlasen = False
uzivatele = []

print('Vitej v nasi aplikaci, nejdrive se musis prihlasit')
uzivatele.append(registrace())
if uzivatele[-1] == 'CHYBA':
    print('Zadal jsi spatne registracni udaje')
    del uzivatele[-1]

if not auth(login(),uzivatele):
    print('Zadal jsi spatne prihlasovaci udaje')
else:
    prihlasen = True
nabidka(destinace,ceny)
vyber = []
while True:
    vyber.append(input('Vyber destinaci: '))
    if vyber[-1] == 'nic':
        del vyber[-1]
        break
print('Tvuj nakup bude stat', nakup(destinace, ceny, vyber), 'korun')