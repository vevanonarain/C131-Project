import pandas as pd

df = pd.read_csv('final.csv')

star_name = df["Star_name"]
distance = df["Distance"]
mass = df["Mass"]
radius = df["Radius"]

new_mass = []
new_radius = []

for i in range(len(mass)):
    try:
        var_mass = float(mass[i]) *  1.989e+30
        var_radius = float(radius[i]) * 6.957e+8

        new_mass.append(var_mass)
        new_radius.append(var_radius)
    
    except:
        new_mass.append(mass[i])
        new_radius.append(radius[i])

        pass



gravity = []

for i in range(0, len(distance)):
    try:
        var_gravity = (6.674e-11 * float(new_mass[i])) / (float(new_radius[i])**2)
        gravity.append(var_gravity)
        
    except:
        gravity.append('unknown')
        pass

print(gravity)

rows = pd.DataFrame(list(zip(star_name, distance,new_mass, new_radius, gravity)), columns=["Star Name", "Distance", "Mass", "Radius","Gravity"])
rows.to_csv("Star_Data.csv")