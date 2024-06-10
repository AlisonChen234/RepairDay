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
c.set_hammer(h)
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

start_time = None
fix = False
lose = False
no_time = False

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

    if not rubble.draw(screen):
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


    # Move the wave towards the left
    if run_game:
        w.move()

        # Check if the wave goes off the screen
        if w.x < -100:
            w.x = 550  # Reset the wave position when it goes off the screen

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

    health_left = "Health:", health
    hammer_health_left = "Hammer Health:", hammer_health

    display_health_left = my_font.render(str(health_left), True, (255, 255, 255))
    display_hammer_health_left = my_font.render(str(hammer_health_left), True, (255, 255, 255))

    # Drawing the screen
    if game_not_started:
        screen.fill((100, 200, 40))
        screen.blit(display_welcome, (10, 50))
        screen.blit(display_welcome_1, (10, 70))
        screen.blit(display_welcome_2, (10, 90))
    elif run_game:
        screen.blit(background, (0, 0))
        c.draw(screen)
        screen.blit(display_health_left, (0, 10))
        screen.blit(display_hammer_health_left, (0, 30))

        if background == park_background:
            if rubble_place == 2:
                rubble.draw(screen)
                w.draw(screen)

        if background == store_background:
            if rubble_place == 3:
                rubble.draw(screen)
                w.draw(screen)
            v.draw(screen)
            box_1.draw(screen)
            box_2.draw(screen)

        if rubble_place == 1:
            rubble_x = 200
            rubble_y = 75
            rubble = Rubble(rubble_x, rubble_y)
            rubble.draw(screen)
            w.draw(screen)

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
