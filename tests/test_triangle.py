from mygeopy.triangle import hypot

def test_hypot():
    """Test the hypot function with various inputs."""
    assert hypot(3, 4) == 5.0
    assert hypot(5, 12) == 13.0
    assert hypot(8, 15) == 17.0
    assert hypot(7, 24) == 25.0
    
    # Test with zero
    assert hypot(0, 0) == 0.0
    assert hypot(0, 3) == 3.0
    
    # Test with non-integer floats
    assert hypot(3.0, 4.0) == 5.0

