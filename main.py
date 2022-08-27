from turtle import Turtle, Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time 

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down,"Down")

game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    for cars in car.all_cars : 
        if cars.distance(player) < 20 : 
            game_running = False
            scoreboard.game_over()
            

    if player.is_at_finish_line() : 
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()