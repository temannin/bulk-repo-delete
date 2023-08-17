# GitHub Repo Delete
A python script to delete GitHub repositories quickly and safely.

## Requirements
- python3
- GitHub CLI 

## Running
Either clone or copy the script `main.py`. In a shell, run:

```export  GITHUB_USERNAME <username>```

Then run the python script. It will go down the list of all the repos (capped at 1000) and ask you one-by-one if you want to delete that repo. (y/n)