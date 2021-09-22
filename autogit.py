import os
import sys

def split(x, s="="):
    return x.split("=")


if sys.argv[1:]:
    comments = list(map(split, sys.argv[1:]))
    for i, cmt in enumerate(comments):
        if "message" in cmt:
            comments[i].remove("message")
            comment = comments[i][0]
else:
    comment = input("Git commit message >> ")

git_add = "git add ."
git_commit = "git commit -m {}"
git_push = "git push origin main"

os.system(git_add)
os.system(git_commit.format(comment))
os.system(git_commit)
