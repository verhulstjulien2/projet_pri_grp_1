from entitées import Entité

class balle(Entité):
    def __init__(self, image):
        super().__init__(image, 0, 480)

        self.speed = 10
        self.active = False

    def tirer(self, x, y):

        # empeche de tirer si une balle est active
        if self.active:
            return False

        self.x = x
        self.y = y
        self.active = True

        return True

    def deplacer(self):

        if not self.active:
            return

        self.y -= self.speed

        # La balle a quitté l'écran
        if self.y <= 0:
            self.reset()

    def reset(self):
        self.active = False
        self.y = 480

    def afficher(self, screen):

        if self.active:
            screen.blit(
                self.image,
                (self.x + 16, self.y + 10)
            )
