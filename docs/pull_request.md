# Send a Pull-Request to a GitHub project

* If you don't have yet, create an account on [GitHub](https://github.com/).
* We assume you have already [installed and configured git](install_git.md) on your local machine.
* Visit the GitHub page of the project. [project](https://github.com/szabgab/modiin-co-learning/). This is the full Git repository of the project.
* 'fork' this repository: See the fork button on the GitHub page of the project. Assuming your username on GitHub is foobar, this will create a copy of the whole Git repository in your GitHub account and you'll have a URL: https://github.com/foobar/modiin-co-learning/ 
* 'clone' the forked repository to your local disk.
   * Open your terminal or Command Prompt if you are on Windows
   * Change to a directory where you'd like to have a subdirectory for the project. e.g. I have a directory called `~/work` and inside I have a directory for each project. So I'd `cd ~/work` and then `git clone https://github.com/foobar/modiin-co-learning.git` 
   * On Windows I have a directory called `c:\\work` so I `cd \work` and then run the clone command.
   * In both cases it will create a subdirectory called 'modiin-co-learning' and will create a copy of the whole Git repository in that directory on your local machine.
* Create a branch: `git checkout -b myname`
* Add yourself to the '''participants.json''' file.
  * `name` and `github user ID` are required fields
  * the rest are optional
* Add the changed file to the staging area of git: `git add participants.json`
* Commit the changes: `git commit -m "adding my name"`
* Push out the changes to your forked repository `git push`
* Send a Pull-request with the changes (on GitHub)
* Look at the results, check if the Travis-CI job was successful. If not, check why not, fix the problem, commit the changes, and push the new changes out to GitHub again.
* Observe how someone sees the PR and how can that person react.
* **_Once the pull request has been accepted and merged_**, delete the branch locally, and push the delete to your remote.  This will delete the remote branch as well.
```
   git branch -d <branchname>
```

```
   git push origin :<branchname>
```

