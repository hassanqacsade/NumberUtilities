def find_largest_number(numbers):
    if not numbers:
        return None
    return max(numbers)

# Test the function
if __name__ == "__main__":
    print(find_largest_number([3, 1, 4, 1, 5, 9]))  # Expected output: 9
