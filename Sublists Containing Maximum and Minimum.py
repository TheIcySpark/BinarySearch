class Solution:
    def solve(self, nums):
        if len(nums) == 0:
            return 0
        min_value = min(nums)
        max_value = max(nums)
        return_max = 0
        if min_value == max_value:
            return sum(range(len(nums) + 1))
        return_max = max(calculate_number_sublists(min_value, max_value, nums), return_max)

        min_index = nums.index(min_value)
        new_min_value = min(nums[0:min_index] + nums[min_index + 1:len(nums)])
        if new_min_value != min_value:
            if new_min_value == max_value:
                return_max = max(sum(range(len(nums))), return_max)
            else:
                return_max = max(calculate_number_sublists(new_min_value, max_value, nums[0:min_index] + nums[min_index + 1:len(nums)]), return_max)

        max_index = nums.index(max_value)
        new_max_value = max(nums[0:max_index] + nums[max_index + 1:len(nums)])
        if new_max_value != max_value:
            if new_max_value == min_value:
                return_max = max(sum(range(len(nums))), return_max)
            else:
                return_max = max(calculate_number_sublists(min_value, new_max_value, nums[0:max_index] + nums[max_index + 1:len(nums)]), return_max)
                
        return return_max
        

def calculate_number_sublists(min_value, max_value, nums):
    start, end, last_start = 0, 0, 0
    first_found = ''
    i = 0
    s = 0
    while i < len(nums):
        if nums[i] == min_value:
            if first_found == '':
                start = i
                first_found = 'MIN'
            elif first_found == 'MIN':
                start = i
            elif first_found == 'MAX':
                end = i
                s += (start - last_start + 1) * (len(nums) - end)
                last_start = start + 1
                last_end = end
                first_found = 'MIN'
                start = end
        elif nums[i] == max_value:
            if first_found == '':
                start = i
                first_found = 'MAX'
            elif first_found == 'MAX':
                start = i
            elif first_found == 'MIN':
                end = i
                s += (start - last_start + 1) * (len(nums) - end)
                last_start = start + 1
                last_end = end
                first_found = 'MAX'
                start = end
        i += 1
    return s
