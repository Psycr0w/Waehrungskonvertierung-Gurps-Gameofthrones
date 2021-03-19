# Währungskonvertierung-Gurps-Gameofthrones

Powershellversion ist commandline only
Standardmäßig werden keine Monde gerechnet, allerdings gibts hinten einen -md switch mit dem Monde berechnet werden
Beispiel in und Output:

.\ConverterMonde.exe 40000
1 Drachen , 147 Hirschen , 1 Sterne

.\ConverterMonde.exe 40000 -md
1 Drachen , 21 Monde , 1 Sterne

***

Converter.py ist eine Python implementierung der Selben Logik, allerdings noch ohne Commandlineoptionen.


***

finalconverter.py ist eine vollständige Implementierung als GUI - Applikation unter zuhilfenahme von PyQT5, QT5Designer und der Basis die durch die Umstellung auf Pythoncode erstellt wurde.
