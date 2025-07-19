#MAKING INTRESTING CODES FOR LEARNING
flat= {
    "A101":{"location":"madhapur","bhk":3,"rent":200000},
     "B202":{"location":"masab tank","bhk":5,"rent":200000},
     "H404":{"location":"gachbowli","bhk":2,"rent":190000},
      "K303":{"location":"tolichowki","bhk":4,"rent":300000},
       "K808":{"location":"mallepally","bhk":3,"rent":90000}
}
flat_no = input("Enter flat no: ")
if flat_no in flat:
    info = flat[flat_no]
    print(f"BHK: {info['bhk']}")
    print(f"Rent: Rs{info['rent']}")
else:
    print("Flat not found")