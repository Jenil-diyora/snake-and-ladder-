from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox

def load_dice_images():
    global Dice
    names = ["1.png","2.png","3.png","4.png","5.png","6.png"]
    for i in names:
        dice_images = Image.open("images/"+i)
        dice_images = dice_images.resize((50,50))
        dice_images = ImageTk.PhotoImage(dice_images)
        Dice.append(dice_images)
        
def roll_dice():
    global Dice
    global turn
    global pos1,pos2
    global btn_player1,btn_player2
    global start,start1
    global Snake,Ladder

    r = random.randint(1,6)
    dice = Button(root,image=Dice[r - 1])
    dice.place(x=1200,y=300)
    if turn == 1:
        if r == 1 and start == 1:
            pos1 = pos1 + r
            move_player(turn,pos1)
            start = 2
        elif(pos1 > 0):
            if(pos1 + r) <= 100:
                pos1 = pos1 + r
                move_player(turn,pos1)
            if pos1 in Ladder:
                pos1 = Ladder[pos1]
                move_player(turn,pos1)
            if pos1 in Snake:
                pos1 = Snake[pos1]
                move_player(turn,pos1)
        if r != 6:
            turn = 2 
            btn_player2.config(state=NORMAL)
            btn_player1.config(state="disabled")
    else:
        if r == 1 and start1 == 1:
            pos2 = pos2 + r
            move_player(turn,pos2)
            start1 = 2
        elif(pos2 > 0):
            if(pos2 + r) <= 100:
                pos2 = pos2 + r
                move_player(turn,pos2)
            if pos2 in Ladder:
                pos2 = Ladder[pos2]
                move_player(turn,pos2)
            if pos2 in Snake:
                pos2 = Snake[pos2]
                move_player(turn,pos2)
        if r != 6:
            turn = 1
            btn_player1.config(state=NORMAL)
            btn_player2.config(state="disabled")

    if pos1 == 100:
        Winner = messagebox.showinfo("Alert","Green player is winner 👑")
        btn_player1.config(state="disabled")
        btn_player2.config(state="disabled")
    elif pos2 == 100:
        Winner = messagebox.showinfo("Alert","Red player is winner 👑")
        btn_player1.config(state="disabled")
        btn_player2.config(state="disabled")
            
def move_player(Turn,pos):
    global canvas,canvas1

    if Turn == 1:
        canvas.place(x=Index[pos][1],y=Index[pos][0])
    else:
        canvas1.place(x=Index[pos][1],y=Index[pos][0])

def get_index():
    global canvas, canvas1,Index
    # canvas.place(x=25,y = 745)

    Nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
            80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
            60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
            40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    row = 25
    i = 0

    for x in range(1, 11):
        col = 25

        for y in range(1, 11):
            Index[Nums[i]] = (row, col)
            col = col + 80
            i += 1
        row = row + 80
    

def reset_players_pos():
    global canvas,canvas1
    global pos1,pos2
    canvas.place(x=1,y=800)
    canvas1.place(x=50,y=800)
    pos1 = 0
    pos2 = 0

Ladder = {4:25,13:46,33:49,42:63,50:69,62:81,74:92}

Snake = {27:5,40:3,43:18,54:31,66:45,89:53,95:77,99:41}


Dice = []

Index = {}

pos1 = None
pos2 = None



root = Tk()
root.geometry("1900x960")

background_image = Image.open("images/background6.png")
background_image = background_image.resize((1920,1080))
background_image = ImageTk.PhotoImage(background_image)
background_img = Label(root,image=background_image)
background_img.place(x=0,y=0)

board_image = Image.open("images/board6.png")
board_image = ImageTk.PhotoImage(board_image)

main_frame = Frame(root)
main_frame.place(x=0,y=0)

label = Label(main_frame, image=board_image)
label.pack()

# player positions
canvas = Canvas(root, width=40, height=40)
canvas.create_oval(10, 10, 40, 40, outline="darkgreen", fill="green", width=2)
canvas1 = Canvas(root, width=40, height=40)
canvas1.create_oval(10, 10, 40, 40, outline="red", fill="red", width=2)

turn = 1
start = 1
start1 = 1

# players button
btn_player1 = Button(root,text="Player-1",height=2,width=20,background="green",activebackground="lightgreen",font="cursive 14 bold",command=roll_dice)
btn_player1.place(x=1100,y=500)
btn_player2 = Button(root,text="Player-2",height=2,width=20,background="red",activebackground="pink",font="cursive 14 bold",command=roll_dice)
btn_player2.place(x=1100,y=600)



# exit button
Exit = Button(root,text="CLICK HEAR TO END GAME",height=2,width=22,background="blue",fg="white",activebackground="cyan",command=root.destroy,font="cursive 14 bold")
Exit.place(x=1090,y=50)


# dice images and button
dice_images = Image.open("images/1.png")
dice_images = dice_images.resize((50,50))
dice_images = ImageTk.PhotoImage(dice_images)

dice = Button(root,image=dice_images)
dice.place(x=1200,y=300)
reset_players_pos()
load_dice_images()

get_index()


root.mainloop()