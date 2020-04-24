from top_scores import sort_scores


def test_no_scores():
    assert sort_scores([], 100) == []
   
def test_one_score():
    assert sort_scores([55], 100) == [55]

def test_two_scores():
    assert sort_scores([30, 60], 100) == [60, 30]
    

# def test_many_scores():
#     assert sort_scores([37, 89, 41, 65, 91, 53], 100) == [91, 89, 65, 53, 41, 37]
     

def test_repeated_scores():
    assert sort_scores([20, 10, 30, 30, 10, 20], 100) == [30, 30, 20, 20, 10, 10]
