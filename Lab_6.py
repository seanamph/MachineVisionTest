import time
import ctypes 
import os

# 計算絕對路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
library_path = os.path.join(current_dir, "MyDLL.dll")

MyDLL = ctypes.CDLL(library_path)
b = MyDLL.Fibo_C(40)
print(b)