import math

def logistic(x, b0, b1):
    return 1.0 / (1.0 + math.exp(-(b0 + b1*x)))

b0 = -7.0587 #A
b1 = 2.2047 #B
x = 6 #C

p = logistic(x, b0, b1) #D
print(f"P({x}):", p) #D

odds = p / (1 - p) #E
print(f"O({x}):", odds) #E

log_odds = math.log(odds) #F
print(f"log(O({x})):", log_odds) #F

linear_fx_log_odds = b0 + b1*x #G
print(f"Linear Function Log-Odds:", linear_fx_log_odds) #G

#A intercept parameter
#B slope / coefficient for x
#C input value (in this example = 4)
#D predicted probability, P(4): 0.8532221840498468
#E odds, O(4): 5.813018667205182
#F natural log of the odds, log(O(4)): 1.7600999999999996
#G linear prediction (equals log-odds), 1.7600999999999996