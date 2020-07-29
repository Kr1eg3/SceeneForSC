import pygame, sys
from pygame.locals import *
from math import *
from numpy import *


pygame.init()


class Main:
    """Класс, который будет выступать в качестве стартового экрана, на котором будут расположены гексы
     с условными районами с транспортными графами
    """
    def __init__(self, width=1028, heigh=772):
        """Конструктор

        Arguments:
            width  {int} -- ширина экрана
            height {int} -- высота экрана
        """
        self.width     = width
        self.heigh     = heigh
        self.pygame    = pygame
        self.sys       = sys
        self.game      = True
        self.show      = True
        self.clock     = self.pygame.time.Clock()
        self.FPS       = 5
          
        self.menu_back  = self.pygame.image.load('./Images/Background_second.png')
        self.background = self.pygame.Surface((100, 100))
        self.screen     = self.pygame.display.set_mode((self.width, self.heigh))

        """Создание текста:
            f1 -- создает шрифт для заголовка 
            f2 -- создает шрифт для подписи блока с информацией 
            f3 -- создает шрифт для работы в блоке
        """
        self.f1 = pygame.font.Font('./Fonts/ISOCT2.ttf' , 28)
        self.f2 = pygame.font.Font('./Fonts/ISOCT2.ttf' , 20)
        self.f3 = pygame.font.Font('./Fonts/ISOCT2.ttf' , 18)

        """Так как текст заголовка и подписи блока с информацией статичен, то объявлен в __init__()
        """
        #Текст заголовка
        self.text1 = self.f1.render('Smart city project', 1, (0, 0, 0))
        self.f1.set_bold(True)
        
        #Текст в блоке
        self.text2 = self.f2.render('Information', 1, (0, 0, 0))
        self.f2.set_bold(True)


    def DrawBackg(self):
        """Отображение бека
        """
        self.screen.blit(self.menu_back, (0, 0))


    def StaticText(self):
        """Отображение статического текста
        """
        self.screen.blit(self.text1, (200, 10))
        self.screen.blit(self.text2, (800, 50))


    def InfoBlockText(self):
        """Метод для создания текста в блоке с информацией
        Новую строку текста смещать по оси y на 20-30 
        """
        self.b = random.randint(0, 100)
        self.blocktext1 = self.f3.render('Sometext = ' + str(self.b), 1, (0, 0, 0))
        self.f3.set_bold(True)
        self.screen.blit(self.blocktext1, (790, 120))
        

    def Terminate(self):
        self.pygame.quit()
        self.sys.exit()
    

    def Update(self):
        self.pygame.display.update()


    def Hex_creator(self):
        """in progress
        """
        self.hex = Hex()
    

    def Run(self):
        """Метод, который отрисовывает экран
        """
        self.pygame.display.set_caption('MainSceene')

        while self.show:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.Terminate()

            """Алгоритм работы сцены с гексами

            -- Отрисовать бек
            -- Отрисовать статический текст
            -- Заполнить информациооный блок

            """
            self.DrawBackg()
            self.StaticText()
            self.InfoBlockText()
            self.clock.tick(self.FPS) 
            self.Update()
            



class Hex(pygame.sprite.Sprite):
    """Класс, который должен отрисовывать гексы с которыми можно взаимодействовать -- in progress
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        #self.rect.centerx = self.width / 2
        #self.rect.bottom  = self.height - 10
    

    def drawhex(self):
        pass


"""Далее идёт код, который я использовал в качестве второй сцены на которую нужно перейти из меню
Начало - 138 строка
Конец  - 191 строка

Func   - 197 строка
Main   - 234 строка
"""

FPS = 30
WIDTH = 1028
HEIGHT = 772
RANDOM = random.randint(0, HEIGHT)

#             R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)



def main():
	global FPSCLOCK, DISPLAYSURF


	"""pygame.init() - необходимая конструкция, вводить каждый раз
    """
	pygame.init()

	"""DISPLAYSURF.fill() - заполнение фона цветом
    """
	DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT)) 
	pygame.display.set_caption('Gospodi spasi')

	"""Рисуем объекты 
    """
	squre = pygame.Surface((40, 40))
	squre.fill((CYAN))
	
	screen = pygame.Surface((WIDTH, HEIGHT))

	"""Main game loop 
    """
	while True:  
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			

		screen.fill(WHITE)
		screen.blit(squre, (0, 0))
		DISPLAYSURF.blit(screen, (0, 0))
		pygame.display.flip()
		#pygame.display.update()


def Switcher(x):
    if x == True:
        x = False
    elif x == False:
        x = True
    return x


def change_sceene():  # TODO 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Switcher(b)
                    print(Switcher(b))
            
        while b == True:
            go.Run() 
        else: 
            main()
        pygame.display.update()
        pygame.display.flip()
        print(Switcher(b))    


""" 
_____Main_________

"""
"""all_sprites = pygame.sprite.Group()
hex1 = Hex()
all_sprites.add(hex1)"""

go = Main()
b = True 

if __name__ == '__main__':       
    change_sceene()


