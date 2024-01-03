#!/usr/bin/python3
for b in range(97, 123):
    if b in [101, 113]:
        continue
    print("{}".format(chr(b)), end="")
