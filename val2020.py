import numpy        #importing numpy for a randomizer with max and min value

Partier = [         #Defining all parties in a list of dictionaries
    {
        "namn" : "Gröngöligarna",       #Name of the party
        "inriktning" : "Vänster",       #Political ideology
        "block" : "Småpartierna",       #Political coalition
        "min_röst" : 3,                 #Minimum availible votes
        "max_röst" : 12,                #Maximum available votes
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

slutres = 0                 #Defining all variables used in the code
nyres = slutres
mandat = 0
just = 0
Oljeblocket = 0
Småpartierna = 0
hproc = 0
vproc = 0
röstare= 0
fuskare= 0
stop= False
röstberättigade=int(input("Hur många rösberättigade finns i samhället som ska rösta\n"))        #Asking how many people that are eligeble to vote in the country
print("\n----------------------------------------------------------------------------\n")       #Making a distinct break in the terminal for better readability
while stop == False:
    for Parti in Partier:
        resultat = numpy.random.randint(high= Parti["max_röst"],low= Parti["min_röst"])     #Randomizing result depinding on each parties special max/min votes
        slutres = slutres + resultat        #Adding all parties results together
        Parti["resultat"] = resultat        #Adding a new key in the dictionaries with the result
    if slutres>100:
        slutres = 0         #if result is over 100% it starts over
    else:
        break


for dic in Partier:
    if dic["resultat"]<4:       #Counting on wether the party makes it into the parliament
        just=dic["resultat"]+just     #fixing the result so that the mandates is based on the ones that come in not every party  

nyres=slutres-just

for dic in Partier:
    if dic["resultat"]>=4:
        mandat= int(dic["resultat"]/nyres*349)      #counting how many mandates the party gets in the parliament
        print(dic["namn"],"fick", dic["resultat"],"%","vilket är",mandat,"mandat i riksdagen")      #printing the result of the mandates if the got any
        if dic["block"]=="Oljeblocket":
            Oljeblocket=Oljeblocket+mandat      #counting mandates for each political coalition
        elif dic["block"]=="Småpartierna":
            Småpartierna=Småpartierna+mandat
    else:
        print(dic["namn"],"fick", dic["resultat"],"% och kommer då inte in i riksdagen")       #printing the result if the party didnt make it to the parliament
    
    if dic["inriktning"]=="Höger":          #counting percentage for the left or right 
        hproc=hproc+dic["resultat"]
    else:
        vproc=vproc+dic["resultat"]

print("\n----------------------------------------------------------------------------\n")

print("Oljeblocket får",Oljeblocket,"mandat")       #printing overall facts not for each party
print("Småpartierna får",Småpartierna,"mandat")     #result of mandates for the coalitions

if vproc>hproc:
    print("Folk röstar mer mot vänster med totalt",vproc-hproc,"% enheter")     #printing peoples voting tendencies either left or right and by how much
elif vproc==hproc:
    print("Folk röstar lika mycket vänster som höger")
else:
    print("Folk röstar mer mot höger med totalt",hproc-vproc,"% enheter")
print("Valdeltagandet var",slutres,"%")     #Presenting how high the voting participation was
röstare=int(röstberättigade*slutres/100)        #calculating the number of total voters there was
fuskare= röstberättigade-röstare        #calculating the peple who didnt vote
if fuskare==0:
    print("Alla röstberättigade i hela samhället röstade, hurra för demokratin!!!")     #if everybody voted this result shows
else:
    print("Det var",fuskare,"personer som inte röstade, fy på dem!!!")      #if not everybody voted it shows how many didnt
