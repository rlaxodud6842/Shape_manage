from enum_collection import Menu
from enum_collection import ShapeType
import shape
import shape_list
import pickle


class MainMenu:
    def main_menu(self):#메인 메소드
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
            shape_list.SetUpList.show_list()
            self.delete_shape()
            shape_list.SetUpList.delete_shape(self.delete_shape_id)

        elif user_select == Menu.PRINT_SHAPE.value:
            shape_list.SetUpList.show_list()

        elif user_select == Menu.EXIT.value:
            with open("shape.dat", "wb") as file:
                pickle.dump(shape_list.SetUpList.set_up_list, file)
            quit()

    def input_circle(self): #원 정보 입력
        self.x = int(input("중심좌표를 x를 입력하세요:"))
        self.y = int(input("중심좌표를 y를 입력하세요:"))
        self.r = int(input("반지름을 입력하세요:"))
        print("도형이 추가되었습니다")

    def input_height_width(self): #나머지 도형 정보 입력
        self.width = int(input("가로 길이를 입력하세요:"))
        self.height = int(input("세로 길이를 입력하세요:"))
        print("도형이 추가되었습니다")

    def delete_shape(self): #도형 삭제 입력
        self.delete_shape_id = int(input("삭제하고 싶은 도형의 ID를 입력해주세요:"))

    def select_shape(self): #도형 선택함수
        print("1.원형", "\n2.삼각형", "\n3.사각형")
        user_select_shpae = int(input(("어떤 도형을 추가 하시겠습니까:\n")))

        if user_select_shpae == ShapeType.CIRCLE.value:
            self.input_circle()
            shape_list.SetUpList.add_shape(shape.Circle(self.x, self.y, self.r))

        elif user_select_shpae == ShapeType.TRIANGLE.value:
            self.input_height_width()
            shape_list.SetUpList.add_shape(shape.Triangle(self.width,self.height))

        elif user_select_shpae == ShapeType.RECTANGLE.value:
            self.input_height_width()
            shape_list.SetUpList.add_shape(shape.Rectangle(self.width,self.height))

if __name__ == '__main__':
    while True:
        main = MainMenu()
        main.main_menu()