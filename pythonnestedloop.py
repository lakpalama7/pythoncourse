
num1=[1,2,3]
num2=[1,2]

for x in num1:
    for y in num2:
        print(x,y)

print("---"*10)

for x in range(3):
    for y in range(2):
        for z in range(2):
            print(f"({x},{y},{z})")


print("---"*10)

colors=['red','green','blue']
sizes=['L','M','S']

for color in colors:
    for size in sizes:
        print(f"Color - {color} & Size- {size}")

print("---"*10)
#dispaly years, month and day report

years=[2025,2027]
months=['jan','feb']
days=range(1,30)

for y in years:
    for m in months:
        for d in days:
            print(f"Report_{y}_{m}_{d}.csv")


print("---"*10)
#Select count(*) from Customers where id IS NULL;

tables = ['customers','order','product']
columns = ['id','create_date']

for t in tables:
    for c in columns:
        print(f"SELECT count(*) from {t} where {c} IS NULL:")

