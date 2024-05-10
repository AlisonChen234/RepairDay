import pygame
from goomba import Goomba
from hammer import Hammer
from vending import Vending

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
city_background = pygame.image.load("city.jpg")
store_background = pygame.image.load("store.jpg")
park = pygame.image.load("park.jpg")

# set up variables for the display
size = (400, 300)
screen = pygame.display.set_mode(size)


g=Goomba(200,250)
h=Hammer(200,250)
v=Vending(0,40)
coins=0
health=100


game_not_started = True
run=False
display_shop=False
repair_hammer = False
restore_10_health = False
faster_repair = False

welcome="Hi,welcome to my game!"
welcome_1="Press the mouse to start the game and use wasd or the arrow keys to move your character!"
welcome_2="Your objective here is to earn coins and use these coins to buy tools and help rebuild the city after a natural disaster."

# render the text for later
display_welcome = my_font.render(welcome, True, (255, 255, 255))
display_welcome_1 = my_font.render(welcome_1, True, (255, 255, 255))
display_welcome_2 = my_font.render(welcome_2, True, (255, 255, 255))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run_game = True
start_screen= True
# -------- Main Program Loop -----------
while run:
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        g.move_direction("right")
        h.move_direction("right")
    if keys[pygame.K_w]:
        g.move_direction("up")
        h.move_direction("up")
    if keys[pygame.K_a]:
        g.move_direction("left")
        h.move_direction("left")
    if keys[pygame.K_s]:
        g.move_direction("down")
        h.move_direction("down")

    if keys[pygame.K_RIGHT]:
        g.move_direction("right")
        h.move_direction("right")
    if keys[pygame.K_UP]:
        g.move_direction("up")
        h.move_direction("up")
    if keys[pygame.K_LEFT]:
        g.move_direction("left")
        h.move_direction("left")
    if keys[pygame.K_DOWN]:
        g.move_direction("down")
        h.move_direction("down")

    if g in pygame.Rect(100, 100, 10, 10):
        g = 200, 0
        background = store_background


    if display_shop==True:
        print("What would you like to buy")
        if repair_hammer:
            coins=coins-15
        if restore_10_health:
            coins=coins-20
        if faster_repair:
            coins=coins-5



    # --- Main event loop
    for event in pygame.event.get(): # User did something
        clock = pygame.time.Clock()
        clock.tick(60)

        if event.type == pygame.MOUSEBUTTONDOWN:
            game_not_started=False
        if event.type == pygame.MOUSEBUTTONUP:
            run = True


        if event.type == pygame.QUIT:  # If user clicked close
            run_game = False


    if game_not_started:
        screen.fill((0, 0, 0))
        screen.blit(display_welcome, (170, 150))
        screen.blit(display_welcome_1, (170, 190))
        screen.blit(display_welcome_2, (170, 190))
    if run_game == True:
        screen.fill((city_background))

    else:
        pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

