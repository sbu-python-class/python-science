# gaussian elimination with scaled pivoting
#
# M. Zingale (2013-02-25)

import numpy

def gaussElim(A, b, returnDet=0):
    """ perform gaussian elimination with pivoting, solving A x = b A
        is an NxN matrix, x and b are an N-element vectors.  Note: A
        and b are changed upon exit to be in upper triangular (row
        echelon) form """

    # b is a vector
    if not b.ndim == 1:
        print "ERROR: b should be a vector"
        return None

    N = len(b)

    # A is square, with each dimension of length N
    if not (A.shape[0] == N and A.shape[1] == N):
        print "ERROR: A should be square with each dim of same length as b"
        return None

    # allocation the solution array
    x = numpy.zeros((N), dtype=A.dtype)

    # find the scale factors for each row -- this is used when pivoting
    scales = numpy.max(numpy.abs(A), 1)

    # keep track of the number of times we swapped rows
    numRowSwap = 0

    printAb(A, b)

    # main loop over rows
    for k in range(N):
        
        # find the pivot row based on the size of column k -- only consider
        # the rows beyond the current row
        rowMax = numpy.argmax(A[k:, k]/scales[k:]) 
        if (k > 0): rowMax += k  # we sliced A from k:, correct for total rows

        # swap the row with the largest scaled element in the current column
        # with the current row (pivot) -- do this with b too!
        if not rowMax == k:
            A[[k, rowMax],:] = A[[rowMax, k],:]
            b[[k, rowMax]] = b[[rowMax, k]]
            numRowSwap += 1

        # do the forward-elimination for all rows below the current
        for i in range(k+1, N):
            coeff = A[i,k]/A[k,k]

            for j in range(k+1, N):
                A[i,j] += -A[k,j]*coeff

            A[i,k] = 0.0
            b[i] += -coeff*b[k]
        #print A, "\n"
        printAb(A, b)
    
    # back-substitution
    
    # last solution is easy
    x[N-1] = b[N-1]/A[N-1,N-1]

    for i in reversed(range(N-1)):
        sum = b[i]
        for j in range(i+1,N):
            sum += -A[i,j]*x[j]
        x[i] = sum/A[i,i]


    # determinant
    det = numpy.prod(numpy.diagonal(A))*(-1.0)**numRowSwap
    
    if not returnDet:
        return x
    else:
        return x, det



# for debugging:
# output: numpy.savetxt("test.out", a, fmt="%5.2f", delimiter="  ")
# convert -font Courier-New-Regular -pointsize 20 text:test.out test.png

def printAb(A, b):
    """ printout the matrix A and vector b in a pretty fashion.  We
        don't use the numpy print here, because we want to make them
        side by side"""

    N = len(b)

    openT = "/"
    closeT = "\\"

    openB = "\\"
    closeB = "/"

    # numbers take 6 positions + 2 spaces
    aFmt = " %6.3f "
    space = 8*" "

    line = "|" + N*aFmt + "|" + space + "|" + aFmt + "|"
    top = openT + N*space + closeT  + space + openT + space + closeT
    bottom = openB + N*space + closeB + space + openB + space + closeB + "\n"

    print top
    for i in range(N):
        out = tuple(A[i,:]) + (b[i],)
        print line % out
    print bottom

