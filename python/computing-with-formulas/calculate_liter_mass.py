iron_density = 7870 #g/l
air_density = 1.2 #g/l
ice_density = 916.7 #g/l
human_density = 1.1 #g/cc
silver_density = 10500 ##g/l
platinum_density = 21450 #g/l
gasoline_density = .755 #g/cc

#liter = 1000 cubic centimeters
#density = mass/Volume -> mass = volume*density

gasoline_mass = gasoline_density * 1000
human_mass = human_density * 1000
print("Gasoline mass (in grams) in a liter:", gasoline_mass)
print("Human mass (in grams) in a liter:",  human_mass)
print("Iron mass (in grams) in a liter:",  iron_density)
print("Air mass (in grams) in a liter:",  air_density)
print("Ice mass (in grams) in a liter:",  ice_density)
print("Silver mass (in grams) in a liter:",  silver_density)
print("Platinum mass (in grams) in a liter:", platinum_density)
