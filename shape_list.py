import pickle




class SetUpList:
    #초기 리스트 설정
    set_up_list = []

    #파일을 열게 시키고, 열리면 loas_list를 set_up_list로 바꿔치기
    try:
        with open("shape.dat", "rb") as fr:
            load_list = pickle.load(fr)
            set_up_list = load_list
    except:
        pass

    @staticmethod
    def add_shape(shape):
        SetUpList.set_up_list.append(shape)
    @staticmethod
    def get_list_len():
        list_len = len(SetUpList.set_up_list)
        return list_len
    @staticmethod
    def show_list():
        for i in range(SetUpList.get_list_len()):
            SetUpList.set_up_list[i].get_info()


#SetUpList.add_shape('도형') 도형 추가 메소드
#SetUpList.show_list() 도형 보여주기 메소드