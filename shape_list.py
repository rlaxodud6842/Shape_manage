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

    #리스트 길이 구하기
    def get_list_len(self):
        self.list_len = len(self.set_up_list)
        return self.list_len
    #리스트 보여주기
    def show_list(self):
        for i in range(self.get_list_len()):
            self.set_up_list[i].get_info()

    #도형 삭제
    def delete_shape(self,deleted_id):
        try:
            for i in range(self.get_list_len()):
                shape_id = self.set_up_list[i].id
                if deleted_id == shape_id:
                    self.set_up_list.pop(i)
                    print("선택한 도형이 삭제되었습니다")
                    break
        except:
            print("그런 id를 가진 도형이 존재하지 않습니다.")