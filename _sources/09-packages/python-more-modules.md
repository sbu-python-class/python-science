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
 '/usr/lib64/python314.zip',
 '/usr/lib64/python3.14',
 '/usr/lib64/python3.14/lib-dynload',
 '',
 '/home/zingale/.local/lib/python3.14/site-packages',
 '/usr/lib64/python3.14/site-packages',
 '/usr/lib/python3.14/site-packages']
```

```{note}
You can explicitly add paths to the ``sys.path`` by setting the `PYTHONPATH`
environment variable.
```


Notice that the general places that it looks are in `~/.local` and in
`/usr`.  The first is the user-specific path&mdash;you can install things
here without admin privileges.  The second is a system-wide path.

You can find your user-specific path via:

```bash
python3 -m site --user-site
```

on my machine, this gives:

```
/home/zingale/.local/lib/python3.14/site-packages
```

```{tip}
Using `PYTHONPATH` to quickly add a module to your search path is an easy hack,
but if you are developing a library that will be used by others, it is better
to make the modules installable to the system search paths.  This is where
_packaging_ comes into play.
```
