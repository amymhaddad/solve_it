from min_cost_climbing_stairs import min_cost_climb_stairs


def test_min_cost_climb_stairs():
    assert min_cost_climb_stairs([0, 0, 0, 0]) == 0
    assert min_cost_climb_stairs([10, 15, 20]) == 15
    assert min_cost_climb_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert min_cost_climb_stairs([1, 0, 0, 0]) == 0
