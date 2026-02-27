from numpy.random import exponential as expon

mu = .3  #A

time_elapsed = 0.0  #B
shots_pulled = 0  #C

while True:  #D
    time_elapsed_to_shot = expon(scale=1/mu, size=1)[0]  #E
    time_elapsed += time_elapsed_to_shot  #F
    if time_elapsed > 180:  #G
        break  #H
    shots_pulled += 1  #I
    print(f"{time_elapsed:.2f} minutes: {shots_pulled} shots pulled")  #J

print(f"Total shots pulled in 3 hours: {shots_pulled}")  #K

#A Set exponential rate parameter to 0.3
#B Initialize total time elapsed to 0.0
#C Initialize total shots pulled to 0
#D Start loop to simulate shots until time exceeds 3 hours
#E Generate time to next shot from exponential distribution
#F Add time to next shot to total time elapsed
#G Check if total time exceeds 180 minutes
#H Exit loop if time exceeds 180 minutes
#I Increment shots pulled counter
#J Print time elapsed and shots pulled for current shot
#K Print total shots pulled over 3 hours
