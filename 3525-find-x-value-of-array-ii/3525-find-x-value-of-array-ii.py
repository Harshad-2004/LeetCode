from typing import List

class Node:
    __slots__ = ('prod', 'remain')
    def __init__(self, k: int):
        self.prod = 1
        self.remain = [0] * k

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]
        self._build(nums, 0, 0, self.n - 1)

    def _merge(self, left: Node, right: Node) -> Node:
        res = Node(self.k)
        res.prod = (left.prod * right.prod) % self.k
        for r in range(self.k):
            res.remain[r] = left.remain[r]
        for r in range(self.k):
            res.remain[(r * left.prod) % self.k] += right.remain[r]
        return res

    def _build(self, nums: List[int], idx: int, l: int, r: int):
        if l == r:
            val = nums[l] % self.k
            self.tree[idx].prod = val
            self.tree[idx].remain[val] = 1
            return
        mid = (l + r) // 2
        self._build(nums, 2 * idx + 1, l, mid)
        self._build(nums, 2 * idx + 2, mid + 1, r)
        self.tree[idx] = self._merge(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def update(self, idx: int, l: int, r: int, pos: int, val: int):
        if l == r:
            mod_val = val % self.k
            self.tree[idx].prod = mod_val
            self.tree[idx].remain = [0] * self.k
            self.tree[idx].remain[mod_val] = 1
            return
        mid = (l + r) // 2
        if pos <= mid:
            self.update(2 * idx + 1, l, mid, pos, val)
        else:
            self.update(2 * idx + 2, mid + 1, r, pos, val)
        self.tree[idx] = self._merge(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def query(self, idx: int, l: int, r: int, ql: int, qr: int) -> Node:
        if ql <= l and r <= qr:
            return self.tree[idx]
        mid = (l + r) // 2
        if qr <= mid:
            return self.query(2 * idx + 1, l, mid, ql, qr)
        if ql > mid:
            return self.query(2 * idx + 2, mid + 1, r, ql, qr)
        left_node = self.query(2 * idx + 1, l, mid, ql, qr)
        right_node = self.query(2 * idx + 2, mid + 1, r, ql, qr)
        return self._merge(left_node, right_node)


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = SegmentTree(nums, k)
        ans = []
        
        for idx, val, start, x in queries:
            tree.update(0, 0, n - 1, idx, val)
            res_node = tree.query(0, 0, n - 1, start, n - 1)
            ans.append(res_node.remain[x])
            
        return ans