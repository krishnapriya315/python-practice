# ********************************

class animal:
    def eat(self):
        print('animal eat')

class Walker():
    def walkes(self):
        print('walk')

class Dog(animal,Walker): 
    def bark(self):
        print('Bark')


dog=Dog()
dog.eat()
dog.bark()
dog.walkes()

# ******************************

class camera:
    def Takephoto(self):
        print('capturing photo')

class call:
    def Makecall(self):
        print('calling friend')

class Smartphone:
    def Internet(self):
        print('browsing internet')

# smartphone=Smartphone()
# smartphone.Internet()
# smartphone.Makecall() 
# smartphone.Takephoto()


# ********************

class Mediaplayer:
    def play_video(self):
        print('playing video')

class Internetdivice:
    def connect_wifi(self):
        print('connected to wifi')

class Smartv(Mediaplayer,Internetdivice):
    def change_chanel(self):
        print('changing tv chaneel')

smartv=Smartv()
smartv.change_chanel()
smartv.connect_wifi()
smartv.play_video()


