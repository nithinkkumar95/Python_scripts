import random
import sys
import os
print(random.randint(2, 5))

for i in range(2,5):
  print(i)

print(sys.argv[0])
#print(sys.exit(0))

#print(sys.argv[1])
print(sys.path)

#os.chdir("/home/ubuntu")

#os.makedirs("dir1")

print(os.getcwd())

print(os.listdir("/home/ubuntu"))

for path, dir, files in os.walk("/home/ubuntu"):
    print(path)
    print(dir)
    print(files)
