import random
from entitées import Entité


class ennemy(Entité):
    def __init__(self, image, x, y, speed):
        super().__init__(image, x, y)

        self.speed = speed
        self.descente = 40

    def deplacer(self, largeur):
        self.x += self.speed

        limite = largeur - self.image.get_width()

        if self.x <= 0:
            self.x = 0
            self.speed *= -1
            self.y += self.descente

        elif self.x >= limite:
            self.x = limite
            self.speed *= -1
            self.y += self.descente

    def reapparaitre(self, largeur, image_1, image_2):

        val = random.randint(0, 11)

        if val < 9:
            self.image = image_1
            self.speed = 4

        else:
            self.image = image_2
            self.speed = 6

        self.x = random.randint(
            0, largeur - self.image.get_width()
        )

        self.y = random.randint(50, 150)


