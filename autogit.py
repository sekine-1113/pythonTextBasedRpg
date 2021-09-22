import os


comment = input("Git commit message >> ")

git_add = "git add ."
git_commit = "git commit -m {}"
git_push = "git push origin main"

os.system(git_add)
os.system(git_commit.format(comment))
os.system(git_commit)
