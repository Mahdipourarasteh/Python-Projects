print("Hallo liebe/r Benutzer/in.")
print("Hier werden die Schaltjahren berechnet.")
print("Bitte geben Sie Ihre gewuenschte Jahreszahl ein:")
z=int(input())
#24.02.1582 ~= 1583
if z<1583:
    print("die eingegebene Jahreszahl fällt nicht in den Gültigkeitsbereich des Gregorianischen Kalenders.")
else:
    if z % 400 == 0:
        print("Das Jahr ", z, " ist ein Schaltjahr.")
    elif z % 100 == 0:
        print("Das Jahr ", z, " ist kein Schaltjahr.")
    elif z % 4 == 0:
        print("Das Jahr ", z, " ist ein Schaltjahr.")
    else:
        print("Das Jahr ", z, " ist kein Schaltjahr.")