import pyhot.pyhot as pyhot


class TestObj(pyhot.HotObj):
    obj_id = 0
    def __init__(self, obj_id=0):
        super(TestObj, self).__init__()
        self.obj_id = obj_id
    
    def test_fun(self):
        print("class:%s, obj_id:%s, var:%s"%(self.__class__, self.obj_id, 2))

class TestObj_1(pyhot.HotObj):
    obj_id = 0
    new_obj_id = 0
    new_obj_id_1 = 1
    new_obj_id_2 = 1
    new_obj_id_3 = 3
    new_obj_id_4 = 4
    def __init__(self, obj_id=0):
        super(TestObj_1, self).__init__()
        self.obj_id = obj_id
    
    def test_fun(self):
        print("class:%s, obj_id:%s, var:%s, new_obj_id_4:%s"%(self.__class__, self.obj_id, 2, self.new_obj_id_4))
        