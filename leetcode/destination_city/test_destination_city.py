from destination_city import dest_city


def test_dest_city():
    assert (
        dest_city([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
        == "Sao Paulo"
    )
    assert dest_city([["B", "C"], ["D", "B"], ["C", "A"]]) == "A"
    assert dest_city([["A", "Z"]]) == "Z"
