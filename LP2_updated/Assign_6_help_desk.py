# Define an empty list to store the tickets
tickets = []

# Function to create a new ticket
def create_ticket(ticket_id, description):
    ticket = {
        "id": ticket_id,
        "description": description,
        "status": "Open",
        "agent": None
    }
    tickets.append(ticket)
    print("Ticket created successfully.")

# Function to assign a ticket to an agent
def assign_ticket(ticket_id, agent_name):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["agent"] = agent_name
            ticket["status"] = "Assigned"
            print("Ticket assigned successfully.")
            return
    print("Ticket not found.")

# Function to resolve a ticket
def resolve_ticket(ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            if ticket["status"] == "Assigned":
                ticket["status"] = "Resolved"
                print("Ticket resolved successfully.")
            else:
                print("Ticket is not assigned to an agent.")
            return
    print("Ticket not found.")

# Function to display all tickets
def display_tickets():
    if tickets:
        print("Tickets:")
        for ticket in tickets:
            print(f"Ticket ID: {ticket['id']}")
            print(f"Description: {ticket['description']}")
            print(f"Status: {ticket['status']}")
            print(f"Assigned Agent: {ticket['agent']}")
            print("----------")
    else:
        print("No tickets available.")

# Main program loop
while True:
    print("\n--- Help Desk Management Expert System ---")
    print("1. Create a new ticket")
    print("2. Assign a ticket to an agent")
    print("3. Resolve a ticket")
    print("4. Display all tickets")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        ticket_id = input("Enter ticket ID: ")
        description = input("Enter ticket description: ")
        create_ticket(ticket_id, description)
    elif choice == "2":
        ticket_id = input("Enter ticket ID to assign: ")
        agent_name = input("Enter agent name: ")
        assign_ticket(ticket_id, agent_name)
    elif choice == "3":
        ticket_id = input("Enter ticket ID to resolve: ")
        resolve_ticket(ticket_id)
    elif choice == "4":
        display_tickets()
    elif choice == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")

