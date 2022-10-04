def dailyTemperatures(self, temperatures):
    length = len(temperatures)
    result = [0] * length
    stack = []
    
    for day, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            previous = stack.pop()
            result[previous] = day - previous
        stack.append(day)
    
    return result