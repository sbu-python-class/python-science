ALL: laplace_fortran.so laplace_C.so laplace_CAPI.so

laplace_fortran.so: laplace_fortran.f90
	f2py3 --fcompiler=gnu95 -c laplace_fortran.f90 -m laplace_fortran

laplace_C.so: laplace_C.c
	gcc -c -fPIC laplace_C.c -o laplace_C.o
	gcc -shared -o laplace_C.so laplace_C.o

laplace_CAPI.so: laplace_CAPI.c
	python3 setup.py build_ext --inplace


.PHONY: clean

clean: 
	rm -f laplace_fortran.so laplace_C.so laplace_CAPI.so
	rm -rf build
