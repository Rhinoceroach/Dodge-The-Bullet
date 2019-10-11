#Imports
from tkinter import *
from tkinter import messagebox
import random

#Classes
class Player:
    def __init__(self,x,y,size,xSpeed,ySpeed,maxHp,color="red",direction="",player=""):
        self.x = x
        self.y = y
        self.size = size
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.maxHp = maxHp
        self.hp = maxHp
        self.direction = direction
        self.player = c.create_rectangle(x,y,x+size,y+size,width = size,outline=color,fill="")
        

    def move(self,c,direction):
        if direction == "n":
            if not self.y <= 10:
                c.move(self.player, 0,-self.ySpeed)
                self.y -= self.ySpeed
        elif direction == "w":
            if not self.x <= 10:
                c.move(self.player, -self.xSpeed,0)
                self.x -= player.xSpeed
        elif direction == "s":
            if not self.y >= 490:
                c.move(self.player, 0,self.ySpeed)
                self.y += self.ySpeed
        elif direction == "e":
            if not self.x >= 490:
                c.move(self.player, self.xSpeed,0)
                self.x += self.xSpeed
        c.update()

class Enemy:
    def __init__(self,x,y,size,xSpeed,ySpeed,color="blue",enemy=""):
        self.x = x
        self.y = y
        self.size = size
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.color = color
        self.enemy = ""

    def move(self,moveX,moveY):
        c.move(self.enemy,moveX,moveY)
        self.x += moveX
        self.y += moveY

    def redraw(self,c):
        c.delete(self.enemy)
        self.enemy = c.create_rectangle(self.x,self.y,self.x+self.size,self.y + self.size,width = self.size,outline=self.color,fill=self.color)

    def spawn(self,minx,miny,maxx,maxy):
        self.x = random.randint(minx,maxx)
        self.y = random.randint(miny,maxy)

    def createGhost(self):
        self.enemy = c.create_rectangle(self.x,self.y,self.x+self.size,self.y + self.size,width = self.size,outline="white",fill="black")

    def unGhost(self):
        c.delete(self.enemy)
        self.enemy = c.create_rectangle(self.x,self.y,self.x+self.size,self.y + self.size,width = self.size,outline=self.color,fill=self.color)

class Food:
    def __init__(self,x,y,size,color="yellow",food=""):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.food = c.create_rectangle(self.x,self.y,self.x+self.size,self.y + self.size,width = self.size,outline=self.color,fill=self.color)

    def spawn(self,minx,maxx,miny,maxy):
        c.delete(self.food)
        self.x = random.randint(minx,maxx)
        self.y = random.randint(miny,maxy)
        self.food = c.create_rectangle(self.x,self.y,self.x+self.size,self.y + self.size,width = self.size,outline=self.color,fill=self.color)
        
#Functions
def hitDetect(x1,y1,x2,y2):
    hit = False
    if (x1 <= x2 + 19 and x1 >= x2 - 19) and (y1 <= y2 + 19 and y1 >= y2 - 19):
        hit = True
    return hit

def updateHp(hpbar):
    c.coords(hpbar,100,450,percenthp.get()*3+100,470)

def damagePlayer(hpbar):
    player.hp -= 1
    if time.get() > 1000 and player.hp != 0:
        player.hp -= 1
    percenthp.set(player.hp/player.maxHp*100)
    updateHp(hpbar)
    if player.hp <= 0:
        endGame()

def endGame():
    messagebox.showinfo("Console","Score: "+str(score.get()))
    pause.set(True)

def borders(enemy):
    if (enemy.y <= 10 or enemy.y >= 490):
        enemy.ySpeed *= -1
    if (enemy.x <= 10 or enemy.x >= 490):
        enemy.xSpeed *= -1
        
def track(enemy):
    if player.x > enemy.x and player.y > enemy.y:
        enemy.move(enemy.xSpeed,enemy.ySpeed)
        
    elif player.x < enemy.x and player.y > enemy4.y:
        enemy.move(-enemy.xSpeed,enemy.ySpeed)
        
    elif player.x > enemy.x and player.y < enemy4.y:
        enemy.move(enemy.xSpeed,-enemy.ySpeed)
        
    elif player.x < enemy.x and player.y < enemy4.y:
        enemy.move(-enemy.xSpeed,-enemy.ySpeed)
        
    elif player.x > enemy.x:
        enemy.move(enemy.xSpeed,0)
        
    elif player.x < enemy.x:
        enemy.move(-enemy.xSpeed,0)
        
    elif player.y > enemy.y:
        enemy.move(0,enemy.ySpeed)
        
    else:
        enemy.move(0,-enemy.ySpeed)

def animate():
    if not pause.get():
        if hitDetect(player.x,player.y,food.x,food.y):
            score.set(score.get()+50)
            coins.set(coins.get()+1)
            strCoins.set(value="Coins: "+str(coins.get()))
            food.spawn(30,470,30,470)

        if time.get() == 1000:
            enemy1.color = "red"
            enemy2.color = "red"
            enemy3.color = "red"
            enemy4.color = "grey"
            enemy5.color = "red"
            enemy6.color = "red"
            enemy1.xSpeed = round(enemy1.xSpeed*1.2)
            enemy2.xSpeed = round(enemy2.xSpeed*1.2)
            enemy3.xSpeed = round(enemy3.xSpeed*1.2)
            enemy5.xSpeed = round(enemy5.xSpeed*1.2)
            enemy6.xSpeed = round(enemy6.xSpeed*1.2)
            enemy1.ySpeed = round(enemy1.xSpeed*1.2)
            enemy2.ySpeed = round(enemy2.xSpeed*1.2)
            enemy3.ySpeed = round(enemy3.xSpeed*1.2)
            enemy5.ySpeed = round(enemy5.xSpeed*1.2)
            enemy6.ySpeed = round(enemy6.xSpeed*1.2)
            enemy1.redraw(c)
            enemy2.redraw(c)
            enemy3.redraw(c)
            enemy4.redraw(c)
            enemy5.redraw(c)
            enemy6.redraw(c)

        elif time.get() == 500:
            enemy6.unGhost()
        elif time.get() == 450:
            enemy6.spawn(30,30,470,470)
            enemy6.createGhost()
        elif time.get() == 400:
            enemy5.unGhost()
        elif time.get() == 350:
            enemy5.spawn(30,30,470,470)
            enemy5.createGhost()
        elif time.get() == 300:
            enemy4.unGhost()
        elif time.get() == 250:
            enemy4.spawn(30,30,470,470)
            enemy4.createGhost()
        elif time.get() == 200:
            enemy3.unGhost()
        elif time.get() == 150:
            enemy3.spawn(30,30,470,470)
            enemy3.createGhost()
        elif time.get() == 100:
            enemy2.unGhost()
        elif time.get() == 50:
            enemy1.unGhost()
            enemy2.spawn(30,30,470,470)
            enemy2.createGhost()
        elif time.get() == 0:
            enemy1.spawn(30,30,470,470)
            enemy1.createGhost()

        if time.get() > 500:
            borders(enemy6)
            if hitDetect(player.x,player.y,enemy6.x,enemy6.y):
                damagePlayer(hpbar)
            enemy6.move(enemy6.xSpeed,enemy6.ySpeed)

            borders(enemy5)
            if hitDetect(player.x,player.y,enemy5.x,enemy5.y):
                damagePlayer(hpbar)
            enemy5.move(enemy5.xSpeed,enemy5.ySpeed)

            if hitDetect(player.x,player.y,enemy4.x,enemy4.y):
                damagePlayer(hpbar)
            track(enemy4)

            borders(enemy3)
            if hitDetect(player.x,player.y,enemy3.x,enemy3.y):
                damagePlayer(hpbar)
            enemy3.move(enemy3.xSpeed,enemy3.ySpeed)

            borders(enemy2)
            if hitDetect(player.x,player.y,enemy2.x,enemy2.y):
                damagePlayer(hpbar)
            enemy2.move(enemy2.xSpeed,enemy2.ySpeed)

            borders(enemy1)
            if hitDetect(player.x,player.y,enemy1.x,enemy1.y):
                damagePlayer(hpbar)
            enemy1.move(enemy1.xSpeed,enemy1.ySpeed)

        elif time.get() > 400:
            borders(enemy5)
            if hitDetect(player.x,player.y,enemy5.x,enemy5.y):
                damagePlayer(hpbar)
            enemy5.move(enemy5.xSpeed,enemy5.ySpeed)

            if hitDetect(player.x,player.y,enemy4.x,enemy4.y):
                damagePlayer(hpbar)
            track(enemy4)

            borders(enemy3)
            if hitDetect(player.x,player.y,enemy3.x,enemy3.y):
                damagePlayer(hpbar)
            enemy3.move(enemy3.xSpeed,enemy3.ySpeed)

            borders(enemy2)
            if hitDetect(player.x,player.y,enemy2.x,enemy2.y):
                damagePlayer(hpbar)
            enemy2.move(enemy2.xSpeed,enemy2.ySpeed)

            borders(enemy1)
            if hitDetect(player.x,player.y,enemy1.x,enemy1.y):
                damagePlayer(hpbar)
            enemy1.move(enemy1.xSpeed,enemy1.ySpeed)

        elif time.get() > 300:
            if hitDetect(player.x,player.y,enemy4.x,enemy4.y):
                damagePlayer(hpbar)
            track(enemy4)

            borders(enemy3)
            if hitDetect(player.x,player.y,enemy3.x,enemy3.y):
                damagePlayer(hpbar)
            enemy3.move(enemy3.xSpeed,enemy3.ySpeed)

            borders(enemy2)
            if hitDetect(player.x,player.y,enemy2.x,enemy2.y):
                damagePlayer(hpbar)
            enemy2.move(enemy2.xSpeed,enemy2.ySpeed)

            borders(enemy1)
            if hitDetect(player.x,player.y,enemy1.x,enemy1.y):
                damagePlayer(hpbar)
            enemy1.move(enemy1.xSpeed,enemy1.ySpeed)

        elif time.get() > 200:
            borders(enemy3)
            if hitDetect(player.x,player.y,enemy3.x,enemy3.y):
                damagePlayer(hpbar)
            enemy3.move(enemy3.xSpeed,enemy3.ySpeed)

            borders(enemy2)
            if hitDetect(player.x,player.y,enemy2.x,enemy2.y):
                damagePlayer(hpbar)
            enemy2.move(enemy2.xSpeed,enemy2.ySpeed)

            borders(enemy1)
            if hitDetect(player.x,player.y,enemy1.x,enemy1.y):
                damagePlayer(hpbar)
            enemy1.move(enemy1.xSpeed,enemy1.ySpeed)

        elif time.get() > 100:
            borders(enemy2)
            if hitDetect(player.x,player.y,enemy2.x,enemy2.y):
                damagePlayer(hpbar)
            enemy2.move(enemy2.xSpeed,enemy2.ySpeed)

            borders(enemy1)
            if hitDetect(player.x,player.y,enemy1.x,enemy1.y):
                damagePlayer(hpbar)
            enemy1.move(enemy1.xSpeed,enemy1.ySpeed)

        elif time.get() > 50:
            borders(enemy1)
            if hitDetect(player.x,player.y,enemy1.x,enemy1.y):
                damagePlayer(hpbar)
            enemy1.move(enemy1.xSpeed,enemy1.ySpeed)

        player.move(c,player.direction)

        time.set(time.get()+1)
        score.set(score.get()+1)
        
        master.after(33, animate)

def increaseMaxHP(player,hpbar):
    if coins.get() >= 5:
        player.maxHp += 2
        coins.set(coins.get() - 5)
        strCoins.set(value="Coins: "+str(coins.get()))
        percenthp.set(player.hp/player.maxHp*100)
        updateHp(hpbar)

def healPlayer(player,hpbar):
    if coins.get() >= 10:
        player.hp = player.maxHp
        coins.set(coins.get() - 10)
        strCoins.set(value="Coins: "+str(coins.get()))
        percenthp.set(player.hp/player.maxHp*100)
        updateHp(hpbar)

def increasePlayerSpeed(player):
    if coins.get() >= 5:
        player.xSpeed = round(player.xSpeed * 1.2)
        player.ySpeed = round(player.ySpeed * 1.2)
        coins.set(coins.get() - 5)
        strCoins.set(value="Coins: "+str(coins.get()))

def keyPressed(event):
    if event.char == "w":
        player.direction = "n"
    elif event.char == "a":
        player.direction = "w"
    elif event.char == "s":
        player.direction = "s"
    elif event.char == "d":
        player.direction = "e"
    elif event.char == "r":
        if pause.get():
            c.itemconfigure(increaseHp,state="hidden")
            c.itemconfigure(heal,state="hidden")
            c.itemconfigure(increaseSpeed,state="hidden")
            pause.set(False)
            animate()
        else:
            c.itemconfigure(increaseHp,state="normal")
            c.itemconfigure(heal,state="normal")
            c.itemconfigure(increaseSpeed,state="normal")
            pause.set(True)

#Main Program
master = Tk()
master.title("Dodge the bullet")
master.resizable(False,False)
c = Canvas(master, width = 500, height = 500)
x = 10
y = 10
score = IntVar()
score.set(0)
time = IntVar()
time.set(0)
coins = IntVar()
coins.set(0)
strCoins = StringVar()
strCoins.set(value="Coins: "+str(coins.get()))
pause = BooleanVar()
pause.set(False)

hpImage = PhotoImage(file="hp.png")
healImage = PhotoImage(file="heal.png")
speedImage = PhotoImage(file="speed.png")
increaseHp = c.create_image(250,250,image=hpImage)
heal = c.create_image(400,250,image=healImage)
increaseSpeed = c.create_image(100,250,image=speedImage)
player = Player(10,10,10,10,10,10)

food = Food(10,10,10)
food.spawn(30,470,30,470)

spd = random.randint(5,20)
enemy1 = Enemy(10,10,10,spd,25-spd)
spd = random.randint(5,20)
enemy2 = Enemy(10,10,10,spd,25-spd)
spd = random.randint(5,20)
enemy3 = Enemy(10,10,10,spd,25-spd)
enemy4 = Enemy(10,10,10,2,2,"green")
spd = random.randint(5,20)
enemy5 = Enemy(10,10,10,spd,25-spd)
spd = random.randint(5,20)
enemy6 = Enemy(10,10,10,spd,25-spd)

percenthp = IntVar()
percenthp.set(player.hp/player.maxHp*100)
hpbar = c.create_rectangle(100,450,percenthp.get()*3+100,470,fill="red")
maxhpbar = c.create_rectangle(100,450,400,470)
Label(master,textvariable = strCoins).place(x=445,y=470)

c.tag_bind(increaseSpeed,"<Button-1>",lambda x:increasePlayerSpeed(player))
c.tag_bind(increaseHp,"<Button-1>",lambda x:increaseMaxHP(player,hpbar))
c.tag_bind(heal,"<Button-1>",lambda x:healPlayer(player,hpbar))
c.bind("<Key>", keyPressed)
c.pack()
c.focus_set()

c.itemconfigure(increaseHp,state="hidden")
c.itemconfigure(heal,state="hidden")
c.itemconfigure(increaseSpeed,state="hidden")

animate()
master.mainloop()
