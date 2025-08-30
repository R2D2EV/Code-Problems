# This function processes astronaut names and planets from a string
# then prints out a neat summary of who is exploring which planet.
def process_astronaut_data(data):
    astronaut_details = data.split(';')
    for detail in astronaut_details:
        # TODO: Extract the astronaut name and explored planet from the detail, strip away the whitespace.
        astronaut, planet = detail.split('-')
        # TODO: Print the statement in the format "Astronaut [name] is exploring [planet]."
        print(f"Astronaut {astronaut.strip()} is exploring {planet.strip()}.")
        
# String containing astronaut names and planets, separated by semicolons.
# Each astronaut-planet pair is separated by a dash.
astronaut_data = "    Neil-Mars; Buzz-Jupiter; Sally-Venus    "
process_astronaut_data(astronaut_data)