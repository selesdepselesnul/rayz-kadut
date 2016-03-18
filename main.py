import pygame

class MainController:
	RESOLUTION = (600, 400)


class Color:

	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)

class SnakeSprite(pygame.sprite.Sprite):

	WIDTH = 20
	HEIGHT = 60

	def __init__(self, surface):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('snake.png')
		self.rect = self.image.get_rect()
		self.surface = surface
		self.DEFAULT_X = MainController.RESOLUTION[0]/2 - SnakeSprite.WIDTH
		self.DEFAULT_Y = MainController.RESOLUTION[1] - SnakeSprite.HEIGHT
		
	def update(self, coordinat = None):
		if coordinat:
			self.surface.blit(self.image, (coordinat[0], coordinat[1]))
		else:	
			self.surface.blit(self.image, 
				(self.DEFAULT_X,self.DEFAULT_Y))

def main():
	pygame.init()

	x_move = 0
	clock = pygame.time.Clock()
	resolution = (MainController.RESOLUTION[0], MainController.RESOLUTION[1])
	pygame.display.set_caption('Rayz Kadut')
	
	main_surface = pygame.display.set_mode(resolution)
	main_surface.fill(Color.WHITE)
	snake_sprite = SnakeSprite(main_surface)
	snake_sprite.update()
	x = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()


		clock.tick(30)
		pygame.display.update()			
		
if __name__ == '__main__':
	main()