import random
from random import shuffle
from random import randint

num_citizens = 100

simulations = 10000

total_untouched = 0

totals = [0] * num_citizens

for i in range(simulations):
	citizens = [[1, True] for i in range(num_citizens)]
	left_untouched = num_citizens
	for thief in citizens:
		victim = citizens[randint(0, num_citizens - 1)]
		thief[0] += victim[0]
		victim[0] = 0
		if (victim[1]):
			left_untouched -= 1
			victim[1] = False
	for i in range(num_citizens - 1):
		totals[i] += citizens[i][0]
	total_untouched += left_untouched
maxval = 0
maxloc = 0
for cit in totals:
	if cit > maxval:
		maxval = cit
		maxloc = totals.index(cit)
	print(totals.index(cit), cit)
print("")
print(total_untouched);
print(maxloc, maxval);
