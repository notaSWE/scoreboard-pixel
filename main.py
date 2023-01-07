from scores import Scoreboard
from settings import *
import ctypes, os, pygame, sys

# Maintain resolution regardless of Windows scaling settings
ctypes.windll.user32.SetProcessDPIAware()

class Game:
    def __init__(self):

        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE_STRING)
        self.clock = pygame.time.Clock()
        
        # Background image
        self.bg_image = pygame.image.load(BG_IMAGE_PATH)

        # Create our scoreboard
        self.scoreboard = Scoreboard(0, 0)

    def run(self):
        self.start_time = pygame.time.get_ticks()

        while True:
            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a and self.scoreboard.can_increment:
                        self.scoreboard.p1_score += 1
                        self.scoreboard.increment_time = pygame.time.get_ticks()
                        self.scoreboard.can_increment = False
                    elif event.key == pygame.K_f and self.scoreboard.can_increment:
                        self.scoreboard.p2_score += 1
                        self.scoreboard.increment_time = pygame.time.get_ticks()
                        self.scoreboard.can_increment = False

            # Time variables
            self.start_time = pygame.time.get_ticks()

            # Display
            pygame.display.update()
            self.screen.blit(self.bg_image, (0, 0))
            self.clock.tick(FPS)

            # Game specific updates
            self.scoreboard.update()

if __name__ == '__main__':
    game = Game()
    game.run()