from photoStat import *

# test values 
phrase1 = "The mean entry level salary of an employee at a company is $58,000. You believe it is higher for IT professionals in the company. State the null and alternative hypotheses."
phrase2 = "You are testing that the mean speed of your cable Internet connection is more than three Megabits per second. State the null and alternative hypotheses."
phrase3 = "A sociologist claims the probability that a person picked at random in Times Square in New York City is visiting the area is 0.83. You want to test to see if the claim is correct. State the null and alternative hypotheses."

def test_find_test_val(): 
    result = find_test_val(phrase1)
    assert result == "58,000"
    
    result = find_test_val(phrase2)
    assert result == "3"

    result = find_test_val(phrase3)
    assert result == "0.83"

def test_find_test_type(): 
    result = find_test_type(phrase1)
    assert result == "mean"

    result = find_test_type(phrase2)
    assert result == "mean"

    result = find_test_type(phrase3)
    assert result == "p"

def test_find_tailed():
    result = find_tailed(phrase1)
    assert result == ">"

    result = find_tailed(phrase2)
    assert result == ">"

    result = find_tailed(phrase3)
    assert result == "!="

def test_find_hypothesis(): 
    result = find_hypothesis(phrase1)
    # print(result)
    assert result == "H0: mean = 58,000\nH1: mean > 58,000"
    
    result = find_hypothesis(phrase2)
    # print(result)
    assert result == "H0: mean = 3\nH1: mean > 3"
    
    result = find_hypothesis(phrase3)
    # print(result)
    assert result == "H0: p = 0.83\nH1: p != 0.83"



def test_find_z_score():
    result = find_z_score(1, 1, 1)
    assert result == 0

    result = find_z_score(0, 0, 0)
    assert result == 0

    result = find_z_score(0.90, 0.83, 0.15)
    assert round(result, 4) == 0.4667

    result = find_z_score(-2, 3, 2)
    assert round(result, 4) == -2.5

def test_find_p_val():
    result = find_p_val(0, False)
    assert result == 0.5

    result = find_p_val(0, True)
    assert result == 1

    result = round(find_p_val(0.4667, False), 4)
    assert result == 0.3204

    result = round(find_p_val(-2.5, True), 4)
    assert result == 0.0124

def test_find_conclusion():
    result = find_conclusion(0.5, 0.05)
    assert result == "p-value of 0.5 is greater than alpha = 0.05\nFail to reject H0\n"

    result = find_conclusion(0.3204, 0.10)
    assert result == "p-value of 0.3204 is greater than alpha = 0.1\nFail to reject H0\n"

    result = find_conclusion(0.0124, 0.05)
    assert result == "p-value of 0.0124 is less than alpha = 0.05\nReject H0\n"


# test_find_test_val()
# test_find_test_type()
# test_find_tailed()
# test_find_hypothesis()

# test_find_z_score()
# test_find_p_val()
# test_find_conclusion()