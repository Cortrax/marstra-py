import pygame


class Player1:
    def __init__(self, screen, player, x, y, step, dt):
        self.screen = screen
        self.player = pygame.image.load(player)
        self.x = x
        self.y = y
        self.player_rect = self.player.get_rect(center=(self.x, self.y))
        self.step = step
        self.dt = dt

    def update(self):
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_d]:
            self.x += self.step * self.dt
        if key_input[pygame.K_a]:
            self.x -= self.step * self.dt
        if key_input[pygame.K_w]:
            self.y -= self.step * self.dt
        if key_input[pygame.K_s]:
            self.y += self.step * self.dt

        self.player_rect = self.player.get_rect(center=(self.x, self.y))
        self.screen.blit(self.player, (self.x, self.y))

    def bullet_collision(self, bullet_group_right, right_health):
        for bullet in bullet_group_right:
            if self.player_rect.colliderect(bullet):
                return True

    def wall_collision(self):
        if self.x <= 0:
            self.x += self.step
        if self.x >= 260:
            self.x -= self.step
        if self.y >= 660:
            self.y -= self.step
        if self.y <= 0:
            self.y += self.step

    def returnX(self):
        return self.x + 32

    def returnY(self):
        return self.y + 22
