import copy as copy
import random as random


# Consider using the modules imported above.
class Hat:
    def __init__(self, **kwarg):
        contents = []
        for key in kwarg.keys():
            for n in range(kwarg[key]):
                contents.append(key)
        self.contents = contents

    def draw(self, n):
        contents = self.contents
        if n >= len(contents):
            return contents

        res = []

        for n in range(n):
            len_contents = len(contents)
            index = random.randrange(len_contents)
            ball = contents[index]
            res.append(ball)
            contents = contents[0:index] + contents[index + 1:]

        # update contents
        self.contents = contents
        return res



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hits = 0
    for n in range(num_experiments):
        example = copy.copy(hat)
        sample = example.draw(num_balls_drawn)
        success = True
        for key in expected_balls.keys():
            if sample.count(key) < expected_balls[key]:
                success = False
                break
        if success:
            hits += 1

    return hits / num_experiments




hat = Hat(blue=3,red=2,green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue":2,"green":1},
    num_balls_drawn=4,
    num_experiments=1000)
print("Probability:", probability)

# https://replit.com/@nahuelcastro/boilerplate-probability-calculator#prob_calculator.py


