subroutine square(a, b, nx, ny)

  implicit none

  integer, intent(in) :: nx, ny
  double precision, intent(in) :: a(nx, ny)
  double precision, intent(out) :: b(nx, ny)

!f2py depend(nx, ny) :: a, b
!f2py intent(in) :: a
!f2py intent(out) :: b

! call this as b = numpy_in_f.square(a, nx, ny)

  integer :: i, j

  do j = 1, ny
     do i = 1, nx
        b(i,j) = a(i,j)**2
     enddo
  enddo

end subroutine square
