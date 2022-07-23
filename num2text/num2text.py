'''
Egész számok betűvel történő kiírása
'''

EGYESEK = ['', 'egy', 'kettő', 'három', 'négy', 'öt', 'hat', 'hét', 'nyolc', 'kilenc']
TIZESEK = ['', 'tíz', 'húsz', 'harminc', 'negyven', 'ötven', 'hatvan', 'hetven', 'nyolcvan', 'kilencven']
TIZHATVANYAI = ['', 'száz', 'ezer', 'millió', 'milliárd', 'billió', 'billiárd', 'trillió', 'trilliárd']
EXTRA = ['', 'tizen', 'huszon']


def szazas(szam: int) -> str:
    tmp = ''
    if szam > 999:
        return '#'
    length_of_the_number = len(str(szam))
    if length_of_the_number == 1:
        return EGYESEK[szam]
    elif length_of_the_number == 2:
        if (((szam // 10) == 1) or ((szam // 10) == 2)) and (szam - ((szam // 10) * 10) != 0):
            tmp = EXTRA[szam // 10]
        else:
            tmp = TIZESEK[szam // 10]
        return tmp + EGYESEK[szam - ((szam // 10) * 10)]
    elif length_of_the_number == 3:
        tmp = EGYESEK[szam // 100] + 'száz'
        if ((szam - ((szam // 100) * 100)) // 10) in [1, 2] and (((szam - ((szam // 100) * 100)) % 10) > 0):
            tmp = tmp + EXTRA[((szam - ((szam // 100) * 100)) // 10)]
        else:
            tmp = tmp + TIZESEK[((szam - ((szam // 100) * 100)) // 10)]
        return tmp + EGYESEK[((szam - ((szam // 100) * 100)) % 10)]


def szambolbetu(szam: int) -> str:
    tmpstr = ''
    minusz = ''

    if not (type(szam) is int):
        return 'A kapott érték nem egy pozitív egész szám!'

    if szam == 0:
        return 'Nulla'

    if szam < 0:
        minusz = 'mínusz '
        szam = szam * -1

    tmpszam = szam

    if len(str(tmpszam)) > 9:
        return 'A szám túl nagy'

    tmpint = tmpszam // 1000000

    if tmpint != 0:
        tmpstr = tmpstr + szazas(tmpint)
        if szam % 1000000 > 0:
            tmpstr = tmpstr + 'millió-'
        else:
            return (minusz + tmpstr + 'millió').capitalize()

    tmpszam = tmpszam - (tmpint * 1000000)
    tmpint = tmpszam // 1000
    if tmpint != 0:
        tmpstr = tmpstr + szazas(tmpint)
        if (szam > 2000) and (tmpszam % 1000 != 0):
            tmpstr = tmpstr + 'ezer-'
        else:
            tmpstr = tmpstr + 'ezer'
            if tmpszam % 1000 == 0:
                return (minusz + tmpstr).capitalize()

    tmpszam = tmpszam - (tmpint * 1000)
    tmpstr = tmpstr + szazas(tmpszam)
    return (minusz + tmpstr).capitalize()


if __name__ == "__main__":

    while True:
        x = input('Kérek egy pozitív egész számot [0 - 999 999 999]: ')
        try:
            x = int(x)
        except ValueError:
            print('A beírt érték nem szám!')
            continue
        else:
            break
    print(szambolbetu(x))
