Klausur Python Grundlagen
Name: Daniil Belik
Klasse: FAG46
Datum: 10.01.2025


Aufgabe 1 Operatoren:

a) Beschreiben Sie den Unterschied zwischen logischen Operatoren und Vergleichsoperatoren.
Logische Operatoren verknüpfen logische Ausdrücke, während Vergleichsoperatoren zwei Werte vergleichen.

Lösung:

a) Logische Operatoren sind: and, or, not
Logische Operatoren sind Operatoren, die dazu dienen, logische Ausdrücke zu verknüpfen.
Sie sind in der Regel binär, d.h. sie verknüpfen zwei Operanden.

Beispiele:

print("Logische Operatoren:")
print("True and False:", True and False)  # False
print("not True:", not True)  # False
print("False or True:", False or True)  # True

print("\n")

# b) Vergleichsoperatoren sind: ==, !=, <, >, <=, >=
# Vergleichsoperatoren dienen dazu, zwei Werte zu vergleichen.
# Sie geben in der Regel ein boolsches Ergebnis zurück.

# Beispiele:

print("Vergleichsoperatoren:")
print("5 == 5:", 5 == 5)  # True
print("10 > 5:", 10 > 5)  # True
print("7 <= 3:", 7 <= 3)  # False

# Was ist ein kombinierter Operator?
# Losung: Ein kombinierter Operator ist ein Operator, der eine Operation mit einer Zuweisung kombiniert.
# Beispiele: += , -=, *=, /=, %=, //=, **=

# Schreiben Sie ein Inkrement(Erhöhung eines Wertes um 1) in Python Code(4P)

# Losung:
x = 5
x += 1  # Erhöht x um 1,
print(x)  # x ist jetzt 6

# c) Gegeben seien die Variablen A, B C und D vom Typ bool.

# Losung:
A = True
B = False
C = False
D = True

# Erzeugen Sie eine Abfrage, die dann wahr liefert, wenn A und D wahr werden. (8P)

# Losung:
if A and D:
    print("Wahr")

# ======================================================================================================================


# Aufgabe 2 Verzweigungen:
# a) In einem Kino gibt es unterschiedliche Preise für Besuchergruppen.
#  Schreiben Sie ein Python-Programm, welches den Nutzer nach seinem Status fragt.
# Der Standardpreis eines Tickets beträgt 12 €.
# Kinder: 50 % Rabatt
# Studenten: 25 % Rabatt
# Rentner: 30 % Rabatt
# VIP-Kartenbesitzer: Aufpreis von 20 %
# Geben Sie den Preis auf dem Bildschirm aus. Nutzen Sie hierfür den f-Modus von Strings. (15P)

# Losung:

status = input(
    "Bitte geben Sie Ihren Status ein (Kind, Student, Rentner, VIP): ").lower() # Status abfragen und in Kleinbuchstaben konvertieren
standardpreis = 12

if status == "kind":
    preis = standardpreis * 0.5
elif status == "student":
    preis = standardpreis * 0.75
elif status == "rentner":
    preis = standardpreis * 0.7
elif status == "vip":
    preis = standardpreis * 1.2
else:
    preis = standardpreis

print(f"Der Ticketpreis beträgt: {preis:.2f} €")


# b) Beschreiben Sie den Unterschied zwischen einfachen if -Bedingungen und if .. elif .. else Bedingungen. (6P)

# Losung:

# if: Prüft eine Bedingung.
# if ..elif ..else - Ermöglicht mehrere Bedingungen, wobei nur die erste erfüllte Bedingung ausgeführt wird.

# c) Überführen Sie diese Aufgabe a) in ein match … case Konstrukt. (9P)

# Losung:

standardpreis = 12

while True:
    status = input(
        "Bitte geben Sie Ihren Status ein (Kind, Student, Rentner, VIP): ").lower()  # Eingabe in Kleinbuchstaben umwandeln

    match status:
        case "kind":
            preis = standardpreis * 0.5
            break
        case "student":
            preis = standardpreis * 0.75
            break
        case "rentner":
            preis = standardpreis * 0.7
            break
        case "vip":
            preis = standardpreis * 1.2
            break
        case _:
            print(
                "Ungültiger Status. Bitte geben Sie nur 'Kind', 'Student', 'Rentner' oder 'VIP' ein.")  # Fehlermeldung
            continue

print(f"Der Ticketpreis beträgt: {preis:.2f} €")


# ======================================================================================================================

# Aufgabe 3: Listen und Dictionaries

# a) Beschreiben Sie KURZ den Unterschied zwischen einem Tupel, einem Set und einem Dictionary. (5P)

# Losung:

# Unterschiede:
# Tuple: Unveränderlich, z. B. (1, 2, 3).
# Set: Keine Duplikate, z. B. {1, 2, 3}.
# Dictionary: Schlüssel-Wert-Paare, z. B. {"a": 1, "b": 2}.


# b) Legen Sie eine Liste mit 5 Strings an und sortieren Sie diese nach nach Länge des Wortes. (5P)

# Losung:
strings = ["Python", "Java", "JavaScript", "PHP", "C", "C++", "Ruby", "Go", "Rust"]
sorted_strings = sorted(strings, key=len)  # Sortiert nach Länge
print(sorted_strings)

#  c) Gegeben sei folgende Liste: temp = [20, 18, 28, 22, 19, 20, 25 ] Extrahieren Sie mit slicing die ersten 3 Tage und die letzten 2 Tage. (5P)

# Losung:

temp = [20, 18, 28, 22, 19, 20, 25]
firsr_three = temp[:3]  # Erste 3 Tage
last_two = temp[-2:]  # Letzte 2 Tage
print(firsr_three, last_two)  # [20, 18, 28] [20, 25]

#  d) Gegeben sei folgender Python-Code: Schreiben Sie eine list comprehension, die eine Liste von Zahlen erzeugt und diese mit 3 multipliziert. (5P)

# Losung:

numbers = [1, 2, 3, 4, 5]
multiple_numbers = [x * 3 for x in numbers]  # Multipliziert jede Zahl mit 3
print(multiple_numbers)  # [3, 6, 9, 12, 15]


# ======================================================================================================================

# Aufgabe 4: Praktische Programmierung
# Implementieren Sie folgendes Szenario in Python:
# Sie betreiben einen Süßigkeiten-Automaten.
# Dieser Automat hat insgesamt 5 verschiedene Süßigkeiten im Angebot:
# Schokolade, Gummibären, Nüsse, Powerriegel und Bonbons.
# Jede Ware hat die Eigenschaft Anzahl.
# Es soll zwei Funktionen geben: Auffüllen(setzt die Anzahl ALLER Waren auf 30) und Ziehen(verringert die Anzahl um 1).
# Es kann nur gezogen werden, wenn Ware da ist.
# Hinweise: Nutzen Sie ein Dictionary für die Ware und jeweils ein Dictionary für die Eigenschaften.

# Losung:

class CandyMachine:
    def __init__(self):
        # Initialisiert den Automaten mit Produkten und Mengen
        self.products = {1: "Schokolade", 2: "Gummibären", 3: "Nüsse", 4: "Powerriegel", 5: "Bonbons"}
        self.stock = {product: 0 for product in self.products.values()}

    def refill(self):
        """Füllt den Automaten auf: alle Produkte auf 30 setzen."""
        self.stock = {product: 30 for product in self.stock}
        print("Automat wurde aufgefüllt: 30 Stück pro Ware.")

    def dispense(self, product_number):
        """Gibt ein Produkt aus, wenn es verfügbar ist."""
        product = self.products.get(product_number)
        if not product:
            print(f"Ungültige Auswahl. '{product_number}' ist keine gültige Produktnummer.")  # Ungültige Produktnummer
        elif self.stock[product] > 0:
            self.stock[product] -= 1
            print(f"{product} wurde ausgegeben. Verbleibende Anzahl: {self.stock[product]}")
        else:
            print(f"{product} ist ausverkauft!")  # Produkt nicht verfügbar

    def display_stock(self):
        """Zeigt den aktuellen Warenbestand im Automaten an."""
        print("\nAktueller Warenbestand:")
        for product, quantity in self.stock.items():
            print(f"{product}: {quantity} Stück")
        print()


def main_menu():
    # Erstellt einen neuen Automaten
    machine = CandyMachine()
    machine.refill()

    # Menüoptionen mit Beschreibungen
    options = {
        "1": ("Warenbestand anzeigen", machine.display_stock),
        "2": ("Ware ziehen", lambda: select_product(machine)),
        "3": ("Automat auffüllen", machine.refill),
        "4": ("Beenden", lambda: exit("Vielen Dank!"))
    }

    while True:
        # Zeigt das Hauptmenü mit Optionen an
        print("\nSüßigkeiten-Automat")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")

        # Benutzerwahl
        choice = input("Bitte wählen Sie eine Option (1-4): ")
        if choice in options:
            options[choice][1]()  # Führt die gewählte Funktion aus
        else:
            print("Ungültige Option. Bitte versuchen Sie es erneut.")  # Fehlernachricht


def select_product(machine):
    print("\nVerfügbare Produkte:")
    for number, product in machine.products.items():
        print(f"{number}. {product}")

    try:
        product_number = int(input("Bitte wählen Sie die Produktnummer (1-5): "))
        machine.dispense(product_number)
    except ValueError:
        print("Ungültige Eingabe! Bitte eine Zahl eingeben.")


# Startpunkt des Programms
if __name__ == "__main__":
    main_menu()








