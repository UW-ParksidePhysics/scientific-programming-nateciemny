earth_gravity = 9.8067  # m/s/s
neptune_gravity = 11.28  # m/s/s

initial_velocity = 10.00  # m/s

earth_total_time = 2 * initial_velocity / earth_gravity
neptune_total_time = 2 * initial_velocity / neptune_gravity

interval_number = 20
# create separate times for earth and neptune and separate positions
# we need to define list of times
for time in times:
    print(f'{time:7.3f}\t{position:7.3f}\t')