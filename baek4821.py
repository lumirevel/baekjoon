while True:
    maxPage = int(input())
    if maxPage != 0:
        pageRangeList = []
        for pageRange in input().split(","):
            start = 0
            end = 0
            first = True
            for char in pageRange:
                if first:
                    if char == "-":
                        first = False
                    else:
                        start *= 10
                        start += int(char)
                else:
                    end *= 10
                    end += int(char)
            if first:
                pageRangeList.append((start, start))
            elif start <= end and start <= maxPage:
                pageRangeList.append((start, min(end, maxPage)))
        pageRangeList.sort(key=lambda x:x[0])
        realPageList = []
        for pageRange in pageRangeList:
            if len(realPageList) > 0:
                beforeRange = realPageList.pop()
                if pageRange[0] <= beforeRange[1]:
                    realPageList.append((beforeRange[0], max(beforeRange[1], pageRange[1])))
                else:
                    realPageList.append(beforeRange)
                    realPageList.append(pageRange)
            else:
                realPageList.append(pageRange)
        totalPage = 0
        for start, end in realPageList:
            totalPage += end-start+1
        print(totalPage)
    else:
        break
