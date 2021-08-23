# Skriv ett program som skriver ut en multiplikationstabell för 1-12.
# Här finns halva lösningen: https://www.programiz.com/python-programming/examples/multiplication-table
# Tips! Kika på nästlade for-loopar

for n in range(1, 13):
    for i in range(1, 13):
        print(n, 'x', i, '=', n*i)
