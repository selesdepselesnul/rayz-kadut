import pygame
import random
import sqlite3
import os.path
import sys
import os
'''
author : Moch Deden
github : https://github.com/selesdepselesnul
site   : http://selesdepselesnul.com
'''

class MainController:
    RESOLUTION = (640, 417)


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

    def update(self, grades_sprite_group, snake_sprite):
        self.rect.y -= 5
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
        coll_grade_group = pygame.sprite.spritecollide(
            self, grades_sprite_group, True)
        for coll_grade in coll_grade_group:
            if coll_grade.val == 'a':
                snake_sprite.current_score -= 100
                snake_sprite.health -= 4
            elif coll_grade.val == 'b':
                snake_sprite.current_score -= 10
            elif coll_grade.val == 'c':
                snake_sprite.current_score += 10
            elif coll_grade.val == 'd':
                snake_sprite.current_score += 50
            else:
                snake_sprite.current_score += 100

            grades_sprite_group.add(GradeSprite(
                coll_grade.image_url, coll_grade.val))


class SnakeSprite(pygame.sprite.Sprite):

    WIDTH = 30
    HEIGHT = 60
    current_score = 0
    health = 100

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
            if coll_grade.val == 'a':
                self.current_score += 1000
            elif coll_grade.val == 'b':
                self.current_score += 100
            elif coll_grade.val == 'c':
                self.health -= 5
            elif coll_grade.val == 'd':
                self.health -= 10
            else:
                self.health -= 100  
            grades_sprite_group.add(GradeSprite(coll_grade.image_url, coll_grade.val))
        
def make_font_surface(content, size, color):
    return pygame.font.Font(
        pygame.font.get_default_font(), size).render(
            content, True, color)

def _clear():
    if sys.platform.startswith('linux'):
        os.system('clear')
    else:
        os.system('cls')

def main():


    if not os.path.exists('cucok.db'):
        conn = sqlite3.connect('cucok.db')
        cursor = conn.cursor()        
        cursor.execute('CREATE TABLE Player ( name TEXT, score BIGINT)')
    else:
        _clear()
        conn = sqlite3.connect('cucok.db')
        cursor = conn.cursor()
        print('Current Top 10\n\n')
        for player in cursor.execute('SELECT * FROM Player ORDER BY score DESC LIMIT 10'):
            print(player)
        print('\nWanna be next ?')  
    player_name = input('\nwhat is your name ? ')
    pygame.init()
    speed = 5

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
    game_over_surface = pygame.image.load('image/game_over.jpg')
    is_alive = True
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    _clear()
                    print('Good bye {}!'.format(player_name))
                    quit()
                if event.key == pygame.K_RIGHT:
                    move = 5
                if event.key == pygame.K_LEFT:
                    move = -5
                if event.key == pygame.K_SPACE:
                    student_group_sprite.add(
                        StudentSprite(main_surface, 
                            (snake_sprite.rect.x, snake_sprite.rect.y - 60)))
                if event.key == pygame.K_r:
                    main()

          
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    move = 0    
        
   
        if snake_sprite.rect.x >= MainController.RESOLUTION[0] - snake_sprite.WIDTH + 2:
            snake_sprite.rect.x = snake_sprite.rect.x - 6
        elif snake_sprite.rect.x <=  2:
            snake_sprite.rect.x = 3
        if is_alive:
            main_surface.fill(Color.WHITE)
            score_surface = pygame.font.Font(
                pygame.font.get_default_font(), 20).render(
                'Raynizm : ' + str(snake_sprite.current_score), True, (0, 0, 0))
            health_surface = pygame.font.Font(
                pygame.font.get_default_font(), 20).render(
                'Health     : ' + str(snake_sprite.health), True, (0, 0, 0))
        
            snake_sprite.current_score += int(0.1 * speed)
            main_surface.blit(score_surface, (0, 0))
            main_surface.blit(health_surface, (0, 30))
            snake_sprite.update(
                (snake_sprite.rect.x + move, snake_sprite.rect.y), grades_sprite_group)
            grades_sprite_group.update(main_surface, speed)
            speed += 0.004

            student_group_sprite.update(grades_sprite_group, snake_sprite)
        if snake_sprite.health <= 0:
           
            main_surface.blit(game_over_surface, 
                    (0, 0))
            final_raynizm = make_font_surface(
                    "All Hail to {} your total Raynizm is {}".
                    format(player_name, str(snake_sprite.current_score)) , 
                    18, (0, 0, 0))
            main_surface.blit(final_raynizm, 
                    (6, 20))
            if is_alive:
                cursor.execute('INSERT INTO Player VALUES (?, ?)', (player_name, snake_sprite.current_score))
                conn.commit()
                conn.close()
                is_alive = False             
        
        pygame.display.update()         
        


          
if __name__ == '__main__':
    main()