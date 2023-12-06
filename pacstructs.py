import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class SearchNode():
    def __init__(self, location = None, parent = None):
        self.gridloc = location
        self.f = 0
        self.g = 0
        self.parent = parent

class GridCell():
    def __init__(self):
        self.gridloc = [0,0]
        self.pixelloc = [0,0]
        self.traversable = False
        self.coin = False
        

class PacMan(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pacmanright.png").convert()

        self.rect = self.image.get_rect()

        self.coins = 0

        self.gridloc = [0,0]

        self.goal_cell = [9, 15]

        # 'r' = right
        # 'l' = left
        # 'u' = up
        # 'd' = down
        # 'n' = no movement at this time
        self.dir = "n"

    def update(self):

        if self.dir == 'r':
            self.rect.x += 1
        elif self.dir == 'l':
            self.rect.x += -1
        elif self.dir == 'u':
            self.rect.y += -1
        elif self.dir == 'd':
            self.rect.y += 1

        if (self.goal_cell[0] * 32 == self.rect.x) & (self.goal_cell[1] * 32 == self.rect.y):
            self.dir = 'n'

            self.gridloc = self.goal_cell

    def draw(self, screen):
        if self.dir == 'r': # moving right
            self.image = pygame.image.load("pacmanright.png").convert()
        elif self.dir == 'l': # moving left
            self.image = pygame.image.load("pacmanleft.png").convert()
        elif self.dir == 'd': # moving down
            self.image = pygame.image.load("pacmandown.png").convert()
        elif self.dir == 'u': # moving up
            self.image = pygame.image.load("pacmanup.png").convert()
        screen.blit(self.image, [self.rect.x, self.rect.y])
        

class Ghost(pygame.sprite.Sprite):

    def __init__(self, color):
        super().__init__()
        if color == "orange":
            self.image = pygame.image.load("OrangeGhost.png").convert()
            self.image.set_colorkey(WHITE)
        elif color == "red":
            self.image = pygame.image.load("RedGhost.png").convert()
            self.image.set_colorkey(WHITE)
        elif color == "green":
            self.image = pygame.image.load("GreenGhost.png").convert()
            self.image.set_colorkey(WHITE)
            
        self.rect = self.image.get_rect()

        self.gridloc = [0,0]

        self.goal_cell = [9, 15]

        # used to define current direction of the Ghost.
        # 'r' = right
        # 'l' = left
        # 'u' = up
        # 'd' = down
        # 'n' = no movement at this time
        self.dir = "n"


    def update(self):
        if self.dir == 'r':
            self.rect.x += 1
        elif self.dir == 'l':
            self.rect.x += -1
        elif self.dir == 'u':
            self.rect.y += -1
        elif self.dir == 'd':
            self.rect.y += 1

        if (self.goal_cell[0] * 32 == self.rect.x) & (self.goal_cell[1] * 32 == self.rect.y):
            self.dir = 'n'

            self.gridloc = self.goal_cell
            
    def draw(self, screen):
        screen.blit(self.image, [self.rect.x, self.rect.y])      
