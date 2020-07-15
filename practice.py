#importing modules
import os

print(os.getcwd())
os.chdir("/home/aurnam18/github/OS-and-Shutil")
fd = "text_file.txt"
file = open(fd, 'w')
file.write("hello")
file.close()
os.rename(fd, "text.txt")
print(os.path.exists("/home/aurnam18/github/OS-and-Shutil"))
