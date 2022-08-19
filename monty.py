N = 10
result = [None]*N
for i in range(N):
    alice_door = random.choice(doors)
    prize_door = random.choice(doors)
    monty_door = monty_door_random(doors, alice_door, prize_door)
		

    while monty_door == prize_door:
    alice_door = random.choice(doors)
    prize_door = random.choice(doors)
    monty_door = monty_door_random(doors, alice_door, prize_door)
    remaining_doors = set(doors) - {alice_door} - {monty_door}
    result[i] = random.choice(list(remaining_doors)) == prize_door

print "Probability of getting prize when Monty chooses the door randomly?\n %f" % (float(sum(result))/N)

