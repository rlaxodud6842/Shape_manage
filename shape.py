import math

#도형 클래스
class Shape:
    id = 0
    def __init__(self):
        Shape.id += 1
        self.id = Shape.id
        self.get_round()
        self.get_area()

    def get_area(self):
        self.area = 1/2 * self.height * self.width

    def get_round(self):
        self.round = self.hypotenuse + self.height + self.width

    def get_info(self):
        pass

#원 클래스
class Circle(Shape):
    def __init__(self,x,y,radius):
        self.coordinate_x = x
        self.coordinate_y = y
        self.radius = radius
        super().__init__()
    def get_area(self):
        self.area = math.pi * (self.radius^2)

    def get_round(self):
        self.round = (2 * math.pi) * (self.radius)

    def get_info(self):
        print("\nID:",self.id,"\n중심좌표:(",self.coordinate_x,",",self.coordinate_y,")","\n반지름:",self.radius,"\n면적:",self.area,"\n둘레:",self.round)

#삼각형 클래스
class Triangle(Shape):
    def __init__(self,h,w):
        self.height = h
        self.width = w
        self.get_hypotenuse()
        self.get_eren()
        super().__init__()

    def get_hypotenuse(self):
        self.hypotenuse = math.sqrt(self.height ^ 2 + self.width ^ 2)

    def get_eren(self):
        self.eren =[(0, 0),(0,self.width),(self.height,self.width)]

    def get_info(self):
        print("\nID:",self.id,"\n가로,세로:(",self.height,",",self.width,")","\n면적:",self.area,"\n둘레:",self.round,"\n빗변길이:",self.hypotenuse,"\n꼭짓점 좌표:",self.eren)


#사각형 클래스
class Rectangle(Shape):
    def __init__(self,h,w):
        self.height = h
        self.width = w
        self.get_hypotenuse()
        self.get_eren()
        super().__init__()

    def get_hypotenuse(self):
        self.hypotenuse = math.sqrt(self.height ^ 2 + self.width ^ 2)

    def get_eren(self):
        self.eren =[(0, 0),(0,self.width),(self.width,self.width)]

    def get_info(self):
        print("\nID:",self.id,"\n가로,세로:(",self.height,",",self.width,")","\n면적:",self.area,"\n둘레:",self.round,"\n빗변길이:",self.hypotenuse,"\n꼭짓점 좌표:",self.eren)
