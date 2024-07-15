import streamlit as st

# Conversion functions from European numerals to various Indian scripts

def europeanToTelugu(europeanNumber):
    mapping = {
        '0': '౦', '1': '౧', '2': '౨', '3': '౩', '4': '౪',
        '5': '౫', '6': '౬', '7': '౭', '8': '౮', '9': '౯'
    }
    teluguNumber = "".join(mapping[char] if char in mapping else char for char in europeanNumber)
    return teluguNumber

# Add other conversion functions similarly for Devanagari, Gurmukhi, Bengali, Gujarati, Oriya, Tamil, Kannada, Malayalam, Sinhala, Manipuri, Nepali, Assamese

def europeanToDevanagari(europeanNumber):
    mapping = {
        '0': '०', '1': '१', '2': '२', '3': '३', '4': '४',
        '5': '५', '6': '६', '7': '७', '8': '८', '9': '९'
    }
    devanagariNumber = "".join(mapping[char] if char in mapping else char for char in europeanNumber)
    return devanagariNumber

def europeanToGurmukhi(europeanNumber):
    gurmukhiDigits = ['੦', '੧', '੨', '੩', '੪', '੫', '੬', '੭', '੮', '੯']
    gurmukhiNumber = ''.join(gurmukhiDigits[int(char)] if char.isdigit() and int(char) < len(gurmukhiDigits) else char for char in europeanNumber)
    return gurmukhiNumber

def europeanToBengali(europeanNumber):
    mapping = {
        '0': '০', '1': '১', '2': '২', '3': '৩', '4': '৪',
        '5': '৫', '6': '৬', '7': '৭', '8': '৮', '9': '৯'
    }
    bengaliNumber = "".join(mapping[char] if char in mapping else char for char in europeanNumber)
    return bengaliNumber

def europeanToGujarati(europeanNumber):
    mapping = {
        '0': '૦', '1': '૧', '2': '૨', '3': '૩', '4': '૪',
        '5': '૫', '6': '૬', '7': '૭', '8': '૮', '9': '૯'
    }
    gujaratiNumber = "".join(mapping[char] if char in mapping else char for char in europeanNumber)
    return gujaratiNumber

def europeanToOriya(europeanNumber):
    mapping = {
        '0': '୦', '1': '୧', '2': '୨', '3': '୩', '4': '୪',
        '5': '୫', '6': '୬', '7': '୭', '8': '୮', '9': '୯'
    }
    oriyaNumber = "".join(mapping[char] if char in mapping else char for char in europeanNumber)
    return oriyaNumber

def europeanToTamil(europeanNumber):
    tamilDigits = ['௦', '௧', '௨', '௩', '௪', '௫', '௬', '௭', '௮', '௯']
    tamilNumber = ''.join(tamilDigits[int(char)] if char.isdigit() and int(char) < len(tamilDigits) else char for char in europeanNumber)
    return tamilNumber

def europeanToKannada(europeanNumber):
    kannadaDigits = ["೦", "೧", "೨", "೩", "೪", "೫", "೬", "೭", "೮", "೯"]
    kannadaNumber = ''.join(kannadaDigits[int(char)] if char.isdigit() and int(char) < len(kannadaDigits) else char for char in europeanNumber)
    return kannadaNumber

def europeanToMalayalam(europeanNumber):
    malayalamDigits = ["൦", "൧", "൨", "൩", "൪", "൫", "൬", "൭", "൮", "൯"]
    malayalamNumber = ''.join(malayalamDigits[int(char)] if char.isdigit() and int(char) < len(malayalamDigits) else char for char in europeanNumber)
    return malayalamNumber

def europeanToSinhala(europeanNumber):
    mapping = {
        '0': '෦', '1': '෧', '2': '෨', '3': '෩', '4': '෪',
        '5': '෫', '6': '෬', '7': '෭', '8': '෮', '9': '෯'
    }
    sinhalaNumber = "".join(mapping[char] if char in mapping else char for char in europeanNumber)
    return sinhalaNumber

def europeanToManipuri(europeanNumber):
    mapping = {
        '0': '꯰', '1': '꯱', '2': '꯲', '3': '꯳', '4': '꯴',
        '5': '꯵', '6': '꯶', '7': '꯷', '8': '꯸', '9': '꯹'
    }
    manipuriNumber = "".join(mapping[char] if char in mapping else char for char in europeanNumber)
    return manipuriNumber

def europeanToNepali(europeanNumber):
    mapping = {
        '0': '०', '1': '१', '2': '२', '3': '३', '4': '४',
        '5': '५', '6': '६', '7': '७', '8': '८', '9': '९'
    }
    nepaliNumber = "".join(mapping[char] if char in mapping else char for char in europeanNumber)
    return nepaliNumber

def europeanToAssamese(europeanNumber):
    mapping = {
        '0': '০', '1': '১', '2': '২', '3': '৩', '4': '৪',
        '5': '৫', '6': '৬', '7': '৭', '8': '৮', '9': '৯'
    }
    assameseNumber = "".join(mapping[char] if char in mapping else char for char in europeanNumber)
    return assameseNumber

# Streamlit app code
def main():
    st.set_page_config(page_title="European to Indian Numeral Converter", layout="wide", initial_sidebar_state="expanded")
    st.title("European to Indian Numeral Converter")
    st.markdown(
        """
        Welcome to the European to Indian Numeral Converter App!
        Enter a European numeral (0-9) and see its equivalent in various Indian and other scripts.
        """
    )

    # Text input for the European numeral
    european_number = st.text_input("Enter a European numeral (0-9)")

    # Checkbox for selecting languages to compare
    st.sidebar.markdown("### Select Languages to Compare")
    compare_telugu = st.sidebar.checkbox("Telugu")
    compare_devanagari = st.sidebar.checkbox("Devanagari")
    compare_gurmukhi = st.sidebar.checkbox("Gurmukhi")
    compare_bengali = st.sidebar.checkbox("Bengali")
    compare_gujarati = st.sidebar.checkbox("Gujarati")
    compare_oriya = st.sidebar.checkbox("Oriya")
    compare_tamil = st.sidebar.checkbox("Tamil")
    compare_kannada = st.sidebar.checkbox("Kannada")
    compare_malayalam = st.sidebar.checkbox("Malayalam")
    compare_sinhala = st.sidebar.checkbox("Sinhala")
    compare_manipuri = st.sidebar.checkbox("Manipuri")
    compare_nepali = st.sidebar.checkbox("Nepali")
    compare_assamese = st.sidebar.checkbox("Assamese")

    # Display all languages numbers if no comparison is selected
    if not (compare_telugu or compare_devanagari or compare_gurmukhi or compare_bengali or compare_gujarati or compare_oriya or compare_tamil or compare_kannada or compare_malayalam or compare_sinhala or compare_manipuri or compare_nepali or compare_assamese):
        st.markdown("### Converted Numbers")
        st.write("Telugu:", europeanToTelugu(european_number))
        st.write("Devanagari:", europeanToDevanagari(european_number))
        st.write("Gurmukhi:", europeanToGurmukhi(european_number))
        st.write("Bengali:", europeanToBengali(european_number))
        st.write("Gujarati:", europeanToGujarati(european_number))
        st.write("Oriya:", europeanToOriya(european_number))
        st.write("Tamil:", europeanToTamil(european_number))
        st.write("Kannada:", europeanToKannada(european_number))
        st.write("Malayalam:", europeanToMalayalam(european_number))
        st.write("Sinhala:", europeanToSinhala(european_number))
        st.write("Manipuri:", europeanToManipuri(european_number))
        st.write("Nepali:", europeanToNepali(european_number))
        st.write("Assamese:", europeanToAssamese(european_number))
    else:
        # Display the selected comparisons in a table format
        st.markdown("### Comparison Table")
        comparisons = []
        if compare_telugu:
            comparisons.append(("Telugu", europeanToTelugu(european_number)))
        if compare_devanagari:
            comparisons.append(("Devanagari", europeanToDevanagari(european_number)))
        if compare_gurmukhi:
            comparisons.append(("Gurmukhi", europeanToGurmukhi(european_number)))
        if compare_bengali:
            comparisons.append(("Bengali", europeanToBengali(european_number)))
        if compare_gujarati:
            comparisons.append(("Gujarati", europeanToGujarati(european_number)))
        if compare_oriya:
            comparisons.append(("Oriya", europeanToOriya(european_number)))
        if compare_tamil:
            comparisons.append(("Tamil", europeanToTamil(european_number)))
        if compare_kannada:
            comparisons.append(("Kannada", europeanToKannada(european_number)))
        if compare_malayalam:
            comparisons.append(("Malayalam", europeanToMalayalam(european_number)))
        if compare_sinhala:
            comparisons.append(("Sinhala", europeanToSinhala(european_number)))
        if compare_manipuri:
            comparisons.append(("Manipuri", europeanToManipuri(european_number)))
        if compare_nepali:
            comparisons.append(("Nepali", europeanToNepali(european_number)))
        if compare_assamese:
            comparisons.append(("Assamese", europeanToAssamese(european_number)))

        comparisons_table = "<table><tr><th>Language</th><th>Converted Number</th></tr>"
        for comparison in comparisons:
            comparisons_table += f"<tr><td>{comparison[0]}</td><td>{comparison[1]}</td></tr>"
        comparisons_table += "</table>"
        st.write(comparisons_table, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
