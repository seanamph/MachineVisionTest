import time
import ctypes 
import os

def get_dll_path(dll_name):
    if os.name == "nt":
        return f"{dll_name}.dll"
    else:
        return f"./{dll_name}.so"

# 計算絕對路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
library_path = os.path.join(current_dir, get_dll_path("MyDLL"))

MyDLL = ctypes.CDLL(library_path)
b = MyDLL.Fibo_C(40)
print(b)