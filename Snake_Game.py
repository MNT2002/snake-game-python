import sys
import pygame
import random
import time

pygame.init()
WIDTH = 600
WIDTH_SCREEN = 1200
HEIGHT_SCREEN = 600
screen_size = [WIDTH_SCREEN, HEIGHT_SCREEN]
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
# GREEN = (0, 255, 0)
SNAKE_BORDER = (0, 60, 255)
SNAKE_COLOR = (0, 128, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW  = (204, 204, 0)
ORANGE = (255, 128, 0)
WHITE = (255, 255, 255)
# BLUE = (252, 68, 132)
GRID_COLOR_1 = (133, 214, 82)
GRID_COLOR_2 = (102, 204, 50)
x_speed = 1
y_speed = 0
BLOCK_COLOR = (243, 97, 17)
BLOCK_BORDER = (166, 66, 11)
flag = 1

class Square:
    def __init__(self, x, y, color, width):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw_it(self):
        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.width, self.width),
            0,
        )

    def draw_border(self, border_color):
        pygame.draw.rect(
            screen,
            border_color,
            (self.x, self.y, self.width, self.width),
            0,
        )
        pygame.draw.rect(
            screen,
            self.color,
            (self.x+2, self.y+2, self.width-4, self.width -4),
            0,
        )

class Block:
    def __init__(self, length, color):
        self.square = []
        self.color = color
        self.length = length
        distance_base_x = grid.square[63].x
        distance_base_y = grid.square[63].y
        size_box = grid.size + grid.distance

        # block 1
        x = distance_base_x
        y = distance_base_y
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x + size_box
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x + size_box * 2
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x + size_box * 3
        self.square.append(Square(x, y, color, grid.size))

        x = distance_base_x
        y = distance_base_y + size_box
        self.square.append(Square(x, y, color, grid.size))
        y = distance_base_y + size_box * 2
        self.square.append(Square(x, y, color, grid.size))
        y = distance_base_y + size_box * 3
        self.square.append(Square(x, y, color, grid.size))

        # block 2
        distance_base_x = grid.square[76].x
        distance_base_y = grid.square[76].y
        x = distance_base_x
        y = distance_base_y
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x - size_box
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x - size_box * 2
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x - size_box * 3
        self.square.append(Square(x, y, color, grid.size))

        x = distance_base_x
        y = distance_base_y + size_box
        self.square.append(Square(x, y, color, grid.size))
        y = distance_base_y + size_box * 2
        self.square.append(Square(x, y, color, grid.size))
        y = distance_base_y + size_box * 3
        self.square.append(Square(x, y, color, grid.size))

        # block 3
        distance_base_x = grid.square[323].x
        distance_base_y = grid.square[323].y
        x = distance_base_x
        y = distance_base_y
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x + size_box
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x + size_box * 2
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x + size_box * 3
        self.square.append(Square(x, y, color, grid.size))

        x = distance_base_x
        y = distance_base_y - size_box
        self.square.append(Square(x, y, color, grid.size))
        y = distance_base_y - size_box * 2
        self.square.append(Square(x, y, color, grid.size))
        y = distance_base_y - size_box * 3
        self.square.append(Square(x, y, color, grid.size))

        # block 4
        distance_base_x = grid.square[336].x
        distance_base_y = grid.square[336].y
        x = distance_base_x
        y = distance_base_y
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x - size_box
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x - size_box * 2
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x - size_box * 3
        self.square.append(Square(x, y, color, grid.size))

        x = distance_base_x
        y = distance_base_y - size_box
        self.square.append(Square(x, y, color, grid.size))
        y = distance_base_y - size_box * 2
        self.square.append(Square(x, y, color, grid.size))
        y = distance_base_y - size_box * 3
        self.square.append(Square(x, y, color, grid.size))

        # block 5
        distance_base_x = grid.square[209].x
        distance_base_y = grid.square[209].y
        x = distance_base_x
        y = distance_base_y
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x + size_box
        self.square.append(Square(x, y, color, grid.size))

        y = distance_base_y - size_box
        self.square.append(Square(x, y, color, grid.size))
        x = distance_base_x
        self.square.append(Square(x, y, color, grid.size))

    def draw_it(self):
        for i in range(len(self.square)):
            self.square[i].draw_border(BLOCK_BORDER)


class Grid:
    def __init__(self, size, distance, color):
        self.size = size  # kích thước của một ô bản đồ
        self.distance = distance  # kích thước viền của bản đồ
        self.color = color  # máu nền
        self.square = []  # list lưu vị trị các ô trong bản đồ 20x20
        x = 0
        y = 0  # toạ độ ô đầu tiên
        check = 0
        reverse = 1
        for i in range(self.size**2):
            if reverse == 1:
                if check == 0:
                    self.square.append(Square(x, y, GRID_COLOR_1, self.size))
                    check = 1
                else:
                    self.square.append(Square(x, y, GRID_COLOR_2, self.size))
                    check = 0
            else:
                if check == 0:
                    self.square.append(Square(x, y, GRID_COLOR_2, self.size))
                    check = 1
                else:
                    self.square.append(Square(x, y, GRID_COLOR_1, self.size))
                    check = 0
            x += self.size + self.distance
            if x >= WIDTH:
                x = 0
                if y < HEIGHT_SCREEN:
                    y += self.size + self.distance
                    reverse *= -1

    def draw_gird(self, color):
        for i in range(self.size**2):
            self.square[i].draw_it()



class Snake:
    def __init__(self, length, color):
        self.square = []
        self.color = color
        self.length = length
        self.points = 0
        self.count = 0
        self.countspeed = 0
        self.upspeed = 0
        self.x = 90
        self.y = 0
        self.sound = pygame.mixer.Sound('sound.wav')
        for i in range(length):
            if i == 0:
                self.square.append(Square(self.x, self.y, SNAKE_COLOR, grid.size))
            else:
                self.square.append(Square(self.x, self.y, color, grid.size))
            self.x -= grid.size + grid.distance

    def play_sound(self):
        self.sound.play()

    def draw_it(self):
        for i in range(len(self.square)):
            if i == 0:
                self.square[i].draw_border(SNAKE_BORDER)
            else:
                self.square[i].draw_it()

    def move_it(self):
        for i in range(len(self.square) - 1, 0, -1):
            self.square[i].x = self.square[i - 1].x
            self.square[i].y = self.square[i - 1].y
        # rắn tịnh tiến vè phía trước
        self.square[0].x += (grid.size + grid.distance) * x_speed 
        self.square[0].y += (grid.size + grid.distance) * y_speed
        if self.square[0].x >= WIDTH:
            self.square[0].x = 0
        if self.square[0].y >= HEIGHT_SCREEN:
            self.square[0].y = 0
        if self.square[0].x < 0:
            self.square[0].x = WIDTH - (grid.size + grid.distance)
        if self.square[0].y < 0:
            self.square[0].y = WIDTH - (grid.size + grid.distance)

    def check_food(self):
        if self.square[0].x == apple.x and self.square[0].y == apple.y:
            if apple.foodType == "normal":
                self.count += 1
                self.countspeed += 1
                if self.countspeed == 5:
                    self.upspeed = 1
                if self.count == 5:
                    apple.foodType = "bonus"
                    apple.foodTimer = time.time()
                apple.foodSpawn()
                self.points += 1
                self.square.append(Square(-100, -100, self.color, grid.size))
            elif apple.foodType == "bonus":
                apple.foodSpawn()
                self.points += 5
                self.square.append(Square(-100, -100, self.color, grid.size))
                apple.foodType = "normal"
                self.count = 0
            self.play_sound()

    def check_block(self):
        print(len(self.square));
        # print(self.length);
        for i in range(len(block.square)):
            if (
                self.square[0].x == block.square[i].x
                and self.square[0].y == block.square[i].y
            ):
                for j in range(len(self.square) - 1, self.length - 1, -1):
                    del self.square[j]
              
                    
                apple.foodType = "normal"
                restart_game()

    def check_die(self):
        for i in range(1, len(self.square), 1):
            if (
                self.square[0].x == self.square[i].x
                and self.square[0].y == self.square[i].y
            ):
                for j in range(len(self.square) - 1, self.length - 1, -1):
                    del self.square[j]
                    self.points = 0
                apple.foodType = "normal"
                # self.countspeed = 0
                restart_game()
                break


class Food(Square):
    def __init__(self, x, y, color, width):
        super().__init__(x, y, color, width)
        self.foodType = "normal"
        self.foodTimer = 0
        self.bonusDuration = 5  # thời gian bonus
        self.check = 0
    def foodSpawn(self):
        self.x = int(
            random.randint(0, (WIDTH // (grid.size + grid.distance)) - 1)
            * (grid.size + grid.distance)
        )
        self.y = int(
            random.randint(0, (HEIGHT_SCREEN // (grid.size + grid.distance)) - 1)
            * (grid.size + grid.distance)
        )
        for i in range(len(snake.square)):
            if snake.square[i].x == self.x and snake.square[i].y == self.y:
                Food.foodSpawn(self)

        for i in range(len(block.square)):
            if block.square[i].x == self.x and block.square[i].y == self.y:
                Food.foodSpawn(self)

        # reset lại thời gian bonus
        self.bonusDuration = 5
        self.foodTimer = time.time()

    def draw_circle(self):
        if self.foodType == "normal":
            pygame.draw.circle(
                screen,
                self.color,
                (self.x + self.width / 2, self.y + self.width / 2),
                self.width / 2,
                int(self.width / 2),
            )
        else:
            # print(time.time())
            # hiệu ứng nhấp nháy
            if self.check == 0: #tính theo thời gian thực x2 tốc độ sau đó trả về 0 hoặc 1
                pygame.draw.circle(
                    screen,
                    YELLOW,
                    (self.x + self.width / 2, self.y + self.width / 2),
                    self.width / 2,
                    int(self.width / 2),
                )
                self.check = 1
            else:
                pygame.draw.circle(
                    screen,
                    ORANGE,
                    (self.x + self.width / 2, self.y + self.width / 2),
                    self.width / 2,
                    int(self.width / 2),
                )
                self.check = 0

            if time.time() - self.foodTimer > self.bonusDuration:
                snake.count = 0
                self.foodType = "normal"
                Food.foodSpawn(self)


def movement():
    global x_speed
    global y_speed
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                if y_speed != 1:  # x0,y-1 đi lên,
                    x_speed = 0
                    y_speed = -1
                    break
            if event.key == pygame.K_DOWN:
                if y_speed != -1:  # x0,y1 đi xuống,
                    x_speed = 0
                    y_speed = 1
                    break
            if event.key == pygame.K_RIGHT:
                if x_speed != -1:  # x1,y0 đi r,
                    y_speed = 0
                    x_speed = 1
                    break
            if event.key == pygame.K_LEFT:  # x-1,y0 đi l,
                if x_speed != 1:
                    y_speed = 0
                    x_speed = -1
                    break
            if event.key == pygame.K_SPACE:
                if gamestatus == False:
                    resume_game()
                else:
                    pause_game()
            if event.key == pygame.K_r:
                restart_game()

font = pygame.font.Font(None, 36)

def restart_game():
    global x_speed
    global y_speed
    x_speed = 1
    y_speed = 0
    global snake, apple, block, speed, gamestatus

    # Khởi tạo lại Snake

    snake = Snake(3, SNAKE_COLOR)

    # Khởi tạo lại Food
    # apple = Food(-100, -100, RED, grid.size)
    apple.foodSpawn()

    # Khởi tạo lại Block
    block = Block(3, BLOCK_COLOR)

    # Khởi tạo lại tốc độ+
    speed = 5

    # Khởi tạo lại điểm
    snake.points = 0
    snake.countspeed = 0
    snake.count = 0
    # Khởi tạo lại trạng thái game
    gamestatus = False


def pause_game():
    global gamestatus
    gamestatus = False
    print("Game paused. Press 'P' to resume.")


def resume_game():
    global gamestatus
    gamestatus = True
    print("Game resumed.")


# Khoi tao
grid = Grid(30, 0, WHITE)
snake = Snake(3, SNAKE_COLOR)
apple = Food(-100, -100, RED, grid.size)
block = Block(3, BLOCK_COLOR)
font = pygame.font.Font("font.ttf", 30)
apple.foodSpawn()
speed = 5
white = (255, 255, 255)
gamestatus = False

while flag == 1:
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH_SCREEN, HEIGHT_SCREEN), 0)
    pygame.draw.rect(screen, BLOCK_COLOR, (0, 0, WIDTH + 5, HEIGHT_SCREEN), 0)
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT_SCREEN), 0)
    while gamestatus == True:
        if snake.points == 0:
            snake.countspeed = 0
            snake.count = 0
            speed = 5
        pygame.draw.rect(screen, WHITE, (0, 0, WIDTH_SCREEN, HEIGHT_SCREEN), 0)
        pygame.draw.rect(screen, BLOCK_COLOR, (0, 0, WIDTH + 5, HEIGHT_SCREEN), 0)
        pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT_SCREEN), 0)
        grid.draw_gird(WHITE)
        movement()
        snake.move_it()
        snake.check_die()
        snake.check_food()
        snake.check_block()
        snake.draw_it()
        apple.draw_circle()
        block.draw_it()
        # pygame.display.flip()
        text = font.render("Điểm: " + str(snake.points), True, (0, 0, 0))
        textlevel = font.render(
            "Cấp độ: " + str(int((speed - 5) / 2) + 1), True, (0, 0, 0)
        )
        screen.blit(text, (650, 50))
        screen.blit(textlevel, (650, 150))
        textrule1 = font.render("Bấm Space để dừng trò chơi ", True, (0, 0, 0))
        textrule2 = font.render("Bấm R để Restart trò chơi ", True, (0, 0, 0))
        textrule3 = font.render("Bấm ESC để thoát trò chơi ", True, (0, 0, 0))
        screen.blit(textrule1, (650, 200))
        screen.blit(textrule2, (650, 250))
        screen.blit(textrule3, (650, 300))
        pygame.display.update()
        if snake.upspeed == 1:
            speed += 1
            snake.upspeed = 0
            snake.countspeed = 0
        clock.tick(speed)
    while gamestatus == False:
        pygame.draw.rect(screen, WHITE, (0, 0, WIDTH_SCREEN, HEIGHT_SCREEN), 0)
        pygame.draw.rect(screen, BLOCK_COLOR, (0, 0, WIDTH + 5, HEIGHT_SCREEN), 0)
        pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT_SCREEN), 0)
        grid.draw_gird(WHITE)
        movement()
        snake.draw_it()
        apple.draw_circle()
        block.draw_it()

        text = font.render("Điểm: " + str(snake.points), True, (0, 0, 0))
        notification = font.render("Trò chơi đang dừng! ", True, (0, 0, 0))
        textlevel = font.render(
            "Cấp độ: " + str(int((speed - 5) / 2) + 1), True, (0, 0, 0)
        )
        textrule1 = font.render("Bấm Space để Tiếp tục trò chơi ", True, (0, 0, 0))
        textrule2 = font.render("Bấm R để Restart trò chơi ", True, (0, 0, 0))
        textrule3 = font.render("Bấm ESC để thoát trò chơi", True, (0, 0, 0))
        screen.blit(text, (650, 50))
        screen.blit(notification, (650, 150))
        screen.blit(textlevel, (650, 100))
        screen.blit(textrule1, (650, 200))
        screen.blit(textrule2, (650, 250))
        screen.blit(textrule3, (650, 300))
        pygame.display.update()
        clock.tick(speed)