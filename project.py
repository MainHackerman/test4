#rezervacni system

def nabidka(destinace, ceny):
    print('We can offer you the following destinations:')
    print('=' * 80)
    for i in len(destinace):
        print('| ' + destinace[i] + ' | ' + ceny[i])
    print('=' * 80)

def registrace(databaze, udaje):
    pass

def login(jmeno, heslo):
    pass

def nakup(*destinace):
    pass
