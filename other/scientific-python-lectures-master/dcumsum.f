c File dcumsum.f
       subroutine dcumsum(a, b, n)
       double precision a(n)
       double precision b(n)
       integer n
cf2py  intent(in) :: a
cf2py  intent(out) :: b
cf2py  intent(hide) :: n

       b(1) = a(1)
       do 100 i=2, n
           b(i) = b(i-1) + a(i)
100    continue
       end
