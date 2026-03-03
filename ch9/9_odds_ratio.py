import math

def logistic(x, b0, b1):
    return 1.0 / (1.0 + math.exp(-(b0 + b1 * x)))

b0 = -7.0587 #A
b1 = 2.2047 #B

p_4 = logistic(4, b0, b1) #C
odds_4 = p_4 / (1 - p_4) #D

p_6 = logistic(6, b0, b1) #E
odds_6 = p_6 / (1 - p_6) #F

print("O(4): ", odds_4) #G
print("O(6): ", odds_6) #G
print("O(6) / O(4): ", odds_6 / odds_4) #G

#A intercept (log-odds when x = 0)
#B slope (change in log-odds per unit increase in x)
#C predicted probability at x = 4
#D odds at x = 4 is about ~5.813
#E predicted probability at x = 6
#F odds at x = 6 is about ~477.947
#G odds ratio O(6)/O(4) shows an increase factor 82.22