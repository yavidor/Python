import pygame

__author__ = "yavidor"


def main():
    pygame.init()
    # consts
    width, height = 500, 500
    x, y = width / 2, height / 2
    fps = 60
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    size = (width, height)
    screen = pygame.display.set_mode(size)
    sprite = pygame.image.load('slime1.png').convert()
    sprite.set_colorkey((255, 0, 0))
    pygame.display.set_caption("Game")
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y -= 10
                if event.key == pygame.K_s:
                    y += 10
                if event.key == pygame.K_a:
                    x -= 10
                if event.key == pygame.K_d:
                    x += 10
        screen.fill((255, 255, 255))
        screen.blit(sprite, (x, y))
        pygame.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    main()
