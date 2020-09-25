import os

def createnewproject(directory):
    if not os.path.exists(directory):
        print("Creating new project"+directory)
        os.makedirs(directory)

createnewproject('newshivam')


