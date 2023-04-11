import ctypes

lib = ctypes.CDLL("./mylib.so")

lib.print_list.argtypes = [ctypes.py_object]

l = ['hello', 'world', 1]
lib.print_list(l)

del l[1]
lib.print_list(l)

l.append(2)
l.append(4)
lib.print_list(l)
