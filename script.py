destinations = ['Paris, France', 'Shanghai, China',
                'Los Angeles, USA', 'Sao Paulo, Brazil', 'Cairo, Egypt']

attractions = [[] for i in range(len(destinations))]
# print(attractions)

# name, location, list of likes
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# gets the index of location from destinations


def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

#print(get_destination_index('Hyderabad, India'))

# using the travelers current location to return an index


def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index)

# adding attractions to a list based on index


def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return attractions


add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", [
               "historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", [
               "garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", [
               "skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", [
               "monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
# print(attractions)


# matches the destination with attractions
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]

    attractions_with_interest = []
    for possible_attraction in attractions_in_city:
        attraction_tags = possible_attraction[1]

        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest


# Test Data
# la_arts = find_attractions('Los Angeles, USA', ['art'])
# print(la_arts)


# main function to display attractions based on traveler location
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]

    traveler_attractions = find_attractions(
        traveler_destination,    traveler_interests)
    attractions_lst = [attraction for attraction in traveler_attractions]
    interests_string = f"Hi {traveler[0]}, we think you'll like these places around {traveler_destination}: {attractions_lst}"
    return interests_string


# Test Data
smills_france = get_attractions_for_traveler(
    ['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
