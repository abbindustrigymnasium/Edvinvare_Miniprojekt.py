import numpy

Partier = [  
    {
        "namn" : "Gröngöligarna",
        "inriktning" : "Vänster",
        "block" : "Småpartierna",
        "min_röst" : 3,
        "max_röst" : 12,
    },
        {
        "namn" : "Partikelpartiet",
        "inriktning" : "Vänster",
        "block" : "Småpartierna",
        "min_röst" : 2,
        "max_röst" : 8,
    },
        {
        "namn" : "Mälarpartiet",
        "inriktning" : "Höger",
        "block" : "Småpartierna",
        "min_röst" : 8,
        "max_röst" : 18,
    },
        {
        "namn" : "Sjörövarpartiet",
        "inriktning" : "Höger",
        "block" : "Småpartierna",
        "min_röst" : 3,
        "max_röst" : 12,
    },
        {
        "namn" : "Extremisterna",
        "inriktning" : "Höger",
        "block" : "Oljeblocket",
        "min_röst" : 3,
        "max_röst" : 6,
    },
        {
        "namn" : "Maskinpartiet",
        "block" : "Oljeblocket",
        "inriktning" : "Vänster",
        "min_röst" : 12,
        "max_röst" : 22,
    },
        {
        "namn" : "Framtidspartiet",
        "inriktning" : "Höger",
        "block" : "Oljeblocket",
        "min_röst" : 12,
        "max_röst" : 18,
    },
        {
        "namn" : "Allpartiet",
        "inriktning" : "Vänster",
        "block" : "Inget",
        "min_röst" : 20,
        "max_röst" : 34,
    }]

slutres= 0
stop= False
nödbroms= 0 
nyres= slutres
mandat= 0
just=0
Oljeblocket=0
Småpartierna=0
hproc=0
vproc=0

while stop == False:
    for Parti in Partier:
        resultat = numpy.random.randint(high= Parti["max_röst"],low= Parti["min_röst"])
        slutres = slutres + resultat
        Parti["resultat"] = resultat
    if slutres>100:
        slutres = 0
    else:
        break
nyres=slutres-just

for dic in Partier:
    if dic["resultat"]<4:
        just=dic["resultat"]-just
    print(dic["namn"],"fick", dic["resultat"],"%",end=" ")

    if dic["resultat"]>=4:
        mandat= int(dic["resultat"]/nyres*349)
        print("vilket är",mandat,"mandat i riksdagen")
        if dic["block"]=="Oljeblocket":
            Oljeblocket=Oljeblocket+mandat
        elif dic["block"]=="Småpartierna":
            Småpartierna=Småpartierna+mandat
    else:
        print("och kommer då inte in i riksdagen")
    
    if dic["inriktning"]=="Höger":
        hproc=hproc+dic["resultat"]
    else:
        vproc=vproc+dic["resultat"]

print("\n----------------------------------------------------------------------------\n")

print("Oljeblocket får",Oljeblocket,"mandat")
print("Småpartierna får",Småpartierna,"mandat")
print("Totalt var det",slutres,"%","som röstade!")
if vproc>hproc:
    print("Folk röstar mer mot vänster med totalt",vproc-hproc,"% enheter")
elif vproc==hproc:
    print("Folk röstar lika mycket vänster som höger")
else:
    print("Folk röstar mer mot höger med totalt",hproc-vproc,"% enheter")