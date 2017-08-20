# Send a Pull-Request to a GitHub project

* If you don't have yet, create an account on GitHub.
* 'fork' this repository (see the green fork button on the GitHub page of the project)
* 'clone' the forked repository to your local disk  `git clone ...`
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

