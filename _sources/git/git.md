# A Git Walkthrough

We'll do a walkthrough on git.

```{note}
An alternate walkthrough is provided by the [Software
Carpentry](https://software-carpentry.org/) lesson [_Version Control
with Git_](https://swcarpentry.github.io/git-novice/index.html) and it
is highly suggested that you work through that on your own.
```

There are a few ways in which we can use git.  We'll start by assuming
that we are the only developer on a project and learn the basics and
then we'll see how to share what we've done locally and remotely using
GitHub.

```{important}
You should create a [GitHub account](https://github.com).  Pick a
username that is professional and meaningful.
```

Let's start by setting up our git environment:

```bash
git config --global user.name "name"
git config --global user.email "email"
git config --global core.editor "nano -w"
```

Replace `name` with your name and `email` with your email.  This sets `nano`
as our default editor, but you can choose something else that you are comfortable
with (see https://swcarpentry.github.io/git-novice/02-setup/index.html#line-endings).

This information will be stored in a file called ``.gitconfig`` in your home directory.


Our goal here is to create a project (we'll call the directory
`project/`) and have git keep track of the files and changes to our
project.

1. First create a project directory with some basic content:

   ```bash
   mkdir project
   cd project
   echo "this is the start of my awesome new project" > README
   ```

2. Now let's tell git that we want to track this directory.

   ```bash
   git init
   ```

   If you do `ls` it will look like nothing has changed, but this
   command created a `.git/` sub-directory in our project, which you
   can see by doing:

   ```bash
   ls -a
   ```

3. At this point, we haven't told git about any of our files.  To tell git
   to track the file `README` we do:

   ```bash
   git add README
   git commit README
   ```

   ```{note}
   When you `commit`, and editor window will pop up asking you to
   make a commit message.  This is where you describe the change so
   "future you" or someone else can understand why the change was
   made.
   ```

   The editor will be whatever your default is.
   We can now ask git the state of our project with

   ```bash
   git status
   ```

   You should see something like:

   ```
   On branch main
   nothing to commit, working tree clean
   ```

   We can also see our log message:

   ```bash
   git log
   ```

   The output will look like:

   ```
   commit 2001a0e996110926a576dcb5fc13fc8022864d0b (HEAD -> main)
   Author: Michael Zingale <michael.zingake@stonybrook.edu>
   Date:   Sun Jan 30 13:11:24 2022 -0500

       my first change
   ```

   But should show your name, and the long string of numbers of
   letters after `commit` on the first line will be different.  We'll call
   the string the `hash`.  More on that later...

4. Now let's modify the file

   Open the file with nano and add a second line of text:

   ```bash
   nano README
   ```
   
   Here's my file:

   ```bash
   cat README
   ```
   
   ```
   this is the start of my awesome new project
   this is now under version control!
   ```
  
   What does git think about our changes?

   ```bash
   git status
   ```
   
   you should see something like:

   ```
   On branch main
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git checkout -- <file>..." to discard changes in working directory)

           modified:   README

   no changes added to commit (use "git add" and/or "git commit -a")
   ```
   
   This is telling you that you have local changes but you haven't yet told git to care about them.

   Let's `add` the changes:

   ```bash
   git add README
   ```

   and now `git status` will show something like:

   ```
   On branch main
   Changes to be committed:
     (use "git reset HEAD <file>..." to unstage)

           modified:   README
   ```

   ```{note}
   **What is add really doing?**

   Git has a concept call the *staging area*.  When we ``add`` a
   file, git puts the changes into the staging area.  We can add
   multiple changes via separate ``git add`` invocations, and git
   will accumulate these in the staging area.

   Once we do `git commit`, git will record the all of the
   changes that are staged into a "commit".
   ```
   
   To have git track these changes, we can now just do:

   ```bash
   git commit
   ```
   
   Notice that we didn't specify the file here -- all the changes that
   were staged were part of that commit.

   If we now do `git log`, we'll see that there is a second commit
   in our project, and it has a different unique hash:

   ```
   commit 78b6925752e8388dddb3d65b6355bfeeb87b87a7 (HEAD -> main)
   Author: Michael Zingale <michael.zingake@stonybrook.edu>
   Date:   Sun Jan 30 14:23:09 2022 -0500

       make some modifications

   commit 2001a0e996110926a576dcb5fc13fc8022864d0b
   Author: Michael Zingale <michael.zingake@stonybrook.edu>
   Date:   Sun Jan 30 13:11:24 2022 -0500

       my first change
   ```

This repo now captures the state of our project.  Next we'll see how to use branches to
help our development process.


Summary
=======

We learned:

* `git init`

* `git add`

* `git commit`

* `git status`

* `git log`
