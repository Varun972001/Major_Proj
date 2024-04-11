from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Get the date 6 months ago
six_months_ago = current_date - timedelta(days=6*30)

print("Current Date:", current_date)
print("Date 6 Months Ago:", six_months_ago)
