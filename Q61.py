#Amanda Miloserny
import dbm
photo_category = dbm.open("photos", "c")
photo_category["animals.png"] = "animals all look different"
photo_category["food.png"] = "food is delicious and comforting"
photo_category["weather.png"] = "the weather changes with the seasons"
print(photo_category["animals.png"])
print(photo_category["food.png"])
print(photo_category["weather.png"])

for item in photo_category:
    print(item, photo_category[item])
