C File  hellofortran.f
        subroutine hellofortran (n)
        integer n
       
        do 100 i=0, n
            print *, "Fortran says hello"
100     continue
        end
