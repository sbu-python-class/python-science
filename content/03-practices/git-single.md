A single-user interaction with git:

* Make your project

  We'll start by making our project directory and moving into it:

  ```
  $ mkdir myproject
  $ cd myproject/
  ```

* Now have git track this

  Now we do `git init .` -- this tells git to initialize this
  directory under version control

  ```
  $ git init .
  ```

  If we do `ls` at this point, we see nothing.  However, there is a
  "hidden" directory called `.git/` which we can see by passing `-a`
  to `ls`:

  ```
  $ ls -al
  $ ls -l .git
  ```

  In that directory are the files that git uses to keep track of
  changes and the history.

* Create a file

  We'll create a file called `README` (use whatever editor you like,
  I'll use emacs):

  ```
  $ emacs -nw README
  ```

  Add some descriptive text to the file and save it.  At the moment,
  git doesn't know about this file -- you can see this via `git
  status`:

  ```
  $ git status
  ```

* Tell git about the file

  Now we need to tell git to start tracking the file.  We use
  `git add` for this.  Then we need to tell git to store the current
  state of the file -- we use `git commit` for this:

  ```
  $ git add README
  $ git commit README
  ```

  Notice that an editor window pops up -- take the time to give a
  descriptive message about the changes.

  If you make more changes to the file, git won't store them until
  you commit them.  So you'll commit the same file over and over as
  it changes, but only add it once.

* Create another file

  Let's create a python program, `awesome.py` with the line:

  ```
  print("hello")
  ```

  Now add that file and commit it too

  ```
  $ git add awesome.py
  $ git commit .
  ```

* Look at your log

  `git log` will show you all the commits, the message you entered
  when you made the commit (that helps you understand what was done).
  It will also have a "hash" next to the commit (like
  `dbc2916bb609759d54ca7668558bc639bab9b60b`)

  ```
  $ git log
  ```

* Add to you code

  Edit `awesome.py` and make it a function and have your program call
  the function.  Now we need to commit this again:

  ```
  $ git commit awesome.py 
  ```

  And `git log` will show this commit as separate from the one we made
  when we created the file.

* Go back in time

  Suppose our code is not working anymore, and we know it was in the
  past.  We can go back to any previous version of the code by using
  `checkout` and the hash next to that commit (note: your hashes will
  be different than mine).

  ```
  $ git log
  $ git checkout dbc2916bb609759d54ca7668558bc639bab9b60b
  ```

  Look at the file, and you'll see it is different.  

  If you want to go back to the latest version, you can checkout `master`
  -- that's the name of the main "branch" git recognizes.

  ```
  git checkout master
  ```

* Working with branches

  Suppose we want to do some development that might be invasive and we
  don't want to break the working code on "master".  We can use a
  branch for this -- thing of this as a parallel development that can
  track the master branch and merge back and forth with it.  We can
  work on this new branch until we are happy, and then incorporate our
  changes back to `master`.
 
  Here we'll create a new branch called `development`:

  ```
  $ git checkout -b development
  ```

  Now make some changes to `awesome.py` and commit them.

  ```
  $ emacs -nw awesome.py
  $ git commit awesome.py
  ```

  If you go back to `master`, you won't see these changes:

  ```
  $ git checkout master
  $ more awesome.py
  ```

  If you are happy with the changes, you can do a merge.  While on
  `master`, merge `development` into `master` with:

  ```
  $ git merge development
  ```

