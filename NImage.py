import numpy as np
import ctypes 
import os
from ctypes import *

def get_dll_path(dll_name):
    if os.name == "nt":
        return f"{dll_name}.dll"
    else:
        return f"./{dll_name}.so"

# 計算絕對路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
library_path = os.path.join(current_dir, get_dll_path("NImageDLL"))

lib = ctypes.CDLL(library_path)

class ImageClass(object):

	def __init__(self):
		self.obj = lib.CreateNImage()

	def __del__(self):
		lib.DestroyNImage(self.obj)
	
	def GetHandle(self):
		return self.obj
	
	def GetWidth(self):
		return lib.GetWidth(self.obj)
    
	def GetHeight(self):
		return lib.GetHeight(self.obj)

	def LoadBMP(self, path):
		b_string1 = path.encode('utf-8')
		if(lib.LoadBMP(self.obj, create_string_buffer(b_string1)) == 0): return
		x = np.arange(0, lib.GetSize(self.obj), 1, c_uint8)
		if (lib.MemCopy(self.obj, x.ctypes.data_as(POINTER(c_uint8)), lib.GetWidth(self.obj), 
		lib.GetHeight(self.obj))): my_2D_x = x.reshape((lib.GetHeight(self.obj),lib.GetWidth(self.obj)))
		return my_2D_x
		
	def ReSize(self, wid, hei):
	    if(lib.ReSize(self.obj, wid, hei) == 0): return
	    x = np.arange(0, wid*hei, 1, c_uint8)
	    if (lib.MemCopy(self.obj, x.ctypes.data_as(POINTER(c_uint8)), wid, hei)): my_2D_x = x.reshape(hei,wid)
	    return my_2D_x
	    
	def ReturnArray(self):
	    if (lib.GetSize(self.obj) == 0): return
	    x = np.arange(0, lib.GetSize(self.obj), 1, c_uint8)
	    if (lib.MemCopy(self.obj, x.ctypes.data_as(POINTER(c_uint8)), lib.GetWidth(self.obj), 
		lib.GetHeight(self.obj))): my_2D_x = x.reshape((lib.GetHeight(self.obj),lib.GetWidth(self.obj)))
	    return my_2D_x    
