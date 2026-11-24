class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #we initilize an ans 
        #we are going to add the first temperature to a stack alongside its index (tuple : (temperature, index)),
        #we then go through the temperatures list,
            #while currtemp > the element on top of stack:
                #ans[index of stack.top element] = currtemp index - index of stack.top element
            # add currtemp and its index to stack

        # i = 6
        #stack = [(40, 5)]
        #res = [1, 4, 1, 2, 1]
        if len(temperatures) < 2:
            return [0]

        res = [0]*len(temperatures)
        stack = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            
            stack.append((temperatures[i], i))
        
        return res





            


                
        