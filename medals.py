import csv
import json

class CountryMedals():
    def __init__(self, name = None, gold = None, silver = None, bronze = None, total = None):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
        self.total = total

    # Return JSON format string
    def to_json(self):
        return json.dumps(self.__dict__)

    # Get the number of medals by medal type
    def get_medals(self, medal_type):
        if medal_type.lower() == "gold":
            return self.gold
        elif medal_type.lower() == "silver":
            return self.silver
        elif medal_type.lower() == "bronze":
            return self.bronze
        elif medal_type.lower() == "total":
            return self.total
        else: return None

    # Print a summary for a team
    def print_summary(self):
        print("{} received {} medals in total; {} gold, {} silver, and {} bronze.".format(self.name, self.total, self.gold, self.silver, self.bronze)) 

    # Used for comparing two teams by numbers of gold, silver, bronze, total
    def compare(self, country_2):
        for medal_type in ["gold", "silver", "bronze", "total"]:
            temp_1 = self.get_medals(medal_type)
            temp_2 = country_2.get_medals(medal_type)
            if temp_1 > temp_2: print("- {} received {} {} medal(s), {} more than {}, which reveived {} of them.".format(self.name, temp_1, medal_type, temp_1 - temp_2, country_2.name, temp_2))
            elif temp_1 < temp_2: print("- {} received {} {} medal(s), {} less than {}, which reveived {} of them.".format(self.name, temp_1, medal_type, temp_2 - temp_1, country_2.name, temp_2))
            elif temp_1 == temp_2: print("- Both {} and {} received {} {} medal(s).".format(self.name, country_2.name, temp_1, medal_type))

# Sort instances ascending oeder
def sort_countries_by_medal_type_ascending(country_instances, medal_type):
    if medal_type == "gold": return sorted(country_instances, key = lambda x: x.gold)
    elif medal_type == "silver": return sorted(country_instances, key = lambda x: x.silver)
    elif medal_type == "bronze": return sorted(country_instances, key = lambda x: x.bronze)
    elif medal_type == "total": return sorted(country_instances, key = lambda x: x.total)

# Sort instances descending oeder
def sort_countries_by_medal_type_descending(country_instances, medal_type):
    if medal_type == "gold": return sorted(country_instances, key = lambda x: x.gold, reverse = True)
    elif medal_type == "silver": return sorted(country_instances, key = lambda x: x.silver, reverse = True)
    elif medal_type == "bronze": return sorted(country_instances, key = lambda x: x.bronze, reverse = True)
    elif medal_type == "total": return sorted(country_instances, key = lambda x: x.total, reverse = True)

# Used for entering the threshold, and check input whether is input >= 0
def read_positive_integer():
    while True:
        try:
            value = int(input("Enter the threshold (a positive integer): "))
            if value >= 0: break
            else: print("It isn't a positive integer.")
        except: print("It isn't an integer.")
    return value

# Return all the countries' name
def read_country_name():
    while True:
        value = input(">> Insert a country name ('q' for quit): ").lower()
        for key in countries.keys():
            if value == key.lower(): return key
        else: print("The options of countries are: \n{}".format("\n".join(countries.keys())))

# Return a medal type
def read_medal_type():
    while True:
        value = input("Enter a medal type (gold, silver, bronze, or total): ").lower()
        if value in ["gold", "silver", "bronze", "total"]: break
        else: print("The medal type doesn't exist.")
    return value

# Read the csv file, and change it to a Python dictionary
def read_csv_to_list(file_name):
    with open(file_name, encoding = 'utf-8-sig') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for index, header in enumerate(headers) :
            if header == "Team/NOC":
                headers[index] = "name"
            elif header == "Rank by Total":
                headers[index] = "rank_by_total"
            else: headers[index] = headers[index].lower()
        return [dict(zip(headers, row)) for row in reader]

# Change the "string" number to integer
def str2int(country_list):
    for country in country_list:
        country["rank"] = int(country["rank"])
        country["gold"] = int(country["gold"])
        country["silver"] = int(country["silver"])
        country["bronze"] = int(country["bronze"])
        country["total"] = int(country["total"])
        country["rank_by_total"] = int(country["rank_by_total"])
    return country_list

# Return the countries dictionary
def create_countries_dictionary(unsorted_list_country):
    countries = {}
    for country in unsorted_list_country:
        countries[country["name"]] = country
    return countries

# Return a dictionary of ling dictionary
def get_country_instance(countries):
    country_instances = []
    for country in countries.values():
        country_medals = CountryMedals()
        for key in vars(country_medals).keys():
            if key == "name":
                setattr(country_medals, key, country["name"])
            elif key == "gold":
                setattr(country_medals, key, country["gold"])
            elif key == "silver":
                setattr(country_medals, key, country["silver"])
            elif key == "bronze":
                setattr(country_medals, key, country["bronze"])
            elif key == "total":
                setattr(country_medals, key, country["total"])
        country_instances.append(country_medals)
    return country_instances

# Alphabetically sort country by name
def get_sorted_list_of_country_names(countries):
    return sorted(countries.keys())

# Print medals based on threshold and medal type, given more or fewer option
def fewer_or_more(option):
    print("Given a medal type, lists all the countries that received {} medals than a threshold;".format(option))
    medal_type = read_medal_type()
    threshold = read_positive_integer()
    print("Countries that received {} than {} '{}' medals:\n".format(option,threshold,medal_type))
    if option == "fewer":
        # Sort the instances by medal type, ascending
        ascending = sort_countries_by_medal_type_ascending(country_instances, medal_type)
        for instance in ascending:
            medal_num = instance.get_medals(medal_type)
            if medal_num < threshold: print(" - {} received {}".format(instance.name, medal_num))
    elif option == "more":
        # Sort the instances by medal type, descending
        descending = sort_countries_by_medal_type_descending(country_instances, medal_type)
        for instance in descending:
            medal_num = instance.get_medals(medal_type)
            if medal_num > threshold: print(" - {} received {}".format(instance.name, medal_num))

if __name__ == '__main__':
    # Medals_dataset.csv should be in the same folder as the medals.py file
    file_name = "Medals_dataset.csv"

    # Get countries dictionary
    countries = create_countries_dictionary(str2int(read_csv_to_list(file_name)))

    # Get a list of country instances
    country_instances = get_country_instance(countries)

    # Flag to stop the loop
    terminated = False

    # Start looping
    while not terminated:
        c = input("Insert a command (Type 'H' for help): ").lower()
        # Show sorted countries' names
        if c == "l":
            sorted_list_by_name = get_sorted_list_of_country_names(countries)
            print("The dataset contains {} countries: {}.".format(len(sorted_list_by_name),", ".join(sorted_list_by_name)))

        # Show a summary about the number of gold, silver, bronze, and total for a country
        elif c == "s":
            country_name = read_country_name()
            for instance in country_instances:
                if instance.name == country_name: instance.print_summary()

        # Medal comparison
        elif c == "c":
            # Get two countries to compare with
            print("Compare two countries")
            while True:
                country_1 = read_country_name()
                if country_1 != None: break
                
            print("\nInsert the name of the country you want to compare against '{}'".format(country_1))
            while True:
                country_2 = read_country_name()
                if country_2 != None: break

            print("\nMedals comparison between '{}' and '{}':".format(country_1, country_2))

            # Compare the two countries
            compare_countries = []
            for instance in country_instances:
                if instance.name == country_1:
                    compare_countries.append(instance)
            for instance in country_instances:
                if instance.name == country_2:
                    compare_countries.append(instance)
            compare_countries[0].compare(compare_countries[1])

        # Call the function that use threshold and medal type to show comparison, given more or fewer condition
        elif c == "m":
            fewer_or_more("more")
        elif c == "f":
            fewer_or_more("fewer")

        # Export to JSON format, and store the file to diractory where is the same as the medals.py
        elif c == "e":
            value = input("Enter the file name (.json): ")

            json_dict = {}
            for instance in country_instances:
                json_dict[instance.name] = json.loads(instance.to_json())

            # The JSON file is saved in the same diractory as the medals.py file
            with open('{}.json'.format(value), 'w') as f:
                json.dump(json_dict, f, indent = 4)

            print("File '{}' correctly saved".format(value))

        # Quit the programme
        elif c == "q": terminated = True

        # Show help
        elif c == "h":
            print("\nList of commands:")
            print(" - (H)elp shows the list of comments;")
            print(" - (L)ist shows the list of countries present in the dataset;")
            print(" - (S)ummary prints out a summary of the medals won by a single country;")
            print(" - (C)ompare allows for a comparison of the medals won by two countries;")
            print(" - (M)ore, given a medal type, lists all the countries that received more medals than a threshold;")
            print(" - (F)ewer, given a medal type, lists all the countries that received fewer medals than a threshold;")
            print(" - (E)xport, save the medals table as '.json' file")
            print(" - (Q)uit.")
        else: print("Command not recognised. Please try again.")

    print('Goodbye.')