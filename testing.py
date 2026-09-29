"""To test the code in the terminal run python -m."""

def get_valid_score(prompt):
    """Ensures input is a float between 0 and 100."""
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            print("   [!] Score must be between 0 and 100.")
        except ValueError:
            print("   [!] Invalid input. Please enter a number.")