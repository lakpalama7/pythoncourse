
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

OUTPUT:
--------------------------
1 1
1 2
2 1
2 2
3 1
3 2
------------------------------
(0,0,0)
(0,0,1)
(0,1,0)
(0,1,1)
(1,0,0)
(1,0,1)
(1,1,0)
(1,1,1)
(2,0,0)
(2,0,1)
(2,1,0)
(2,1,1)
------------------------------
Color - red & Size- L
Color - red & Size- M
Color - red & Size- S
Color - green & Size- L
Color - green & Size- M
Color - green & Size- S
Color - blue & Size- L
Color - blue & Size- M
Color - blue & Size- S
------------------------------
Report_2025_jan_1.csv
Report_2025_jan_2.csv
Report_2025_jan_3.csv
Report_2025_jan_4.csv
Report_2025_jan_5.csv
Report_2025_jan_6.csv
Report_2025_jan_7.csv
Report_2025_jan_8.csv
Report_2025_jan_9.csv
Report_2025_jan_10.csv
Report_2025_jan_11.csv
Report_2025_jan_12.csv
Report_2025_jan_13.csv
Report_2025_jan_14.csv
Report_2025_jan_15.csv
Report_2025_jan_16.csv
Report_2025_jan_17.csv
Report_2025_jan_18.csv
Report_2025_jan_19.csv
Report_2025_jan_20.csv
Report_2025_jan_21.csv
Report_2025_jan_22.csv
Report_2025_jan_23.csv
Report_2025_jan_24.csv
Report_2025_jan_25.csv
Report_2025_jan_26.csv
Report_2025_jan_27.csv
Report_2025_jan_28.csv
Report_2025_jan_29.csv
Report_2025_feb_1.csv
Report_2025_feb_2.csv
Report_2025_feb_3.csv
Report_2025_feb_4.csv
Report_2025_feb_5.csv
Report_2025_feb_6.csv
Report_2025_feb_7.csv
Report_2025_feb_8.csv
Report_2025_feb_9.csv
Report_2025_feb_10.csv
Report_2025_feb_11.csv
Report_2025_feb_12.csv
Report_2025_feb_13.csv
Report_2025_feb_14.csv
Report_2025_feb_15.csv
Report_2025_feb_16.csv
Report_2025_feb_17.csv
Report_2025_feb_18.csv
Report_2025_feb_19.csv
Report_2025_feb_20.csv
Report_2025_feb_21.csv
Report_2025_feb_22.csv
Report_2025_feb_23.csv
Report_2025_feb_24.csv
Report_2025_feb_25.csv
Report_2025_feb_26.csv
Report_2025_feb_27.csv
Report_2025_feb_28.csv
Report_2025_feb_29.csv
Report_2027_jan_1.csv
Report_2027_jan_2.csv
Report_2027_jan_3.csv
Report_2027_jan_4.csv
Report_2027_jan_5.csv
Report_2027_jan_6.csv
Report_2027_jan_7.csv
Report_2027_jan_8.csv
Report_2027_jan_9.csv
Report_2027_jan_10.csv
Report_2027_jan_11.csv
Report_2027_jan_12.csv
Report_2027_jan_13.csv
Report_2027_jan_14.csv
Report_2027_jan_15.csv
Report_2027_jan_16.csv
Report_2027_jan_17.csv
Report_2027_jan_18.csv
Report_2027_jan_19.csv
Report_2027_jan_20.csv
Report_2027_jan_21.csv
Report_2027_jan_22.csv
Report_2027_jan_23.csv
Report_2027_jan_24.csv
Report_2027_jan_25.csv
Report_2027_jan_26.csv
Report_2027_jan_27.csv
Report_2027_jan_28.csv
Report_2027_jan_29.csv
Report_2027_feb_1.csv
Report_2027_feb_2.csv
Report_2027_feb_3.csv
Report_2027_feb_4.csv
Report_2027_feb_5.csv
Report_2027_feb_6.csv
Report_2027_feb_7.csv
Report_2027_feb_8.csv
Report_2027_feb_9.csv
Report_2027_feb_10.csv
Report_2027_feb_11.csv
Report_2027_feb_12.csv
Report_2027_feb_13.csv
Report_2027_feb_14.csv
Report_2027_feb_15.csv
Report_2027_feb_16.csv
Report_2027_feb_17.csv
Report_2027_feb_18.csv
Report_2027_feb_19.csv
Report_2027_feb_20.csv
Report_2027_feb_21.csv
Report_2027_feb_22.csv
Report_2027_feb_23.csv
Report_2027_feb_24.csv
Report_2027_feb_25.csv
Report_2027_feb_26.csv
Report_2027_feb_27.csv
Report_2027_feb_28.csv
Report_2027_feb_29.csv
------------------------------
SELECT count(*) from customers where id IS NULL;
SELECT count(*) from customers where create_date IS NULL;
SELECT count(*) from order where id IS NULL;
SELECT count(*) from order where create_date IS NULL;
SELECT count(*) from product where id IS NULL;
SELECT count(*) from product where create_date IS NULL;

