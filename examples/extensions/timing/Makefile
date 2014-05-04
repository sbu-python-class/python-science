ALL: laplace_fortran.so

laplace_fortran.so: laplace_fortran.f90
	f2py --fcompiler=gnu95 -c laplace_fortran.f90 -m laplace_fortran
