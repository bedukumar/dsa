result = []
t = []


def sub(i, l):
    if i == len(l):
        result.append(t[:])
        return
    sub(i+1, l)
    t.append(l[i])
    sub(i+1, l)
    t.pop()


l = [1, 2, 3]
sub(0, l)
print(result)


# l = []
# x = [1, 2, 3, 4]

# l.append(x)
# print(l)
