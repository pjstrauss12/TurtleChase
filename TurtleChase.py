import superturtle, turtle
 
turtle.setup(500,500)
wn = turtle.Screen() 
wn.title("Turtle Chase!") 
wn.bgcolor("pink")

player_one = superturtle.SuperTurtle()
player_two = superturtle.SuperTurtle()

# helper functions
def quit_window():
   wn.bye() 

# PLAYER ONE CONTROLS
wn.onkey(player_one.move_forward, "Up")
wn.onkey(player_one.turn_left, "Left")
wn.onkey(player_one.turn_right, "Right")

# PLAYER TWO CONTROLS
wn.onkey(player_two.move_forward, "w")
wn.onkey(player_two.turn_left, "a")
wn.onkey(player_two.turn_right, "d")

# GAME CONTROLS
wn.onkey(quit_window, "q")

wn.listen()
wn.mainloop()