#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"a", "e", "f", "i"}
    b = {"a", "b", "k", "n"}
    c = {"e", "f", "n", "o", "w", "x"}
    d = {"a", "d", "e", "o", "p", "t", "u"}

    # а является подмножеством множества b и это все пересекается с d
    x = (a.union(b)).intersection(d)
    print(f"x = {x}")

    # Найдем дополнения множеств
    an = u.difference(a)
    ab = u.difference(b)

    y = (an.intersection(ab)).difference(c.union(d))
    print(f"y = {y}")