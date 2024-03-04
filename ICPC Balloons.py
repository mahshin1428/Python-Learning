for s in [*open(0)][2::2]:
    print(len(s) + len({*s}) - 2)
