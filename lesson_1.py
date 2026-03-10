print("Hello, world!")
print('Hello, world! Number two!')
print("\"This is a quote from a famous person\"")
print('"This is a quote from a famous person"')
# "citat"
# textsträngar kan skrivas med " " eller ' '
# detta är en kommentar

"""
this
is
a
multi
line
comment
"""

# Operatorer
# ** = kortvariant för upphöjt i 2**3 = 2^3
# % = modulus = rest vid division 22 % 8 = 6
# % = ett jämnt tal x % 2 då får vi en rest på 0
# % = ett ojämnt tal x % 2 då får vi en rest på 1
# // = speciellt python-koncept 22//8 = 2
# / = 22/8 = 2.75
# * = 2 * 3 = 6
# - = 5 - 5 = 0
# + = 5 + 5 = 10

5 + 5  # unused expression. om något är unused, varför finns det då?
# Vi kan dock ha vårt expression fristående utan att det påverkar programmet
# Ett expression är något som evalueras till ett värde 5 + 5 evalueras till 10 (heltal)

# Vi kan tilldela ett expression till en variabel
# Detta är då en referens till något värde som existerar medan scriptet körs
resultat = 5 + 5  # expression på högra sidan
# variabel på vänstra sidan

# att något är dynamiskt
# innebär att vi kan ändra variabler och datatyper som vi vill under körning

heltal = 1 # heltal
heltal = 1.0 # nu är variabeln heltal en float, alltså flyttal med decimaler

# försök att ha så beskrivande namn som möjligt
# undvik svenska tecken
# a-z, små bokstäver och _ mellan orden
this_is_an_integer = 12 # Detta signalerar lite mer tanke bakom namnet

print(type(this_is_an_integer)) # vi kan få ut datatypen med type()

# dynamiska språk känner till datatypen
# när vi kommer till den raden
# annars vet inte Python om det

first_name = "Kimmo"
last_name = "Ahola"

# + mellan textsträngar = konkatenering
full_name = first_name + " " + last_name
print(full_name)

# kan inte blanda datatyper

forbidden = full_name + str(25)

# print(forbidden)

# att man inte kan blanda datatyper kallas för strong typing
# weak typing = kan blanda hur vi vill
# javascript = weak typing

x = 1  # heltal = integer
y = 1.0  # flyttal = float
z = True  # boolean = Sant/Falskt

# integer, float och boolean delar samma underliggande datatyp
# print(x+y+z)

x = int("1")
# x = int("Hej") Detta går inte
x = int(1.5)  # python klarar av detta men inte "1.5"

print(x)

text_string = f"{x+2}"  # f-string
# f-sträng kallas för interpolation

print(text_string)

# jämförelseoperatorer

## x == y : lika med > Sant eller Falskt
# != : inte lika med
# < mindre än
# > större än
# <= mindre eller lika med
# >= större eller lika med

# Allt ovanför evalueras till sant eller falskt

result = 2 == 2
print(f"Resultatet är: {result}")

result = 2 == 2
print(f"Resultatet är: {result}")

result = 0.1 + 0.2 == 0.3

print(result, f"0.1 + 0.2 = {0.1 + 0.2}")

result = 5 > 4 and 5 > 3  # båda måste stämma
result = 5 > 4 or 1 > 5  # den ena måste stämma
# not och is
# den speciella blå nyansen betyder att det är ett keyword
# keyword = reserverat ord i Python

# dessa kan inte användas som variablenamn eftersom de är upptagna
# and = 5
# class = 2
# def = 3

user_input = input("Ge mig något: ")

print(f"Du skrev {user_input}")

user_input = int(input("Ge mig en siffra: "))

print(f"Du skrev siffran {user_input}")

x = "TEX-MEX"  # tex-mex är samma som Tex-mex

print("T" in x) # Sant
print("t" in x) # Falskt
# Python är case-sensitive

result = x.lower() == "tex-mex"
print(x)
print(result)

# funktioner kräver dot notation
x.lower()


with open("random.txt", "r", encoding="utf-8") as f:
    my_text = f.read()

search_word = "Amanda Olsson"

number_of_rows = my_text.count("\n")
print("Antal rader: ", number_of_rows)

print("Ordet förekommer: ", my_text.count(search_word))

with open("new_file.txt", "a", encoding="utf-8") as f:
    f.write("\n" + "Test")
