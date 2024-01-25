import pygame, time, random, sys, pygame_menu
from pygame_menu import themes

pygame.init()

WIDTH, HEIGHT = 400, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game")

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (125, 125, 125)

clock = pygame.time.Clock()
FPS = 10
x, y = 200, 200
delta_x, delta_y = 0, 0
body_list = [(x, y)]
food_x, food_y = random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)
score = 0
name = ''
leaderboard = []

game_over = False

font = pygame.font.SysFont("arialblack", 25)
score_font = pygame.font.SysFont("arialblack", 15)
leaderboard_font = pygame.font.SysFont("arialblack", 20)

def load_leaderboard():
    global leaderboard
    list = []
    with open("scores.txt", "r") as f:
        for line in f:
            d = line.strip()
            list.append(d)
    for i in range(len(list)):
        x = WIDTH / 2 - 50
        y = 100 + i*30
        leaderboard.append([x, y, list[i]])

def update_score():
    scores = {}
    update = False

    with open("scores.txt", "r") as f:
        for line in f:
            line = line.strip().split(":")
            scores[line[0]] = int(line[1])

    if name in scores:
        scores[name] = max(scores[name], score)
        update = True

    if not update:
        scores[name] = score

    with open("scores.txt", "w") as f:
        for key, value in scores.items():
            f.write(f"{key}: {value}\n")

def snake():
    global x, y, food_x, food_y, game_over, score
    x = (x + delta_x)
    y = (y + delta_y)
        
    if (x, y) in body_list[:-1] or x < 0 or x > WIDTH - 10 or y < 0 or y > HEIGHT - 10:
        game_over = True
        return

    body_list.append((x, y))

    if food_x == x and food_y == y:
        while (food_x, food_y) in body_list:
            food_x, food_y = random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)
            score +=1
    else:
        del body_list[0]


    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, RED, [food_x, food_y, 10, 10])
    for i, j in body_list:
        pygame.draw.rect(SCREEN, (GREEN), [i, j, 10, 10])
    text = score_font.render(f"{name} score : {score}", True, WHITE)
    SCREEN.blit(text, (20, 20))
    pygame.display.update()

def main_game():
    global delta_x, delta_y, game_over
    while True: 
        if game_over:
            SCREEN.fill(BLACK)
            message = font.render("GAME OVER !", True, WHITE)
            SCREEN.blit(message, [110, HEIGHT//3])
            pygame.display.update()
            time.sleep(5)
            update_score()
            reset()
            game_over = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if delta_x != 10:
                        delta_x = -10
                        delta_y = 0
                elif event.key == pygame.K_DOWN:
                    if delta_y != -10:
                        delta_x = 0
                        delta_y = 10
                elif event.key == pygame.K_RIGHT:
                    if delta_x != -10:
                        delta_x = 10
                        delta_y = 0
                elif event.key == pygame.K_UP:
                    if delta_y != 10:
                        delta_x = 0
                        delta_y = -10
                elif event.key == pygame.K_ESCAPE:
                    return
                else:
                    continue
        snake()
        clock.tick(FPS)

def reset():
    global x, y, delta_x, delta_y, body_list, food_x, food_y, score
    x, y = 200, 200
    delta_x, delta_y = 0, 0
    body_list = [(x, y)]
    food_x, food_y = random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)
    score = 0

def get_name(player_name):
    global name
    name = player_name

def display_leaderboard():
    frames = 15
    SCREEN.fill(GRAY)
    load_leaderboard()

    while True:
        clock.tick(frames)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        
        titre = font.render("scores", True, BLACK)
        SCREEN.blit(titre, (WIDTH / 2 - titre.get_width()/2, 30))
        for i in leaderboard:
            x, y, name_score = i
            text = leaderboard_font.render(name_score, True, BLACK)
            SCREEN.blit(text, (x, y))
            
        pygame.display.update()

mainmenu = pygame_menu.Menu("Bienvenue", WIDTH, HEIGHT, theme=themes.THEME_DARK)
mainmenu.add.text_input("Nom: ", default="Prénom", maxchar=20, onchange=get_name)
mainmenu.add.button("Jouer", main_game)
mainmenu.add.button("scores", display_leaderboard)
running = True

if __name__ == '__main__':
    while running:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if mainmenu.is_enabled():
                mainmenu.mainloop(SCREEN)
            
            pygame.display.update()
            clock.tick(60)

pygame.quit()