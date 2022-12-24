import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **keywords) -> None:
        self.contents = [ball for sublist in [[key for i in range(value) ] for key, value in keywords.items()] for ball in sublist]

    def draw(self, n):
        sample = self.contents.copy() if n > len(self.contents) else random.sample(self.contents, n)
        for ball in sample:
            self.contents.remove(ball)
        return sample

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for i in range(num_experiments):
        drawn_list = hat.draw(num_balls_drawn)
        matches = []
        for key, value in expected_balls.items():
            matches.append(True if drawn_list.count(key) >= value else False)
        if all(matches):
            successes += 1
        hat.contents.extend(drawn_list)
    return successes / num_experiments
