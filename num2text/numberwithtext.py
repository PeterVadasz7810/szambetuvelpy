EGYESEK = ['', 'egy', 'kettő', 'három', 'négy', 'öt', 'hat', 'hét', 'nyolc', 'kilenc']
TIZESEK = ['', 'tíz', 'húsz', 'harminc', 'negyven', 'ötven', 'hatvan', 'hetven', 'nyolcvan', 'kilencven']
TIZHATVANYAI = ['', 'ezer', 'millió', 'milliárd', 'billió', 'billiárd', 'trillió', 'trilliárd', 'kvadrillió',
                'kvadrilliárd', 'kvintillió', 'kvintilliárd', 'szextillió', 'szextilliárd', 'szeptillió',
                'szeptilliárd', 'oktillió', 'oktilliárd']
EXTRA = ['', 'tizen', 'huszon']


class NotANumber(Exception):
    def __init__(self, value, message='The value is not a number'):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{value} not a number'


class TooLargeNumber(Exception):
    def __init__(self, value, message='The number is too large'):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{value} is too large'


class NotAnInteger(Exception):
    def __init__(self, value, message='The number is not an integer'):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{value} is not an integer'


class NumberWithText(object):

    def __init__(self, number: int):

        if isinstance(number, (int, float)):
            if isinstance(number, int):
                self.number = number
            else:
                raise NotAnInteger(number)
        else:
            raise NotANumber(number)

        if number > 9999999999999999999999999999999999999999999999999999:
            raise TooLargeNumber(number)

        self.__set_minus()

        if self.__check_negative_number():
            number = abs(number)

        self.__mynumstr = str(number)

        length_of_the_number = len(self.__mynumstr)

        if length_of_the_number % 3 != 0:
            myrange = (length_of_the_number // 3) + 1
        else:
            myrange = length_of_the_number // 3

        templist = []

        for i in range(myrange):
            templist.append(int(self.__mynumstr[-3:]))
            self.__mynumstr = self.__mynumstr[:-3]

        if number % self.__generate_divider(length_of_the_number) == 0:
            self._outstr = [self.__szazas(templist[len(templist) - 1]) + TIZHATVANYAI[myrange - 1]]
        else:
            self._outstr = [self.__szazas(num) + TIZHATVANYAI[i] if self.__szazas(num) != '' else self.__szazas(num) for
                            i, num in enumerate(templist)]
            self._outstr.reverse()

        # remove empty strings from the list
        self._outstr[:] = [x for x in self._outstr if x]

    def __generate_divider(self, length: int) -> int:
        one = '1'
        zero = '0'
        k = 0
        if length % 3 == 1:
            k = 1
        elif length % 3 == 2:
            k = 2
        elif (length % 3 == 0) and (length // 3 >= 3):
            k = 3
        return int(one + (zero * (length - k)))

    def __check_negative_number(self) -> bool:
        return self.number < 0

    def __set_minus(self):
        if self.__check_negative_number():
            self.__minus = 'mínusz '
        else:
            self.__minus = ''

    def __szazas(self, szam: int) -> str:
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
            if EGYESEK[szam // 100] == 'kettő':
                tmp = 'kétszáz'
            else:
                tmp = EGYESEK[szam // 100] + 'száz'
            if ((szam - ((szam // 100) * 100)) // 10) in [1, 2] and (((szam - ((szam // 100) * 100)) % 10) > 0):
                tmp = tmp + EXTRA[((szam - ((szam // 100) * 100)) // 10)]
            else:
                tmp = tmp + TIZESEK[((szam - ((szam // 100) * 100)) // 10)]
            return tmp + EGYESEK[((szam - ((szam // 100) * 100)) % 10)]

    def __check_zero(self) -> bool:
        if self.number == 0:
            return True
        else:
            return False

    def get_number_with_text(self) -> str:
        if self.__check_zero():
            return 'nulla'
        else:
            if abs(self.number) > 2000:
                return self.__minus + ('-'.join(self._outstr))
            else:
                return self.__minus + (''.join(self._outstr))

    def __str__(self):
        output = self.get_number_with_text()
        return output

    number_with_text = property(get_number_with_text)


if __name__ == "__main__":

    while True:
        x = input('Kérek egy egész számot: ')
        try:
            x = int(x)
        except ValueError:
            print('A beírt érték nem szám!')
            continue
        else:
            break

    value = NumberWithText(x)
    print(value)
