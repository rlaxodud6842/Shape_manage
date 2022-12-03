import pickle
import math

class Shape:
    id = 0
    is_id_loaded = True
    def __init__(self):
        self.load_id()
        Shape.id += 1
        self.id = Shape.id
        self.get_round()
        self.get_area()

    def load_id(self):
        if Shape.is_id_loaded == True:
            try:
                with open("shape.dat", "rb") as file:
                    load_list = pickle.load(file)
                    load_id = load_list[-1].id
                    Shape.id = load_id
                    Shape.is_id_loaded = False
            except:
                pass

    def get_area(self):
        pass

    def get_round(self):
        pass

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
        print("\nID:",self.id,"[원형]","\n중심좌표:(",self.coordinate_x,",",self.coordinate_y,")","\n반지름:",self.radius,"\n면적:",self.area,"\n둘레:",self.round)

#삼각형 클래스
class Triangle(Shape):
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.get_hypotenuse()
        self.get_eren()
        super().__init__()

    def get_hypotenuse(self):
        self.hypotenuse = math.sqrt(self.height ^ 2 + self.width ^ 2)

    def get_eren(self):
        self.eren = [(0, 0), (self.width, 0), (0, self.height)]

    def get_area(self):
        self.area = (self.height * self.width)*1/2

    def get_round(self):
        self.round = self.hypotenuse + self.height + self.width

    def get_info(self):
        print("\nID:",self.id,"[삼각형]","\n가로,세로:(",self.width,",",self.height,")","\n면적:",self.area,"\n둘레:",self.round,"\n빗변길이:",self.hypotenuse,"\n꼭짓점 좌표:",self.eren)

#사각형 클래스
class Rectangle(Shape):
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.get_eren()
        super().__init__()

    def get_eren(self):
        self.eren =[(0, 0),(self.width,0),(0,self.height),(self.width,self.height)]

    def get_round(self):
        self.round = (self.height+self.width)*2

    def get_area(self):
        self.area = self.height * self.width

    def get_info(self):
        print("\nID:",self.id,"[사각형]","\n가로,세로:(",self.width,",",self.height,")","\n면적:",self.area,"\n둘레:",self.round,"\n꼭짓점 좌표:",self.eren)