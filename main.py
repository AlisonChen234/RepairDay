import pygame
from character import Character
from hammer import Hammer
from vending import Vending
from wave import Wave
from rubble import Rubble
from box import Box
import random


# Set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
old_sheet_paper = pygame.image.load("old_piece_paper.jpg")
city_background = pygame.image.load("city.jpg")
store_background = pygame.image.load("store.jpg")
park_background = pygame.image.load("park.jpg")
background = city_background


# Set up variables for the display
size = (540, 350)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("City Rebuild Game")
rubble_place = 1


c_start_x = 200
c_start_y = 225
wave_start_x = 550
rubble_x = 0
rubble_y = 50
box_1 = Box(200, 150)
box_2 = Box(200, 180)
c = Character(c_start_x, c_start_y)
h = Hammer(100, 250)
v = Vending(-60, 120)
w = Wave(wave_start_x, 40)
rubble = Rubble(rubble_x, rubble_y)
coins = 100
health = 100
hammer_health = 100


game_not_started = True
run_game = False
display_shop = False


welcome = "Hi, welcome to my game!"
welcome_1 = "Press the mouse to start the game and use WASD or the arrow keys to move your character!"
welcome_2 = "Your objective here is to earn coins and use these coins to buy tools and help rebuild the city after a natural disaster."
lose_message = "You lost due to a broken hammer or no health!"
shop_message = "What would you like to buy?"
no_coins_message = "You do not have enough coins to purchase this item."
no_time_message = "You ran out of time"
restore_health_message = "Restore 10 health for 20 coins"
restore_hammer_message = "Restore 10 health on hammer for 20 coins"
health_left = "Health:", health
hammer_health_left = "Hammer Health:", hammer_health


# Render the text for later
display_welcome = my_font.render(welcome, True, (255, 255, 255))
display_welcome_1 = my_font.render(welcome_1, True, (255, 255, 255))
display_welcome_2 = my_font.render(welcome_2, True, (255, 255, 255))
display_lose_message = my_font.render(lose_message, True, (255, 255, 255))
display_shop_message = my_font.render(shop_message, True, (255, 255, 255))
display_no_coins_message = my_font.render(no_coins_message, True, (255, 255, 255))
display_no_time_message = my_font.render(no_time_message, True, (255, 255, 255))
display_restore_health = my_font.render(restore_health_message, True, (255, 255, 255))
display_restore_hammer = my_font.render(restore_hammer_message, True, (255, 255, 255))
display_health_left = my_font.render(str(health_left), True, (255, 255, 255))
display_hammer_health_left = my_font.render(str(hammer_health_left), True, (255, 255, 255))


start_time = 0
fix = False
lose = False
no_time = False
restore_health=False
restore_hammer=False
wave_left = False  # Flag to track if the wave has left the screen


def fade_in(screen, color, duration=300):
   fade_surface = pygame.Surface(screen.get_size())
   fade_surface.fill(color)
   for i in range(0, 255):
       fade_surface.set_alpha(i)
       screen.blit(fade_surface, (0, 0))
       pygame.display.flip()
       pygame.time.delay(duration // 255)


def fade_out(screen, color, duration=300):
   fade_surface = pygame.Surface(screen.get_size())
   fade_surface.fill(color)
   for i in range(255, 0, -1):
       fade_surface.set_alpha(i)
       screen.blit(fade_surface, (0, 0))
       pygame.display.flip()
       pygame.time.delay(duration // 255)


# -------- Main Program Loop -----------
while True:


   keys = pygame.key.get_pressed()  # checking pressed keys
   if keys[pygame.K_d]:
       c.move_direction("right")
   if keys[pygame.K_w]:
       c.move_direction("up")
   if keys[pygame.K_a]:
       c.move_direction("left")
   if keys[pygame.K_s]:
       c.move_direction("down")


   if keys[pygame.K_RIGHT]:
       c.move_direction("right")
   if keys[pygame.K_UP]:
       c.move_direction("up")
   if keys[pygame.K_LEFT]:
       c.move_direction("left")
   if keys[pygame.K_DOWN]:
       c.move_direction("down")


   if c.x <= -120:
       fade_out(screen, (255, 255, 255), duration=150)
       if background == store_background:
           background = park_background
       elif background == city_background:
           background = store_background
       elif background == park_background:
           background = city_background
       c.x = 540
       fade_in(screen, (255, 255, 255), duration=150)


   elif c.x >= 540:
       fade_out(screen, (255, 255, 255), duration=150)
       if background == store_background:
           background = city_background
       elif background == city_background:
           background = park_background
       elif background == park_background:
           background = store_background
       c.x = 0
       fade_in(screen, (255, 255, 255), duration=150)


   if display_shop:
       if restore_hammer and coins >= 20:
           coins -= 20
           hammer_health = 100
       if restore_health and coins >= 20:
           coins -= 20
           health += 10


   if not screen.blit(rubble.image, (rubble.rect.x, rubble.rect.y)):
       fix = False


   if fix:
       coins += 30
       hammer_health -= 20
       health -= 30
       c = Character(rubble_x, rubble_y + 175)
       fix = False


       for _ in range(10):
           for _ in range(10):
               c.move_direction("up")
           for _ in range(10):
               c.move_direction("down")


   if health <= 0 or hammer_health <= 0:
       lose = True

   if run_game:
       w.move()

       if w.x < -250:
           wave_left = True

       if wave_left:
           if background==city_background:
               if rubble_place== 1:
                screen.blit(rubble.image, (rubble.rect.x, rubble.rect.y))
           if background == park_background:
               if rubble_place == 2:
                   screen.blit(rubble.image, (rubble.rect.x, rubble.rect.y))
           elif background == store_background:
               if rubble_place == 3:
                   screen.blit(rubble.image, (rubble.rect.x, rubble.rect.y))


       if w.x < -550:
           w.x = 550
           wave_left = False  # Reset the flag indicating wave has left


   # --- Main event loop
   for event in pygame.event.get():  # User did something
       if event.type == pygame.QUIT:  # If user clicked close
           pygame.quit()
           quit()


       if event.type == pygame.MOUSEBUTTONDOWN:
           game_not_started = False
           run_game = True
           x, y = pygame.mouse.get_pos()
           if background == store_background and display_shop:
               if coins >= 20:
                   if x < 200 and y < 150:
                       restore_hammer = True
                   if x < 200 and y < 150:
                       restore_health = True


       if event.type == pygame.MOUSEBUTTONUP:
           mouse_pos = pygame.mouse.get_pos()
           if rubble.rect.collidepoint(mouse_pos):
               fix = True
           else:
               fix = False
           if fix:
               rubble_place = random.randint(1, 3)
           if background == store_background and v.rect.collidepoint(mouse_pos):
               display_shop = True
           else:
               display_shop = False


           if background == store_background and box_1.rect.collidepoint(mouse_pos):
               restore_health = True
           else:
               restore_health = False
           if background == store_background and box_2.rect.collidepoint(mouse_pos):
               restore_hammer = True
           else:
               restore_hammer = False




           if w.rect.collidepoint(mouse_pos):
               pass


       if c.x+247==w.x:
           health-=20


   health_left = "Health:", health
   hammer_health_left = "Hammer Health:", hammer_health


   display_health_left = my_font.render(str(health_left), True, (255, 255, 255))
   display_hammer_health_left = my_font.render(str(hammer_health_left), True, (255, 255, 255))


   if health==0:
       lose=True


   if game_not_started:
       screen.fill((100, 200, 40))
       screen.blit(display_welcome, (10, 50))
       screen.blit(display_welcome_1, (10, 70))
       screen.blit(display_welcome_2, (10, 90))
   elif run_game:
       screen.blit(background, (0, 0))
       screen.blit(c.image, (c.rect.x, c.rect.y))
       screen.blit(display_health_left, (0, 10))
       screen.blit(display_hammer_health_left, (0, 30))


       while rubble_place<4:
            if rubble_place == 1 and background == city_background:
               rubble = Rubble(rubble_x, rubble_y)
               for _ in range(1):
                   if w.x > -250:
                       screen.blit(w.image, (w.rect.x, w.rect.y))
                   elif w.x < -250:
                        screen.blit(rubble.image, (rubble.rect.x, rubble.rect.y))
                        rubble_place=rubble_place + 1
            if rubble_place == 2 and background == park_background:
                for _ in range(1):
                    if w.x > -250:
                        screen.blit(w.image, (w.rect.x, w.rect.y))
                    elif w.x < -250:
                        screen.blit(rubble.image, (rubble.rect.x, rubble.rect.y))
                        rubble_place=rubble_place+1
            if rubble_place == 3 and background == store_background:
               for _ in range(1):
                   if w.x > -250:
                       screen.blit(w.image, (w.rect.x, w.rect.y))
                   elif w.x < -250:
                       screen.blit(rubble.image, (rubble.rect.x, rubble.rect.y))
                   rubble_place = rubble_place + 1





       if background == store_background:
           screen.blit(v.image, (v.rect.x, v.rect.y))
           screen.blit(box_1.image, (box_1.rect.x, box_1.rect.y))
           screen.blit(box_2.image, (box_2.rect.x, box_2.rect.y))



       if display_shop:
           screen.blit(old_sheet_paper, (200, 20))
           screen.blit(display_restore_health, (200, 150))
           screen.blit(display_restore_hammer, (200, 180))


       if lose:
           screen.blit(display_lose_message, (10, 150))
       elif no_time:
           screen.blit(display_no_time_message, (10, 120))
           screen.blit(display_no_time_message, (10, 150))


   pygame.display.update()
   pygame.time.Clock().tick(60)

