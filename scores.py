from pixels import *
from settings import *
import pygame

class Scoreboard():
    def __init__(self, p1_score, p2_score):
        self.display_surface = pygame.display.get_surface()
        self.p1_score, self.p2_score = int(p1_score), int(p2_score)
        self.off_surf = pygame.image.load(OFF_IMG).convert_alpha()
        self.p1_surf = pygame.image.load(P1_IMG).convert_alpha()
        self.p2_surf = pygame.image.load(P2_IMG).convert_alpha()
        self.can_increment = True
        self.increment_time = None
        self.game_over = False
        self.game_over_time = None
        self.winner = None

    def check_for_winner(self):
        if self.p1_score == 10:
            self.winner = "p1"
            self.game_over = True
            self.game_over_time = pygame.time.get_ticks()
        elif self.p2_score == 10:
            self.winner = "p2"
            self.game_over = True
            self.game_over_time = pygame.time.get_ticks()

    def cooldowns(self):
        curr_time = pygame.time.get_ticks()

        if not self.can_increment:
            if curr_time - self.increment_time > 100:
                self.can_increment = True

        if self.game_over:
            if curr_time - self.game_over_time > 1000:
                # Reset scoreboard
                self.p1_score, self.p2_score = 0, 0
                self.can_increment = True
                self.increment_time = None
                self.game_over = False
                self.game_over_time = None
                self.winner = None

    def draw_p1(self):
        if not self.winner:
            x, y = 0, 0
            for pix in led_numbers[self.p1_score]:
                if x > 930:
                    x = 0
                    y += 30
                if pix == 1:
                    off_rect = self.off_surf.get_rect(topleft = (x, y))
                    self.display_surface.blit(self.off_surf, off_rect)
                    x += 30
                elif pix == 2:
                    p1_rect = self.p1_surf.get_rect(topleft = (x, y))
                    self.display_surface.blit(self.p1_surf, p1_rect)
                    x += 30

        # Draw blue (p1) win screen
        elif self.winner and self.winner == "p1":
            x, y = 0, 0
            for pix in led_wins[self.winner]:
                if x > 1890:
                    x = 0
                    y += 30
                if pix == 1:
                    off_rect = self.off_surf.get_rect(topleft = (x, y))
                    self.display_surface.blit(self.off_surf, off_rect)
                    x += 30
                elif pix == 2:
                    p1_rect = self.p1_surf.get_rect(topleft = (x, y))
                    self.display_surface.blit(self.p1_surf, p1_rect)
                    x += 30

    def draw_p2(self):
        if not self.winner:
            x, y = 960, 0
            for pix in led_numbers[self.p2_score]:
                if x > 1890:
                    x = 960
                    y += 30
                if pix == 1:
                    off_rect = self.off_surf.get_rect(topleft = (x, y))
                    self.display_surface.blit(self.off_surf, off_rect)
                    x += 30
                elif pix == 2:
                    p2_rect = self.p2_surf.get_rect(topleft = (x, y))
                    self.display_surface.blit(self.p2_surf, p2_rect)
                    x += 30

        # Draw blue (p2) win screen
        elif self.winner and self.winner == "p2":
            x, y = 0, 0
            for pix in led_wins[self.winner]:
                if x > 1890:
                    x = 0
                    y += 30
                if pix == 1:
                    off_rect = self.off_surf.get_rect(topleft = (x, y))
                    self.display_surface.blit(self.off_surf, off_rect)
                    x += 30
                elif pix == 3:
                    p2_rect = self.p2_surf.get_rect(topleft = (x, y))
                    self.display_surface.blit(self.p2_surf, p2_rect)
                    x += 30
            x, y = 0, 0

    def update(self):
        self.check_for_winner()
        self.cooldowns()
        self.draw_p1()
        self.draw_p2()