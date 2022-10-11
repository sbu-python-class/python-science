ALL: numpy_in_f.so

numpy_in_f.so: numpy_in_f.f90
	f2py3 --fcompiler=gnu95 -c numpy_in_f.f90 -m numpy_in_f
