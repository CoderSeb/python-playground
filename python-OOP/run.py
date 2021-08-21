# Denna trevliga, minimala uppgift ger dig en introduktion till objekt-orienterad-programmering i Python.
# Du skall skapa en klass i en annan fil (Snake.py) som du sedan ska importera in i denna fil (run.py)
# för att sedan använda klassen genom att skapa ett objekt och sedan använda det objektet.

# Importera här klassen Snake du skapade i filen Snake.py
from Snake import Snake

# Skapa ett objekt av klassen Snake som du kallar för mySnake med värden för species, name och age.
mySnake = Snake(species="Ball Python", name="Otto", age=2)

# Skriv ut i konsollen en trevlig mening där du berättar om din orm.
# Samtliga attribut i ditt objekt ska finnas med.
print(f"My {mySnake.species}, {mySnake.name}, is already {mySnake.age} years old.")
