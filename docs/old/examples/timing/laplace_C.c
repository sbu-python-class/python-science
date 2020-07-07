int C_update(double *iarray, int ilen, int jlen, double dx2, double dy2) {
		  

  /* here iarray is a pointer to a contiguous space in
     memory.  We wish to access it as a 2-d array. */

  /* note: there is no error or bounds checking done here! */
  double *iA[ilen];

  int i;
  for (i = 0; i < ilen; i++) {
    iA[i] = iarray + i*jlen;
  }


  int j;
  for (i = 1; i < ilen-1; i++) {
    for (j = 1; j < jlen-1; j++) {
      iA[i][j] = ( (iA[i+1][j] + iA[i-1][j])*dy2 +
		   (iA[i][j+1] + iA[i][j-1])*dx2 ) /
	(2.0*(dx2 + dy2));
    }
  }

  return 0;
}
