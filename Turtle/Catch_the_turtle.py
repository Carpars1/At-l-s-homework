import turtle
import random


# Oyun parametreleri
score = 0
game_time = 30  # 30 saniyelik oyun süresi

# Ekranı ayarla
window = turtle.Screen()
window.title("Catch the Turtle")
window.bgcolor("lightblue")
window.setup(width=600, height=600)

# Kaplumbağayı ayarla
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()

# Skor ve zaman gösteren turtle objeleri
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-250, 250)
score_writer.write(f"Skor: {score}", font=("Arial", 16, "normal"))

timer_writer = turtle.Turtle()
timer_writer.hideturtle()
timer_writer.penup()
timer_writer.goto(150, 250)
timer_writer.write(f"Zaman: {game_time}", font=("Arial", 16, "normal"))

# Kaplumbağanın kaçmasını sağlayan fonksiyon
def move_turtle():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    t.goto(x, y)

# Kaplumbağaya tıkladığında skoru artıran fonksiyon
def clicked(x, y):
    global score
    score += 1
    score_writer.clear()
    score_writer.write(f"Skor: {score}", font=("Arial", 16, "normal"))
    move_turtle()

# Zamanlayıcı fonksiyonu
def countdown():
    global game_time
    if game_time > 0:
        game_time -= 1
        timer_writer.clear()
        timer_writer.write(f"Zaman: {game_time}", font=("Arial", 16, "normal"))
        window.ontimer(countdown, 1000)
    else:
        t.hideturtle()

        window.bye()  # Oyunu kapat

# Oyun başlangıcı
def start_game():
    move_turtle()
    countdown()
    t.onclick(clicked)

# Oyunu başlat
start_game()

# Oyun ekranını açık tut
window.mainloop()
