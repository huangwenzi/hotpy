import pyhot.pyhot as pyhot
import test


a = test.TestObj(1)
b = test.TestObj_1(2)
c = test.TestObj(3)
while True:
    a.test_fun()
    b.test_fun()
    c.test_fun()
    in_str = input("输入:\n")
    if in_str == "1":
        pyhot.hot_mgr.hot("test")
    else:
        pass