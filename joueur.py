import pygame
from entitées import Entité


class joueur(Entité):
    def __init__(self, image):
        super().__init__(image, 370, 480)
        self.speed = 5
        self.kill = {"nb_morts":0}

    def deplacer(self, touches, largeur):

        if touches[pygame.K_e]:
            self.x -= self.speed

        if touches[pygame.K_d]:
            self.x += self.speed

        # empêchee le joueur de sortir de l'écran
        limite = largeur - self.image.get_width()
        self.x = max(0, min(self.x, limite))
