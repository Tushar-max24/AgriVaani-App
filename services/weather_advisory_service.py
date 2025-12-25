def get_crop_advisory(temp, humidity, condition):
    if temp > 35 and humidity < 40:
        return "High temperature detected. Increase irrigation and avoid fertilizer use."

    if condition.lower() == "rain":
        return "Rain expected. Delay pesticide spraying."

    if humidity > 80:
        return "High humidity may cause fungal diseases. Monitor crops closely."

    return "Weather conditions are favorable for crop growth."
