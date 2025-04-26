import streamlit as st

def convert_units(value: float, unit_from: str, unit_to: str):
   # print("value>>>", value)
   # print("unit_from>>>", unit_from)
   # print("unit_to>>>" , unit_to)

    # 1 kilometer = 1000 meters
    # 1 meters = 0.001 kilometer
    # 1 kilogram = 1000 grams
    # 1 gram = 0.001 kilogram

    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif   unit_from == "meters" and unit_to == "kilometers":
        return value * 0.001
    elif   unit_from == "kilograms" and unit_to == "grams":
        return value * 1000
    elif   unit_from == "grams" and unit_to == "kilograms":
        return value * 0.001
    else:
        return "conversion is not supported"
    
#result1 = convert_units(3, "kilometers", "meters")
#print("The value in meters is:", result1)
#result2 = convert_units(5, "grams", "kilograms")
#print("The value in kilograms is:", result2)

def main():
    st.title("Unit Converter")
    st.write("Welcome to unit Converter!")
    value = st.number_input("Enter the value you want to convert:",min_value=0.0)
    unit_from = st.text_input("Enter the value you want to convert from: (e.g. meters, kilometers, grams, kilograms)")
    unit_to = st.text_input("Enter the value you want from conversion: (e.g. meters, kilometers, grams, kilograms)")


    if st.button("Convert"):
        result = convert_units(value, unit_from, unit_to)
        st.write("Converted value is:", result)
#     print("Unit Converter")
#     print("Welcome to unit Converter!")
#     value = float (input("Enter the value you want to convert:"))
#     unit_from = input("Enter the value you want to convert from (e.g. meters, kilometers, grams, kilograms)")
#     unit_to = input("Enter the value you want from conversion (e.g. meters, kilometers, grams, kilograms)")

#     print("value", value)
#     print("unit_from", unit_from)
#     print("nuit_to", unit_to)
#     result = convert_units(value, unit_from, unit_to)
#     print("Converted value is:", result)

main()