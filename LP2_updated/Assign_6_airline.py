rules = [
    {"source": "mumbai", "destination":"pune","type": "passenger", "recommendation": "Flight XYZ123 is available from New York."},
    {"source": "pune", "destination":"mumbai","type": "passenger", "recommendation": "Flight XYZ123 is available from New York."},
    {"source": "pune", "destination":"shirdi","type": "passenger", "recommendation": "Flight XYZ123 is available from New York."},
    {"source": "mumbai", "destination":"dubai","type": "passenger", "recommendation": "Flight XYZ123 is available from New York."},
    {"source": "banglore", "destination":"pune","type": "cargo", "recommendation": "Flight XYZ123 is available from New York."},
    {"source": "mumbai", "destination":"pune","type": "cargo", "recommendation": "Flight XYZ123 is available from New York."},
]

def process_input(source,destination,type):
    matching_rules = []
    for rule in rules:
        if rule["source"] == source and rule["destination"] == destination and rule["type"] == type:
            matching_rules.append(rule)

    if len(matching_rules) == 0:
        return "No matching options found."

    recommendations = []
    for rule in matching_rules:
        recommendations.append(rule["recommendation"])

    return ", ".join(recommendations)


def addFlight(source,destination,type,recommendation):
    rules.append({"source":source,"destination":destination,"type":type,"recommendation":recommendation})

while(True):
    print("1. Search flight")
    print("2. Add flight")
    print("3. display")
    print("3. quit")

    choice = int(input("Enter choice : "))
    if(choice == 1):
        source = input("Enter boarding city: ")
        destination = input("Enter alighting city: ")
        user_type = input("Enter type (Passenger or Cargo): ")

        output = process_input(source,destination,user_type)
        print(output)
    
    elif(choice == 2):
        source = input("Enter boarding city: ")
        destination = input("Enter alighting city: ")
        user_type = input("Enter type (Passenger or Cargo): ")
        recommendation = input("Enter recommendation: ")

        
        addFlight(source,destination,type,recommendation)
        print("flight added successfully")
    
    elif(choice == 3):
        for rule in rules:
            print(rule["source"],rule["destination"])
 
    else:
        break