 Scenario 1: Data Validation
Python
def validate_data(data):
    invalid_entries = []
    
    for entry in data:
        if "age" not in entry or not isinstance(entry["age"], int):
            invalid_entries.append(entry)
    
    return invalid_entries
