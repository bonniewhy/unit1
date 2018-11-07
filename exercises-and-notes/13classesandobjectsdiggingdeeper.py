# NOTE TAKING ---
# A function that is used in a class, but is not a part of a class, is called
# ----- a helper function.
# A method that doesn't return anything, but instead modifies the object itself
# ----- is called a mutator method because it mutates or changes the internal
# ----- state of the object.
# Shallow equality compares only the references, not the contents, of the
# ----- objects. They are only equal (==) if they are the same object.
# Deep equality compares the values "deep" in the object, not just the reference
# ----- to the object.
# One of the core principles of good program design is that you should strive
# ----- to repeat yourself as little as possible. We called this principle "DRY".
# In general, the syntax for any subclass that inherits from some superclass is:
# ----- class Subclass(Superclass):
# ----- # method definitions for Subclass
# To recap: inheritance allows you to define new types like "Tiger" by extending
# ----- the code from previously defined types like "Cat". A subclass like "Tiger"
# ----- inherits all the functionality of its superclass, but can additionally
# ----- define its own new attributes and methods (such as angry method), and
# ----- can override the implementation of preexisting methods (such as the 
# ----- "noise" method).

# __________________________________________________________________________

# CLASS NOTES: )

#___________________________________________________________________________
# TURTLE STAR EXAMPLES

#import turtle

#class StarTurtle(turtle.Turtle):

#    def star(self, numpoints, radius):
#        for i in range(0, numpoints):
#            self.forward(radius)
#            self.back(radius)
#            self.left(360 / numpoints)

#def main():
#    wn = turtle.Screen()
#    wn.bgcolor("black")

#    tess = StarTurtle()
#    tess.color("yellow")

#    # draw a star
#    tess.star(7, 60)

#    # move somewhere else
#    tess.penup()
#    tess.forward(30)
#    tess.left(45)
#    tess.pendown()

#    #draw another star
#    tess.color("hot pink")
#    tess.star(14, 45)

#    # and one more
#    tess.color("white")
#    tess.star(15, 30)

#if __name__ == "__main__":
#    main()

# ___________________________________________________________________________
# CAT EXAMPLES
#class Cat:
    
#    def __init__(self):
#        # every Cat comes into this world tired and hungry
#        self.tired = True
#        self.hungry = True

#    def sleep(self):
#        self.tired = False
#        # a Cat always wakes up hungry
#        self.hungry = True

#    def eat(self):
#        if self.hungry:
#            self.hungry = False
#        else:
#            # eating when already full makes a Cat sleepy
#            self.tired = True

#    def noise(self):
#        # sleepy cats say prrrr, energized cats say meow!
#        if self.tired:
#            return "prrrr"
#        else:
#            return "meow!"

#class HouseCat(Cat):
#    def __init__(self, name):
#        # first, initialize as a normal Cat
#        Cat.__init__(self)
#        # then set the name attribute
#        self.name = name

#    def satisfied(self):
#        return not self.hungry and not self.tired

#    def noise(self):
#        if self.satisfied():
#            return "Hello, my name is " + self.name + "!"
#        else:
#            return Cat.noise(self)

#class Tiger(Cat): # notice that (Cat) in parentheses
#    def angry(self):
#        # a Tiger is angry whenever it is both hungry and tired
#        return self.tired and self.hungry

#    def noise(self):
#        # an angry Tiger says GRRRR!
#        if self.angry():
#            return "GRRRR!"
#        else:
#            # a non-angry Tiger behaves like a Cat
#            return Cat.noise(self)

#def main():
#    garfield = HouseCat("Garfield")
#    print("Garfield says:", garfield.noise())
#    garfield.sleep()
#    print("After sleeping, Garfield says:", garfield.noise())
#    garfield.eat()
#    print("After eating, Garfield says:", garfield.noise())
#    garfield.eat()
#    print("After eating again, Garfield says:", garfield.noise())

#    hobbes = Tiger()
#    print("Hobbes says:", hobbes.noise())
#    hobbes.sleep()
#    print("After sleeping, Hobbes says:", hobbes.noise())
#    hobbes.eat()
#    print("After eating, Hobbes still says:", hobbes.noise())
#    hobbes.eat()
#    print("After eating again, Hobbes says:", hobbes.noise())

#    tom = Cat()
#    print("Tom says:", tom.noise())
#    tom.sleep()
#    print("After sleeping, Tom says:", tom.noise())
#    tom.eat()
#    print("After eating, Tom still says:", tom.noise())
#    tom.eat()
#    print("After eating again, Tom says:", tom.noise())

#if __name__ == "__main__":
#    main()

# ___________________________________________________________________________
# FRACTION EXAMPLES
#def find_gcd(numerator, denominator):
#    while numerator % denominator != 0:
#        old_num = numerator
#        old_den = denominator

#        numerator = old_den
#        denominator = old_num % old_den

#    return denominator

#class Fraction:
    
#    def __init__(self, top, bottom):
#        self.num = top # the numerator is on the top
#        self.den = bottom # the denominator is on the bottom

#    def __str__(self):
#        return str(self.num) + "/" + str(self.den)

#    def get_numerator(self):
#        return self.num

#    def get_denominator(self):
#        return self.den

#    def simply(self):
#        common = find_gcd(self.num, self.den)

#        self.num = self.num // common
#        self.den = self.den // common

#    def __add__(self, fraction2):
#        new_num = self.num * fraction2.den + self.den * fraction2.num
#        new_den = self.den * fraction2.den

#        common = find_gcd(new_num, new_den)

#        return Fraction(new_num // common, new_den // common)

#def main():
#    f1 = Fraction(1, 2)
#    f2 = Fraction(1, 4)

#   f3 = f1 + f2
#    print(f3)

#if __name__ == "__main__":
#    main()

# _________________________________________________________________________

# Exercise 1 --
# We can represent a rectangle by knowing three things: the location of its
# lower left corner, its width, and its height. Create a class definition
# for a Rectangle class using this idea. For instance, to create a Rectangle
# object at location (4, 5) with width 6 and height 6, we would do the
# following...
#
# loc = Point(4, 5)
# r = Rectangle(loc, 6, 5)

#class Point:

#    def __init__(self, init_x, init_y):
#        """ Create a new point at the given coordinates. """
#        self.x = init_x
#        self.y = init_y

#    def get_x(self):
#        return self.x

#    def get_y(self):
#        return self.y

#    def distance_from_origin(self):
#        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#    def __repr__(self):
#        return "x=" + str(self.x) + ", y=" + str(self.y)

#class Rectangle:

#    def __init__(self, point, width, height):
#        self.location = point
#        self.width = width
#        self.height = height

#    def __repr__(self):
#        return "I am a rectangle with width {} and height {}".format(self.width, self.height)

#def main():
#    loc = Point(4, 5)
#    r = Rectangle(loc, 6, 5)
#    print(r)

#if __name__ == "__main__":
#    main()

# __________________________________________________________________________

# Exercise 2 --
# Add the following accessor methods to the Rectangle class: get_width and
# get_height.

#class Point:

#    def __init__(self, init_x, init_y):
#        """ Create a new point at the given coordinates. """
#        self.x = init_x
#        self.y = init_y

#    def get_x(self):
#        return self.x

#    def get_y(self):
#        return self.y

#    def distance_from_origin(self):
#        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#    def __repr__(self):
#        return "x=" + str(self.x) + ", y=" + str(self.y)

#class Rectangle:
#    def __init__(self, point, width, height):
#        self.location = point
#        self.width = width
#        self.height = height

#    def __repr__(self):
#        return "I am a rectangle with width {} and height {}.".format(self.width, self.height)

#    def get_width(self):
#        return self.width

#    def get_height(self):
#        return self.height

# __________________________________________________________________________

# Exercise 3 --
# Add a method area to the Rectangle class that returns the area of any
# instance:
#
# r = Rectangle(Point(0, 0), 10, 5)
# testEqual(r.area(), 50)

#class Point:

#    def __init__(self, init_x, init_y):
#        """ Create a new point at the given coordinates. """
#        self.x = init_x
#        self.y = init_y

#    def get_x(self):
#        return self.x

#    def get_y(self):
#        return self.y

#    def distance_from_origin(self):
#        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#    def __repr__(self):
#        return "x=" + str(self.x) + ", y=" + str(self.y)

#class Rectangle:
#    def __init__(self, point, width, height):
#        self.location = point
#        self.width = width
#        self.height = height

#    def __repr__(self):
#        return "I am a rectangle of width {} and height {}.".format(self.width, self.height)

#    def get_width(self):
#        return self.width

#    def get_height(self):
#        return self.height

#    def area(self):
#        return self.width * self.height

#from test import testEqual
#r = Rectangle(Point(0, 0), 10, 5)
#testEqual(r.area(), 50)

# __________________________________________________________________________

# Exercise 4 --
# Write a perimeter method in the Rectangle class so that we can find the
# perimeter of any rectangle instance:
#
# r = Rectangle(Point(0, 0), 10, 5)
# testEqual(r.perimeter(), 30)

#class Point:

#    def __init__(self, init_x, init_y):
#        """ Create a new point at the given coordinates. """
#        self.x = init_x
#        self.y = init_y

#    def get_x(self):
#        return self.x

#    def get_y(self):
#        return self.y

#    def distance_from_origin(self):
#        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#    def __repr__(self):
#        return "x=" + str(self.x) + ", y=" + str(self.y)

#class Rectangle:
    
#    def __init__(self, point, width, height):
#        self.location = point
#        self.width = width
#        self.height = height

#    def __repr__(self):
#        return "I am a rectangle with width {} and height {}.".format(self.width, self.height)

#    def get_width(self):
#        return self.width

#    def get_height(self):
#        return self.height
    
#    def area(self):
#        return self.width * self.height

#    def perimeter(self):
#        return (self.width * 2) + (self.height * 2)
    


#from test import testEqual
#r = Rectangle(Point(0, 0), 10, 5)
#testEqual(r.perimeter(), 30)

# __________________________________________________________________________

# Exercise 5 --
# Write a transpose method in the Rectangle class that swaps the width and
# the height of any rectangle instance:
#
# r = Rectangle(Point(100, 5), 10, 5)
# testEqual(r.width, 10)
# testEqual(r.height, 5)
# r.transpose()
# testEqual(r.width, 5)
# testEqual(r.height, 10)

#class Point:

#    def __init__(self, init_x, init_y):
#        """ Create a new point at the given coordinates. """
#        self.x = init_x
#        self.y = init_y

#    def get_x(self):
#        return self.x

#    def get_y(self):
#        return self.y

#    def distance_from_origin(self):
#        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#    def __repr__(self):
#        return "x=" + str(self.x) + ", y=" + str(self.y)

#class Rectangle:

#    def __init__(self, point, width, height):
#        self.location = point
#        self.width = width
#        self.height = height

#    def __repr__(self):
#        return "I am a rectangle with width {} and height {}.".format(self.width, self.height)

#    def get_width(self):
#        return self.width

#    def get_height(self):
#        return self.height

#    def area(self):
#        return self.width * self.height

#    def perimeter(self):
#        return (self.width * 2) + (self.height * 2)

#    def transpose(self):
#        init_width = self.width
#        init_height = self.height

#        self.width = init_height
#        self.height = init_width

#from test import testEqual
#r = Rectangle(Point(100, 50), 10, 5)
#testEqual(r.width, 10)
#testEqual(r.height, 5)
#r.transpose()
#testEqual(r.width, 5)
#testEqual(r.height, 10)

# _________________________________________________________________________

# Exercise 6 --
# Write a new method called contains in the Rectangle class to test if a
# Point falls within the rectangle. For this exercise, assume that a
# rectangle at (0,0) with width 10 and height 5 has open upper bounds on the
# width and height, i.e. it stretches in the x direction from [0 to 10],
# where 0 is included but 10 is excluded, and from [0 to 5] in the y
# direction. So it does not contain the point (10, 2). These tests should
# pass.

# r = Rectangle(Point(0, 0), 10, 5)
# testEqual(r.contains(Point(0, 0)), True)
# testEqual(r.contains(Point(3, 3)), True)
# testEqual(r.contains(Point(3, 7)), False)
# testEqual(r.contains(Point(3, 5)), False)
# testEqual(r.contains(Point(3, 4.99999)), True)
# testEqual(r.contains(Point(-3, -3)), False)

#from test import testEqual

#class Point:

#    def __init__(self, init_x, init_y):
#        """ Create a new point at the given coordinates. """
#        self.x = init_x
#        self.y = init_y

#    def get_x(self):
#        return self.x

#    def get_y(self):
#        return self.y

#    def distance_from_origin(self):
#        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#    def __repr__(self):
#       return "x=" + str(self.x) + ", y=" + str(self.y)

#class Rectangle:

#    def __init__(self, point, width, height):
#        self.location = point
#        self.width = width
#        self.height = height

#    def __repr__(self):
#        return "I am a rectangle with width {} and height {}.".format(self.width, self.height)

#    def get_location(self):
#        return self.location
    
#    def get_width(self):
#        return self.width

#    def get_height(self):
#        return self.height

#    def area(self):
#        return self.width * self.height
    
#    def perimeter(self):
#        return (self.width * 2) + (self.height * 2)

#    def transpose(self):
#        init_width = self.width
#        init_height = self.height

#        self.width = init_height
#        self.height = init_width

#    def contains(self, point):
#        if self.location.get_x() + self.width > point.get_x() and self.location.get_x() <= point.get_x():
#            if self.location.get_y() + self.height > point.get_y() and self.location.get_y() <= point.get_y():
#                return True
#            else:
#                return False
#        else:
#            return False

# IN CLASS DEMO ----------------------------------------------------------------------

#    def contains(self, point):
#        or_x = self.location.get_x()
#        or_y = self.location.get_y()
#        x_limit = or_x + self.width # establish the bounds
#        y_limit = or_y + self.height

#        return or_x <= point.x < x_limit and or_y <= point.y < y_limit

#def main():
#    r = Rectangle(Point(0, 0), 10, 5)
#    print(r.contains(Point(0, 0)), True)
#    print(r.contains(Point(3, 3)), True)
#    print(r.contains(Point(3, 7)), False)
#    print(r.contains(Point(3, 5)), False)
#    print(r.contains(Point(3, 4.99999)), True)
#    print(r.contains(Point(-3, -3)), False)

#if __name__ == "__main__":
#    main()

# I used "get_x" and "get_y" which Johnathan said was "good practice".


# __________________________________________________________________________

# Exercise 7 --
# Write a new method called diagonal that will return the length of the
# diagonal that runs from the lower left corner and the opposite corner.

#class Point:

#    def __init__(self, init_x, init_y):
#        """ Create a new point at the given coordinates. """
#        self.x = init_x
#        self.y = init_y

#    def get_x(self):
#        return self.x

#    def get_y(self):
#        return self.y

#    def distance_from_origin(self):
#        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#    def distance_from_point(self, new_point):
#        x_difference = new_point.get_x() - self.x
#        y_difference = new_point.get_y() - self.y
#        return ((x_difference ** 2) + (y_difference ** 2)) ** 0.5

#    def __repr__(self):
#        return "x=" + str(self.x) + ", y=" + str(self.y)

#class Rectangle:

#    def __init__(self, point, width, height):
#        self.location = point
#        self.width = width
#        self.height = height

#    def get_width(self):
#        return self.width

#    def get_height(self):
#        return self.height

#    def area(self):
#        return self.width * self.height

#    def perimeter(self):
#        return (self.width * 2) + (self.height * 2)

#    def transpose(self):
#        init_width = self.width
#        init_height = self.height

#        self.width = init_height
#        self.height = init_width

#    def contains(self, point):
#        if self.location.get_x() + self.width > point.get_x() and self.location.get_x() <= point.get_x():
#            if self.location.get_y() + self.height > point.get_y() and self.location.get_y() <- point.get_y():
#                return True
#            else:
#                return False
#        else:
#            return False

#    def diagonal(self):
#        x_difference = self.width - self.location.get_x()
#        y_difference = self.height - self.location.get_y()
#        return ((x_difference ** 2) + (y_difference ** 2)) ** 0.5

#from test import testEqual
#r = Rectangle(Point(0, 0), 10, 5)
#testEqual(r.diagonal(), 11.1803398875)

#r1 = Rectangle(Point(0,0), 12, 4)
#testEqual(r1.diagonal(), 12.6491106407)

#r2 = Rectangle(Point(0,0), 1,2)
#testEqual(r2.diagonal(), 2.2360679775)

# __________________________________________________________________________

# Exercise 8 --
# There are some games where we put a rectangular "bounding box" around our
# sprites in the game. We can the do collision detection between, say, bombs
# and spaceships, by comparing whether their rectangles overlap anywhere.

# Write a function to determine whether two rectangles collide. Hint: this
# might be quite a tough exercise! Think carefully about all the cases
# as you code.

