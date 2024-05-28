class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # this will be a n squared solution worse case
        temps_days_stack = []
        # [[70, 7], [76, 6], [72, 5], [69, 4]]
        # temp = 76
        steps = []
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            #print(temps_days_stack, i, temp)
            # if we need to look at values after, go backwards
            while temps_days_stack:
                prev_temp = temps_days_stack[-1][0] # 0 for temp # 73
                prev_index = temps_days_stack[-1][1] # 1 for index # 7
                if prev_temp <= temp:
                    temps_days_stack.pop()
                else:
                    steps.append(prev_index - i)
                    break
            if not temps_days_stack:
                steps.append(0)                    
            temps_days_stack.append([temp, i]) # always
        return reversed(steps)

