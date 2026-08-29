for x in [1, 1.5, 1+2j, True, "a", [1], (1,), {"k": 1}, {1}, None]:
    print(f"{x!r:>12} → {type(x).__name__}")
