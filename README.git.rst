Git
===

Moving a subdirectory from one repo into a whole new repo
---------------------------------------------------------

So you want to create a brand new repository containing
files from a subdirectory in an existing repository,
while preserving history.
No problem, just follow this example.
Let's assume the existing repo is called `repo1` and the
subdirectory of interest is `repo1/foo/bar`
at revision `0123456789abcdef`.
And let's assume the new repo will be called `repo2`.

First move the directory `repo1/foo/bar`:
::

   cd repo1
   git co 0123456789abcdef
   cd ..
   git clone repo1 repo1-clone
   cd repo1-clone
   git filter-branch --prune-empty --subdirectory-filter foo/bar


Now create a new empty repo called `repo1`.

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
