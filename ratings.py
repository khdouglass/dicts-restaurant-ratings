def display_restaurant_list(ratings):
    """Display alphabetized restaurant list with ratings"""

    for restaurant, rating in sorted(ratings.items()):
            print "%s: %s" % (restaurant, rating) 



def sort_rated_restaurants(file_name):
    """Restaurant rating lister."""

    restaurant_data = open(file_name)
    ratings = {}

    for line in restaurant_data:
        line = line.rstrip()
        line_data = line.split(":")

        ratings[line_data[0]] = line_data[1]

    while True:

        display_restaurant_list(ratings)

        new_restaurant = raw_input("What restaurant would you like to rate? ")
        new_rating = raw_input("What score would you like to give this restaurant? ")

        ratings[new_restaurant] = new_rating

        display_restaurant_list(ratings)

        add_another = raw_input("Would you like to add another restaurant? (y/n) ")

        if add_another == "n":
            break

sort_rated_restaurants("scores.txt")
