subroutine mandelbrot(N, xmin, xmax, ymin, ymax, max_iter, m)

  implicit none

  integer, intent(in) :: N
  double precision, intent(in) :: xmin, xmax, ymin, ymax
  integer, intent(in) :: max_iter

  integer, intent(out) :: m(N, N)

  double complex, parameter :: i_unit = (0, 1)

!f2py depend(N) :: m
!f2py intent(out) :: m

  integer :: i, j, niter
  double precision :: x(N), y(N)
  double precision :: dx, dy
  double complex, allocatable :: c(:, :)
  double complex, allocatable :: z(:, :)

  ! compute coordinates
  dx = (xmax - xmin) / (N - 1)
  dy = (ymax - ymin) / (N - 1)

  do i = 1, N
     x(i) = xmin + (i-1) * dx
     y(i) = ymin + (i-1) * dy
  enddo

  allocate(c(N, N))

  do j = 1, N
     do i = 1, N
        c(i, j) = x(i) + i_unit * y(j)
     enddo
  enddo

  m(:, :) = 0

  allocate(z(N, N))
  z(:, :) = 0.0

  do niter = 1, max_iter

     do j = 1, N
        do i = 1, N

           if (m(i, j) == 0) then
              z(i, j) = z(i, j) * z(i, j) + c(i, j)

              if (abs(z(i,j)) > 2) then
                 m(i, j) = niter
              endif
           endif

        enddo
     enddo

  enddo

end subroutine mandelbrot
