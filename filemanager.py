import pickle

class FileManager:
    def save_shape(self,save_list):
        with open("shape.dat", "wb") as file:
            pickle.dump(save_list, file)

    def load_list(self):
        try:
            with open("shape.dat", "rb") as fr:
                load_list = pickle.load(fr)
                return load_list
        except:
            return None