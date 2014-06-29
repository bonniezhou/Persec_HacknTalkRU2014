import csv
import math

radius = 0.03
r2 = math.pow(radius, 2)

#within_radius: float float float float -> bool
def within_radius(gps_x, gps_y, crime_x, crime_y):
	dist = math.pow((gps_x - crime_x), 2) + math.pow((gps_y - crime_y), 2)
	return dist < r2

#total_danger: float float csv_file -> float
def total_danger(gps_x, gps_y, crime_file):
	total = 0
	with open(crime_file, 'rU') as f:
		reader = csv.reader(f)
		next(reader)
		for row in reader:
			crime_x = float(row[9])
			crime_y = float(row[10])

			if within_radius(gps_x, gps_y, crime_x, crime_y):
				total = total + 1
	return total

#get_score: float float -> int[0,4]
def get_score(x, y):
	danger = total_danger(x, y, crime_file="crimes_final.csv")

	if total_danger < 2000:
		return 0
	elif 2000 <= total_danger <= 4000:
		return 1
	elif 4000 <= total_danger <= 8000:
		return 2
	elif 8000 <= total_danger <= 16000:
		return 3
	else:
		return 4
	
