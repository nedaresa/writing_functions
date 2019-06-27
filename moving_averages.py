from typing import List, Dict

J = [4, 4, 4, 9, 10, 11, 12]
p = 3


def gen_seq(j_list: List[int], p: int) -> Dict[str, float]:
    """Generates a sequence of tuples from a list & returns the min-max means
    """
    sequences = []
    for ind, _ in enumerate(j_list):
        end_range = ind + p
        sequence = j_list[ind:end_range]
        if len(sequence) == p:
            sequences.append(sequence)
    avgs = [sum(sequence) / len(sequence) for sequence in sequences]

    output = {}
    output["min"] = min(avgs)
    output["max"] = max(avgs)
    return output
def test_calc_min_max():
    """
    we are testing th eoutput of the test_calc_min_max() function
    """
    assert gen_seq(j_list=[1,2,3,4,5,6], p=3) == {"min": 1.5, "max": 5.5}
print(gen_seq(j_list=J, p=p))
