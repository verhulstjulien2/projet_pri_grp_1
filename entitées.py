class Entité:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    def afficher(self, screen):
        screen.blit(self.image, (self.x, self.y))
