try:
    import hashlib
except ImportError:
    print("SKIP")
    raise SystemExit


for algo_name in ("md5", "sha1", "sha256"):
    algo = getattr(hashlib, algo_name, None)
    if not algo:
        continue

    h = algo(b"123")
    h.digest()

    # Partial digests are not supported.
    h = algo(b"123")
    h.digest()
    try:
        h.update(b"456")
        print("fail")
    except ValueError:
        # Expected path, don't print anything so test output is the
        # same even if the algorithm is not implemented on the port.
        pass

print("done")
