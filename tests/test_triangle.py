from mygeopy.triangle import hypot

def test_hypot(a:float, b:float, expected:float):
    """Test the hypot function with given legs a and b."""
    result = hypot(a, b)
    assert result == expected, f"Expected {expected}, got {result}"

def test_hypot_cases():
    test_hypot(5, 12, 13)
    test_hypot(8, 15, 17)
    test_hypot(7, 24, 25)
    # Test with negative numbers
    try:
        hypot(-3, -4)
    except ValueError:
        pass
    else:
        assert False, "Negative numbers test failed"

    # Test with non-numeric inputs
    try:
        hypot('a', 4)
    except ValueError:
        pass
    else:
        assert False, "Non-numeric input test failed"

    # Test with zero
    test_hypot(0, 4, 4)
    test_hypot(3, 0, 3)
    test_hypot(0, 0, 0)
    test_hypot(0, 0, 0)  # Hypotenuse of a triangle with both legs zero is zero
    # Test with large numbers
    test_hypot(3000, 4000, 5000)            
    
    test_hypot(6000, 8000, 10000)
    test_hypot(9000, 12000, 15000)  
    
    