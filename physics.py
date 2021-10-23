print("TO FIND OUT THE HEIGHT OF THE BALLOON AT EACH SECOND, TYPE THE INITIAL HEIGHT")
height_of_building = float(input("What is the height of the building (in meters)?: "))
g = 9.8 #meters per seconds
seconds_fallen = 0
distance_fallen = (g*(seconds_fallen**2))/2
balloon_height = height_of_building - distance_fallen
balloon_height_rounded = round(balloon_height, 2)

while (balloon_height >=0):
    print(f"At {seconds_fallen} second(s), the balloon is at height: {balloon_height_rounded} meters")
    seconds_fallen = seconds_fallen +1
    distance_fallen = (g * (seconds_fallen ** 2)) / 2
    balloon_height = height_of_building - distance_fallen
    balloon_height_rounded = round(balloon_height, 2)



