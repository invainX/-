import pygame
import time
import random
from PIL import Image
from tkinter import *
from tkinter.messagebox import *
import random
from PIL import Image, ImageTk
import os
import pygame, sys, random
from PIL.ImageTk import PhotoImage
from pygame.locals import *
import cv2operator
import os
pygame.init()
import datetime

white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 255)

car_width = 100

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('D:\software_practice\get\question(5)0.jpg')








def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_diaplay(text):
    largeText = pygame.font.SysFont('comicsansms', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()





def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    ##                if action == "play":
    ##                    action()
    ##                if action == "quit":
    ##                    pygame.quit()
    ##                    quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont('comicsansms', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comicsansms', 115)
        TextSurf, TextRect = text_objects('Welcome', largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        button("GO", 150, 450, 100, 50, green, bright_green, game_loop1)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        button("record", 350, 450, 100, 50, gray, bright_red, record)
        pygame.display.update()
        clock.tick(15)

def record():
    root = Tk('D:\pythonProject\deng')
    root.title("puzzlegame")
    WIDTH = 450
    HEIGHT = 450
    f = open('D:\puzzlegame\\record.txt', 'r')
    lines = f.readlines()
    for line in lines:
        label2 = Label(root, text=line, fg="red", width=40, height=2)
        label2.pack()
    f.close()
    root.mainloop()

def game_loop1():
    # 分割成九张小图片
    def splitimage(sre, rownum, colnum, dstpath):
        img = Image.open(src)
        img = Image.open(src)
        (x, y) = img.size  # read image size
        x_s = gameRect.width * 2  # define standard width
        y_s = gameRect.height * 2  # calc height based on standard width
        img = img.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
        w, h = img.size  # 图片大小
        if rownum <= h and colnum <= w:
            print('original image info:%sx%s,%s,%s' % (w, h, img.format, img.mode))
            print('开始处理图片切割，请稍候-')
            s = os.path.split(src)
            if dstpath == '':  # 没有输入路径
                dstpath = s[0]  # 使用源图片所在目录s[0]
            fn = s[1].split('.')  # s[1]是源图片文件名
            basename = fn[0]  # 主文件名
            ext = fn[-1]  # 扩展名
            num = 0
            rowheight = (gameRect.width * 2 - 1) // rownum
            colwidth = (gameRect.height * 2 - 1) // colnum
            for r in range(rownum):
                for c in range(colnum):
                    box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                    img.crop(box).save(os.path.join(dstpath, basename + '' + str(num) + '.' + ext))
                    num = num + 1
            print('图片切割完毕，共生成%s张小图片。' % num)
        else:
            print('不合法的行列切割参数！')

    # 导入图片
    src = r'D:\software_practice\无框字符\\test(16).jpg'
    # src="C：\woman.png"
    outfile = r'D:\software_practice\无框字符\\test(16).jpg'
    img = Image.open(src)
    # 让导入的图片像素都变为400*400
    (x, y) = img.size  # read image size
    x_s = 400  # define standard width
    y_s = 400  # calc height based on standard width
    out = img.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
    out.save(outfile)
    gameImage = pygame.image.load(src)
    gameRect = gameImage.get_rect()
    if os.path.isfile(src):
        dstpath = ('')
        if (dstpath == '') or os.path.exists(dstpath):
            row = 3
            col = 3
            if row > 0 and col > 0:
                splitimage(src, row, col, dstpath)
            else:
                print('无效的行列切割参数！')
        else:
            print('图片输出目录%s不存在！' % dstpath)
    else:
        print('图片文件%s不存在!' % src)

    # 本程序deng目录下已经有用1.图片分解切出的9张小图片

    # 定义常量
    # 画布的尺寸

    WIDTH = gameRect.width * 2
    HEIGHT = gameRect.height * 2
    # 图像块的边长
    IMAGE_WIDTH = (WIDTH) / 3
    IMAGE_HEIGHT = (HEIGHT) / 3
    # 游戏的行/列数
    ROWS = 3
    COLS = 3
    # 移动步数
    steps = 0
    # 保存所有图像块的列表
    board = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]]
    root = Tk('D:\pythonProject\deng')
    root.title("puzzlegame")

    # 载入外部事先生成的9个小图像块
    Pics = []
    for i in range(9):
        filename = "D:\software_practice\无框字符\\test(16)" + str(i) + ".jpg"
        Pics.append(PhotoImage(file=filename))

    def swap(i, j, r, c):
        swap_square = board[j // ROWS][j % COLS]
        board[j // ROWS][j % COLS] = board[i // ROWS][i % COLS]
        board[i // ROWS][i % COLS] = swap_square
        cv.delete('all')
        # 清除画布上的内容
        drawBoard(cv)

    class Square:
        def __init__(self, orderID):
            self.orderID = orderID

        def draw(self, canvas, board_pos):
            img = Pics[self.orderID]
            canvas.create_image(board_pos, image=img)
    def solve(L):
        count = 0
        for i in range(9):
            for j in range(i+1, 9):
                if L[i] > L[j] and L[i]!=4 and L[j]!=4:
                    count += 1
        return count


    def init_board():
        L = list(range(9))  # L列表中[0,1,2,3,4,5,6,7,8]
        # 打乱图像块
        random.shuffle(L)


        # 填充拼图板
        for i in range(ROWS):
            for j in range(COLS):
                idx = i * ROWS + j
                orderID = L[idx]
                if orderID == 4:  # 8号拼块不显示,所以存为None
                    board[i][j] = None
                else:
                    board[i][j] = Square(orderID)

        while solve(L) %2 == 1:
            for i in range(9):
                for j in range(i+1,9):
                    if L[i] < L[j] and L[i] != 4 and L[j] != 4:
                        swap(i,j,3,3)
                        temp = L[i]
                        L[i] = L[j]
                        L[j] = temp
                        leap = 1
                        break
                if leap == 1:
                    break




    def drawBoard(canvas):
        canvas.create_polygon((0, 0, WIDTH, 0, WIDTH, HEIGHT, 0, HEIGHT),
                              width=1, outline='White', fill='White')
        # 画所有图像块
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] is not None:
                    board[i][j].draw(canvas, (IMAGE_WIDTH * (j + 0.5), IMAGE_HEIGHT * (i + 0.5)))

    def mouseclick(pos):
        global steps
        global start_time
        # 将单击位置换算成拼图板上的棋盘坐标
        r = int(pos.y / IMAGE_HEIGHT)
        c = int(pos.x / IMAGE_WIDTH)
        if r < 3 and c < 3:  # 单击位置在拼图板内才移动图片
            if board[r][c] is None:  # 单击空位置,什么也不移动
                return
            else:
                # 依次检查被单击当前图像块的上、下、左、右是否有空位置,如果有,就移动当前图像块
                current_square = board[r][c]
                if r - 1 >= 0 and board[r - 1][c] is None:  # 判断上面
                    board[r][c] = None
                    board[r - 1][c] = current_square
                    steps += 1
                elif c + 1 <= 2 and board[r][c + 1] is None:  # 判断右面
                    board[r][c] = None
                    board[r][c + 1] = current_square
                    steps += 1
                elif r + 1 <= 2 and board[r + 1][c] is None:  # 判断下面
                    board[r][c] = None
                    board[r + 1][c] = current_square
                    steps += 1
                elif c - 1 >= 0 and board[r][c - 1] is None:  # 判断左面
                    board[r][c] = None
                    board[r][c - 1] = current_square
                    steps += 1
                if steps == 1:
                    start_time = datetime.datetime.now()
                # print(board)
                label1["text"] = "步数：" + str(steps)
                cv.delete('all')
                # 清除画布上的内容
                drawBoard(cv)
                #if steps == 20:
                    #swap(5, 3, r, c)


        if win():

            end_time = datetime.datetime.now()
            interval = (end_time - start_time).seconds
            file_object = open('D:\puzzlegame\\record.txt', 'a')
            file_object.write('步数: ' + str(steps) +' 耗时: ' + str(interval) + 's\n')
            file_object.close()
            steps = 0

            showinfo(title="恭喜", message="你成功了！ 用时" + str(interval) + 's')


    def win():
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] is not None and board[i][j].orderID != i * ROWS + j:
                    return False
        return True

    def play_game():
        global steps
        steps = 0
        init_board()

    def callBack2():
        print("重新开始")
        play_game()
        cv.delete('all')
        # 清除画布上的内容
        drawBoard(cv)
        wid = int(gameRect.width)

    path = "D:\software_practice\无框字符\\test(16).jpg"
    image1 = Image.open(path)  # 通过Image=photo设置要展示的图片
    photo1: PhotoImage = ImageTk.PhotoImage(image1)  # 创建tkinter兼容的图片
    cv = Canvas(root, bg='green', width=WIDTH, height=HEIGHT)
    bl = Button(root, text="重新开始", command=callBack2, width=gameRect.width // 7)
    b2 = Label(root, image=photo1, width=0)
    label1 = Label(root, text="步数：" + str(steps), fg="red", width=40)
    label1.pack()
    cv.bind("<Button-1>", mouseclick)
    cv.pack(side='right')
    bl.pack()

    # b2.pack()
    b2.place(y=150, width=gameRect.width, height=gameRect.height)
    play_game()
    drawBoard(cv)
    root.mainloop()

def game_loop():
    x = display_width * 0.45
    y = display_height * 0.8
    x_change = 0

    dodged = 0

    gameExit = False

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)
        car(x, y)

        if x > display_width - car_width or x < 0:
            gameExit = True

        pygame.display.update()
        clock.tick(60)


# crash()
game_intro()
game_loop()
pygame.quit()
quit()
