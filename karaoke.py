


class Player: 
    def __init__(self,pseudo,score):
        self.__prénom = pseudo
        self.__score = score 
    def getprénom(self):
        return self.__prénon
    def getscore(self):
        return self.__score 
joueur1 = Player("banana",70/100)
joueur2 = Player("ananas",80/100)
joueur3 = Player("fraise",60/100)
joueur4 = Player("orange",70/100)

#si nouvelle chansson -= ancienne chanson alors pas compter 
#self.__ancienscore
#elf.__nouveauscore -= __ancienscore 
#if 
#ecraser l'ancien  score si il est moins bon que le précédent 

class Karaoke:
    def __init__(self,chansons,numerochansons):
        self.__chanson = chansons 
        self.__numero = numerochansons

        numerochansons = Karaoke(1,2,3,4,5)


