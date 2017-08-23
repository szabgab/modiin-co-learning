
# Update your local Git repository from the central repository of the project.

There are several cases we are going to cover.

* In the first case we assume you have forked and cloned the project but have not made any local changes yet.
* In the second case we assume you created a local branch, made some changes, pushed them out to GitHub and they were integrated into the main repository of the project.
* In the third case you made some changes in a local branch but have not pushed it out yet.
* In the 4th case you made changes in the local branch, pushed it out, maybe even sent a Pull-request, but it has not been integrated yet.


### No local changes yet

```
git remote add upstream
git pull origin master
git push
```

### Integrated branch

* The project has a Github repository. e.g. https://github.com/szabgab/codeandtalk.com
* You created a fork e.g. https://github.com/demo/codeandtalk.com   (if your GitHub username is demo)
* You created a copy of the git repository on your own computer by running `git clone git@github.com:demo/codeandtalk.com.git`
* You created a branch (e.g. one called myname) using `git checkout -b myname`
* You made some progress there, you have pushed your changes out to your GitHub account, sent a Pull Request. It was accepted and your changes were merged.

* In the meantime the repository where it all started https://github.com/szabgab/codeandtalk.com has also moved forward. You need to get your clone and your fork up to date with that.

At this point we can assume that if you run `git status` it will tell the there is nothing to do in your repository.
`git branch` will show that there are two branches

```
* myname
master
```

First we need to switch to the `master` branch using

```
git checkout main
```

Then we need to map the 'central' GitHub repository to be one of you remote repositories
If you run

```
git remote -v
```

It will list all the remote repositories currently mapped in your local repository.

```
origin  git@github.com:demo/codeandtalk.com.git (fetch)
origin  git@github.com:demo/codeandtalk.com.git (push)
```

This means the repository 'codeandtalk.com' in GitHub in the account of 'demo' is locally called 'origin'.
We have two entries as they map the communication to and from the remote reposiotry. Theoretically we could have them point
to two different repositories, but that's rearly needed.

The command

```
git remote add upstream https://github.com/szabgab/codeandtalk.com.git
```

will map the codeandtalk.com repository of user szabgab to the name 'upstream'. This is another arbitrary name, but one that is
commonly accepted to point to the 'central' repository of a project. I put the word central in quotes because Git does not really
have the concept of central repository. It is only a convention that makes the life of the developers easier. It is also accepted
to be the official repository of the project.

Running this command again:

```
git remote -v
```

We will see 4 entries:

```
upstream  git@github.com:szabgab/codeandtalk.com.git (fetch)
upstream  git@github.com:szabgab/codeandtalk.com.git (push)
origin  git@github.com:demo/codeandtalk.com.git (fetch)
origin  git@github.com:demo/codeandtalk.com.git (push)
```

Now we can update our local repository from the official repository of the project by executing:

```
git pull upstream main
```

Then we can update our repository in our GitHub account by executing:

```
git push
```

Here we don't need to specify extra information because the 'main' branch in our local repository was
already mapped to the 'main' branch of our repository in our GitHub account.


The changes we pulled from upstream and then we pushed out to our origin aleady contain the content of our branch
as it was merged by the author of the project. This means we don't need our development branch any more. We should delete it locally
using the

```
git branch -d myname
```

command.

We should also delete the branch from our repository in our GitHub account using:

```
git push origin :myname
```

We are now done. Our changes were integrated. All the progress of the project was brought to our repositories.
We can not tackle the next problem.


### Changes that were not pushed out

Update the main branch from upstream:
```
git checkout main
git pull upstream main
git push
```

Then rebase your branch fixing the conflict:

```
git checkout name-of-the-local-branch
git rebase main
```

Git will tell you there is a conflict when you rebase.
You should open the file with your editor, fix the conflict to whatever you think it should look like and then continue the rebase.

### Rebase your local branch and update a PR

Like in the previous case, but after you have finished rebasing the branchm, you also need
to push out the new changes to the parallel branch in your GitHub account.

```
git push
```

will fail because you effectively changed the history.

You can use the force:
```
git push --force
```

With this you should be done.

