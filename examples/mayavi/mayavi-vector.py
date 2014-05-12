# http://docs.enthought.com/mayavi/mayavi/mlab_case_studies.html

import numpy as np

from mayavi import mlab

x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]

u =    np.sin(np.pi*x) * np.cos(np.pi*z)
v = -2*np.sin(np.pi*y) * np.cos(2*np.pi*z)
w = np.cos(np.pi*x)*np.sin(np.pi*z) + np.cos(np.pi*y)*np.sin(2*np.pi*z)


# a quiver field
mlab.quiver3d(u, v, w)
mlab.outline()
mlab.show()


# thin things out -- this doesn't seem to work?
src = mlab.pipeline.vector_field(u, v, w)
#mlab.pipeline.vectors(src, mask_points=20, scale_factor=1.)  # keep only one point out of 20
#mlab.outline()
#mlab.show()


mlab.pipeline.vector_cut_plane(src, mask_points=2, scale_factor=3)
mlab.outline()
mlab.show()


# isosurfaces of the magnitude -- doesn't work
#magnitude = mlab.pipeline.extract_vector_norm(src)
#mlab.pipeline.iso_surface(magnitude, contours=[1.9, 0.5])
#mlab.outline()
#mlab.show()


mlab.figure(fgcolor=(0., 0., 0.), bgcolor=(1, 1, 1))
src = mlab.pipeline.vector_field(u, v, w)
magnitude = mlab.pipeline.extract_vector_norm(src)

# We apply the following modules on the magnitude object, in order to
# be able to display the norm of the vectors, eg as the color.
iso = mlab.pipeline.iso_surface(magnitude, contours=[1.9, ], opacity=0.3)

#vec = mlab.pipeline.vectors(magnitude, mask_points=40,
#                                    line_width=1,
#                                    color=(.8, .8, .8),
#                                    scale_factor=4.)

flow = mlab.pipeline.streamline(magnitude, seedtype='plane',
                                        seed_visible=False,
                                        seed_scale=0.5,
                                        seed_resolution=1,
                                        linetype='ribbon',)

vcp = mlab.pipeline.vector_cut_plane(magnitude, mask_points=2,
                                        scale_factor=4,
                                        colormap='jet',
                                        plane_orientation='x_axes')
mlab.show()


