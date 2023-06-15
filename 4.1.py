def strcounter1(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
        print(sym, counter)

def strcounter2(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
        print(sym, counter)



def strcounter3(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    for sym, count in syms_counter.items():
        print(sym, count)

strcounter3('abvackd')