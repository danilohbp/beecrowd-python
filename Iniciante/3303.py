# -*- coding: utf-8 -*-

w = str(input())
w = w.lower()

if len(w) <= 20:
    if len(w) >= 10:
        print("palavrao")
    else:
        print("palavrinha")