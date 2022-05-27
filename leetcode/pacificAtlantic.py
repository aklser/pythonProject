from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    l = len(heights)
    if l == 0:
        return heights
    res = []
    res.extend([[0, l - 1], [l - 1, 0]])

    return res


print(pacificAtlantic([[2, 1],
                       [1, 2]]))

