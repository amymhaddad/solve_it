# Option 1
def shoeDetails(shoe):
    brand, color, size = shoe.strip().split("\t")
    return {"brand": brand, "color": color, "size": size}


# Option 2
def shoeDetails2(shoe):
    return dict(zip(["brand", "color", "size"], shoe.strip().split("\t")))


shoes = [shoeDetails2(shoe) for shoe in open("shoe-data.txt")]

for shoe in shoes:
    print(f"Brand: {shoe['brand']} Color: {shoe['color']} Size: {shoe['size']}")
