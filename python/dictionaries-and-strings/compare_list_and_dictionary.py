code_snippets = {
    "dictionary_snippet": {
        "code": "numbers = {}\nnumbers[0] = -5\nnumbers[1] = 10.5",
        "explanation": "This is because dictionaries take on new keys dynamically. Any time you add a value to a key that hasn't yet been added, it is added to the dictionary.",
        "fix": None  # This one works
    },
    "list_snippet": {
        "code": "other_numbers = []\nother_numbers[0] = -5\nother_numbers[1] = 10.5",
        "explanation": "This won't work since lists must already contain elements at some index to be able to assign something to them. Indexing a list beyond its current length causes an IndexError. ",
        "fix": "other_numbers = [0, 0]  # Pre-allocate two elements\nother_numbers[0] = -5\nother_numbers[1] = 10.5"
    }
}

for key, snippet in code_snippets.items():
    print(f"--- {key} ---\n")
    print("Code Snippet:")
    print(snippet["code"])
    print("\nExplanation:")
    print(snippet["explanation"])
    if snippet["fix"]:
        print("\nFixed Code:")
        print(snippet["fix"])
    print("\n" + "="*40 + "\n")
