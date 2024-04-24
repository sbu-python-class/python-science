#include <iostream>
#include <cmath>
#include <complex>
#include <vector>

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>


namespace py = pybind11;

using cmplx_arr = std::vector<std::vector<std::complex<double>>>;

using namespace std::complex_literals;


py::array_t<int> mandelbrot(int N,
                            double xmin, double xmax,
                            double ymin, double ymax, int max_iter) {

    // construct the numpy array we will return
    // we need to specify the strides manually

    constexpr size_t elsize = sizeof(int);
    size_t shape[2]{N, N};
    size_t strides[2]{N * elsize, elsize};
    auto m = py::array_t<int>(shape, strides);
    auto m_view = m.mutable_unchecked<2>();

    // for the other arrays used only here, we can
    // do whatever we want.  Since we can't yet rely
    // on C++23 mdspan, we'll just do a vector of vectors

    std::vector<double> x(N, 0.0);
    std::vector<double> y(N, 0.0);

    double dx = (xmax - xmin) / static_cast<double>(N - 1);
    double dy = (ymax - ymin) / static_cast<double>(N - 1);

    for (int i = 0; i < N; ++i) {
        x[i] = xmin + static_cast<double>(i) * dx;
        y[i] = ymin + static_cast<double>(i) * dy;
    }

    cmplx_arr c(N, std::vector<std::complex<double>>(N, 0.0));
    cmplx_arr z(N, std::vector<std::complex<double>>(N, 0.0));

    // initialize c;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            c[i][j] = x[i] + 1i * y[j];
        }
    }

    // zero out the output array

    for (int i = 0; i < m.shape(0); ++i) {
        for (int j = 0; j < m.shape(1); ++j) {
            m_view(i, j) = 0;
        }
    }

    for (int niter = 1; niter <= max_iter; ++niter) {

        for (int i = 0; i < m.shape(0); ++i) {
            for (int j = 0; j < m.shape(1); ++j) {

                if (m_view(i, j) == 0) {
                    z[i][j] = z[i][j] * z[i][j] + c[i][j];

                    if (std::abs(z[i][j]) > 2) {
                        m_view(i, j) = niter;
                    }
                }
            }
        }
    }

    return m;
}


PYBIND11_MODULE(mandel, m) {
    m.doc() = "C++ Mandelbrot example";
    m.def("mandelbrot", &mandelbrot, "generate the Mandelbrot set of size N");
}
