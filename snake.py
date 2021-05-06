from turtle import Screen, Turtle

# Set up constants, move distance is 20px at a time, define starting position. Direction constants for reptile movement
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT =180
RIGHT = 0

# Create the reptile class, init creates the body segment list then defines the reptiles head for movement purposes.
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]

# move each segment forward following the head
    def move(self):

        for seg_num in range(len(self.segments) - 1, 0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

# Create a new limbless reptile
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

# Move the reptile, can't turn it back on itself
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

# call add segment function, define position to add it to
    def extend(self):
        self.add_segment(self.segments[-1].position())

# function to add segment to the end of the tail
    def add_segment(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

# reset position and size
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]