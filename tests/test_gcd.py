from super_gcd import gcd


def test_gcd_of_2_and_3():
    result = gcd(2, 3)
    assert result == 1


def test_gcd_of_2_and_4():
    result = gcd(2, 4)
    assert result == 2


def test_gcd_of_3_and_6():
    result = gcd(3, 6)
    assert result == 3


def test_gcd_of_100_and_10000():
    result = gcd(100, 10000)
    assert result == 100


def test_gcd_of_250_and_300():
    result = gcd(250, 300)
    assert result == 50


def test_gcd_of_1500_and_500():
    result = gcd(1500, 500)
    assert result == 500
