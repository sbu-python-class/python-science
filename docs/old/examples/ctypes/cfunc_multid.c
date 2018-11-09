#include <stdio.h>

int my_subroutine(double *iarray, int ilen, int jlen,
		  double *oarray) {

  /* here iarray and oarray are pointers to a contiguous space in
     memory.  We wish to access them as 2-d arrays. */

  /* note: there is no error or bounds checking done here! */
  double *iA[ilen], *oA[ilen];

  int i;
  for (i = 0; i < ilen; i++) {
    iA[i] = iarray + i*jlen;
    oA[i] = oarray + i*jlen;
  }


  int j;
  for (i = 0; i < ilen; i++) {
    for (j = 0; j < jlen; j++) {
      oA[i][j] = iA[i][j]*iA[i][j];
    }
  }

  return 0;
}
