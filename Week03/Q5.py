contacts = {
    "Alice": "444-1234",
    "Bob": "555-5678",
    "Charlie": "666-6789"
    
}

print("Alice's number:", contacts["Alice"])

contacts["Diana"] = "777-7890"
print("Contacts after addin:", contacts["Diana"])

contacts["Bob"] = "555-0000"
print("Bob's updated number:", contacts["Bob"]) 
del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)
print("All names: ", contacts.keys())
print("All numbers: ", contacts.values())
print("Total contact ", len(contacts))