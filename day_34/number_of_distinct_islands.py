###################
# Geeks for Geeks #
###################
# https://practice.geeksforgeeks.org/problems/number-of-distinct-islands/1
###################




import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        self.pow = 397
        self.pow_i = 2003
        self.modulo = 100000000069
        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0])
        self.island_dict = {}
        self.island_map = {}
        self.island_count = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    hash = (row*self.pow + col) % self.modulo
                    if hash not in self.island_map:
                        # print("...........")
                        # print(row, col)
                        self.island_count += 1
                        self.island_map[hash] = self.island_count
                        self.island_dict[self.island_count] = [[row, col]]
                        
                        self.trace_all_connected_points([row, col])
                        
                        
        hash_set = set()
        for key in self.island_dict:
            first = self.island_dict[key][0].copy()
            for i in self.island_dict[key]:
                i[0] = i[0] - first[0]
                i[1] = i[1] - first[1]
        for key in self.island_dict:
            hash = 0
            for i in self.island_dict[key]:
                hash = ((hash + i[0]*self.pow + i[1]) * self.pow_i) % self.modulo
            if hash not in hash_set:
                hash_set.add(hash)

        # print(island_map)
        # print(hash_set)
        return len(hash_set)
    
    def trace_all_connected_points(self, point):
        connected_points = self.return_connected_points(point)
        for i in connected_points:
            hash = (i[0] * self.pow + i[1]) % self.modulo
            if hash not in self.island_map:
                self.island_map[hash] = self.island_count
                self.island_dict[self.island_count].append([i[0], i[1]])
                self.trace_all_connected_points([i[0], i[1]])
                        
                
                    
    def return_connected_points(self, point):
        i = point[0]
        j = point[1]
        connected_points = []
        # for col in range(j-1, j+2):
        #     if col >= 0 and col < self.m and i-1 >= 0 and i-1 < self.n:
        #         if self.grid[i-1][col] == 1:
        #             hash = ((i-1)*self.pow + col) % self.modulo
        #             if hash not in self.island_map:
        #                 connected_points.append([i-1, col])
                        # return [i-1, col]
        if i-1 >= 0 and i-1 < self.n:
            if self.grid[i-1][j] == 1:
                hash = ((i-1)*self.pow + j) % self.modulo
                if hash not in self.island_map:
                    connected_points.append([i-1, j])
        if j+1 >= 0 and j+1 < self.m:
            if self.grid[i][j+1] == 1:
                hash = (i*self.pow + (j+1)) % self.modulo
                if hash not in self.island_map:
                    connected_points.append([i, j+1])
                    # return [i, j+1]
        # for col in range(j-1, j+2):
        # for col in range(j+1, j-2, -1):
        #     if col >= 0 and col < self.m and i+1 >= 0 and i+1 < self.n:
        #         if self.grid[i+1][col] == 1:
        #             hash = ((i+1)*self.pow + col) % self.modulo
        #             if hash not in self.island_map:
        #                 connected_points.append([i+1, col])
                        # return [i+1, col]
        if i+1 >= 0 and i+1 < self.n:
            if self.grid[i+1][j] == 1:
                hash = ((i+1)*self.pow + j) % self.modulo
                if hash not in self.island_map:
                    connected_points.append([i+1, j])
        if j-1 >= 0 and j-1 < self.m:
            if self.grid[i][j-1] == 1:
                hash = (i*self.pow + (j-1)) % self.modulo
                if hash not in self.island_map:
                    connected_points.append([i, j-1])
                    # return [i, j-1]
        return connected_points
                    
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends