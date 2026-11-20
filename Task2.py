max_snow = -1.0
max_date = ""
days_over_1 = 0
total_days = 0

with open("Snow_Fall.txt", "r") as infile:
    for line in infile:
        parts = line.strip().split()
        
        if len(parts) == 2:
            date = parts[0]
            try:
                snow = float(parts[1])
            except ValueError:
                continue
            
            total_days += 1
            
            # Part A: Find maximum snowfall and date
            if snow > max_snow:
                max_snow = snow
                max_date = date
                
            # Part B: Count days exceeding 1 inch
            if snow > 1.0:
                days_over_1 += 1

percent_over_1 = (days_over_1 / total_days) * 100

print(f"Maximum snowfall: {max_snow:.2f} inches on {max_date}")
print(f"Percentage of Days Snowfall Exceeded 1 inch: {percent_over_1:.2f}%")
