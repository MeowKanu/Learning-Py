#Simple Interest Calculator 
# This program calculates simple interest based on user input for principal, rate of interest, and time in years.
P= input('Principal:  ')
P   = int(P)
R= input('Rate of Interest: ') 
R = int(R)
T = input('Time in years: ')    
T = int(T)
    # Calculate simple interest
si = (P * R * T) / 100
print(f"The Simple Interest is:", si)
