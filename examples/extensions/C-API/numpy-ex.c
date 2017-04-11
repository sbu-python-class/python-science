/* see 
   http://wiki.scipy.org/Cookbook/C_Extensions/NumPy_arrays
   http://scipy-lectures.github.io/advanced/interfacing_with_c/interfacing_with_c.html 
   http://stackoverflow.com/questions/24189002/seg-fault-while-using-numpy-with-python3
   https://docs.python.org/3/extending/extending.html
*/

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

#include <Python.h>
#include <numpy/arrayobject.h>
#include <math.h>


/* a static function in C limits its scope to this file -- the linker
   won't complain about clashes */
static PyObject* ex_function(PyObject* self, PyObject* args)
{

  PyArrayObject *iarray, *oarray;
  double **iA, **oA;
  int i, j, m, n, dims[2];

  /* parse the inputs -- we need to know what the arguments of our
     call were.  We'll assume:

     ex_function(array)

     and that we return a new array of the same dimensions

     In the parsing, you can do O or O! here (from the docs):

     O (object) [PyObject *]

       Store a Python object (without any conversion) in a C object
       pointer. The C program thus receives the actual object that was
       passed. The object’s reference count is not increased. The
       pointer stored is not NULL.

     O! (object) [typeobject, PyObject *]

       Store a Python object in a C object pointer. This is similar to
       O, but takes two C arguments: the first is the address of a
       Python type object, the second is the address of the C variable
       (of type PyObject*) into which the object pointer is stored. If
       the Python object does not have the required type, TypeError is
       raised.
    
     O! seems safer and preferred

  */

  if (!PyArg_ParseTuple(args, "O!", &PyArray_Type, &iarray)) return NULL;
  if (NULL == iarray) return NULL;

  /* check to make sure we are a double type */
  if (PyArray_DTYPE(iarray)->type_num != NPY_DOUBLE ||
      PyArray_NDIM(iarray) != 2) {
    PyErr_SetString(PyExc_ValueError, "wrong input array type");
    return NULL;
  }

  /* get the dimensions */
  n = dims[0] = PyArray_DIM(iarray, 0);
  m = dims[1] = PyArray_DIM(iarray, 1);
  

  /* the new C interface can create iteration "object" using NpyIter, but we
     are not going to do that here, we want to explicitly see the different
     dimensions 
  */

  /* make a NumPy double matrix with the same dimensions -- this will
     be contiguous, and will be our output (note, there is also a
     PyArray_NewLikeArray function) */
  oarray = (PyArrayObject *) PyArray_FromDims(2, dims, NPY_DOUBLE);

  /* change contigous arrays into C ** arrays -- we need to have a
     vector of pointers that point to the correct location in the
     contiguous block of memory that stores the multi-dimensional
     array data */
  iA = (double **) malloc( (size_t) (n*sizeof(double)));
  for (i = 0; i < n; i++) {
    iA[i] = (double *) PyArray_DATA(iarray) + i*m;
  }

  oA = (double **) malloc( (size_t) (n*sizeof(double)));
  for (i = 0; i < n; i++) {
    oA[i] = (double *) PyArray_DATA(oarray) + i*m;
  }
  
  /* now we can do our manipulation */
  for (i = 0; i < n; i ++) {
    for (j = 0; j < m; j++) {
      oA[i][j] = iA[i][j]*iA[i][j];
    }
  }

  /* free up the memory we allocated for the array indexing */
  free (iA);
  free (oA);

  /* return our python array */
  return PyArray_Return(oarray);

}

     
/* this is the table for function names that Python will see */ 
static PyMethodDef numpy_in_cMethods[] = {
  {"example", ex_function, METH_VARARGS, 
   "a simple example: square the elements of an array"},
  {NULL, NULL}
};

static struct PyModuleDef moduledef = {
  PyModuleDef_HEAD_INIT,
  "numpy_in_c",  // name
   "a simple example: square the elements of an array",  // documentation
  -1,  // size
  numpy_in_cMethods,  // methods
};

/* this tells python what to do when it first imports this module --
   the name follows directly from the table name above */
PyMODINIT_FUNC PyInit_numpy_in_c(void) {
  PyObject *m;
  m = PyModule_Create(&moduledef);
  import_array();
  return m;
}
