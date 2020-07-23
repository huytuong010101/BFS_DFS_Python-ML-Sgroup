class Graph:
    def __init__(self, numOfPoint, data):
        self.matrix = [[False for i in range(numOfPoint)] for j in range(numOfPoint)]
        self.numOfPoint = numOfPoint
        for i, j in data:
            self.matrix[i - 1][j - 1] = True
            self.matrix[j - 1][i - 1] = True

    def BFS(self, start, end):
        """
        Find the shortest way from start to end via BFS
        :param start: start point
        :param end: end point
        :return: a list of point from start to end
        """
        # init data
        if start > self.numOfPoint or end > self.numOfPoint:
            raise ValueError("Value is out of range")
        start -= 1
        end -= 1
        queue = []
        path = [-1 for i in range(self.numOfPoint)]
        flag = [False for i in range(self.numOfPoint)]
        queue.append(start)
        flag[start] = True
        while len(queue) != 0:
            current = queue[0]
            del queue[0]
            for index in range(self.numOfPoint):
                if self.matrix[current][index] and current != index and not flag[index]:
                    path[index] = current
                    if index == end:
                        # finish, this is shortest way
                        numOfStep = 0
                        way = []
                        while start != end:
                            way.append(end + 1)
                            end = path[end]
                            numOfStep += 1
                        way.append(start + 1)
                        way.reverse()
                        return way
                    else:
                        # go to next point
                        queue.append(index)
                        flag[index] = True
        else:
            return []

    def DFS(self, start, end):
        """
        Find the shortest way from start to end via DFS
        :param start: start point
        :param end: end point
        :return: a list of point from start to end
        """
        if start > self.numOfPoint or end > self.numOfPoint:
            raise ValueError("Value is out of range")
        way = []
        flag = [False for i in range(self.numOfPoint)]
        ans = []
        flag[start - 1] = True
        self.__DFS(start - 1, end - 1, way, flag, ans)
        if len(ans) != 0:
            ans.insert(0, start)
        return ans

    def __DFS(self, start, end, way, flag, ans):
        if start == end and (len(way) <= len(ans) or len(ans) == 0):
            ans.clear()
            ans += way
        for index in range(self.numOfPoint):
            if index != start and self.matrix[start][index] and not flag[index]:
                way2 = way.copy()
                flag2 = flag.copy()
                way2.append(index + 1)
                flag2[index] = True
                self.__DFS(index, end, way2, flag2, ans)

    def __str__(self):
        s = ""
        s += "Graph has {} point".format(self.numOfPoint) + "\n"
        for row in self.matrix:
            s += str(row) + "\n"
        return s


'''This is example'''
if __name__ == "__main__":
    '''
    find minimum step
    (1)  --  (2) -- (3)
     |     /  |
    (4) _/   (5) -- (6)
    
    '''
    graph = Graph(6, [[1, 2], [2, 3], [1, 4], [2, 4], [5, 6], [2, 5]])
    print(graph)
    print("Shortest way from 1 -> 6 by BFS")
    print(graph.BFS(1, 6))
    print("Shortest way from 1 -> 6 by DFS")
    print(graph.DFS(1, 7))
