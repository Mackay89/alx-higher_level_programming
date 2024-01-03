#!/usr/bin/python3
for b in range(97, 123):
    if b in [103, 113]:
        continue
    print("{:c}".format(b), end="")
