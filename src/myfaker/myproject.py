from fake_geo import FakeGeo

my_geos = [FakeGeo(center={'lat':59.32932349999999, 'lan':18.068580800000063} , radius=0.5),
           FakeGeo(center={'lat':40.7127837, 'lan':-74.00594130000002} , radius=0.5),
           FakeGeo(center={'lat':38.0279762, 'lan':-121.88468060000002} , radius=0.05)
           ]

for geo in my_geos:
    for a in range(5):
        lan , lat= geo.get()
        print ('{0}, {1}'.format(lan, lat))
