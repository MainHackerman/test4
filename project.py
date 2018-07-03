# rezervacni system

def nabidka(destinace, ceny):
    print('We can offer you the following destinations:')
    print('=' * 80)
    for i in range(len(destinace)):
        print('| ' + destinace[i] + ' | ' + ceny[i])
    print('=' * 80)


def registrace(databaze, udaje):
    pass


def login(jmeno, heslo, databaze):
    for zaznam in databaze:
        if zaznam[1] == jmeno and zaznam[2] == heslo:
            return True
    return False


def nakup(destinace, ceny, *vyber):
    cena = 0
    for i in range(len(destinace)):
        for vec in vyber:
            if destinace[i] == vec:
                cena += ceny[i]
    return cena
