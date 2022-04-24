# Module Paths

How does python find modules?  It has a search order:

* current directory

* `PYTHONPATH` environment vairable

* System-wide python installation default path

We can look at the path via ``sys.path``.  On my machine I get:

```
['/home/zingale/.local/bin',
 '/home/zingale/development/Microphysics/python_library',
 '/home/zingale/development/AmrPostprocessing/python',
 '/home/zingale/classes/python-science/examples/packaging/single_file',
 '/home/zingale/classes/numerical_exercises',
 '/home/zingale/development/pyro2',
 '/home/zingale/classes/astro_animations',
 '/home/zingale/development/pynucastro',
 '/usr/lib64/python310.zip',
 '/usr/lib64/python3.10',
 '/usr/lib64/python3.10/lib-dynload',
 '',
 '/home/zingale/.local/lib/python3.10/site-packages',
 '/home/zingale/development/pyjournal2',
 '/usr/lib/python3.10/site-packages',
 '/usr/lib64/python3.10/site-packages',
 '/usr/lib/python3.10/site-packages/IPython/extensions',
 '/home/zingale/.ipython']
```

Some of these are things that I explicited added to my `PYTHONPATH` shell variable.


Notice that the general places that it looks are in `~/.local` and in
`/usr`.  The first is the user-specific path -- you can install things
here without admin privileges.  The second is a system-wide path.

You can find your user-specific path via:

```
python3 -m site --user-site
```

