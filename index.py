import datetime

current_date = datetime.date.today()
print(current_date)
one_year_ago = current_date - datetime.timedelta(days=366)
print(one_year_ago)
one_months_before = one_year_ago - datetime.timedelta(days=30)
print(one_months_before)

one_year_ago1 = current_date - datetime.timedelta(days=365)
print(one_year_ago1)
one_months_after = one_year_ago1 + datetime.timedelta(days=30)
print(one_months_after)

two_year_ago = current_date - datetime.timedelta(days=731)
print(two_year_ago)
one_months_before1 = two_year_ago - datetime.timedelta(days=30)
print(one_months_before1)

two_year_ago1 = current_date - datetime.timedelta(days=730)
print(two_year_ago1)
one_months_after1 = two_year_ago1 + datetime.timedelta(days=30)
print(one_months_after1)