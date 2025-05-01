# List of nearby stars: (name, distance, apparent brightness, luminosity)
nearby_star_data = [
    ('Alpha Centauri A', 4.3, 0.26, 1.56),
    ('Alpha Centauri B', 4.3, 0.077, 0.45),
    ('Alpha Centauri C', 4.2, 0.00006, 0.00006),
    ("Barnard's Star", 6.0, 0.0004, 0.0005),
    ('Wolf 359', 7.7, 0.00002, 0.00002),
    ('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
    ('Luyten 726-8 A', 8.4, 0.00003, 0.00006),
    ('Luyten 726-8 B', 8.4, 0.00002, 0.00004),
    ('Sirius A', 8.6, 1.00, 23.6),
    ('Sirius B', 8.6, 0.001, 0.003),
    ('Ross 154', 9.4, 0.00002, 0.0005),
]

# Sort functions with lambda expressions
sorted_by_distance = sorted(nearby_star_data, key=lambda star: star[1])
sorted_by_apparent_brightness = sorted(nearby_star_data, key=lambda star: star[2])
sorted_by_luminosity = sorted(nearby_star_data, key=lambda star: star[3])

# Function for table
def print_sorted_table(title, sorted_data, column_name):
    print(f"\n{title}")
    print("=" * 40)
    print(f"{'Star Name':<25} {column_name:<10}")
    print("=" * 40)
    for star in sorted_data:
        print(f"{star[0]:<25} {star[1 if column_name == 'Distance' else (2 if column_name == 'Brightness' else 3)]:<10.6f}")

if __name__ == '__main__':
    # Print tables
    print_sorted_table("Sorted by Distance", sorted_by_distance, "Distance")
    print_sorted_table("Sorted by Apparent Brightness", sorted_by_apparent_brightness, "Brightness")
    print_sorted_table("Sorted by Luminosity", sorted_by_luminosity, "Luminosity")