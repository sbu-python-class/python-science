# http://docs.enthought.com/mayavi/mayavi/mlab_case_studies.html

import numpy as np

from mayavi import mlab

x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
s = np.sin(x*y*z)/(x*y*z)

mlab.contour3d(s)
mlab.show()

# volume rendering
mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.show()


# change the data limits
mlab.pipeline.volume(mlab.pipeline.scalar_field(s), vmin=0, vmax=0.8)
mlab.show()


# cut planes
mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
                                 plane_orientation='x_axes',
                                 slice_index=10)
mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(s),
                                 plane_orientation='y_axes',
                                 slice_index=10)
mlab.outline()
mlab.show()


# combination
src = mlab.pipeline.scalar_field(s)
mlab.pipeline.iso_surface(src, contours=[s.min()+0.1*s.ptp(), ], opacity=0.1)  # ptp is the range 
mlab.pipeline.iso_surface(src, contours=[s.max()-0.1*s.ptp(), ],)
mlab.pipeline.image_plane_widget(src,
                                 plane_orientation='z_axes',
                                 slice_index=10)

mlab.show()
