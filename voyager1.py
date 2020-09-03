x=input('Number of days after 9/25/09: ')
dagar=int(x)
d=16637000000 #fjarlægð frá sólu á dagsetningu í mílum
v=38241 *24 #mílur á dag
dm=d*1.609344 #fjarlægð í kílómetrum á dagsetningu
vm=v*1.609344 #kílómetrar á dag
f=dagar*v+d #Fjarlægð í mílum
fm=dagar*vm+d*1.609344 #fjarlægð í metrum
AU=f/92955887.6 #fjarlægð í AU
yy=round(AU)
zz=round(fm)
mm=round(f)
print('Miles from the sun: ',mm)
print('Kilometers from the sun: ',zz)
print('AU from the sun: ',yy)

