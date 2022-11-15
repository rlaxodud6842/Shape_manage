class Shapelist:
    shape_list = []

    def __init__(self):
        self.list_len = len(self.shape_list)

    def add_shape(self,shape):
        self.shape_list.append(shape)

class ActList(Shapelist):
    def show_shape_list(self):
        super().__init__()
        for i in range(self.list_len):
            self.shape_list[i].get_info()

    def del_shape(self,deleted_id):
        super().__init__()
        for i in range(self.list_len):
            shape_id = self.shape_list[i].id

            if deleted_id == shape_id:
                self.shape_list.pop(i)


list = ActList()
