/* see 
   http://wiki.scipy.org/Cookbook/C_Extensions/NumPy_arrays  and
   http://scipy-lectures.github.io/advanced/interfacing_with_c/interfacing_with_c.html 
*/

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

#include <Python.h>
#include <numpy/arrayobject.h>


/* a static function in C limits its scope to this file -- the linker
   won't complain about clashes */
static PyObject* CAPI_update(PyObject* self, PyObject* args)
{

  PyArrayObject *iarray;
  double **iA;
  int i, j, m, n;
  double dx2, dy2;

  /* parse the inputs -- we need to know what the arguments of our
     call were.  We'll assume:

     ex_function(array, dx2, dy2)

     and array is updated in place
  */

  if (!PyArg_ParseTuple(args, "O!dd", 
			&PyArray_Type, &iarray, &dx2, &dy2)) return NULL;
  if (NULL == iarray) return NULL;

  /* check to make sure we are a double type */
  if (PyArray_DTYPE(iarray)->type_num != NPY_DOUBLE ||
      PyArray_NDIM(iarray) != 2) {
    PyErr_SetString(PyExc_ValueError, "wrong input array type");
    return NULL;
  }

  /* get the dimensions */
  n = PyArray_DIM(iarray, 0);
  m = PyArray_DIM(iarray, 1);

  /* change contigous arrays into C ** arrays -- we need to have a
     vector of pointers that point to the correct location in the
     contiguous block of memory that stores the multi-dimensional
     array data */
  iA = (double **) malloc( (size_t) (n*sizeof(double)));
  for (i = 0; i < n; i++) {
    iA[i] = (double *) PyArray_DATA(iarray) + i*m;
  }

  /* now we can do our manipulation */
  for (i = 1; i < n-1; i++) {
    for (j = 1; j < m-1; j++) {
      iA[i][j] = ( (iA[i+1][j] + iA[i-1][j])*dy2 +
		   (iA[i][j+1] + iA[i][j-1])*dx2 ) /
	(2.0*(dx2 + dy2));
    }
  }


  /* free up the memory we allocated for the array indexing */
  free (iA);

  /* even though we are returning an integer, it is a Python object */
  return Py_BuildValue("d", 0);

}

     
/* this is the table for function names that Python will see */ 
static PyMethodDef laplace_CAPIMethods[] = {
  {"CAPI_update", CAPI_update, METH_VARARGS, "Laplace G-S update in pure C"},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduledef = {
  PyModuleDef_HEAD_INIT,
  "laplace_CAPI",  // name
   "a simple example: square the elements of an array",  // documentation
  -1,  // size
  laplace_CAPIMethods,  // methods
};

/* this tells python what to do when it first imports this module --
   the name follows directly from the table name above */
PyMODINIT_FUNC PyInit_laplace_CAPI(void) {
  PyObject *m;
  m = PyModule_Create(&moduledef);
  import_array();
  return m;
}
