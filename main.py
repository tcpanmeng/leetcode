def sumVal(n):
    return sum(range(1,n+1))
# li :数组，hh:行号
def nextList(li,hh):
    # 奇数
    if hh%2==1:
        l = [ li[x]+li[x+1] for x in range((hh)//2) ]
        return [1]+l+l[:len(l)-1][::-1]+[1]
    # 偶数
    else:
        l = [ li[x]+li[x+1] for x in range((hh+1)//2) ][:-1]
        return [1]+l+l[::-1]+[1]
        
if __name__ == "__main__":
    numRows = 8
    res = []
    for i in range(numRows):
        i = i+1
        if i==1:
            res.append([1])
        elif i==2:
            res.append([1,1])
        else:
            pre = res[-1]
            cur =nextList(res[-1],i)
            res.append(cur)
    print(res)

   
    # print("求和1..{0}是{1}".format(100,sumVal(100)))