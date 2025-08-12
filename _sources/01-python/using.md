# Using These Notes

These notes are built via [Jupyter book](https://jupyterbook.org/), as
a collection of [Jupyter](https://jupyter.org/) notebooks and markdown
pages.

The course is on Github at:
https://github.com/sbu-python-class/python-science, and the course
website is built automatically via a Github action each time a change
is pushed.

If you find any problems or have suggestions for improving the notes,
feel free to create an issue or pull request at the Github repo.

## Interactive Usage

For the Jupyter notebooks in this collection, there are a few ways to
access them to run them on your own.

* clicking on the {octicon}`download` icon in the upper right let's
  you download the raw notebook so you can run it on your local
  computer.

* clicking on the {octicon}`rocket` icon in the upper right will allow
  you to run the notebook directly in the cloud.  There are 2 different
  compute clouds:

  * [mybinder](https://mybinder.org/) : this is an open project with
    ties to the Jupyter project.  It can take a few minutes for the
    page to appear if it hasn't been accessed recently, but then it
    will give you the standard Jupyter experience.

  * [Google colab](https://colab.research.google.com/) : this is
    Google's version of an online notebook, which runs directly in
    Google's cloud.  This starts up almost instantly.

````{note}
Some notebooks use [MyST Markdown](https://jupyterbook.org/en/stable/content/myst.html) to 
allow for more styling.  To see these styles, you need to install `jupyterlab-myst`, which
can be done via:
```
pip install jupyterlab_myst
```

````
