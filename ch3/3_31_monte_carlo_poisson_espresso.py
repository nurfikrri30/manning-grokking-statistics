from numpy.random import poisson

mu = .3  #A

shots_pulled = 1  #B

for i in range(3*60):  #C
    new_shots_pulled = poisson(lam=mu, size=1)[0]  #D
    print(f"MINUTE {i}: {new_shots_pulled} shots pulled")  #E
    shots_pulled += new_shots_pulled  #F

print(f"Total shots pulled in 3 hours: {shots_pulled}")  #G

#A Set Poisson rate parameter to 0.3
#B Initialize total shots pulled to 0
#C Loop over each minute in 3 hours (180 minutes)
#D Generate number of shots pulled in current minute from Poisson distribution
#E Print number of shots pulled for current minute
#F Add new shots to total shots pulled
#G Print total shots pulled over 3 hours
