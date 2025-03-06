import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Unit Converter",
    page_icon="⚖️"
)

# Page title
st.title("⚖️ Unit Converter")

# Unit conversion options
conversion_type = ["Length", "Temperature", "Weight"]
conversion_choice = st.selectbox("Select Conversion Type", conversion_type)

# Conversion logic
if conversion_choice == "Length":
    length_units = ["Kilometers", "Meters", "Feet", "Inches", "Centimeters"]
    input_value = st.number_input("Enter Length Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", length_units, key="length_from")
    to_unit = st.selectbox("To Unit", length_units, key="length_to")

    length_conversion = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Inches": 0.0254,
        "Centimeters": 0.01,
    }

    if st.button("Convert", key="length_convert"):
        result = input_value * (length_conversion[from_unit] / length_conversion[to_unit])
        st.success(f"{input_value} {from_unit} is equal to {result:.2f} {to_unit}")

elif conversion_choice == "Weight":
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    input_value = st.number_input("Enter Weight Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", weight_units, key="weight_from")
    to_unit = st.selectbox("To Unit", weight_units, key="weight_to")

    weight_conversion = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }

    if st.button("Convert", key="weight_convert"):
        result = input_value * (weight_conversion[from_unit] / weight_conversion[to_unit])
        st.success(f"{input_value} {from_unit} is equal to {result:.2f} {to_unit}")

elif conversion_choice == "Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    input_value = st.number_input("Enter Temperature Value:", format="%.2f")
    from_unit = st.selectbox("From Unit", temperature_units, key="temp_from")
    to_unit = st.selectbox("To Unit", temperature_units, key="temp_to")

    def converter_temperature(input_value, from_unit, to_unit):
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return input_value * 9/5 + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return input_value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (input_value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (input_value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return input_value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (input_value - 273.15) * 9/5 + 32
        return input_value

    if st.button("Convert", key="temp_convert"):
        result = converter_temperature(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} is equal to {result:.2f} {to_unit}")

# Footer
st.markdown("---")
st.write("Created with 💖 by [Danish Noor]")
