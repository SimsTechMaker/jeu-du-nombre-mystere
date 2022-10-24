from kivy.properties import StringProperty

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

from kivy.app import App
from random import randint


Config.set('graphics', 'resizable', '0')
 
# fix the width of the window
Config.set('graphics', 'width', '430')
# fix the height of the window
Config.set('graphics', 'height', '932')
# le Backend
VALISTRUE = "Bien joue c'est la bonne réponse"
VALISFALSE = "Mauvaise réponse"

def texte(bool=True):
    if bool: return VALISFALSE + " vous êtes trop hauts"
    else: return VALISFALSE+ " vous êtes trop bas"
    
def nombr_m():
    global dico
    dico = {"nombr": randint(0,100)}
nombr_m()
def verif(val):
    if val == dico["nombr"]: 
        print(2)  
        return 2
    elif val < dico["nombr"]:
        print(0) 
        return 0
    elif val > dico["nombr"]:
        print(1) 
        return 1

class GameLaout(BoxLayout):
    mon_texte = StringProperty("Bonjour le monde")
    def clic_bn(self):
        nombr_m()
        #self.mon_texte = f" le nombre mys est {dico['nombr']}"
    def ver(self,info):
        vla = int(info.text)
        ver = verif(vla)
        if ver ==2:
            a=1
            self.mon_texte= VALISTRUE
        elif ver ==0:
            self.mon_texte= texte(False)
        elif ver ==1: 
            self.mon_texte= texte()
        
   
class MainLaout(BoxLayout):
    pass
 

#mes test




class NombreMysApp(App):
    pass





NombreMysApp().run()