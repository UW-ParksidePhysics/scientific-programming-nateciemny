def analyze_script(file_path):
    total_lines = 0
    code_lines = 0
    function_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            total_lines += 1
            stripped = line.strip()

            if stripped:
                if not stripped.startswith("#") and not stripped.startswith('"""') and not stripped.startswith("'''"):
                    code_lines += 1

            if stripped.startswith("def "):
                function_count += 1

    print(f"Total lines (including comments and blanks): {total_lines}")
    print(f"Total active code lines: {code_lines}")
    print(f"Number of functions: {function_count}")

# Example usage
analyze_script("planet_distance.py")  # Change to your actual filename
