"""Getting input for swimming time, cycling time and running time from
user in minutes.""" 
swimming_time = float(input("Enter swimming time in minutes: "))
cycling_time = float(input("Enter cycling time in minutes: "))
running_time = float(input("Enter running time in minutes: "))

# Calculating sum of the all three events.
total_time = swimming_time + cycling_time + running_time
# Displaying total time in minutes.
print(f"Total time taken for all the events: {total_time}")

# Awards assign according to total time by using conditinal statements.
# The total_time Within qualifiyng time.
if total_time > 0 and total_time <= 100:
    print(f"""Congratulations! You have taken {total_time} minutes to complete
    triathlon and You have received Provincial Colors""")
# The total_time within 5 minutes of the qualifynig time.   
elif total_time >= 101 and total_time <= 105:
    print(f"""Congratulations! You have taken {total_time} minutes to complete 
    triathlon and You have received Provincial Half Colors""")
# The total_time within 10 minutes of the qualifynig time.
elif total_time >= 106 and total_time <= 110:
    print(f"""Congratulations! You have taken {total_time} minutes to complete 
    triathlon and You have received Provincial Scroll""")
#The total_time more than 10 minutes of the qualifynig time.
else:
    print(f"""Unfortunately You have taken {total_time} minutes to complete 
    triathlon and You have not received Award at this time""") 
