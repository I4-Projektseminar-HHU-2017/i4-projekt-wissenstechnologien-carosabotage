# -*- coding: utf-8 -*-

#Python 3

import nltk




Rickdies = 0
Ricklives = 0
Carldies = 0
Carllives = 0
Daryldies = 0
Daryllives = 0
Maggiedies = 0
Maggielives = 0
Glenndies = 0
Glennlives = 0
Michonnedies = 0
Michonnelives = 0
Sashadies = 0
Sashalives = 0
Abrahamdies = 0
Abrahamlives = 0
Eugenedies = 0
Eugenelives = 0
Rositadies = 0
Rositalives = 0
Aarondies = 0
Aaronlives = 0
Negandies = 0
Neganlives = 0

Tweets = 0





# Text anzeigen
#fobj = open("testtweets.txt", "r")
#for line in fobj:
	#print(line)



fobj = open("thewalkingdead22Okt2016.txt", 'r')
for line in fobj:
	#liste = []
	#liste = line.split()
	
	
	
	if "Mehr" in line:
		Tweets = Tweets + 1
	
	#Rick:
	if "Rick die" in line:
		Rickdies = Rickdies + 1
	if "rick die" in line:
		Rickdies = Rickdies + 1
	if "Rick to die" in line:
		Rickdies = Rickdies + 1
	if "rick to die" in line:
		Rickdies = Rickdies + 1
	if "Rick will die" in line:
		Rickdies = Rickdies + 1
	if "rick will die" in line:
		Rickdies = Rickdies + 1
	if "Rick WILL die" in line:
		Rickdies = Rickdies + 1
	if "rick WILL die" in line:
		Rickdies = Rickdies + 1
	if "Rick is going to die" in line:
		Rickdies = Rickdies + 1
	if "rick is going to die" in line:
		Rickdies = Rickdies + 1
	if "Rick is gonna die" in line:
		Rickdies = Rickdies + 1
	if "rick is gonna die" in line:
		Rickdies = Rickdies + 1
	if "Rick dead" in line:
		Rickdies = Rickdies + 1
	if "rick dead" in line:
		Rickdies = Rickdies + 1
	if "kills Rick" in line:
		Rickdies = Rickdies + 1
	if "kills rick" in line:
		Rickdies = Rickdies + 1
	if "kill Rick" in line:
		Rickdies = Rickdies + 1
	if "kill rick" in line:
		Rickdies = Rickdies + 1
	if "killed Rick" in line:
		Rickdies = Rickdies + 1
	if "killed rick" in line:
		Rickdies = Rickdies + 1
	if "Rick killed" in line:
		Rickdies = Rickdies + 1
	if "rick killed" in line:
		Rickdies = Rickdies + 1
	if "Rick will be killed" in line:
		Rickdies = Rickdies + 1
	if "rick will be killed" in line:
		Rickdies = Rickdies + 1
	if "Rick is killed" in line:
		Rickdies = Rickdies + 1
	if "rick is killed" in line:
		Rickdies = Rickdies + 1
	if "Rick lives" in line:
		Ricklives = Ricklives + 1
	if "rick lives" in line: 
		Ricklives = Ricklives + 1
	if "Rick will live" in line:
		Ricklives = Ricklives +1
	if "rick will live" in line:
		Ricklives = Ricklives + 1
	if "Rick survives" in line:
		Ricklives = Ricklives + 1
	if "rick survives" in line: 
		Ricklives = Ricklives + 1
	if "Rick to live" in line:
		Ricklives = Ricklives + 1
	if "rick to live" in line:
		Ricklives = Ricklives + 1
	
	#Carl:
	if "Carl die" in line:
		Carldies = Carldies + 1
	if "carl die" in line:
		Carldies = Carldies + 1
	if "Carl to die" in line:
		Carldies = Carldies + 1
	if "carl to die" in line:
		Carldies = Carldies + 1
	if "Carl will die" in line:
		Carldies = Carldies + 1
	if "carl will die" in line:
		Carldies = Carldies + 1
	if "Carl WILL die" in line:
		Carldies = Carldies + 1
	if "carl WILL die" in line:
		Carldies = Carldies + 1
	if "Carl is going to die" in line:
		Carldies = Carldies + 1
	if "carl is going to die" in line:
		Carldies = Carldies + 1
	if "Carl is gonna die" in line:
		Carldies = Carldies + 1
	if "carl is gonna die" in line:
		carldies = carldies + 1
	if "Carl dead" in line:
		Carldies = Carldies + 1
	if "carl dead" in line:
		Carldies = Carldies + 1
	if "Carl killed" in line:
		Carldies = Carldies + 1
	if "carl killed" in line:
		Carldies = Carldies + 1
	if "kills Carl" in line:
		Carldies = Carldies + 1
	if "kills carl" in line:
		Carldies = Carldies + 1
	if "kill Carl" in line:
		Carldies = Carldies + 1
	if "kill carl" in line:
		Carldies = Carldies + 1
	if "killed Carl" in line:
		Carldies = Carldies + 1
	if "killed carl" in line:
		Carldies = Carldies + 1
	if "Carl will be killed" in line:
		Carldies = Carldies + 1
	if "carl will be killed" in line:
		Carldies = Carldies + 1
	if "Carl is killed" in line:
		Carldies = Carldies + 1
	if "carl is killed" in line:
		Carldies = Carldies + 1
	if "Carl lives" in line:
		Carllives = Carllives + 1
	if "carl lives" in line: 
		Carllives = Carllives + 1
	if "Carl will live" in line:
		Carllives = Carllives +1
	if "carl will live" in line:
		Carllives = Carllives + 1
	if "Carl survives" in line:
		Carllives = Carllives + 1
	if "carl survives" in line: 
		Carllives = Carllives + 1
	if "Carl to live" in line:
		Carllives = Carllives + 1
	if "carl to live" in line:
		Carllives = Carllives + 1
		
	#Daryl: 
	if "Daryl die" in line:
		Daryldies = Daryldies + 1
	if "daryl die" in line:
		Daryldies = Daryldies + 1
	if "Daryl to die" in line:
		Daryldies = Daryldies + 1
	if "daryl to die" in line:
		Daryldies = Daryldies + 1
	if "Daryl will die" in line:
		Daryldies = Daryldies + 1
	if "daryl will die" in line:
		Daryldies = Daryldies + 1
	if "Daryl WILL die" in line:
		Daryldies = Daryldies + 1
	if "daryl WILL die" in line:
		Daryldies = Daryldies + 1
	if "Daryl is going to die" in line:
		Daryldies = Daryldies + 1
	if "daryl is going to die" in line:
		Daryldies = Daryldies + 1		
	if "Daryl is gonna die" in line:
		Daryldies = Daryldies + 1
	if "daryl is gonna die" in line:
		Daryldies = Daryldies + 1
	if "Daryl dead" in line:
		Daryldies = Daryldies + 1
	if "daryl dead" in line:
		Daryldies = Daryldies + 1
	if "Daryl killed" in line:
		Daryldies = Daryldies + 1
	if "daryl killed" in line:
		Daryldies = Daryldies + 1
	if "kills Daryl" in line:
		Daryldies = Daryldies + 1
	if "kills daryl" in line:
		Daryldies = Daryldies + 1
	if "kill Daryl" in line:
		Daryldies = Daryldies + 1
	if "kill daryl" in line:
		Daryldies = Daryldies + 1
	if "killed Daryl" in line:
		Daryldies = Daryldies + 1
	if "killed daryl" in line:
		Daryldies = Daryldies + 1
	if "Daryl will be killed" in line:
		Daryldies = Daryldies + 1
	if "daryl will be killed" in line:
		Daryldies = Daryldies + 1
	if "Daryl is killed" in line:
		Daryldies = Daryldies + 1
	if "daryl is killed" in line:
		Daryldies = Daryldies + 1
	if "Daryl lives" in line:
		Daryllives = Daryllives + 1
	if "daryl lives" in line: 
		Daryllives = Daryllives + 1
	if "Daryl will live" in line:
		Daryllives = Daryllives + 1
	if "daryl will live" in line:
		Daryllives = Daryllives + 1
	if "Daryl survives" in line:
		Daryllives = Daryllives + 1
	if "daryl survives" in line: 
		Daryllives = Daryllives + 1
	if "Daryl to live" in line:
		Daryllives = Daryllives + 1
	if "daryl to live" in line:
		Daryllives = Daryllives + 1
	
	#Maggie:
	if "Maggie die" in line:
		Maggiedies = Maggiedies + 1
	if "maggie die" in line:
		Maggiedies = Maggiedies + 1
	if "Maggie to die" in line:
		Maggiedies = Maggiedies + 1
	if "maggie to die" in line:
		Maggiedies = Maggiedies + 1
	if "Maggie will die" in line:
		Maggiedies = Maggiedies + 1
	if "maggie will die" in line:
		Maggiedies = Maggiedies + 1
	if "Maggie WILL die" in line:
		Maggiedies = Maggiedies + 1
	if "maggie WILL die" in line:
		Maggiedies = Maggiedies + 1
	if "Maggie is going to die" in line:
		Maggiedies = Maggiedies + 1
	if "maggie is going to die" in line:
		Maggiedies = Maggiedies + 1		
	if "Maggie is gonna die" in line:
		Maggiedies = Maggiedies + 1
	if "maggie is gonna die" in line:
		Maggiedies = Maggiedies + 1
	if "Maggie dead" in line:
		Maggiedies = Maggiedies + 1
	if "maggie dead" in line:
		Maggiedies = Maggiedies + 1
	if "Maggie killed" in line:
		Maggiedies = Maggiedies + 1
	if "maggie killed" in line:
		Maggiedies = Maggiedies + 1
	if "kills Maggie" in line:
		Maggiedies = Maggiedies + 1
	if "kills maggie" in line:
		Maggiedies = Maggiedies + 1
	if "kill Maggie" in line:
		Maggiedies = Maggiedies + 1
	if "kill maggie" in line:
		Maggiedies = Maggiedies + 1
	if "killed Maggie" in line:
		Maggiedies = Maggiedies + 1
	if "killed maggie" in line:
		Maggiedies = Maggiedies + 1
	if "Maggie will be killed" in line:
		Maggiedies = Maggiedies + 1
	if "maggie will be killed" in line:
		Maggiedies = Maggiedies + 1
	if "Maggie is killed" in line:
		Maggiedies = Maggiedies + 1
	if "maggie is killed" in line:
		Maggiedies = Maggiedies + 1
	if "Maggie lives" in line:
		Maggielives = Maggielives + 1
	if "maggie lives" in line: 
		Maggielives = Maggielives + 1
	if "Maggie will live" in line:
		Maggielives = Maggielives + 1
	if "maggie will live" in line:
		Maggielives = Maggielives + 1
	if "Maggie survives" in line:
		Maggielives = Maggielives + 1
	if "maggie survives" in line: 
		Maggielives = Maggielives + 1
	if "Maggie to live" in line:
		Maggielives = Maggielives + 1
	if "maggie to live" in line:
		Maggielives = Maggielives + 1	
		
	#Glenn:
	if "Glenn die" in line:
		Glenndies = Glenndies + 1
	if "glenn die" in line:
		Glenndies = Glenndies + 1
	if "Glenn to die" in line:
		Glenndies = Glenndies + 1
	if "glenn to die" in line:
		Glenndies = Glenndies + 1
	if "Glenn will die" in line:
		Glenndies = Glenndies + 1
	if "glenn will die" in line:
		Glenndies = Glenndies + 1
	if "Glenn WILL die" in line:
		Glenndies = Glenndies + 1
	if "glenn WILL die" in line:
		Glenndies = Glenndies + 1
	if "Glenn is going to die" in line:
		Glenndies = Glenndies + 1
	if "glenn is going to die" in line:
		Glenndies = Glenndies + 1		
	if "Glenn is gonna die" in line:
		Glenndies = Glenndies + 1
	if "glenn is gonna die" in line:
		Glenndies = Glenndies + 1
	if "Glenn dead" in line:
		Glenndies = Glenndies + 1
	if "glenn dead" in line:
		Glenndies = Glenndies + 1
	if "Glenn killed" in line:
		Glenndies = Glenndies + 1
	if "glenn killed" in line:
		Glenndies = Glenndies + 1
	if "kills Glenn" in line:
		Glenndies = Glenndies + 1
	if "kills glenn" in line:
		Glenndies = Glenndies + 1
	if "kill Glenn" in line:
		Glenndies = Glenndies + 1
	if "kill glenn" in line:
		Glenndies = Glenndies + 1
	if "killed Glenn" in line:
		Glenndies = Glenndies + 1
	if "killed glenn" in line:
		Glenndies = Glenndies + 1
	if "Glenn will be killed" in line:
		Glenndies = Glenndies + 1
	if "glenn will be killed" in line:
		Glenndies = Glenndies + 1
	if "Glenn is killed" in line:
		Glenndies = Glenndies + 1
	if "glenn is killed" in line:
		Glenndies = Glenndies + 1
	if "Glenn lives" in line:
		Glennlives = Glennlives + 1
	if "glenn lives" in line: 
		Glennlives = Glennlives + 1
	if "Glenn will live" in line:
		Glennlives = Glennlives + 1
	if "glenn will live" in line:
		Glennlives = Glennlives + 1
	if "Glenn survives" in line:
		Glennlives = Glennlives + 1
	if "glenn survives" in line: 
		Glennlives = Glennlives + 1
	if "Glenn to live" in line:
		Glennlives = Glennlives + 1
	if "glenn to live" in line:
		Glennlives = Glennlives + 1
		
	#Michonne:
	if "Michonne die" in line:
		Michonnedies = Michonnedies + 1
	if "michonne die" in line:
		Michonnedies = Michonnedies + 1
	if "Michonne to die" in line:
		Michonnedies = Michonnedies + 1
	if "michonne to die" in line:
		Michonnedies = Michonnedies + 1
	if "Michonne will die" in line:
		Michonnedies = Michonnedies + 1
	if "michonne will die" in line:
		Michonnedies = Michonnedies + 1
	if "Michonne WILL die" in line:
		Michonnedies = Michonnedies + 1
	if "michonne WILL die" in line:
		Michonnedies = Michonnedies + 1
	if "Michonne is going to die" in line:
		Michonnedies = Michonnedies + 1
	if "michonne is going to die" in line:
		Michonnedies = Michonnedies + 1		
	if "Michonne is gonna die" in line:
		Michonnedies = Michonnedies + 1
	if "michonne is gonna die" in line:
		Michonnedies = Michonnedies + 1
	if "Michonne dead" in line:
		Michonnedies = Michonnedies + 1
	if "michonne dead" in line:
		Michonnedies = Michonnedies + 1
	if "Michonne killed" in line:
		Michonnedies = Michonnedies + 1
	if "michonne killed" in line:
		Michonnedies = Michonnedies + 1
	if "kills Michonne" in line:
		Michonnedies = Michonnedies + 1
	if "kills michonne" in line:
		Michonnedies = Michonnedies + 1
	if "kill Michonne" in line:
		Michonnedies = Michonnedies + 1
	if "kill michonne" in line:
		Michonnedies = Michonnedies + 1
	if "killed Michonne" in line:
		Michonnedies = Michonnedies + 1
	if "killed michonne" in line:
		Michonnedies = Michonnedies + 1
	if "Michonne will be killed" in line:
		Michonnedies = Michonnedies + 1
	if "michonne will be killed" in line:
		Michonnedies = Michonnedies + 1
	if "Michonne is killed" in line:
		Michonnedies = Michonnedies + 1
	if "michonne is killed" in line:
		Michonnedies = Michonnedies + 1
	if "Michonne lives" in line:
		Michonnelives = Michonnelives + 1
	if "michonne lives" in line: 
		Michonnelives = Michonnelives + 1
	if "Michonne will live" in line:
		Michonnelives = Michonnelives + 1
	if "michonne will live" in line:
		Michonnelives = Michonnelives + 1
	if "Michonne survives" in line:
		Michonnelives = Michonnelives + 1
	if "michonne survives" in line: 
		Michonnelives = Michonnelives + 1
	if "Michonne to live" in line:
		Michonnelives = Michonnelives + 1
	if "michonne to live" in line:
		Michonnelives = Michonnelives + 1
		
	#Sasha:
	if "Sasha die" in line:
		Sashadies = Sashadies + 1
	if "sasha die" in line:
		Sashadies = Sashadies + 1
	if "Sasha to die" in line:
		Sashadies = Sashadies + 1
	if "sasha to die" in line:
		Sashadies = Sashadies + 1
	if "Sasha will die" in line:
		Sashadies = Sashadies + 1
	if "sasha will die" in line:
		Sashadies = Sashadies + 1
	if "Sasha WILL die" in line:
		Sashadies = Sashadies + 1
	if "sasha WILL die" in line:
		Sashadies = Sashadies + 1
	if "Sasha is going to die" in line:
		Sashadies = Sashadies + 1
	if "sasha is going to die" in line:
		Sashadies = Sashadies + 1	
	if "Sasha is gonna die" in line:
		Sashadies = Sashadies + 1
	if "sasha is gonna die" in line:
		Sashadies = Sashadies + 1
	if "Sasha dead" in line:
		Sashadies = Sashadies + 1
	if "sasha dead" in line:
		Sashadies = Sashadies + 1
	if "Sasha killed" in line:
		Sashadies = Sashadies + 1
	if "sasha killed" in line:
		Sashadies = Sashadies + 1
	if "kills Sasha" in line:
		Sashadies = Sashadies + 1
	if "kills sasha" in line:
		Sashadies = Sashadies + 1
	if "kill Sasha" in line:
		Sashadies = Sashadies + 1
	if "kill sasha" in line:
		Sashadies = Sashadies + 1
	if "killed Sasha" in line:
		Sashadies = Sashadies + 1
	if "killed sasha" in line:
		Sashadies = Sashadies + 1
	if "Sasha will be killed" in line:
		Sashadies = Sashadies + 1
	if "sasha will be killed" in line:
		Sashadies = Sashadies + 1
	if "Sasha is killed" in line:
		Sashadies = Sashadies + 1
	if "sasha is killed" in line:
		Sashadies = Sashadies + 1
	if "Sasha lives" in line:
		Sashalives = Sashalives + 1
	if "sasha lives" in line: 
		Sashalives = Sashalives + 1
	if "Sasha will live" in line:
		Sashalives = Sashalives + 1
	if "sasha will live" in line:
		Sashalives = Sashalives + 1
	if "Sasha survives" in line:
		Sashalives = Sashalives + 1
	if "sasha survives" in line: 
		Sashalives = Sashalives + 1
	if "Sasha to live" in line:
		Sashalives = Sashalives + 1
	if "sasha to live" in line:
		Sashalives = Sashalives + 1
		
	#Abraham:
	if "Abraham die" in line:
		Abrahamdies = Abrahamdies + 1
	if "abraham die" in line:
		Abrahamdies = Abrahamdies + 1
	if "Abraham to die" in line:
		Abrahamdies = Abrahamdies + 1
	if "abraham to die" in line:
		Abrahamdies = Abrahamdies + 1
	if "Abraham will die" in line:
		Abrahamdies = Abrahamdies + 1
	if "abraham will die" in line:
		Abrahamdies = Abrahamdies + 1
	if "Abraham WILL die" in line:
		Abrahamdies = Abrahamdies + 1
	if "abraham WILL die" in line:
		Abrahamdies = Abrahamdies + 1
	if "Abraham is going to die" in line:
		Abrahamdies = Abrahamdies + 1
	if "abraham is going to die" in line:
		Abrahamdies = Abrahamdies + 1	
	if "Abraham is gonna die" in line:
		Abrahamdies = Abrahamdies + 1
	if "abraham is gonna die" in line:
		Abrahamdies = Abrahamdies + 1
	if "Abraham dead" in line:
		Abrahamdies = Abrahamdies + 1
	if "abraham dead" in line:
		Abrahamdies = Abrahamdies + 1
	if "Abraham killed" in line:
		Abrahamdies = Abrahamdies + 1
	if "abraham killed" in line:
		Abrahamdies = Abrahamdies + 1
	if "kills Abraham" in line:
		Abrahamdies = Abrahamdies + 1
	if "kills abraham" in line:
		Abrahamdies = Abrahamdies + 1
	if "kill Abraham" in line:
		Abrahamdies = Abrahamdies + 1
	if "kill abraham" in line:
		Abrahamdies = Abrahamdies + 1
	if "killed Abraham" in line:
		Abrahamdies = Abrahamdies + 1
	if "killed abraham" in line:
		Abrahamdies = Abrahamdies + 1
	if "Abraham will be killed" in line:
		Abrahamdies = Abrahamdies + 1
	if "abraham will be killed" in line:
		Abrahamdies = Abrahamdies + 1
	if "Abraham is killed" in line:
		Abrahamdies = Abrahamdies + 1
	if "abraham is killed" in line:
		Abrahamdies = Abrahamdies + 1
	if "Abraham lives" in line:
		Abrahamlives = Abrahamlives + 1
	if "abraham lives" in line: 
		Abrahamlives = Abrahamlives + 1
	if "Abraham will live" in line:
		Abrahamlives = Abrahamlives + 1
	if "abraham will live" in line:
		Abrahamlives = Abrahamlives + 1
	if "Abraham survives" in line:
		Abrahamlives = Abrahamlives + 1
	if "abraham survives" in line: 
		Abrahamlives = Abrahamlives + 1
	if "Abraham to live" in line:
		Abrahamlives = Abrahamlives + 1
	if "abraham to live" in line:
		Abrahamlives = Abrahamlives + 1
		
	#Eugene:
	if "Eugene die" in line:
		Eugenedies = Eugenedies + 1
	if "eugene die" in line:
		Eugenedies = Eugenedies + 1	
	if "Eugene to die" in line:
		Eugenedies = Eugenedies + 1
	if "eugene to die" in line:
		Rickdies = Rickdies + 1
	if "Eugene will die" in line:
		Eugenedies = Eugenedies + 1
	if "eugene will die" in line:
		Eugenedies = Eugenedies + 1
	if "Eugeme WILL die" in line:
		Eugenedies = Eugenedies + 1
	if "eugene WILL die" in line:
		Eugenedies = Eugenedies + 1
	if "Eugene is going to die" in line:
		Eugenedies = Eugenedies + 1
	if "eugene is going to die" in line:
		Eugenedies = Eugenedies + 1	
	if "Eugene is gonna die" in line:
		Eugenedies = Eugenedies + 1
	if "eugene is gonna die" in line:
		Eugenedies = Eugenedies + 1
	if "Eugene dead" in line:
		Eugenedies = Eugenedies + 1
	if "eugene dead" in line:
		Eugenedies = Eugenedies + 1
	if "Eugene killed" in line:
		Eugenedies = Eugenedies + 1
	if "eugene killed" in line:
		Eugenedies = Eugenedies + 1
	if "kills Eugene" in line:
		Eugenedies = Eugenedies + 1
	if "kills eugene" in line:
		Eugenedies = Eugenedies + 1
	if "kill Eugene" in line:
		Eugenedies = Eugenedies + 1
	if "kill eugene" in line:
		Eugenedies = Eugenedies + 1
	if "killed Eugene" in line:
		Eugenedies = Eugenedies + 1
	if "killed eugene" in line:
		Eugenedies = Eugenedies + 1
	if "Eugene will be killed" in line:
		Eugenedies = Eugenedies + 1
	if "eugene will be killed" in line:
		Eugenedies = Eugenedies + 1
	if "Eugene is killed" in line:
		Eugenedies = Eugenedies + 1
	if "eugene is killed" in line:
		Eugenedies = Eugenedies + 1
	if "Eugene lives" in line:
		Eugenelives = Eugenelives + 1
	if "eugene lives" in line: 
		Eugenelives = Eugenelives + 1
	if "Eugene will live" in line:
		Eugenelives = Eugenelives + 1
	if "eugene will live" in line:
		Eugenelives = Eugenelives + 1
	if "Eugene survives" in line:
		Eugenelives = Eugenelives + 1
	if "eugene survives" in line: 
		Eugenelives = Eugenelives + 1
	if "Eugene to live" in line:
		Eugenelives = Eugenelives + 1
	if "eugene to live" in line:
		Eugenelives = Eugenelives + 1
		
	#Rosita:
	if "Rosita die" in line:
		Rositadies = Rositadies + 1
	if "rosita die" in line:
		Rositadies = Rositadies + 1	
	if "Rosita to die" in line:
		Rositadies = Rositadies + 1
	if "rosita to die" in line:
		Rositadies = Rositadies + 1
	if "Rosita will die" in line:
		Rositadies = Rositadies + 1
	if "rosita will die" in line:
		Rositadies = Rositadies + 1
	if "Rosita WILL die" in line:
		Rositadies = Rositadies + 1
	if "rosita WILL die" in line:
		Rositadies = Rositadies + 1
	if "Rosita is going to die" in line:
		Rositadies = Rositadies + 1
	if "rosita is going to die" in line:
		Rositadies = Rositadies + 1	
	if "Rosita is gonna die" in line:
		Rositadies = Rositadies + 1
	if "rosita is gonna die" in line:
		Rositadies = Rositadies + 1
	if "Rosita dead" in line:
		Rositadies = Rositadies + 1
	if "rosita dead" in line:
		Rositadies = Rositadies + 1
	if "Rosita killed" in line:
		Rositadies = Rositadies + 1
	if "rosita killed" in line:
		Rositadies = Rositadies + 1
	if "kills Rosita" in line:
		Rositadies = Rositadies + 1
	if "kills rosita" in line:
		Rositadies = Rositadies + 1
	if "kill Rosita" in line:
		Rositadies = Rositadies + 1
	if "kill rosita" in line:
		Rositadies = Rositadies + 1
	if "killed Rosita" in line:
		Rositadies = Rositadies + 1
	if "killed rosita" in line:
		Rositadies = Rositadies + 1
	if "Rosita will be killed" in line:
		Rositadies = Rositadies + 1
	if "rosita will be killed" in line:
		Rositadies = Rositadies + 1
	if "Rosita is killed" in line:
		Rositadies = Rositadies + 1
	if "rosita is killed" in line:
		Rositadies = Rositadies + 1
	if "Rosita lives" in line:
		Rositalives = Rositalives + 1
	if "rosita lives" in line: 
		Rositalives = Rositalives + 1
	if "Rosita will live" in line:
		Rositalives = Rositalives + 1
	if "rosita will live" in line:
		Rositalives = Rositalives + 1
	if "Rosita survives" in line:
		Rositalives = Rositalives + 1
	if "rosita survives" in line: 
		Rositalives = Rositalives + 1
	if "Rosita to live" in line:
		Rositalives = Rositalives + 1
	if "rosita to live" in line:
		Rositalives = Rositalives + 1
		
	#Aaron:
	if "Aaron die" in line:
		Aarondies = Aarondies + 1
	if "aaron die" in line:
		Aarondies = Aarondies + 1	
	if "Aaron to die" in line:
		Aarondies = Aarondies + 1
	if "aaron to die" in line:
		Aarondies = Aarondies + 1
	if "Aaron will die" in line:
		Aarondies = Aarondies + 1
	if "aaron will die" in line:
		Aarondies = Aarondies + 1
	if "Aaron WILL die" in line:
		Aarondies = Aarondies + 1
	if "aaron WILL die" in line:
		Aarondies = Aarondies + 1
	if "Aaron is going to die" in line:
		Aarondies = Aarondies + 1
	if "aaron is going to die" in line:
		Aarondies = Aarondies + 1	
	if "Aaron is gonna die" in line:
		Aarondies = Aarondies + 1
	if "aaron is gonna die" in line:
		Aarondies = Aarondies + 1
	if "Aaron dead" in line:
		Aarondies = Aarondies + 1
	if "aaron dead" in line:
		Aarondies = Aarondies + 1
	if "Aaron killed" in line:
		Aarondies = Aarondies + 1
	if "aaron killed" in line:
		Aarondies = Aarondies + 1
	if "Aaron will be killed" in line:
		Aarondies = Aarondies + 1
	if "aaron will be killed" in line:
		Aarondies = Aarondies + 1
	if "Aaron is killed" in line:
		Aarondies = Aarondies + 1
	if "aaron is killed" in line:
		Aarondies = Aarondies + 1
	if "kills Aaron" in line:
		Aarondies = Aarondies + 1
	if "kills aaron" in line:
		Aarondies = Aarondies + 1
	if "kill Aaron" in line:
		Aarondies = Aarondies + 1
	if "kill aaron" in line:
		Aarondies = Aarondies + 1
	if "killed Aaron" in line:
		Aarondies = Aarondies + 1
	if "killed aaron" in line:
		Aarondies = Aarondies + 1
	if "Aaron lives" in line:
		Aaronlives = Aaronlives + 1
	if "aaron lives" in line: 
		Aaronlives = Aaronlives + 1
	if "Aaron will live" in line:
		Aaronlives = Aaronlives + 1
	if "aaron will live" in line:
		Aaronlives = Aaronlives + 1
	if "Aaron survives" in line:
		Aaronlives = Aaronlives + 1
	if "aaron survives" in line: 
		Aaronlives = Aaronlives + 1
	if "Aaron to live" in line:
		Aaronlives = Aaronlives + 1
	if "aaron to live" in line:
		Aaronlives = Aaronlives + 1
	
			
	#print(liste)


print("Untersuchte Tweets:", Tweets)
print("Rick: Sterben:", Rickdies, "Leben:", Ricklives)
print("Carl: Sterben:", Carldies, "Leben:", Carllives)
print("Daryl: Sterben:", Daryldies, "Leben:", Daryllives)
print("Maggie: Sterben:", Maggiedies, "Leben:", Maggielives)
print("Glenn: Sterben:", Glenndies, "Leben:", Glennlives)
print("Michonne: Sterben:", Michonnedies, "Leben:", Michonnelives)
print("Sasha: Sterben:", Sashadies, "Leben:", Sashalives)
print("Abraham: Sterben:", Abrahamdies, "Leben:", Abrahamlives)
print("Eugene: Sterben:", Eugenedies, "Leben:", Eugenelives)
print("Rosita: Sterben:", Rositadies, "Leben:", Rositalives)
print("Aaron: Sterben:", Aarondies, "Leben:", Aaronlives)







