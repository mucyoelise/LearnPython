import math

class Point:
    
    def __init__(self,x,y):
        ''' Initialize the point instance'''
        self.x = x
        self.y = y
    
    def get_x(self):
        ''''Getter for the x coordinate'''
        return self.x
    
    def get_y(self):
        '''Getter for the y coordinate'''
        return self.y
    
    def set_x(self,x):
        '''Setter for the x coordinate'''
        self.x = x
    
    def set_y(self,y):
        '''Setter for the y coordinate'''
        self.y = y
    
    def distance(self,other):
        '''Calculate the distance between two points'''
        dist = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        return dist
    
    def __eq__(self,other):
        '''Two points are equal if they have the same x and y coordinates'''
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        ''''Returns a string representation of the point as (x,y)'''
        return f'({self.x}, {self.y})'
    
class Circle: 
    def __init__(self,center,radius):
        ''' Initialize the circle instance raise a ValueError exception
        if the radius is not a positive number or center is not a point object'''
        
        if not radius > 0 or not isinstance(center, Point):
            raise ValueError('')
        self.center = center
        self.radius = radius

    def get_center(self):
        '''Getter for the center of the circle'''
        return self.center
    
    def get_radius(self):
        '''Getter for the radius of the circle'''
        return self.radius
    
    def set_center(self,center):
        '''Setter for the center of the circle'''
        self.center = center

    def set_radius(self,radius):
        '''Setter for the radius of the circle'''
        self.radius = radius

    def area(self):
        '''Calculate the area of the circle'''
        area_finder = math.pi * (self.radius)**2 

        return area_finder
    
    def __str__(self):
        '''Returns a string representation of the circle as Center:(x,y), Radius: r'''
        return f'Center: {self.center}, Radius: {self.radius}'
      
    def is_in(self,point):
        '''Check if a point is inside the circle'''
        return self.center.distance(point) < self.radius
        
    def __eq__(self,other):
        '''Two circles are equal if they have exactly the same center and the same radius''' 
        return self.center == other.get_center() and self.radius == other.get_radius()
        


origin=Point(0,0)
p1=Point(3,4)
p2=Point(2,3)
c1=Circle(origin,4)
c2=Circle(p1,3)
print(c1)
print(p1)
print(c1.area())
print(c1.is_in(p1))
print(c2.is_in(p1))

