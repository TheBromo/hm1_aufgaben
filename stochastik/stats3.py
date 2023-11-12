# Given probabilities and outcomes for the biased die
outcomes = [1, 2, 3, 4, 5, 6]
probabilities = [1/16, 1/16, 9/32, 3/32, 9/32, 7/32]

# Calculate the expected value of a single roll
expected_value_roll = sum(p * x for p, x in zip(probabilities, outcomes))

# Cost per roll
cost_per_roll = 5

# Net expected value per roll
net_expected_value_per_roll = expected_value_roll - cost_per_roll

# Expected gain or loss for 46 rolls
expected_gain_loss_46_rolls = net_expected_value_per_roll * 46

expected_value_roll, net_expected_value_per_roll, expected_gain_loss_46_rolls
