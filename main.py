import pygame

class MainController:
	RESOLUTION = (600, 540)


class Color:

	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)

class GradeSprite(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('snake.png')
		self.rect = self.image.get_rect()
		self.surface = surface
		self.rect.x = MainController.RESOLUTION[0]/2 - SnakeSprite.WIDTH
		self.rect.y = MainController.RESOLUTION[1] - SnakeSprite.HEIGHT
class SnakeSprite(pygame.sprite.Sprite):

	WIDTH = 30
	HEIGHT = 60

	def __init__(self, surface):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('image/snake.png')
		self.rect = self.image.get_rect()
		self.surface = surface
		self.rect.x = MainController.RESOLUTION[0]/2 - SnakeSprite.WIDTH
		self.rect.y = MainController.RESOLUTION[1] - SnakeSprite.HEIGHT
		
	def update(self, coordinat):
		self.surface.fill(Color.WHITE)
		self.rect.x = coordinat[0]
		self.rect.y = coordinat[1]	
		self.surface.blit(self.image, (coordinat[0], coordinat[1]))
		
def main():
	pygame.init()

	move = 0
	clock = pygame.time.Clock()
	resolution = (MainController.RESOLUTION[0], MainController.RESOLUTION[1])
	pygame.display.set_caption('Rayz Kadut')
	
	main_surface = pygame.display.set_mode(resolution)
	snake_sprite = SnakeSprite(main_surface)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()
				if event.key == pygame.K_RIGHT:
					move = 5
				if event.key == pygame.K_LEFT:
					move = -5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					move = 0 	

		clock.tick(30)
		snake_sprite.update(
			(snake_sprite.rect.x + move, snake_sprite.rect.y))
		pygame.display.update()			
		
if __name__ == '__main__':
	main()