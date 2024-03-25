# Module Paths

How does python find modules?  It has a [search order](https://docs.python.org/3/tutorial/modules.html#the-module-search-path):

* current directory

* `PYTHONPATH` environment variable (this follows the same format as
  the shell `PATH` environment variable)

* System-wide python installation default path (usually has a
  `site-packages` directory)

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
 '/usr/lib64/python311.zip',
 '/usr/lib64/python3.11',
 '/usr/lib64/python3.11/lib-dynload',
 '',
 '/home/zingale/.local/lib/python3.11/site-packages',
 '/home/zingale/development/pyjournal2',
 '/usr/lib/python3.11/site-packages',
 '/usr/lib64/python3.11/site-packages',
 '/usr/lib/python3.11/site-packages/IPython/extensions',
 '/home/zingale/.ipython']
```

Some of these are things that I explicitly added to my `PYTHONPATH` shell variable.


Notice that the general places that it looks are in `~/.local` and in
`/usr`.  The first is the user-specific path&mdash;you can install things
here without admin privileges.  The second is a system-wide path.

You can find your user-specific path via:

```bash
python3 -m site --user-site
```

on my machine, this gives:

```
/home/zingale/.local/lib/python3.11/site-packages
```

```{tip}
Using `PYTHONPATH` to quickly add a module to your search path is an easy hack,
but if you are developing a library that will be used by others, it is better
to make the modules installable to the system search paths.  This is where
_packaging_ comes into play.
```
