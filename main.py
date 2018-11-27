import csv
import time

t1 = time.time()

def cities():
    with open('cities.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            yield line

def points():
    with open('points.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for point in csv_reader:
            yield point

def genList(gen):
    glist = []
    for it in gen():
        glist.append(it)
    return glist

citiesList = genList(cities)
pointsList = genList(points)
cityIter = iter(citiesList)
pointsIter = iter(pointsList)

with open('output_points.csv','w') as csv_file:
    fields = ['ID','X','Y','Name']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
    csv_writer.writeheader()
    currentPoint = next(pointsIter)
    while True:
        newDict = currentPoint
        try:
            currentCity = next(cityIter)
        except:
            newDict['Name'] = "None"
            csv_writer.writerow(newDict)
            break
        if int(currentPoint['X']) >= int(currentCity['TopLeft_X']) and int(currentPoint['X']) <= int(currentCity['BottomRight_X']) and int(currentPoint['Y']) >= int(currentCity['TopLeft_Y']) and int(currentPoint['Y']) <= int(currentCity['BottomRight_Y']):
            newDict['Name'] = currentCity['Name']
            csv_writer.writerow(newDict)
            cityIter = iter(citiesList)
            try:
                currentPoint = next(pointsIter)
            except:
                break



t2 = time.time()
print t2-t1