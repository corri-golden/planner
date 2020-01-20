from building import Building
from city import City


# Create 5 building instances
eight_hundred_eighth = Building("800 8th Street", 12)
ninety_nine = Building("99 9th Ave South", 3)
eleven_eleven = Building("1111 18th Street", 55)
one_ten = Building("110", 22)
forty_forty = Building("4040 14th Steet W", 2)


megalopolis = City()
# megalopolis.name = "Megalopolis"
# megalopolis.mayor = "Chuck Berry"
# megalopolis.year_built = 1988
# megalopolis.add_building.append("Sears Building")

megalopolis.add_building(eight_hundred_eighth)
megalopolis.add_building(ninety_nine)
megalopolis.add_building(eleven_eleven)
megalopolis.add_building(one_ten)
megalopolis.add_building(forty_forty)

for building in megalopolis.buildings:
    print(f"{building.address} was purchased by a {building.owner} on and has {building.stories} stories.")