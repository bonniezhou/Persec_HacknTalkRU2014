import csv
import sys
import serial
import time

PORT = #port on our machine

radius = 0.03
r2 = radius^2

#within_radius: float float float float -> bool
def within_radius(gps_x, gps_y, crime_x, crime_y):
	dist = (gps_x - crime_x)^2 + (gps_y - crime_y)^2
	return dist < r2

#total_danger: float float csv_file -> float
def total_danger(gps_x, gps_y, crime_file):
	total = 0
	with open(crime_file, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            crime_x = int(row[9])
			crime_y = int(row[10])

			if within_radius(gps_x, gps_y, crime_x, crime_y) == true:
				#add severity by crime type (row[12]) and recentness (row[13])
				total = total + 1
	return total


#RUN:
num_lights = 3



