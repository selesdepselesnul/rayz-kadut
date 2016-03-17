import pygame

class Color:

	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)

class SnakeSprite(pygame.sprite.Sprite):

	"""docstring for SnakeSprite"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('snake.png')
		self.rect = self.image.get_rect()
		
	def update(self, source):
		source.blit(self.image, (20, 20))



def main():
	pygame.init()


	running = True
	resolution = (600, 400)
	pygame.display.set_caption('Rayz Kadut')
	
	main_surface = pygame.display.set_mode(resolution)
	main_surface.fill(Color.WHITE)
	snake_sprite = SnakeSprite()
	snake_sprite.update(main_surface)
	
	while running:
		for event in pygame.event.get():
			if event.dict.get('key') == pygame.K_q:
				running = False
				pygame.quit()
				quit()
		pygame.display.update()			
		
if __name__ == '__main__':
	main()