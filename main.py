import pygame
from character import Character
from hammer import Hammer
from vending import Vending
import time


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
city_background = pygame.image.load("city.jpg")
store_background = pygame.image.load("store.jpg")
park_background = pygame.image.load("park.jpg")
background=city_background

# set up variables for the display
size = (400, 300)
screen = pygame.display.set_mode(size)

c_start_x=200
c=Character(c_start_x,250)
h=Hammer(200,250)
v=Vending(0,40)
coins=0
health=100
hammer_health=100


game_not_started = True
run=False
display_shop=False
repair_hammer = False
restore_10_health = False
faster_repair = False

welcome="Hi,welcome to my game!"
welcome_1="Press the mouse to start the game and use wasd or the arrow keys to move your character!"
welcome_2="Your objective here is to earn coins and use these coins to buy tools and help rebuild the city after a natural disaster."
lose_message = "You lost due to broken hammer or no health!"
shop_message="What would you like to buy?"
no_coins_message="You do not have enough coins to purchase this item."

# render the text for later
display_welcome = my_font.render(welcome, True, (255, 255, 255))
display_welcome_1 = my_font.render(welcome_1, True, (255, 255, 255))
display_welcome_2 = my_font.render(welcome_2, True, (255, 255, 255))
display_lose_message = my_font.render(lose_message, True, (255, 255, 255))
display_shop_message= my_font.render(shop_message, True, (255, 255, 255))
display_no_coins_message= my_font.render(no_coins_message, True, (255, 255, 255))

run_game = True
start_screen= True
fix=False
lose=False

# The loop will carry on until the user exits the game (e.g. clicks the close button).
# -------- Main Program Loop -----------
while run:
    start_time=time.time()
    current_time=time.time()-start_time


    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        c.move_direction("right")
        h.move_direction("right")
    if keys[pygame.K_w]:
        c.move_direction("up")
        h.move_direction("up")
    if keys[pygame.K_a]:
        c.move_direction("left")
        h.move_direction("left")
    if keys[pygame.K_s]:
        c.move_direction("down")
        h.move_direction("down")

    if keys[pygame.K_RIGHT]:
        c.move_direction("right")
        h.move_direction("right")
    if keys[pygame.K_UP]:
        c.move_direction("up")
        h.move_direction("up")
    if keys[pygame.K_LEFT]:
        c.move_direction("left")
        h.move_direction("left")
    if keys[pygame.K_DOWN]:
        c.move_direction("down")
        h.move_direction("down")

    if c_start_x <= 0:
        c_start_x = 200
        c = (c_start_x, 250)
        if background==store_background:
            background = store_background
        if background == city_background:
            background = park_background
        if background==park_background:
            background = store_background

    if c_start_x >= 0:
        c_start_x = 200
        c = (c_start_x, 250)
        if background == store_background:
            background = park_background
        if background == city_background:
            background = city_background
        if background == park_background:
            background = city_background


    if display_shop==True:
        if repair_hammer:
            coins=coins-15
        if restore_10_health:
            coins=coins-20
        if faster_repair:
            coins=coins-5

    if fix==True:
        coins+=30
        hammer_health-=20
        health-=30

    if health==0 or hammer_health==0:
        lose=True


    # --- Main event loop
    for event in pygame.event.get(): # User did something
        clock = pygame.time.Clock()
        clock.tick(60)

        if event.type == pygame.MOUSEBUTTONDOWN:
            game_not_started=False
            run_game=True
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if v.rect.collidepoint(pos):
                display_shop=True
                repair_hammer = True
                restore_10_health = True
                faster_repair = True
            else:
                display_shop=False
                repair_hammer = False
                restore_10_health = False
                faster_repair = False

            if v.rect.collidepoint(pos):
                fix = False
            run = True


        if event.type == pygame.QUIT:  # If user clicked close
            run_game = False


    if game_not_started:
        screen.fill((0, 0, 0))
        screen.blit(display_welcome, (170, 150))
        screen.blit(display_welcome_1, (170, 190))
        screen.blit(display_welcome_2, (170, 190))
    if run_game == True:
        screen.fill((background))

    if background==store_background:
        v = Vending(0, 40)

    if lose==True:
        screen.blit(display_lose_message, (170, 150))

    else:
        pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

