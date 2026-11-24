
import pygame
import random
import math

from pathlib import Path
from joueur import joueur
from ennemy import ennemy
from balle import balle


ASSETS = Path(__file__).resolve().parent / "assets"


class Game:
    def __init__(self, screen):

        self.screen = screen
        self.largeur, self.hauteur = screen.get_size()

        # images
        self.background = pygame.image.load(
            str(ASSETS / "background.png")
        ).convert()

        image_joueur = pygame.image.load(
            str(ASSETS / "player.png")
        ).convert_alpha()

        self.image_ennemi_1 = pygame.image.load(
            str(ASSETS / "enemy.png")
        ).convert_alpha()

        self.image_ennemi_2 = pygame.image.load(
            str(ASSETS / "img.png")
        ).convert_alpha()

        image_balle = pygame.image.load(
            str(ASSETS / "bullet.png")
        ).convert_alpha()

        # joueur
        self.joueur = joueur(image_joueur)

        # ennemis
        self.ennemis = []

        for i in range(6):

            val = random.randint(0, 11)

            if val < 9:
                image = self.image_ennemi_1
                speed = 4
            else:
                image = self.image_ennemi_2
                speed = 6

            x = random.randint(
                0, self.largeur - image.get_width()
            )
            y = random.randint(50, 150)

            ennemi = ennemy(image, x, y, speed)

            self.ennemis.append(ennemi)

        # balle
        self.balle = balle(image_balle)
        self.balle2 = balle(image_balle)

        # Score et état de la partie
        self.score = 0
        self.game_over = False

        # polices
        self.font = pygame.font.Font(None, 32)
        self.over_font = pygame.font.Font(None, 64)

        # bruits
        self.son_tir = pygame.mixer.Sound(
            str(ASSETS / "laser.wav")
        )

        self.son_explosion = pygame.mixer.Sound(
            str(ASSETS / "explosion.wav")
        )

        pygame.mixer.music.load(
            str(ASSETS / "background.wav")
        )

        pygame.mixer.music.play(-1)

    # événements
    def gerer_evenement(self, event):

        if self.game_over:
            return

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s:
                if (self.joueur.kill["nb_morts"] % 3) == 0 and self.joueur.kill["nb_morts"] > 0:
                    tir_1 = self.balle.tirer(
                        self.joueur.x,
                        self.joueur.y
                    )
                    tir_2 = self.balle2.tirer(
                        self.joueur.x +20,
                        self.joueur.y
                    )
                    if tir_1 or tir_2:
                        self.son_tir.play()
                    self.joueur.kill["nb_morts"] = 0
                else:
                    tir_effectue = self.balle.tirer(
                        self.joueur.x,
                        self.joueur.y
                    )
                    if tir_effectue:
                        self.son_tir.play()

    # check des collisions
    def collision(self, ennemi):
        for projectile in (self.balle, self.balle2):
            if not projectile.active:
                continue
            distance = math.hypot(
                ennemi.x - projectile.x,
                ennemi.y - projectile.y
            )
            if distance < 27:
                return projectile
        return None
    # mise à jour du jeu
    def update(self):
        if self.game_over:
            return

        # déplacement du joueur
        touches = pygame.key.get_pressed()
        self.joueur.deplacer(touches, self.largeur)

        # déplacement des ennemis
        for ennemi in self.ennemis:

            ennemi.deplacer(self.largeur)

            # Game Over
            if ennemi.y > 440:
                self.game_over = True
                return

            # Collision entre balle et ennemi
            projectile = self.collision(ennemi)

            if projectile is not None:

                self.son_explosion.play()

                self.score += 1
                self.joueur.kill["nb_morts"] += 1

                # Réinitialiser la balle qui a touché
                projectile.reset()

                # Faire réapparaître un ennemi aléatoire
                ennemi.reapparaitre(self.largeur,self.image_ennemi_1,self.image_ennemi_2)

        # déplacement du projectile
        self.balle.deplacer()
        self.balle2.deplacer()

    # affichage
    def afficher(self):

        # Fond
        self.screen.blit(self.background, (0, 0))

        if not self.game_over:

            # ennemy
            for ennemi in self.ennemis:
                ennemi.afficher(self.screen)

            # Projectile
            self.balle.afficher(self.screen)
            self.balle2.afficher(self.screen)

        # joueur
        self.joueur.afficher(self.screen)

        # score
        texte_score = self.font.render(
            "Score : " + str(self.score),
            True,
            (255, 255, 255)
        )

        self.screen.blit(texte_score, (10, 10))

        # game Over
        if self.game_over:

            texte_fin = self.over_font.render(
                "GAME OVER",
                True,
                (255, 255, 255)
            )

            self.screen.blit(texte_fin, (200, 250))
