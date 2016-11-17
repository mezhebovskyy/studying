import sqlite3 as lite
import sys

class Car:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class CarService:
    def __init__(self):
        self.listofcars = []


con = lite.connect('test.db')
carservice = CarService()

with con:
    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        carservice.listofcars.append(Car(row["Id"], row["Name"], row["Price"]))

for car in carservice.listofcars:
    print "Car Id - %s. Name - %s. Price - %s." % (car.id, car.name, car.price)