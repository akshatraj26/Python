print(ord('A'))

s = 'Hi'
print(type(s))
print(type("Hello"))

by = b"\xe0\xa4\x85"
print(type(by))
print(type(b"\xee\x84\x65"))


eng = 'A B C D'
dev = 'अ आ इ ई'

print("English:-", type(eng))
print("Hindi:-", type(dev))
print("English:-", eng)
print("Hindi:-", dev)

print()

print("UTF-8 eng", eng.encode('utf-8'))
print("UTF-16 eng", eng.encode('utf-16'))
print("UTF-8 dev", dev.encode('utf-8'))
print("UTF-16 dev", dev.encode('utf-16'))
print("UTF-16 dev", dev.encode())


print("A B C D::::-", b'A B C D'.decode('utf-8'))
print("A B C D::::-", b'\xff\xfeA\x00 \x00B\x00 \x00C\x00 \x00D\x00'.decode('utf-16'))


print("अ आ इ ई utf-8::-", b'\xe0\xa4\x85 \xe0\xa4\x86 \xe0\xa4\x87 \xe0\xa4\x88'.decode('utf-8'))
print("अ आ इ ई utf-16::-", b'\xff\xfe\x05\t \x00\x06\t \x00\x07\t \x00\x08\t'.decode('utf-16'))

# to find the default encoding scheme
import sys
print()
print(sys.stdin.encoding)