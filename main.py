import pygame

def main():
	pygame.init()

	running = True
	resolution = (600, 400)
	pygame.display.set_caption('Rayz Kadut')
	main_surface = pygame.display.set_mode(resolution)

	while running:
		for event in pygame.event.get():
			if event.dict.get('key') == pygame.K_q:
				running = False
				pygame.quit()
				quit()
	
if __name__ == '__main__':
	main()