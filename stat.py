import scipy.stats as ss
import numpy as np
import re
from word2number import w2n

#public variables 
x = 0
true_val = 0
sigma = 0
n = 0
alpha = 0 
two_tailed = False

# test values 
phrase1 = "The mean entry level salary of an employee at a company is $58,000. You believe it is higher for IT professionals in the company. State the null and alternative hypotheses."
phrase2 = "You are testing that the mean speed of your cable Internet connection is more than three Megabits per second. State the null and alternative hypotheses."
phrase3 = "A sociologist claims the probability that a person picked at random in Times Square in New York City is visiting the area is 0.83. You want to test to see if the claim is correct. State the null and alternative hypotheses."

def z_test(p, x, sigma, n, alpha, two_tailed): 
    stdErr = sigma/np.sqrt(n)
    z = (x-p)/stdErr
    
    p = ss.norm.sf(abs(z))

    if (two_tailed == True):
        p *= 2
    
    if (p < alpha): 
        return "p-value of " + str(p) + " is smaller than alpha = " + str(alpha) + "\nReject H0\n"
    else: 
        return "p-value of " + str(p) + " is greater than alpha = " + str(alpha) + "\nFail to reject H0\n"

# print(z_test(8.5, 9.26, 1.20, 41, 0.05, True))
# values are a bit off from online sources, but have the same conclusions 

def find_hypothesis(problem): 
    # determine whether it's a z-test or t-test
    test_type = find_test_type(problem)
    tailed = find_tailed(problem) 
    test_val = find_test_val(problem)

    if test_type == "unknown" or tailed == "unknown": 
        return "Error: unknown test type or tailed"

    return "H0: " + test_type + " = " + str(test_val) + "\nH1: " + test_type + " " + tailed + " " + str(test_val)
    
def find_test_val(problem):
    test_val = 0
    # val_equal = True

    nums = re.findall('\d+[,\.]?\d*', problem)
    # print(nums)
    if len(nums) == 1: 
        return nums[0]
    elif len(nums) > 1: 
        nonYears = set()
        for i in range(len(nums)):
            if re.search('[12]\d\d\d', nums[i]) == None: 
                nonYears.append(nums[i])
        if (len(nonYears) == 0):
            return nums[0] # multiple values that start with 1xxx or 2xxx (potentially years). just use the first value. TODO: handle this better
        elif len(nonYears) == 1: 
            return nonYears[0]
        else: # more than 1 non years 
            return nonYears[0] # multiple values that do not appear to be non-years. just use the first value. TODO: handle this better
    else: 
        word_num = w2n.word_to_num(problem)
        return str(word_num)
            


def find_test_type(problem): 
    # determine whether it's a z-test or t-test
    test_type = "unknown"
    if "probability" in problem: 
        test_type = "p"
    elif "mean" in problem: 
        test_type = "mean"
    return test_type

def find_tailed(problem):
    tailed = "unknown"
    if "greater" in problem or "higher" in problem or "bigger" in problem or "more than" in problem: 
        tailed = ">"
    elif "lesser" in problem or "lower" in problem or "smaller" in problem or "less than" in problem: 
        tailed = "<"
    elif "not equal to" in problem or "correct" in problem: 
        tailed = "!="
    return tailed




# def main():
#     phrase = ""
#     find_hypothesis(phrase)


def test_find_hypothesis(): 
    result = find_hypothesis(phrase1)
    print(result)
    assert result == "H0: mean = 58000\nH1: mean > 58000"
    
    result = find_hypothesis(phrase2)
    print(result)
    assert result == "H0: mean = 3 Megabits per second\nH1: mean > 3 Megabits per second"
    
    result = find_hypothesis(phrase3)
    print(result)
    assert result == "H0: mean == 0.83\nH1: mean != 0.83"

# test_find_hypothesis()

def test_find_test_val(): 
    result = find_test_val(phrase1)
    assert result == "58,000"
    
    result = find_test_val(phrase2)
    assert result == "3"

    result = find_test_val(phrase3)
    assert result == "0.83"

test_find_test_val()