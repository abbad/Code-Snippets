__author__ = 'Abbad'
"""

 This is related to master mind game. This is taken from Cracking the coding interview questions.
 Write a method that, given a guess and a solution, return the number of hits and pseudo-hits.

 example of output = "RGBY", "GBBY", "YYGG"

 Chapter 17 --> moderate.
 ex: 17.5
"""


class Result(object):

    def __init__(self):
        self.hits = 0
        self.pseudo_hits = 0

    def get_result(self):
        return "Hits:" + str(self.hits) + " Pseudo Hits:" + str(self.pseudo_hits)


def estimate(guess, solution):
    """
    :param guess: a string of the following combination RGBY
    :param solution: a string of the following combination RGBY
    :return: Result object
    """
    result = Result()
    frequencies = {
        'R': 0,
        'B': 0,
        'G': 0,
        'Y': 0
    }

    # loop over the solution and save the hits.
    for idx, x in enumerate(solution):

        if x == guess[idx]:
            result.hits += 1
        else:
            frequencies[x] += 1

    for idx, x in enumerate(guess):
        if frequencies[x] > 0 and x != solution[idx]:
            result.pseudo_hits += 1
            frequencies[x] -= 1
    return result

if __name__ == "__main__":
    #result = estimate("RGBY", "GGBY")
    print estimate("RGYY", "YYYY").get_result() # h: 2 p:0
    print estimate("YYYY", "BBBB").get_result()
    print estimate("BBGR", "BBGB").get_result()
