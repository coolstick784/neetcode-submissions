class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # We're only looking for > what hasn't been found
        # If it's less than the previous, nothing ever changes -- we just add 1
        # Res = [0 for _ in range(len(temperature))]
        # Done ctr = 0, in between = 0
        # [30], len_stack = 1
        # 38 is greater, so res[done_ctr + len_stack - 1] = res[0] =  in between = 0
        # 30 is less than, so just add 30 to the stack [38, 30] and 1 to in between
        # 36 is greater than 30, so add 1 to the in between counter and 1 to res
        # [38], in between = 1, res

        stack = []
        in_between = []
        res = [0 for _ in range(len(temperatures))]
        num_completed = 0
        len_stack = 0
        sum_all_buffers = 0
        gt = False
        for t in temperatures:
            if stack == []:
                stack.append(t)
                in_between.append(0)
                len_stack += 1
            else:
                if t <= stack[-1]:
                    in_between[-1] += 1
                    gt = False
                
                cur_sum_buffers = 0
                if t > stack[-1]:
                    gt = True
                while stack and t > stack[-1]:
                    print("between", in_between)
                    print("stack", stack)
                    print("t", t)
                    print("res idx", num_completed+len_stack-in_between[-1]-1)
                    print("res val", in_between[-1] + 1)
                    print("\n\n")
                    

                    if len_stack >= 2:
                        in_between[-2] += in_between[-1]
                    res[num_completed+len_stack-in_between[-1]-1] = in_between[-1] + 1
                    stack.pop()
                    in_between.pop()
                    num_completed += 1
                    len_stack -= 1
                if gt:
                    try:
                        in_between[-1] += 1
                    except:
                        pass
                in_between.append(0)
                stack.append(t)
                len_stack += 1
                    
                    




        return res
