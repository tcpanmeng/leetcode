class Solution:


# 思路
# 题目意思挺费解的，但是评论区解释得挺清楚了
# 循环含义
# 每次外循环含义为给定上一个人报的数，求下一个人报的数
# 每次内循环为遍历上一个人报的数
# 具体思路
# 先设置上一人为'1'
# 开始外循环
# 每次外循环先置下一人为空字符串，置待处理的字符num为上一人的第一位，置记录出现的次数为1
# 开始内循环，遍历上一人的数，如果数是和num一致，则count增加。
# 若不一致，则将count和num一同添加到next_person报的数中，同时更新num和count
# 别忘了更新next_person的最后两个数为上一个人最后一个字符以及其出现次数！

    def countAndSay(self, n: int) -> str:
        prev_person = '1'
        for i in range(1,n):
            next_person, num, count = '', prev_person[0], 1
            for j in range(1,len(prev_person)):
                if prev_person[j] == num:count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person

# 递归实现
    def countAndSay2(self, n: int) -> str:
        if n <= 1:
            return '1'
        pre = self.countAndSay2(n - 1)

        res = ''
        count = 1
        for idx in range(len(pre)):

            if idx == 0 :
                count = 1

            elif pre[idx] != pre[idx -1]:
                tmp = str(count) + pre[idx-1]
                res += tmp
                count = 1
            elif pre[idx] == pre[idx-1]:
                count +=1

            if idx == len(pre) - 1:
                tmp = str(count) + pre[idx]
                res += tmp
        return res

#
def countAndSay3(self, n: int) -> str:
        if n == 1: return "1"
        if n == 2: return "11"
        res = [1, 1]
        for i in range(3, n+1):
            # print(res)
            new_res = []
            num = 1
            cur = res[0]
            # res = [2, 1]
            for s in res[1:]:
                if s == cur:
                    num += 1
                else:
                    new_res.append(num)
                    new_res.append(cur)
                    num = 1
                    cur = s 
            new_res.append(num)
            new_res.append(cur)
            res = new_res
        return ''.join(list(map(str, res)))

