from typing import Dict
import random

# District to average soil values mapping (N, P, K, pH)
DISTRICT_SOIL_DATA = {
    # Southern India
    "coimbatore": {"N": 45, "P": 25, "K": 35, "ph": 6.5},
    "salem": {"N": 42, "P": 28, "K": 30, "ph": 6.8},
    "madurai": {"N": 40, "P": 30, "K": 32, "ph": 7.0},
    "tiruchirapalli": {"N": 43, "P": 26, "K": 34, "ph": 6.7},
    "tirunelveli": {"N": 41, "P": 29, "K": 31, "ph": 6.9},
    
    # Northern India
    "ludhiana": {"N": 50, "P": 20, "K": 40, "ph": 7.5},
    "karnal": {"N": 48, "P": 22, "K": 38, "ph": 7.3},
    "meerut": {"N": 47, "P": 24, "K": 36, "ph": 7.2},
    
    # Eastern India
    "kharagpur": {"N": 44, "P": 26, "K": 35, "ph": 6.0},
    "bhubaneswar": {"N": 43, "P": 27, "K": 34, "ph": 6.2},
    
    # Western India
    "nashik": {"N": 46, "P": 25, "K": 37, "ph": 6.8},
    "pune": {"N": 45, "P": 26, "K": 36, "ph": 6.9},
}

# Seasonal adjustments (percentage change from baseline)
SEASONAL_ADJUSTMENTS = {
    "kharif": {"N": 1.1, "P": 1.0, "K": 1.05},  # Monsoon season
    "rabi": {"N": 1.0, "P": 1.1, "K": 1.0},     # Winter season
    "summer": {"N": 0.9, "P": 0.95, "K": 1.15}   # Summer season
}

def get_soil_values(district: str, season: str) -> Dict[str, float]:
    """Get soil values for a district with seasonal adjustments."""
    district_lower = district.lower().strip()
    
    # Get base values or use defaults if district not found
    soil_data = DISTRICT_SOIL_DATA.get(district_lower, {
        "N": 45.0,  # Default values (can be adjusted)
        "P": 25.0,
        "K": 35.0,
        "ph": 6.8
    })
    
    # Apply seasonal adjustments
    season_lower = season.lower().strip()
    if season_lower in SEASONAL_ADJUSTMENTS:
        adjustments = SEASONAL_ADJUSTMENTS[season_lower]
        soil_data["N"] = round(soil_data["N"] * adjustments["N"], 1)
        soil_data["P"] = round(soil_data["P"] * adjustments["P"], 1)
        soil_data["K"] = round(soil_data["K"] * adjustments["K"], 1)
    
    # Add some small random variation to make it more realistic
    soil_data["N"] += random.uniform(-2, 2)
    soil_data["P"] += random.uniform(-1, 1)
    soil_data["K"] += random.uniform(-2, 2)
    soil_data["ph"] = round(soil_data["ph"] + random.uniform(-0.1, 0.1), 1)
    
    # Ensure values are within reasonable bounds
    soil_data["N"] = max(0, min(100, soil_data["N"]))
    soil_data["P"] = max(0, min(100, soil_data["P"]))
    soil_data["K"] = max(0, min(100, soil_data["K"]))
    soil_data["ph"] = max(4.0, min(9.0, soil_data["ph"]))
    
    return soil_data
