subroutine f90_update(u, nx, ny, dx2, dy2)

  implicit none

  integer, intent(in) :: nx, ny
  double precision, intent(inout) :: u(nx, ny)
  double precision, intent(in) :: dx2, dy2

!f2py depend(nx, ny) :: u
!f2py intent(inout) :: u
!f2py intent(in) :: dx2, dy2

  integer :: i, j

  do j = 2, ny-1
     do i = 2, nx-1
        u(i,j) = ( (u(i+1,j) + u(i-1,j))*dy2 + (u(i,j+1) + u(i,j-1))*dx2 ) / &
             (2.0d0*(dx2 + dy2))
     enddo
  enddo

end subroutine f90_update
