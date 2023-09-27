from turtle import Screen
import turtle
import time
import snake
import food
import winsound
import scoreboard



#screen options
screen = Screen()
screen.bgpic("background.gif")
screen.setup(width=600,height=600)
screen.title("Snake game")
screen.tracer(0)

#snake options
size = 3
snake = snake.Snake(size)

#food options
food = food.Food()

#score oiptions
score = scoreboard.Scoreboard()

turtle.listen()
turtle.onkey(key="w",fun=snake.move_up)
turtle.onkey(key="s",fun=snake.move_down)
turtle.onkey(key="d",fun=snake.move_right)
turtle.onkey(key="a",fun=snake.move_left)

game_end = False
while not game_end:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #cheeck eat food
    if snake.head.distance(food) < 15:
        score.score+=1
        score.update_score()
        winsound.PlaySound("eat_food.wav", winsound.SND_ASYNC) 
        food.new_location()
        snake.add_body()
    
    #check eat self
    for i in range(2,len(snake.bodies)):
        if snake.head.distance(snake.bodies[i]) < 1 or snake.check_gameover():
            score.reset_score()
            winsound.PlaySound("gameover.wav", winsound.SND_FILENAME)
            snake.reset(size)
            break




screen.exitonclick()