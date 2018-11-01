# i4-projekt-wissenstechnologien-carosabotage


Auswertung von Fan-Prognosen anhand von Tweets 

Autoren: 
Sandra Wirth 2178749 und Carolin Sabokat 2192929

Kontakt:
Carolin.Sabokat@hhu.de
Sandra.Wirth@hhu.de

1.11.2018

Beide Programme sind mit Python 3 programmiert.
Eine passende Programmierumgebung findet sich unter: https://www.continuum.io/downloads


Name des Programs: 
apicount.py - Twitter API

Version 1

Installation:

- Zur Nutzung des Programms wird Python 3 benötigt


Twitter API zum erhalten der Tweets 

Der Grundcode stammt von folgender Seite: https://pypi.python.org/pypi/TwitterSearch/ 
Und wurde für unsere Zwecke abgeändert. 

Zur Nutzung werden eigene Access Tokens benötigt, eine Anleitung, wie man diese erhält findet sich hier:
http://socialmedia-class.org/twittertutorial.html

Zur Nutzung einfach  unter tso.set_keywords die gewünschten Suchparameter einfügen.


textmining.py - Programm zum Auswerten der Tweets

Das Programm liest die Textdateien der Tweets ein und wertet diese anhand vorgegebener Phrasen aus.
Dazu einfach unter fobj = open("thewalkingdead22Okt2016.txt", 'r') die zur Auswertung gewünschte Datei eintragen. 

Lizenz: Copyright 2018 Carolin Sabokat & Sandra Wirth
