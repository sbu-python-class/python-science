#include <cstddef>
#include <cmath>
#include <complex>
#include <mdspan>

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>


namespace py = pybind11;

using namespace std::complex_literals;

py::array_t<int> mandelbrot(int N,
                            double xmin, double xmax,
                            double ymin, double ymax, int max_iter) {

    // construct the numpy array we will return
    // we need to specify the strides manually

    constexpr std::size_t elsize = sizeof(int);
    std::size_t shape[2]{N, N};
    std::size_t strides[2]{N * elsize, elsize};
    auto m = py::array_t<int>(shape, strides);
    auto m_view = m.mutable_unchecked<2>();

    // we'll use C++23 mdspan here
    std::vector<std::complex<double>> _c(N * N);
    std::mdspan<std::complex<double>, std::dextents<std::size_t, 2>, std::layout_right> c(_c.data(), N, N);

    std::vector<std::complex<double>> _z(N * N);
    std::mdspan<std::complex<double>, std::dextents<std::size_t, 2>, std::layout_right> z(_z.data(), N, N);

    std::vector<double> x(N, 0.0);
    std::vector<double> y(N, 0.0);

    double dx = (xmax - xmin) / static_cast<double>(N - 1);
    double dy = (ymax - ymin) / static_cast<double>(N - 1);

    for (int i = 0; i < N; ++i) {
        x[i] = xmin + static_cast<double>(i) * dx;
        y[i] = ymin + static_cast<double>(i) * dy;
    }

    // initialize c;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            c[i, j] = x[i] + 1i * y[j];
        }
    }

    // zero out the output array

    for (int i = 0; i < m.shape(0); ++i) {
        for (int j = 0; j < m.shape(1); ++j) {
            m_view(i, j) = 0;
        }
    }

    for (int niter = 1; niter <= max_iter; ++niter) {

        for (std::size_t i = 0; i < m.shape(0); ++i) {
            for (std::size_t j = 0; j < m.shape(1); ++j) {

                if (m_view(i, j) == 0) {
                    z[i, j] = z[i, j] * z[i, j] + c[i, j];

                    if (std::abs(z[i, j]) > 2) {
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
