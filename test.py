import numpy as np
import ctypes 
import os
from ctypes import *

MyDLL = ctypes.CDLL( 'c:\\GitHub\\MachineVisionTest\\NImageDLL.dll' )
b = MyDLL.createMyClass()
print(b)