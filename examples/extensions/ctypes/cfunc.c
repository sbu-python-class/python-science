#include <stdio.h>

int my_subroutine(double *array, int len) {

  printf("in my_subroutine\n");

  int i;
  for (i = 0; i < len; i++) {
    printf("%3d: %f\n", i, array[i]);
  }

  return 0;

}
