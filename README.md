# hotpy
热更python的class对象  
已经存在的也会更新已有的属性和函数，没有则会添加新的class的属性和函数

已提供pip安装 项目中引用即可  
`pip install hotpy`

# 使用方法   参考main.py 和 test,py 
## 方法一
在需要热更的类中继承hotpy.HotObj  
调用hotpy.hot_mgr.hot(mod_name)  
会热更mod和它里面的类对象  
![](https://github.com/huangwenzi/hotpy/blob/main/img/hotpy_test.gif)

## 方法二
初始化调用 pyhot.hot_mgr.init_file_record()  
需要更新的时候再调用 pyhot.hot_mgr.hot_all()  
会自动更新项目下的全部文件  
不需要更新全部文件也可以继续用 hotpy.hot_mgr.hot(mod_name)  
