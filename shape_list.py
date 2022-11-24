import pickle
class SetUpList:
    #초기 리스트 설정
    set_up_list = []

    #리스트 로드
    try:
        with open("shape.dat", "rb") as fr:
            load_list = pickle.load(fr)
            set_up_list = load_list
    except:
        pass
    #도형 추가
    @staticmethod
    def add_shape(shape):
        SetUpList.set_up_list.append(shape)
    #리스트 길이 구하기
    @staticmethod
    def get_list_len():
        list_len = len(SetUpList.set_up_list)
        return list_len
    #리스트 보여주기
    @staticmethod
    def show_list():
        for i in range(SetUpList.get_list_len()):
            SetUpList.set_up_list[i].get_info()
    #도형 삭제
    @staticmethod
    def delete_shape(deleted_id):
        try:
            for i in range(SetUpList.get_list_len()):
                shape_id = SetUpList.set_up_list[i].id
                if deleted_id == shape_id:
                    remove_id = i
            SetUpList.set_up_list.pop(remove_id)
            print("선택한 도형이 삭제되었습니다")
        except UnboundLocalError:
            print("그런 id를 가진 도형이 존재하지 않습니다.")