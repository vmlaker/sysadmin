Git
===
Moving a subdirectory from one repo into a whole new repo
---------------------------------------------------------
So you want to create a brand new repository containing
files from a subdirectory in an existing repository,
while preserving history.
No problem, just follow this example.
Let's assume the existing repo is called ``repo1`` and the
subdirectory of interest is ``repo1/foo/bar``
at revision ``0123456789abcdef``.
And let's assume the new repo will be called ``repo2``.

First move the directory ``repo1/foo/bar``:
::

   cd repo1
   git co 0123456789abcdef
   cd ..
   git clone repo1 repo1-clone
   cd repo1-clone
   git filter-branch --prune-empty --subdirectory-filter foo/bar

Now create a new empty repo called ``repo2``.

Next, add the remote origin in the new repo:
::

   git remote rename origin upstream
   git remote add origin ssh://git@<hostname>/repo2

Notice that we're not on the master branch. In fact,
it doesn't exist at all:
::
   
   git branch -l

Finally, create the master branch, and push:
::

   git branch master
   git checkout master
   git push origin master

Frequent commands
-----------------
Query commands:
::

   git branch -r                           # Show all remote branches.
   git log origin/master..HEAD             # Show logs for unpushed commits.
   git diff --stat --cached origin/master  # Show files to be pushed.

Checkout commands:
::
   
   git checkout -t origin/bug-42  # Checkout remote branch bug-42, and track it.
   git checkout -b bug-57         # Create a new local branch bug-57 and navigate to it.
   git push origin bug-57         # Push the new local branch to remote server.
   
Gitk:
::

   gitk --all
   gitk --remotes-origin
   
Merging branches:
::

   git diff ...xxx                   # Preview changes that would result from a merge.
   git diff ...xxx --name-only       # Preview files that would be changed.
   
   git merge xxx                     # Merge branch xxx into current branch.
   git merge --no-commit xxx         # Merge, but without committing.
   git merge --no-commit -no-ff xxx  # Merge, but without comitting or fast-forwarding.
   git merge --abort                 # Abort the merge.
