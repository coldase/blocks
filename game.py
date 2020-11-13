import pygame
import random

pygame.init()
pygame.font.init()

screen_width, screen_height = 800, 600
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
troll_img = pygame.image.load("trollface.png")
troll_img = pygame.transform.scale(troll_img, (70, 70))


FPS = 60

#colors
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

class Player:
	def __init__(self):
		self.size_x = 150
		self.size_y = 20
		self.pos_x = int(screen_width/2) - int(self.size_x/2)
		self.pos_y = int(screen_height-self.size_y - 20)
		self.color = RED
		self.movement_speed = 5
		self.points = 0

	def draw_player(self):
		pygame.draw.rect(screen, self.color, (self.pos_x, self.pos_y, self.size_x, self.size_y))

	def get_rect(self):
		return pygame.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y)

	def keypresses(self):
		
		if keys[pygame.K_LEFT] and self.pos_x > 0:
			self.pos_x -= self.movement_speed
		if keys[pygame.K_RIGHT] and self.pos_x < screen_width - self.size_x:
			self.pos_x += self.movement_speed		
		if keys[pygame.K_q]:
			global run
			run = False

	def draw_score(self):
		text = myfont.render(str(self.points), False, RED)
		screen.blit(text, (50,50))


class Food:
	def __init__(self):
		self.size = 50
		self.drop_speed = 1
		self.pos_x = int(screen_width/2)
		self.pos_y = -100

	def draw_food(self):
		if self.pos_y >= 0 and self.pos_y < screen_height:
			self.pos_y += self.drop_speed
			screen.blit(troll_img, (self.pos_x, self.pos_y))
			#pygame.draw.rect(screen, BLUE, (self.pos_x, self.pos_y, self.size, self.size))
		else:
			self.pos_y = 0

	def get_rect(self):
		return pygame.Rect(self.pos_x, self.pos_y, self.size, self.size)

	def new_food(self):
		self.pos_x = int(random.randint(0,screen_width - self.size))
		self.pos_y = int(random.randint(0,screen_height - self.size))

	def check_collision(self, player):
		if player.get_rect().colliderect(self.get_rect()):
			self.pos_y = 0 - self.size
			self.pos_x = random.randint(0, screen_width - self.size)
			player.points += 1
			self.drop_speed += 1
			print(player.points)
			player_1.movement_speed += 1

myfont = pygame.font.SysFont("Calibri", 50)
clock = pygame.time.Clock()
player_1 = Player()
food = Food()

run = True
while run:


	clock.tick(FPS)
	keys = pygame.key.get_pressed()		
		

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	screen.fill(BLACK)

	food.draw_food()
	food.check_collision(player_1)
	player_1.keypresses()
	player_1.draw_player()
	player_1.draw_score()
	pygame.display.flip()
pygame.quit()