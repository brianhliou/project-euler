from datetime import datetime, timedelta

# Define the start and end dates
start_date = datetime(1901, 1, 1)
end_date = datetime(2000, 12, 31)

# Counter for Sundays that fall on the first of the month
sunday_count = 0

# Iterate through each month from start date to end date
current_date = start_date
while current_date <= end_date:
    # Check if the first day of the month is a Sunday
    if current_date.weekday() == 6:  # 6 represents Sunday
        sunday_count += 1

    # Move to the first day of the next month
    # Check if the current month is December
    if current_date.month == 12:
        current_date = datetime(current_date.year + 1, 1, 1)
    else:
        current_date = datetime(current_date.year, current_date.month + 1, 1)

print(sunday_count)

