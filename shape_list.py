from filemanager import FileManager

class SetUpList:
    #초기 리스트 생성
    def create_list(self):
        self.set_up_list = []
    #리스트 로드
    def load_list(self):
        loaded_list = FileManager()
        self.set_up_list = loaded_list.load_list()
        if self.set_up_list == None:#로드가 안된다면 초기설정
            self.set_up_list = []
    #도형 추가
    def add_shape(self,shape):
        self.set_up_list.append(shape)
    #도형 보여주기
    def show_list(self):
        for shape in self.set_up_list:
            shape.get_info()
    #도형 삭제
    def delete_shape(self,deleted_id):
        for shape in self.set_up_list:
            shape_id = shape.id
            if deleted_id == shape_id:
                self.set_up_list.remove(shape)
                print("선택한 도형이 삭제 되었습니다.")
                break