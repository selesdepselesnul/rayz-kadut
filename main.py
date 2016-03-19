import pygame
import random
from string import Template

class MainController:
	RESOLUTION = (600, 540)


class Color:

	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)

class GradeSprite(pygame.sprite.Sprite):

	def __init__(self, image_url, val):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_url)
		self.rect = self.image.get_rect()
		self._gen_rand_coord()
		self.val = val
		self.image_url = image_url

	def _gen_rand_coord(self):
		self.rect.x = random.randint(0, MainController.RESOLUTION[0] - 30)
		self.rect.y = random.randint(-100, -15)

	def update(self, surface, y):
		if self.rect.y  > MainController.RESOLUTION[1]:
			self._gen_rand_coord()
		else:
			self.rect.y += y	
		surface.blit(self.image, (self.rect.x, self.rect.y))

class StudentSprite(pygame.sprite.Sprite):
	
	def __init__(self, surface, coordinat):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('image/student.png')
		self.rect = self.image.get_rect()
		self.surface = surface
		self.rect.x = coordinat[0]
		self.rect.y = coordinat[1]

	def update(self, grades_sprite_group):
		self.rect.y -= 5
		self.surface.blit(self.image, (self.rect.x, self.rect.y))
		coll_grade_group = pygame.sprite.spritecollide(
			self, grades_sprite_group, True)
		for coll_grade in coll_grade_group:
			grades_sprite_group.add(GradeSprite(coll_grade.image_url, coll_grade.val))


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
		
	def update(self, coordinat, grades_sprite_group):
		self.rect.x = coordinat[0]
		self.rect.y = coordinat[1]	
		self.surface.blit(self.image, (coordinat[0], coordinat[1]))
		coll_grade_group = pygame.sprite.spritecollide(
			self, grades_sprite_group, True)
		for coll_grade in coll_grade_group:
			grades_sprite_group.add(GradeSprite(coll_grade.image_url, coll_grade.val))
		
def main():
	pygame.init()

	move = 0
	clock = pygame.time.Clock()
	resolution = (MainController.RESOLUTION[0], MainController.RESOLUTION[1])
	pygame.display.set_caption('Rayz Kadut')
	
	main_surface = pygame.display.set_mode(resolution)
	snake_sprite = SnakeSprite(main_surface)
	
	grades_sprite_group = pygame.sprite.Group(
		GradeSprite('image/grade_a.png', 'a'), 
		GradeSprite('image/grade_b.png', 'b'),
		GradeSprite('image/grade_c.png', 'c'),
		GradeSprite('image/grade_d.png', 'd'),
		GradeSprite('image/grade_e.png', 'e'))
	
	student_group_sprite = pygame.sprite.Group()
	
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
				if event.key == pygame.K_SPACE:
					student_group_sprite.add(
						StudentSprite(main_surface, 
							(snake_sprite.rect.x, snake_sprite.rect.y - 60)))


			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					move = 0 	
		

		clock.tick(30)
		main_surface.fill(Color.WHITE)
		snake_sprite.update(
			(snake_sprite.rect.x + move, snake_sprite.rect.y), grades_sprite_group)
		grades_sprite_group.update(main_surface, 5)
		student_group_sprite.update(grades_sprite_group)
		pygame.display.update()			
		
if __name__ == '__main__':
	main()