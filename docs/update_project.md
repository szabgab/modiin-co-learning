
### Update your local Git repository from the central reposiotry of the project.

* A project has a Github repository. e.g. https://github.com/szabgab/codeandtalk.com
* You created a fork e.g. https://github.com/demo/codeandtalk.com   (if your GitHub username is demo)
* You created a copy of the git repository on your own computer by running `git clone git@github.com:demo/codeandtalk.com.git`
* You created a branch (e.g. one called myname) using `git checkout -b myname`
* You made some progress there, you might have even pushed it out, sent a Pull Request, and it might be have been even accepted. In any case, you made some progress there.
* In the meantime the repository where it all started https://github.com/szabgab/codeandtalk.com has also moved forward. You need to get your clone and your fork up to date with that.

* `git checkout main`
* `git remote -v`
* `git remote add upstream https://github.com/szabgab/codeandtalk.com.git`
* `git pull upstream main`
* `git push`


# Rebase your local branch and update a PR

Update the main branch from upstream:
```
git checkout main
git pull upstream main
```

Then rebase your branch fixing the conflict:

```
git checkout name-of-the-local-branch
git rebase main
```

Git will tell you there is a conflict when you rebase.
You should open the file with your editor, fix the conflict to whatever you think it should look like and then continue the rebase.


Then push out the branch using
```
git push --force
```

