
"""
    reduce(): 用一个“两参数函数”，把 iterable 中的元素从左到右不断累计合并，最后得到一个值
    
    需要先导入functools包，所以：注意注意注意，reduce不是内置函数

    核心逻辑：
        先取两个值
        ↓
        用 function 处理
        ↓
        得到一个结果
        ↓
        再把这个结果和下一个元素继续处理
        ↓
        一直到只剩一个结果

"""

from functools import reduce
import re

result2 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(result2)  # 15，计算过程为：((((1 + 2) + 3) + 4) + 5)


"""大致等价于"""
nums = [1, 2, 3, 4, 5]

result3 = nums[0]

for num in nums[1: ]:
    result3 += num

print(result3)   # 15

# -------------------------------------------------------------

result4 = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(result4)  # 120，计算过程为：((((1 * 2) * 3) * 4) * 5)


# -------------------------------------------------------------

"""用 reduce()找最大值"""

nums2 = [1, 2, 3, 4, 5]

result5 = reduce(lambda x, y: x if x > y else y, nums2)
print(result5)  # 5