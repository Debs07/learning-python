#!/urs/bin/python3

def americana(metri):
    miglia = metri / 1609.344
    piedi = metri * 3.280840
    pollici = metri * 39.37008
    iarde = metri * 1.093613
    output = (f"{metri} Metri corrispondono a \n{miglia} Miglia Terrestri\n{piedi} Piedi\n{pollici} Pollici\n{iarde} Iarde")
    return output


print(americana(134))