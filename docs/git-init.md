# Git/Github Introduction

Git and Github are used for Version Control and to "backup" code - allowing multiple machines to access and get it from a remote server.

Git is an application on your local machine. Github is a remote application hosted on the cloud (someone else's machine). Github also allows you to "backup" your code: with the right authorization you can access it from any machine.

Now let's Git gud at Git.

Obviously you have a GitHub account it you're here.

[Install Git.](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) Become familiar with using documentation. You need Git installed for any following instructions.

Installing the [Github CLI](https://cli.github.com/) is recommended for ease of use for logging in.

Alternatively, you can use the Github extension in VSCode (if you use it) or Github Desktop (if you use it). Personally, I prefer using git on the Command Line.

Check if Git installed correctly using ```git -v```. 

Then, identify yourself to Git using: <br/> 
```git config --global user.name "your name"``` <br/>
```git config --global user.email "your.name@domain.com"```


When you make your first ```git push``` (more on this later) Git will ask you to login if you aren't already.

Now that we are set up, let's get the YorkGPT repo, make a change and push it to the repo!

First, get the repo on your own machine. Using the terminal of VSCode or your preferred Integrated Development Environment (IDE), navigate to a folder where you want to store your projects and run this: <br/>
```git clone https://github.com/darrylnurse/yorkgpt.git``` 

You should be able to see the YorkGPT directory, and all the files - just like on the Github.

For safety, we are going to introduce you to branches a little early. A branch is like another "timeline" in a project where something *else* happened. We want to create this timeline and compare it to the original timeline and see if there are any paradoxes (conflicts that arise due to differences), and resolve them. If there are no paradoxes, these timelines can be combined (merging).

Let's see what branch we are on now: ```git branch```

You should see '> main'. The main branch is the original timeline.

Create your own timeline: ```git checkout -b <branch_name>``` (Replace branch name with what you want to call the branch. A common name for this branch is 'working'. Because you each will create a branch, it might be helpful to name it 'your_name_working'.)

Run ```git branch``` again and you should see that you are on the new branch. Because you are on a separate branch, there is no risk of you destroying the original timeline and shattering all of reality.

*Now* let's make some changes. 

Go to [README.md](../README.md) and add your name to the list of Project Collaborators. Yep, that's all (for now).

Time to push your code from Git to Github.

Remember the trinity (and order) of sending your code off into the cloud:
* ```git add .```
* ```git commit -m "<your commit message goes here>"```
* ```git push -u origin <your_branch_name>```

Let's break it down. 🕺

```git add .``` adds all untracked (U) or modified (M) files to the staging area. The staging area is pretty much like putting your code in a locker, but not locking it yet.

```git commit -m "<blah blah blah>"``` locks the locker, and etches your changes into the timeline and the fabric of reality itself. The '-m "message"' part is the message attached to the commit. It is incredibly helpful to everyone if your commit message is brief but descriptive. Try leaving it out with ```git commit``` and see what happens (vi jumpscare). You can escape that evil dialogue box by hitting the escape button and typing ```:wq``` (You'll have to redo the commit though).

```git push``` sends your code to the associated remote Github repository. You can check the remote repo by running ```git remote -v```. It should show this: <br/>
```origin  https://github.com/darrylnurse/yorkgpt.git (fetch)``` <br/>
```origin  https://github.com/darrylnurse/yorkgpt.git (push)```

```-u```sets the upstream of your branch. Think of it as just saying "Whenever I want to make a change, I want it to be in this timeline!". In your case, "this timeline" is the branch you created, which is specified by ```origin <your_branch_name>```. When you attempt to push to a branch that exists locally but not remotely, Github will create that branch on the repository.

Nice job guys, now quickly head back to the [YorkGPT repo on the Github website](https://github.com/darrylnurse/yorkgpt) and you should see a little message that says "your_branch_name had recent changes, compare to main" or something like that. Hit compare to main and add Darryl Nurse as a reviewer (this should be on the top right corner of the compare area). After that, there should be a bright green button saying "Create Pull Request". A pull request (you will hear it as a 'pr' a lot) is you saying "hey can we combine timelines pleaseeeee" and someone else says "fineee". Usually it requires someone else to review before branches (timelines) can be merged (combined), but I am too lazy to set that up. I trust you guys.

Once merged, you should see your name on the front of the repo!

Okay, we're done. Yippee!