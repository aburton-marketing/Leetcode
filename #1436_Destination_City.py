# Leetcode problem #1436 Destination City. 
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. 
# Return the destination city, that is, the city without any path outgoing to another city.
# Destination is never i in [i, j] pairs. Get all ends of paths[0][j]

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Dicionary to store routes
        dest = {}

        for i in range(len(paths)):
          # Sets both city A and city B to true
            if paths[i][0] not in dest:
                dest[paths[i][0]] = True
            if paths[i][1] not in dest:
                dest[paths[i][1]] = True
            # if a city is ever in the "coming from" position which is paths[i][0] set it to False. 
            if paths[i][0] in dest:
                dest[paths[i][0]] = False
        print(dest)
        
        # Find the route that still returns True after our above for loop. 
        for x,y in dest.items():
            if y == True:
                return x
        
