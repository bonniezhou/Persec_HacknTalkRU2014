
#constant
radius

#setup - sort crime_points in order of distance from reference_point (on the edge of the data set)
#run in Excel using lookup functions
sort_ref(csv_file):
	for crime_point in csv_file:
		d = distance(gps_point, reference_point)
		csv_file.sort

within_radius(gps_point):
	d = distance(gps_point, reference_point)
	low = d - radius
	high = d + radius + 1
	return csv_file[low:high]

total_danger(gps_point):
	total = 0
	for crime_point in within_radius(gps_point):
		total = total + crime_point.threat_level
	return total




#----------------------------------------------------------

#produces true if crime_point is within radius of gps_point 
within_radius(gps_point, crime_point)

#calculates the level of danger from gps_point
#INEFFICIENT!!
total_danger(gps_point):
	total = 0
	for each crime_point in csv_file:
		if within_radius(gps_point, crime_point):
			total = total + crime_point.threat_level
	return total

