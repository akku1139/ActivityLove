# dict["key"] だけでなく dict.key でもアクセスできる辞書
class Dict2(dict): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.__dict__ = self 
