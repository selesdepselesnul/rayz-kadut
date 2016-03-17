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
		
	def update(self, coordinat = None):
		if coordinat:
			self.surface.blit(self.image, (coordinat[0], coordinat[1]))
		else:	
			self.surface.blit(self.image, 
				(MainController.RESOLUTION[0]/2 - SnakeSprite.WIDTH,
			 	MainController.RESOLUTION[1] - SnakeSprite.HEIGHT))

def main():
	pygame.init()

	running = True
	resolution = (MainController.RESOLUTION[0], MainController.RESOLUTION[1])
	pygame.display.set_caption('Rayz Kadut')
	
	main_surface = pygame.display.set_mode(resolution)
	main_surface.fill(Color.WHITE)
	snake_sprite = SnakeSprite(main_surface)
	snake_sprite.update()
	
	while running:
		for event in pygame.event.get():
			if event.dict.get('key') == pygame.K_q:
				running = False
				pygame.quit()
				quit()

			# if event.dict.get('key') == pygame.K_RIGHT:
			# 	snake_sprite.update()
		pygame.display.update()			
		
if __name__ == '__main__':
	main()