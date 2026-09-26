"""
递归的通用模板：
        def recursive_function(problem):

            if 最小问题:
                return 最简单答案

            return 当前处理 + recursive_function(更小的问题)


        
            
递归的主要场景：

    目录遍历：文件夹里还有子文件夹，比如扫描一整个项目里的 .inp、.k、.key 文件。
    树结构：比如 AST 语法树、XML/HTML DOM、组织树、装配树。
    图搜索：DFS 深度优先搜索，不过工程里很多时候也会改成显式栈实现。
    嵌套数据解析：例如 JSON 里字典套列表、列表又套字典。
    分治算法：归并排序、快速排序、二分结构等。
    某些数学/算法问题：但生产代码里经常会为了性能和稳定性改成循环或动态规划。

"""


def test(n):

    print("进入：", n)

    if n == 1:
        print("到达终点")
        return

    test(n - 1)

    print("返回：", n)

test(4)


# -------------------------------------------------------------


"""
阶乘的递归代码：
"""

def mutiply_mutiply(n: int) -> int:

    if n == 1:
        return 1

    return n * mutiply_mutiply(n - 1)


print(mutiply_mutiply(5))