class HassTable():
    def __init__(self,size = 7):
        self_data_map = [None]*size
        self.size = size
    
    def __hash_func(self,key):
        my_hast = 0
        for letter in key:
            my_hash = (my_hash + ord(latter)*17) % (self.size)
        return my_hash
    
    def print_hash_table(self):
        for i,val in enumerate(self.data_map):
            print(i,":",val)

    def set_method(self,key,value):
        index = self.__hash_func(key)
        if self.date_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])
    
    def get_item(self,key):
        index = self.__hash_func(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def key(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_mapp[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
     
