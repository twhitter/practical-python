# bounce.py
#
# Exercise 1.5

height = 100 # meters
bounce_degradation = 3.0 / 5.0 # percentage bounce height decreases each time
num_of_bounces = 0


while num_of_bounces < 10:
    height = (height * bounce_degradation)
    num_of_bounces += 1
    if num_of_bounces == 1:
        print(num_of_bounces, "bounce,", round(height,4), 'meters')
    else:
        print(num_of_bounces, "bounces,", round(height,4), 'meters')


