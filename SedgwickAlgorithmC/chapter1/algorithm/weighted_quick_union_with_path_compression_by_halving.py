# 半短縮法付き加重高速合併アルゴリズム
class Weighted_Quick_Union_With_Path_Compression_By_Halving:
    def __init__(self, N):
        self.N = N
        self.connected_componet = [i for i in range(N)]
        self.node_num = [1] * N

    def find(self, a):
        if a == self.connected_componet[a]:
            return a
        self.connected_componet[a] = self.connected_componet[self.connected_componet[a]]
        return self.find(self.connected_componet[a])
    
    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if (a_root != b_root):
            if (self.node_num[a_root] <= self.node_num[b_root]):
                self.connected_componet[a_root] = b_root
                self.node_num[b_root] += self.node_num[a_root]
            else:
                self.connected_componet[b_root] = a_root
                self.node_num[a_root] += self.node_num[b_root]