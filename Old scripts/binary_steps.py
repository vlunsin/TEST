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

if __name__ == "__main__":
    binary_input = input("Enter a binary number: ")
    result = binary_steps(binary_input)
    print(f"Steps to reduce {binary_input} to 0: {result}")
