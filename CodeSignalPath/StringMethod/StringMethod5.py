# Space exploration crew members' data, containing their names, missions, and roles
crew_data = "Neil,Armstrong,Apollo 11,C;Buzz,Aldrin,Apollo 11,P;Michael,Collins,Apollo 11,CM"

crew_details = crew_data.split(";")
print(crew_details)

# TODO: Iterate over the list of crew member data
for member in crew_details:
    name, lastname, mission, role = member.split(',')
    astronaut = ('').join(f"{name} {lastname} {mission} {role}")
    # astronauts = ('\n').join(astronaut)
    print(astronaut)
    # TODO: For each member, split their data string using commas as delimiters

    # TODO: Print the crew member's details in a formatted string

# Expected output:
# Neil Armstrong Apollo 11 C
# Buzz Aldrin Apollo 11 P
# Michael Collins Apollo 11 CM