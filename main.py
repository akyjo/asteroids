import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    cl = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # af = AsteroidField()
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for o in updatable:
            o.update(dt)

        for a in asteroids:
            if a.collides(p):
                sys.exit("Game over!")
            for bullet in shots:
                if bullet.collides(a):
                    a.kill()
                    bullet.kill()

        for o in drawable:
            o.draw(screen)

        pygame.display.flip()
        dt = cl.tick(60) / 1000


if __name__ == "__main__":
    main()
