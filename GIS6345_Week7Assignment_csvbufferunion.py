import csv
from shapely.geometry import Point, shape, mapping
from fiona import collection
from shapely.ops import unary_union

with open('some.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print (row)

with open('some.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        point = Point(float(row['lon']), float(row['lat']))


schema = { 'geometry': 'Point', 'properties': { 'name': 'str' } }
with collection(
    "some.shp", "w", "ESRI Shapefile", schema) as output:
    with open('some.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['lon']), float(row['lat']))
            output.write({'properties': {'name': row['name']},'geometry': mapping(point)})

with collection("some.shp", "r") as input:
    for point in input:
        print (shape(point['geometry']))

with collection("some.shp", "r") as input:
    # schema = input.schema.copy()
    schema = { 'geometry': 'Polygon', 'properties': { 'name': 'str' } }
    with collection(
        "some_buffer.shp", "w", "ESRI Shapefile", schema) as output:
        for point in input:
            output.write({'properties': {'name': point['properties']['name']},'geometry': mapping(shape(point['geometry']).buffer(5.0))})

with collection("some_buffer.shp", "r") as input:
    schema = input.schema.copy()
    with collection(
            "some_union.shp", "w", "ESRI Shapefile", schema) as output:
        shapes = []
        for f in input:
            shapes.append(shape(f['geometry']))
        merged = unary_union(shapes)
        output.write({'properties': {'name': 'Buffer Area'},'geometry': mapping(merged)})
