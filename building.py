import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address= address
        self.stories = stories
       
    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, name):
            self.owner = name

# Create 5 building instances
eight_hundred_eighth = Building("800 8th Street", 12)
ninety_nine = Building("99 9th Ave South", 3)
eleven_eleven = Building("1111 18th Street", 55)
one_ten = Building("110", 22)
forty_forty = Building("4040 14th Steet W", 2)

# Have each one get purchased by a real estate magnate
eight_hundred_eighth.purchase("Chuck West")
ninety_nine.purchase("Kanye West")
eleven_eleven.purchase("Manila Bui")
one_ten.purchase("Lina BeBe")
forty_forty.purchase("Darrell Golden")

# After purchased, construct each one
eight_hundred_eighth.construct()
ninety_nine.construct()
eleven_eleven.construct()
one_ten.construct()
forty_forty.construct()



print(f"{eight_hundred_eighth.address} was purchased by {eight_hundred_eighth.owner} on {eight_hundred_eighth.date_constructed.date()} and has {eight_hundred_eighth.stories} stories")

print(f"{ninety_nine.address} was purchased by {ninety_nine.owner} on {ninety_nine.date_constructed.date()} and has {ninety_nine.stories} stories")



