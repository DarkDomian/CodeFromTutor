class Solution:
    def maximumImportamce(n: int, roads: list[list[int]]) -> int:
        answer = 0
        cities = {}
        for road in roads:
            for i in road:
                if i not in cities:
                    cities[i] = 1
                else:
                    cities[i] += 1

        for val in cities.values():
            pass
        
        print(cities)

        return answer
        

    def assigningBiggestValue(road):
        pass



print(Solution.maximumImportamce(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))