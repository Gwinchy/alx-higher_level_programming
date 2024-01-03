#!/usr/bin/python3
alphabet = ''.join('{}' for _ in range(ord('a'), ord('z') + 1)).format(*(chr(i) for i in range(ord('a'), ord('z') + 1)))
print(alphabet, end='')
