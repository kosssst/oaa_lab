import db

t1 = db.table("table1", ["id", "name", "bd"], ["", "", ""])
t1.add_row(["1", "kost", "10"])
print(t1.name)
print(t1.data)