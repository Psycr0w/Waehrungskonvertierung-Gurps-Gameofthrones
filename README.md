# Währungskonvertierung-Gurps-Gameofthrones

Kleines Programm zur Umrechnung von Gurps-Dollar zu den A Song of Ice and Fire Währungen.
***
Commandline - Powershell:
Standardmäßig werden keine Monde gerechnet, allerdings gibts hinten einen -md switch mit dem Monde berechnet werden

Beispiel in und Output:

.\Converter.ps1 40000
1 Drachen , 147 Hirschen , 1 Sterne

.\Converter.ps1 40000 -md
1 Drachen , 21 Monde , 1 Sterne

***

Commandline - Python:
Converter.py ist eine Python implementierung der selben Logik, allerdings noch ohne Commandlineoptionen.

Beispiel in und Output:

python .\Converter.py 40000
1 Drachen , 147 Hirschen , 1 Sterne

python .\Converter.py 40000 md
1 Drachen , 21 Monde , 1 Sterne


***
GUI:

finalconverter.py ist eine vollständige Implementierung als GUI - Applikation unter Zuhilfenahme von PyQT5, QTDesigner und der Basis die durch die Umstellung auf Pythoncode erstellt wurde.
