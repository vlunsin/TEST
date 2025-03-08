def binary_steps(binary_str: str) -> int:
    """
    Convert a binary string to an integer and count the number of steps to reduce it to zero.
    Steps:
      - If the number is odd, subtract 1.
      - If the number is even, divide it by 2.
    """
    # Convert binary string to integer
    num = int(binary_str, 2)
    steps = 0
    
    # Perform the steps until the number reaches 0
    while num > 0:
        if num % 2 == 0:
            num //= 2  # Divide by 2 if even
        else:
            num -= 1  # Subtract 1 if odd
        steps += 1
    
    return steps

# Unit tests using pytest
def test_binary_steps():
    assert binary_steps("0") == 0  # Already zero, no steps needed
    assert binary_steps("1") == 1  # 1 -> 0 (1 step)
    assert binary_steps("10") == 2  # 2 -> 1 -> 0 (2 steps)
    assert binary_steps("11") == 3  # 3 -> 2 -> 1 -> 0 (3 steps)
    assert binary_steps("101") == 5  # 5 -> 4 -> 2 -> 1 -> 0 (5 steps)
    assert binary_steps("1101") == 6  # 13 -> 12 -> 6 -> 3 -> 2 -> 1 -> 0 (6 steps)

if __name__ == "__main__":
    import pytest
    pytest.main()