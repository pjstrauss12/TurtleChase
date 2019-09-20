import superturtle, turtle
 
turtle.setup(500,500)
wn = turtle.Screen() 
wn.title("Turtle Chase!") 
wn.bgcolor("pink")

player_one = superturtle.SuperTurtle()
player_two = superturtle.SuperTurtle()

#make announcements
player_one.write("    Bet you can't catch me!", font=('Arial', 12, 'bold'))
player_two.write("    GET OVER HERE!")

# helper functions
def quit_window():
   wn.bye() 

def check():
   print("checking")
   keep_on_screen()
   collision()
   wn.ontimer(check, 10)

def keep_on_screen():
   #check player_one on all four angles
   if player_one.xcor() < -250:
      player_one.goto(-249, player_one.ycor())
   if player_one.xcor() > 250:
      player_one.goto(249, player_one.ycor())
   if player_one.ycor() < -250:
      player_one.goto(player_one.xcor(), -249)
   if player_one.ycor() > 250:
      player_one.goto(player_one.xcor(), 249)
   #check player_two on all four angles
   if player_two.xcor() < -250:
      player_two.goto(-249, player_two.ycor())
   if player_two.xcor() > 250:
      player_two.goto(249, player_two.ycor())
   if player_two.ycor() < -250:
      player_two.goto(player_two.xcor(), -249)
   if player_two.ycor() > 250:
      player_two.goto(player_two.xcor(), 249)

def collision():
   x_diff = abs(player_one.xcor() - player_two.xcor())
   y_diff = abs(player_one.ycor() - player_two.ycor())
   if x_diff < 20 and y_diff < 20:
      quit_window()

# PLAYER ONE CONTROLS
wn.onkey(player_one.move_forward, "Up")
wn.onkey(player_one.turn_left, "Left")
wn.onkey(player_one.turn_right, "Right")
wn.onkey(player_one.home, "Down") #jump to middle of screen

# PLAYER TWO CONTROLS
wn.onkey(player_two.move_forward, "w")
wn.onkey(player_two.turn_left, "a")
wn.onkey(player_two.turn_right, "d")
wn.onkey(player_two.home, "s")

# GAME CONTROLS
wn.onkey(quit_window, "q")

wn.listen()
# check for collision and out of bounds
check()
wn.mainloop()