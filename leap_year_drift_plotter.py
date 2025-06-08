import matplotlib.pyplot as plt
import sys
import time

# Initialize variables
years = range(0, 3001)
shifts = []
current_shift = 0.0

# Loop through the years to calculate the shift
total_years = len(years)
for i, year in enumerate(years, 1):  # Enumerate to track progress
    current_shift += 0.2425  # days delay per year

    # Check if the year is a leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # Divisible by 400 -> Leap year
                current_shift -= 1.0
            # Divisible by 100 but not 400 -> Not a leap year
        else:
            # Divisible by 4 but not 100 -> Leap year
            current_shift -= 1.0

    # Append the current shift to the list
    shifts.append(current_shift)

    # Print progress
    progress = f"{i} / {total_years} - current_shift: {current_shift}"
    sys.stdout.write(f"\r{progress}")
    sys.stdout.flush()
    time.sleep(0.001)

print("\nCalculation complete!")

# Plotting
plt.figure(figsize=(10, 6))

# Split into segments of 400 years and alternate colors
color_1 = "#0050ff"  # Shade 1 of blue
color_2 = "#00a0ff"  # Shade 2 of blue
for start in range(0, 3001, 400):
    end = min(start + 400, 3000)
    plt.plot(
        years[start : end + 1],
        shifts[start : end + 1],
        color=color_1 if (start // 400) % 2 == 0 else color_2,
        marker=".",
    )

# Add horizontal line at y=0
plt.axhline(0, color="red", linestyle="--", linewidth=1)

# Labels and title
plt.title("Shift in Days Due to Leap Year Rules (Years 0-3000)")
plt.xlabel("Year")
plt.ylabel("Accumulated Shift (days)")
plt.grid(True, linestyle="-", linewidth=2)

# Show plot
plt.show()
