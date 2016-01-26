# git-training
A few branches and commits to practice the rebase and branches

What to do?
===========
1. fetch the code!

```
$ git clone git@github.com:mart-e/git-training.git
$ cd git-training
$ git remote -v
origin	git@github.com:mart-e/git-training.git (fetch)
origin	git@github.com:mart-e/git-training.git (push)
$ git branch
* master
```

2. fork it on your GitHub account

From the web interface, at https://github.com/mart-e/git-training

3. Add your new remote
```
$ git remote add my_user git@github.com:my_account/git-training.git
```

What to rebase?
===============

```
$ git branch -r
  origin/HEAD -> origin/master
  origin/master
  origin/rebase-withconflict
  origin/simple-rebase
```

Simple
------
1. create a local fork of **origin/master** (e.g. `my-master`) and push it on **your** remote
2. fetch the branch **origin/simple-rebase**
3. rebase **simple-rebase** onto your master

Conflict
--------
1. fetch the branch **origin/rebase-withconflict**
2. rebase **rebase-withconflict** onto your master (with simple-rebase already there)
3. resolve the conflicts
