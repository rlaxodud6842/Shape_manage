from enum_collection import Menu
from enum_collection import ShapeType
import shape
import shape_list

class MainMenu:
    def main_menu(self):
        print("\n1)도형추가")
        print("2)도형삭제")
        print("3)도형출력")
        print("4)종료")

        while True:
            try:
                user_select = int(input("번호를 입력 해주세요:"))
                break
            except:
                print("숫자로 번호를 다시 입력 해주세요\n")

        if user_select == Menu.ADD_SHAPE.value:
            self.select_shape()

        elif user_select == Menu.DELETE_SHAPE.value:
            main.delete_shape()
            shape_list.list.del_shape(self.delete_shape_id)

        elif user_select == Menu.PRINT_SHAPE.value:
            shape_list.list.show_shape_list()

    def input_circle(self): #원 정보 입력
        self.x = int(input("중심좌표를 x를 입력하세요:"))
        self.y = int(input("중심좌표를 y를 입력하세요:"))
        self.r = int(input("반지름을 입력하세요:"))

    def input_height_width(self): #나머지 도형 정보 입력
        self.height = int(input("세로 길이를 입력하세요:"))
        self.width = int(input("가로 길이를 입력하세요:"))

    def delete_shape(self): #도형 삭제 입력
        self.delete_shape_id = int(input("삭제하고 싶은 도형의 ID를 입력해주세요:"))

    def select_shape(self): #도형 선택함수
        print("1.원형", "\n2.삼각형", "\n3.사각형")
        user_select_shpae = int(input(("어떤 도형을 추가 하시겠습니까:\n")))
        shape_info = MainMenu() #이런식으로 지역변수 써도 괜찮을까

        if user_select_shpae == ShapeType.CIRCLE.value:
            shape_info.input_circle()#원형생성에 필요한 변수 받기
            shape_list.list.add_shape(shape.Circle(shape_info.x, shape_info.y, shape_info.r)) #받아서 원 객체로 만들고 리스트에 추가

        elif user_select_shpae == ShapeType.TRIANGLE.value:
            shape_info.input_height_width()
            shape_list.list.add_shape(shape.Triangle(shape_info.height, shape_info.width))

        elif user_select_shpae == ShapeType.RECTANGLE.value:
            shape_info.input_height_width()
            shape_list.list.add_shape(shape.Rectangle(shape_info.height, shape_info.width))


while True:
    main = MainMenu()
    main.main_menu()

