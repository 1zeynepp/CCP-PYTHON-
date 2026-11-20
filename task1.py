# Open TempC.txt for reading and store values in a list
temps_c = []
with open("TempC.txt", "r") as infile:
    for line in infile:
        if line.strip():
            temps_c.append(float(line.strip()))

# Convert each temperature to Fahrenheit
temps_f = []
for c in temps_c:
    f = (c * 9 / 5) + 32
    temps_f.append(f)

# Write the converted temperatures to TempF.txt
with open("TempF.txt", "w") as outfile:
    for f in temps_f:
        outfile.write(f"{round(f)}\n")
