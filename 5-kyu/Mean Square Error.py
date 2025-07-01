# kata: https://www.codewars.com/kata/51edd51599a189fe7f000015
def solution(array_a, array_b):
    return sum(map(lambda nums: (nums[0] - nums[1])**2 , zip(array_a, array_b))) / len(array_a)