from random import randint

tracker = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

for i in range(500):
    roll = randint(1,6) + randint(1,6)
    tracker[roll] = tracker[roll] + 1

for combination in tracker:
    print "%s rolled %s times out of 500" %(combination, tracker[combination])
    prob = float(tracker[combination])/500
    percent = prob*100
    print "This is a probability of %s, or %s percent!" %(prob, percent)
