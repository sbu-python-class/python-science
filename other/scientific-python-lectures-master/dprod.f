
       subroutine dprod(x, y, n)
    
       double precision x(n), y
       y = 1.0
    
       do 100 i=1, n
           y = y * x(i)
100    continue
       end
