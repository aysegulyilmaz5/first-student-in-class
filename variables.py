midterm1= 75
midterm2 = 90
midterm3 = 83

final1 = 100
final2 = 50
final3 = 70

avg1 = midterm1*0.3 + final1*0.7
avg2 = midterm2*0.3 +final2*0.7
avg3 = midterm3*0.3 + final3*0.7

namex = "Aysegul"
namey = "Emre"
namez = "Akif"

print("Average Grades")
print(namex,midterm1,final1,avg1)
print(namey,midterm2,final2,avg2)
print(namez,midterm3,final3,avg3)

if avg1>avg2>avg3:
    print("First student in class",namex)
elif avg1 > avg3>avg2:
    print("First student in class",namex)
elif avg2 > avg1 >avg3:
    print("First student in class",namey)
elif avg2 > avg3 > avg1:
    print("First student in class",namey)
elif avg3 > avg1 >avg2:
    print("First student in class",namez)
else:
    print("First student in class",namez)