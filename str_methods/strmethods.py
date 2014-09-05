def find(srcString, sub, start=0, end=-1):
    if end == -1 or end >= len(srcString):
        end = len(srcString)
    if start >= end:
        return -1
    index = start
    while (index < end):
        if (srcString[index] == sub[0]):
            if (len(sub) == 1):
                return index
            else:
                i = index + 1
                j = 1
                found = True
                while (j < len(sub)):
                    if i >= len(srcString) or srcString[i] != sub[j]:
                        found = False
                        break
                    i = i + 1
                    j = j + 1
                if found:
                    return index
            return index;
        index = index + 1
    return -1

def testFind():
    sourceStr = "murugavel"
    print(find(sourceStr, 'm'))
    print(find(sourceStr, 'g'))
    print(find(sourceStr, 'l'))
    print(find(sourceStr, 'x'))
    print(find(sourceStr, 'mu'))
    print(find(sourceStr, 'ga'))
    print(find(sourceStr, 'el'))
    print(find(sourceStr, 'xx'))
    print(find(sourceStr, 'mu', 0))
    print(find(sourceStr, 'ga', 2, 6))
    print(find(sourceStr, 'elasdfasdf', 3, 8))
    print(find(sourceStr, 'xxx', 5, 500))

testFind()
