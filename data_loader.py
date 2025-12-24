import json
import os
from datetime import date

def load_data():
    """Load site data from data.json"""
    data_path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Add dynamic data
    data['footer']['copyright'] = data['footer']['copyright'].format(year=date.today().year)
    
    return data

def validate_data(data):
    """Basic validation of data structure"""
    required_keys = ['bio', 'links', 'footer', 'analytics', 'meta']
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")
    
    # Check bio
    bio_required = ['name', 'greeting', 'subtitle', 'handle', 'avatar', 'avatar_alt']
    for key in bio_required:
        if key not in data['bio']:
            raise ValueError(f"Missing bio key: {key}")
    
    return True

if __name__ == "__main__":
    data = load_data()
    validate_data(data)
    print("Data loaded and validated successfully")