import pygame
from goomba import Goomba

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
city_background = pygame.image.load("city.jpg")
store_background = pygame.image.load("store.jpg")
park = pygame.image.load("park.jpg")
hammer=pygame.image.load("hammer.png")

# set up variables for the display
size = (400, 300)
screen = pygame.display.set_mode(size)


g=Goomba(200,250)

game_not_started = True
run=False

welcome="Hi,welcome to my game!"
welcome_1="Press the mouse to start the game and use wasd or the arrow keys to move your character!"
welcome_2="Your objective here is to earn coins and use these coins to buy tools and help rebuild the city after a natural disaster."

# render the text for later
display_welcome = my_font.render(welcome, True, (255, 255, 255))
display_welcome_1 = my_font.render(welcome_1, True, (255, 255, 255))
display_welcome_2 = my_font.render(welcome_2, True, (255, 255, 255))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
start_screen= True
# -------- Main Program Loop -----------
while run:
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        g.move_direction("right")
    if keys[pygame.K_w]:
        g.move_direction("up")
    if keys[pygame.K_a]:
        g.move_direction("left")
    if keys[pygame.K_s]:
        g.move_direction("down")

    if keys[pygame.K_RIGHT]:
        g.move_direction("right")
    if keys[pygame.K_UP]:
        g.move_direction("up")
    if keys[pygame.K_LEFT]:
        g.move_direction("left")
    if keys[pygame.K_DOWN]:
        g.move_direction("down")

    if g in pygame.Rect(100, 100, 10, 10):
        g = 200, 0
        background = store_background

    # --- Main event loop
    for event in pygame.event.get(): # User did something
        clock = pygame.time.Clock()
        clock.tick(60)

        if event.type == pygame.MOUSEBUTTONDOWN:
            game_not_started=False
        if event.type == pygame.MOUSEBUTTONUP:
            run = True


        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0, 0, 0))
    if game_not_started:
        screen.blit(display_welcome, (170, 150))
        screen.blit(display_welcome_1, (170, 190))
        screen.blit(display_welcome_2, (170, 190))
    if run == True:


    else:
        pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

