import pygame

"""For personal bonus which lets you move around on the display"""
pygame.init()
display = pygame.display.set_mode((500,500))

RUNNING = True


class Personnage:
    def __init__(self, x:int, y:int):
        self.x, self.y = x, y


    """Self explanatory methods (literally in their names)"""
    def Gauche(self):
        self.x -= 1

    def Droite(self):
        self.x += 1

    def Bas(self):
        self.y += 1

    def Haut(self):
        self.y -= 1

    #Draws and returns the position of the character
    def Position(self):
        display.fill((0, 0, 0))
        pygame.draw.rect(display, (50, 255, 50), pygame.Rect(self.x, self.y, 5, 5))
        return (self.x, self.y)
    
    #Defines the character movement
    def Movement(self):
        global RUNNING

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.Haut()

        if keys[pygame.K_DOWN]:
            self.Bas()

        if keys[pygame.K_LEFT]:
            self.Gauche()

        if keys[pygame.K_RIGHT]:
            self.Droite()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False


#Demonstrates the class
personnage = Personnage(0, 0)

#Mainloop used for character movement
while RUNNING:

    personnage.Movement()
    print(personnage.Position())
    pygame.display.update()


