import random


def flip_coin(num_trials: int = 10000, num_flips: int = 10) -> dict:
    heads_count = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        flips = [random.choice(["heads", "tails"]) for _ in range(num_flips)]
        num_heads = flips.count("heads")
        heads_count[num_heads] += 1

    for heads in heads_count:
        heads_count[heads] = round((heads_count[heads] / num_trials) * 100, 2)

    return heads_count
