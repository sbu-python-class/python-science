# github

Github provides a web-based way to interact with git repositories.  At
its heart it hosts a bare repo that we can push-pull to/from, but it
also provides features to make it easier for users to request their
changes be incorporated.


## Creating a repository on github

Let's start by creating a new git repository using github's web interface.  Start
on your github home page and click on the "+" icon and select "New repository":

```{image} github-new.png
:align: center
```

Now we give the repository a name.  Let's use our initials, followed
by `_class_repo`, so for me, it will be `mz_class_repo`.

Make sure that it defaults the repo to be public, which means anyone on the internet
can see the contents&mdash;that's what we want.

Finally, check the box to add a `README` file&mdash;this means that our repository will
not be empty initially.

```{image} github-create.png
:align: center
```

Our project is now found at: ``https://github.com/ [username]/ [reponame]``,
where *username* is your Github username and *reponame* is the name of
the repository you just created.


## SSH interlude

Github works best is we communicate via [secure
shell](https://en.wikipedia.org/wiki/Secure_Shell) or *SSH*.

There is some nice documentation describing key pairs in the Software
Carpentry [Create an SSH key pair](https://swcarpentry.github.io/git-novice/07-github/index.html#3-ssh-background-and-setup)
section.

Here's how we will set things up:

1. A the bash prompt generate a new key pair:

   ```bash
   ssh-keygen -t ed25519
   ```

   The `-t` option picks a secure encryption method.

   It will ask you for a passpharse&mdash;just hit "Enter" to keep it
   empty (if other people had access to your account, the you would
   want to pick a passphrase).

   If you do

   ```bash
   ls -l ~/.ssh
   ```

   you'll see 2 files: `id_ed25519` and `id_ed25519.pub` this is
   the private and public key for encryption.

   ```{caution}
   Never share your private key (`id_ed25519`) with anyone.

   Our public key (`id_ed25519.pub`) is meant to be public, and
   we can give it to places we want to communicate with, like github
   ```

2. Go to you Github profile SSH keys settings: https://github.com/settings/keys

   Click on the *New SSH key* button and:

   * give a *title* which is descriptive of the machine you are using, like
     ``MathLab``

   * copy and paste the contents of `id_ed25519.pub` into the *key*
     text box.  You can see the contents by doing:

     ```bash
     cat ~/.ssh/id_ed25519.pub
     ```
     
   * Click on ``Add SSH key``

3. Test things out:

   ```bash
   ssh -T git@github.com
   ```

   It will ask you if we want to save the *fingerprint*&mdash;say "yes", and then
   it should report:

   ```
   Hi zingale! You've successfully authenticated, but GitHub does
   not provide shell access.
   ```

That means everything is working.


## Working remotely

Now we can git clone this repo.  From the github project page, click on the
*code* button.

```{image} github-clone.png
:align: center
```

Copy the string in the text box there and then on your command line clone
the repo as:

```bash
git clone git@github.com:zingale/mz_class_repo.git
```

(replacing my repo and username with your own).

Now we can go into our repo and look around.

```bash
cd mz_class_repo
ls -al
```

Notice that there is a
`.git/` directory.  Also look at the remotes:

```bash
git remote -v
```

```
origin	git@github.com:zingale/mz_class_repo.git (fetch)
origin	git@github.com:zingale/mz_class_repo.git (push)
```

This is just like the example or remotes we did previously, except now
github is acting as our remote.

This means that we call push to github and pull from there.

Let's add a `hello.py`:

```python
#!/usr/bin/env python

def main():
    print("hello, world")

if __name__ == "__main__":
    main()
```

```bash
git add hello.py
git commit
git push
```

Notice that the `git push` pushes to our remote: github.  If you refresh
your browser page, you'll see that our file now appears on github.

As a single user, this will allow you to develop from any computer
and keep the code base in sync across all of them.

If the project has multiple developers, this can be where all of the
developers sync up their projects.


### `README.md` is special

The web interface that github provides to our repo has a number of features.

First, the `README.md` file is always displayed on the main project
page.  This is where you can put descriptions of what your project is,
how people can contribute, even share the status of testing and
documentation builds (we'll talk about those later in class).

This file is in github-flavored [Markdown
format](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
(that's what the `.md` extension signifies).  Markdown allows you to
do basic formatting.

Here's an example of what you can do in a `README.md` from one of my
projects: https://github.com/pynucastro/pynucastro

