def conv(feet_inches):
    parts=feet_inches.split(' ')
    feet=float(parts[0])
    inches=float(parts[1])
    meters=feet*0.3048+inches*0.0254
    return feet,inches,meters

length=input("Enter the length: ")

m=conv(length)
ml=list(m)
print(f"{m[0]} Feets and {m[1]} inches are equal to {m[2]} meters")