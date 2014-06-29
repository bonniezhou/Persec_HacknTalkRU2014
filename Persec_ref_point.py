import csv

radius = 
ref = [-122.5, 37.7]

#distance: int int (list of int) -> int
def distance(x, y, ref):
	ref_x = ref[0]
	ref_y = ref[1]
	return (x - ref_x)^2 + (y - ref_y)^2

#sort_by_ref: csv_file -> (dict of int:(list of int))
def sort_by_ref(crime_file):
	crimes = {}
    with open(crime_file, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
			incident = int(row[0])
            x = int(row[9])
			y = int(row[10])
			dist = distance(x, y, ref)
			if dist not in crimes:
				crimes[dist] = []
			crimes[dist].append(incident)
	return crimes

def within_radius(gps_point, reference_point):
	d = distance(gps[0], gps[1], reference_point)
	low = d - radius
	high = d + radius + 1
	return csv_file[low:high]
