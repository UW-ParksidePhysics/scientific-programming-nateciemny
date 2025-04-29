def convert_list_of_tuples(data):
    stars = {}
    for name, distance, brightness, luminosity in data:
        stars[name] = {
            'distance': distance,
            'apparent brightness': brightness,
            'luminosity': luminosity
        }
    return stars


def print_star_information(stars_dict, name):
    if name in stars_dict:
        info = stars_dict[name]
        print(f"Star: {name}")
        print(f"    Distance (ly):            {info['distance']}")
        print(f"    Apparent brightness (m):  {info['apparent brightness']}")
        print(f"    Luminosity (L_sun):       {info['luminosity']}")
    else:
        print(f"Star '{name}' not found in the data.")


# Data
nearby_star_data = [
    ('Alpha Centauri A',    4.3,  0.26,      1.56),
    ('Alpha Centauri B',    4.3,  0.077,     0.45),
    ('Alpha Centauri C',    4.2,  0.00001,   0.00006),
    ("Barnard's Star",      6.0,  0.00004,   0.0005),
    ('Wolf 359',            7.7,  0.000001,  0.00002),
    ('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
    ('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
    ('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
    ('Sirius A',            8.6,  1.00,      23.6),
    ('Sirius B',            8.6,  0.001,     0.003),
    ('Ross 154',            9.4,  0.00002,   0.0005),
]

# Convert to nested dictionary
stars = convert_list_of_tuples(nearby_star_data)

# Print info for two stars
print_star_information(stars, 'Alpha Centauri A')
print()
print_star_information(stars, 'Sirius B')
