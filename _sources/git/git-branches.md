# Git Branches

When we develop as a team, we often use *branches* to organize our
changes.  Here we walk through an example of branches.

To get more practice, we'll start a new project and initialize it.

```{figure} https://imgs.xkcd.com/comics/git.png
   :width: 75%
   :align: center
   :alt: xkcd comic on git

   from XKCD
```

1. Let's repeat the setup we did before...

   ```bash
   mkdir project2
   cd project2
   echo "a second git project" > README
   git init
   ```

2. Now let's add our `README` to git and commit:

   ```bash
   git add README
   git commit
   ```

   (Remember to enter a log and save...)

3. Let's create and add another file.

   We write a simple shell script.  Open a new file, called `myscript`, e.g., with nano:

   ```bash
   nano myscript
   ```

   and copy-paste the following content into it:

   ```bash
   ls -l > script.out
   ```

   be sure to end with a new line.

   Now, this script is not that fancy and it needs to be run as:

   ```bash
   bash ./myscript
   ```

   when you do this, you should see the output `script.out` created.

   Now let's tell git that we want it to track this:

   ```bash
   git add myscript
   git commit
   ```

   Be sure to add a useful message.

4. Ignoring things.

   Let's look at the status of our project:

   ```bash
   git status
   ```

   You'll see something like:

   ```
   On branch main
   Untracked files:
     (use "git add <file>..." to include in what will be committed)

        script.out

   nothing added to commit but untracked files present (use "git add" to track)
   ```

   It is telling us that it is not keeping track of `script.out`.
   But we don't want it to&mdash;that is the output from running out
   script, and generally we don't keep the output of our codes in
   version control.

   So we'd like to tell git to ignore that file.  The way to do this is to
   create a `.gitignore` file:

   ```bash
   nano .gitignore
   ```

   and add the following:

   ```
   *.out
   ```

   now if you do `git status`, that file will not appear, but `.gitignore` does!

   Be sure to add `.gitignore` to git by doing `git add` followed
   by `git commit`.



## A Feature Branch

Now let's imagine that our project is mature and we don't want to break it as
we test out some new ideas.  This is where *branches* come into play.

Let's create a new branch called `feature` that we can work on without
disturbing our code in ``main``.

```bash
git checkout -b feature
```

This creates a new branch called `feature` that is initially identical to `main`.

You can tell what branch you are on by doing:

```bash
git branch
```

and we see:

```
* feature
  main
```

The `*` indicates which branch we are currently on.

What about the log?

```bash
git log
```

we see:

```
commit 69eb3bf482bd78c3bf63e890f52b9aac33d5ee2a (HEAD -> feature, main)
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:21:19 2022 -0500

    add an ignore file

commit 9b0ae624393bd28f26f37d633d9692be3c2929f0
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:18:53 2022 -0500

    add my first script

commit 9625926dd4bc26e04d37988ffceaa7eba64a76da
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:18:02 2022 -0500

    start of our new project
```

Notice that the most recent commit line shows that both `feature` and `main`
are at the same hash, and it also calls that commit `HEAD`.
`HEAD` is the most recent change on the branch.


Now let's make a change.

Let's put a "Hello, World" code in our repo!  Create a file called
`hello.cpp` and add the following:

```c++
#include <iostream>

int main() {

    std::cout << "Hello, World!" << std::endl;

}
```

Let's add it to git control:

```bash
git add hello.cpp
git commit
```

Now look at the log:

```
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:23:51 2022 -0500

    add hello world

commit 69eb3bf482bd78c3bf63e890f52b9aac33d5ee2a (main)
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:21:19 2022 -0500

    add an ignore file

commit 9b0ae624393bd28f26f37d633d9692be3c2929f0
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:18:53 2022 -0500

    add my first script

commit 9625926dd4bc26e04d37988ffceaa7eba64a76da
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:18:02 2022 -0500

    start of our new project
```

Now it is clear that `main` is still on the last commit but
`feature` is on the latest (`HEAD`) commit.


Recall that we can compile our `hello.cpp` via:

```bash
g++ -o hello hello.cpp
```

```{tip}
We don't want the executable `hello` to be under git control, so
add it to your `.gitignore` and commit that change.
```


## Switching Branches

Let's go back to `main`.  The `checkout` command does this for us:

```bash
git checkout main
```

Now notice that if you do `ls`, you don't see `hello.cpp`!  That
file is in your `feature` branch, and under git control, and git
knows it is not on `main` so when you switch to main, it does not
appear.

Let's add an `authors.txt` file to our project, just containing your name.

```{admonition} Try it...
create an `authors.txt` and add it to git control.
```

Note that this is on `main`.  If you switch to `feature` you won't see it:

```bash
git checkout feature
```

````{tip}
Just like we can use ``cd -`` to switch to the previous directory we were on,
we can use

```bash
git checkout -
```
to switch back to the previous branch we were on -- in this case, `main`
````

Switch back to ``main``.


## Diff

Let's look at the differences between our branches.  Since we're on
`main`, we can ask git what the difference between our current code
and the code in `feature` is via:

```bash
git diff feature
```

As you use git more and more, you'll see that `diff` is very handy.


## Merging

Now we're happy with the changes we made on `feature` and we want to
incorporate them into `main`&mdash;this is called *merging*, we
accomplish this by doing

```bash
git merge feature
```

This is a special type of commit, and your editor will pop up with a
merge commit already entered.  Just save this, and it will be logged.


## Going back in time...

If we look at our project history so far:

```bash
git log
```

We see something like this (again, your hashes will be different)

```
commit 42596acdd432e1dbdc4f8abd668dffa30c707473 (HEAD -> main)
Merge: c8904ec bb38a3d
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:54:51 2022 -0500

    Merge branch 'feature' into main

commit c8904ec0bd8ac1bc3449ec79ade971ee9902c14e
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:31:03 2022 -0500

    add authors

commit bb38a3d1f3f4f2971ced93a1f203c52c276f37a5 (feature)
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:27:09 2022 -0500

    don't track executable

commit 22e1d58cee38021da961516b24dde689d3b8a66e
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:23:51 2022 -0500

    add hello world

commit 69eb3bf482bd78c3bf63e890f52b9aac33d5ee2a
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:21:19 2022 -0500

    add an ignore file

commit 9b0ae624393bd28f26f37d633d9692be3c2929f0
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:18:53 2022 -0500

    add my first script

commit 9625926dd4bc26e04d37988ffceaa7eba64a76da
Author: Michael Zingale <michael.zingale@stonybrook.edu>
Date:   Tue Feb 1 10:18:02 2022 -0500

    start of our new project
```

Imagine that our current code is not working, but we remember that it
was before we did our branching and added the `hello.cpp`.  Looking
at the log or the graph shows that that change came in with the commit
`22e1d58cee38021da961516b24dde689d3b8a66e`.  We can checkout the
state of the code before that commit by using the hash from the
previous commit:

```bash
git checkout 69eb3bf482bd78c3bf63e890f52b9aac33d5ee2a
```

Note that you don't need to type out the entire hash&mdash;you only need the starting bits,
as long as it is unique.

This command puts you in a detached branch, but you could make it a named branch by using
`git checkout -b name`.
