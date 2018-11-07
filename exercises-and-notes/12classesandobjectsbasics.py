# NOTE TAKING -----
# An object consists of two things: an internal state, and a collection of
# ----- methods that it can perform.
# The state of an object represents those things that the object knows about
# ----- itself. Ex: turtle -- position, color, heading, etc.
# The methods of an object are functions that allow you to change its state
# ----- or ask questions about its state. Ex: turtle -- .forward, .backward, etc.
# Some methods don't cause anything to change, simply report a value back to
# ----- you some information about it's current state. Ex: turtle -- .position
# Any time you create a new class, you should include a method with the special
# ----- name __init__.
# This "initializer method" is automatically called whenever a new instance of
# ----- "Point" is created. It gives you the opportunity to set up the
# ----- attributes required within the new instance by giving them their initial
# ----- values.
# The "self" paramenter (you could choose any other name, but nobody ever does!)
# ----- is automatically set to reference the newly-created object that needs
# ----- to be initialized.
# A function like Turtle() or Point(), which creates a new object instance, is
# ----- called a "constructor". Every class automatically uses the name of the
# ----- class as the name of the constructor function.
# Inside the __init__ function, you have the opportunity to configure the new
# ----- instance into some kind of reasonable "default starting state".
# Think of a class as a "factory for making objects". It isn't itself an insance
# ----- of a point, but it contains the machinery to make point insances.
# Every time you call the constuctor, you're asking the factory to make a new
# ----- object.
# Instantiation -- the combined process of "make me a new object" and "get its
# settings initialized to the factory default settings".
# A method behaves like a function, but it is invoked on a specific instance.
# ----- For example, with a turtle named "tess", tess.right(90) asks the tess
# ----- object to perform its right method and turn 90 degress.
# Methods are accessed using dot notation.
# "dunder" is a naming technique for Python's special methods.f
# __repr__ method is responsible for returning a string representation as
# ----- definied by the class creator. In other words, you as the programmer
# ----- get to choose what a Point should look like when it gets printed.
# __str__ does essentially the same thing as the __repr__ method, however,
# ----- Python tries to do that first. Most programmers use __str__.

#class Point:
#    """ Point class for representing and manipulating x, y coordinates. """
#    def __init__(self, init_x, init_y):
#        """ Create a new point at the origin """
#        self.x = init_x
#        self.y = init_y

#    def get_x(self):
#        return self.x

#    def get_y(self):
#        return self.y

#    def distance_from_origin(self):
#        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#    def __str__(self):
#        return "x=" + str(self.x) + ", y=" + str(self.y)

#    def halfway(self, target):
#        mx = (self.x + target.x) / 2
#        my = (self.y + target.y) / 2
#        return Point(mx, my)

# ____________________________________________________________________

# EXERCISES!!!

# Exercise 1 --
# Add a distance_from_point method that works similar to
# distance_from_origin except that it takes Point as a
# parameter and computes the distance between that point
# and self.

#import math

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

#    def distance_from_point(self, target):
#        new_x = (self.x - target.get_x())
#        new_y = (self.y - target.get_y())
#        return math.sqrt(new_x ** 2 + new_y ** 2)

#    def __repr__(self):
#        return "x=" + str(self.x) + ", y=" + str(self.y)

#def main():
#    first_point = Point(5, 9)
#    second_point = Point(5, 10)
    
#    print(first_point.distance_from_point(second_point))
    
    
#if __name__ == "__main__":
#    main()

# ________________________________________________________________

# Exercise 2 --
# Add a method reflect_x to the class Point which returns a new
# Point, one which is the reflection of the point across the x-axis.
# For example, Point(3, 5).reflect_x() is (3, -5)


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

#    def reflect_x(self):
#        new_x = -self.x
#        return Point(new_x, self.y)

#def main():
#    a = Point(1, 5)
#    b = a.reflect_x()

#    print(a)
#    print(b)

#if __name__ == "__main__":
#    main()


# ___________________________________________________________________

# Exercise 3 --
# Add a method slope_from_origin, which returns the slope of the line
# joining the origin to the point. For example,
# >>> Point(4, 10).slope_from_origin()
# 2.5
# >>> Point(12, -3).slope_from_origin()
# -0.25
# >>> Point(-6, 0).slope_from_origin()
# 0
# The equation for calculating slope between any two points is
# slope = (Y2 - Y1)/(X2 - X1)
# Remember that dividing by 0 is not allowed, so there are some inputs
# that will cause your method to fail. Return None when that happens.

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

#    def slope_from_origin(self):
#        new_y = self.y - 0
#        new_x = self.x - 0
#        if new_x == 0:
#            return None
#        else:
#            return new_y / new_x

## some tests to check your code
#from test import testEqual
#testEqual( Point(4, 10).slope_from_origin(), 2.5 )
#testEqual( Point(5, 10).slope_from_origin(), 2 )
#testEqual( Point(0, 10).slope_from_origin(), None )
#testEqual( Point(20, 10).slope_from_origin(), 0.5 )
#testEqual( Point(20, 20).slope_from_origin(), 1 )
#testEqual( Point(4, -10).slope_from_origin(), -2.5 )
#testEqual( Point(-4, -10).slope_from_origin(), 2.5 )
#testEqual( Point(-6, 0).slope_from_origin(), 0 )

# ___________________________________________________________________

# Exercise 4 --
# Add a method called move that will take two parameters, call them
# dx and dy. The method will cause the point to move in the x and y
# direction the number of units given. (Hint: you will change the values
# of the state of the point)


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

#    def move(self, dx, dy):
#        self.x = self.x + dx
#        self.y = self.y + dy

#def main():
#    p = Point(7, 6)
#    print(p)
#    p.move(5, 10)
#    print(p)

#if __name__ == "__main__":
#    main()


