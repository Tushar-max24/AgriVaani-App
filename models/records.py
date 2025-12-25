from datetime import datetime
from typing import List, Dict, Optional

# In-memory storage
records_storage = []

def add_record(record: Dict) -> Dict:
    """Add a new record to the storage."""
    record_data = {
        "module_name": record["module_name"],
        "title": record["title"],
        "data": record["data"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    records_storage.append(record_data)
    return record_data

def get_all_records() -> List[Dict]:
    """Get all records from storage."""
    return records_storage

def get_records_by_module(module_name: str) -> List[Dict]:
    """Get records filtered by module name."""
    return [record for record in records_storage 
            if record["module_name"].lower() == module_name.lower()]
