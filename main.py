
import pygame
from pathlib import Path
from game import Game


def main():
    #initialisation
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Invader")

    chemin = Path(__file__).resolve().parent
    icon = pygame.image.load(
        str(chemin / "assets" / "ufo.png")
    )

    pygame.display.set_icon(icon)

    # Création du jeu
    game = Game(screen)

    # timer
    clock = pygame.time.Clock()

    running = True
    while running:

        # Événements
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            else:
                game.gerer_evenement(event)

        # Actualiser le jeu
        game.update()

        # Afficher le jeu
        game.afficher()

        pygame.display.update()

        # Limiter à 60 images par seconde
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
