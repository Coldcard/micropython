try:
    import hashlib
except ImportError:
    # MicroPython with hashlib module disabled.
    print("SKIP")
    raise SystemExit


h = hashlib.sha256()
print(h.digest())

h = hashlib.sha256()
h.update(b"123")
print(h.digest())

h = hashlib.sha256()
h.update(b"abcd" * 1000)
print(h.digest())

print(hashlib.sha256(b"\xff" * 64).digest())

# 56 bytes is a boundary case in the algorithm
print(hashlib.sha256(b"\xff" * 56).digest())

h = hashlib.sha256(b'123')
print(h.digest())
print(h.digest())

h = hashlib.sha256(b'123')
print(h.digest())
h.update(b'456')
print(h.digest())
