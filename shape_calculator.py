class Rectangle:
    width = 0
    height = 0
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return 'Rectangle(width=' + str(self.width) +', height=' + str(self.height) + ')'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return ((self.width **2 + self.height **2) **.5)
    
    def get_picture(self):
        if(self.width > 50 or self.height > 50): return 'Too big for picture.'
        line = ''
        res = ''

        for i in range(0, self.width): line += '*'
        line += '\n'
        
        for i in range(0,self.height): res += line
        
        return res

    def get_amount_inside(self, r):
        in_w = self.width // r.width
        in_h = self.height // r.height

        return in_w * in_h


class Square(Rectangle):

    def __init__(self, side): 
        self.width = side
        self.height = side

    def __str__(self):
        return 'Square(side=' + str(self.width) +')'
    
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.set_side(side)
    
    def set_height(self, side):
        self.set_side(side)


# https://replit.com/@nahuelcastro/boilerplate-polygon-area-calculator#README.md