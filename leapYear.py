# Skriv ett program som skriver ut sammanlagt 20 år och om varje år är skottår (leap year).
# Här finns halva lösningen: https://www.programiz.com/python-programming/examples/leap-year
# Tips! Kika på for loopar och funktioner.

def leapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year.".format(year))
            else:
                print("{0} is not a leap year.".format(year))
        else:
            print("{0} is a leap year.".format(year))
    else:
        print("{0} is not a leap year.".format(year))


currentYear = 2021

for x in range(21):
    leapYear(currentYear + x)
