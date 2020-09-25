def countstring(items):
    count = 0
    for i in items:
        if len(i)>1 and i[0] == i[-1]:
            count += 1
    return count

print(countstring(['abc', 'xyz', 'aba', '1221','1111']))