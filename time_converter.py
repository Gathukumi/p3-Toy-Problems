def convert_to_24_hour(hour, minute, period):
    # Check if the period is "am" or "pm" and adjust the hour accordingly
    if period.lower() == "pm" and hour != 12:
        hour += 12
    elif period.lower() == "am" and hour == 12:
        hour = 0

    # Format the hour and minute to ensure they have leading zeros if needed
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)

    # Combine the hour and minute and return the result
    return hour_str + minute_str
