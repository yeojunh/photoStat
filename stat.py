import scipy.stats as ss
import numpy as np

#public variables 
x = 0
true_val = 0
sigma = 0
n = 0
alpha = 0 
two_tailed = False


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
    extract_nums = [int(s) for s in problem.split() if s.isdigit()]
    # if len(extract_nums) > 1: 
    #     test_val = extract_nums[0]
    #     for i in range(0, len(extract_nums)): 
    #         if (test_val == extract_nums[i]):
    #             val_equal = True
    # if (val_equal): 
    # todo: this is hard coded to return the first number in the list. if there are multiple numerical values in the phrase (e.g. year), this will return the first one.
    if (len(extract_nums) > 0):
        test_val = extract_nums[0]
    else:
        test_val = 0
    return test_val

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
    phrase = "The mean entry level salary of an employee at a company is $58,000. You believe it is higher for IT professionals in the company. State the null and alternative hypotheses."
    result = find_hypothesis(phrase)
    print(result)
    assert result == "H0: mean = 58000\nH1: mean > 58000"
    
    phrase = "You are testing that the mean speed of your cable Internet connection is more than three Megabits per second. State the null and alternative hypotheses."
    result = find_hypothesis(phrase)
    print(result)
    assert result == "H0: mean = 3 Megabits per second\nH1: mean > 3 Megabits per second"
    
    phrase = "A sociologist claims the probability that a person picked at random in Times Square in New York City is visiting the area is 0.83. You want to test to see if the claim is correct. State the null and alternative hypotheses."
    result = find_hypothesis(phrase)
    print(result)
    assert result == "H0: mean == 0.83\nH1: mean != 0.83"

test_find_hypothesis()