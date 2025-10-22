import streamlit as st

from main import (MemorablePasswordGenerator, PinGenerator,
                  RandomPasswordGenerator)

if 'pin_result' not in st.session_state:
    st.session_state.pin_result = "PIN Result"

if 'random_result' not in st.session_state:
    st.session_state.random_result = "Random Result"

if 'memorable_result' not in st.session_state:
    st.session_state.memorable_result = "Memorable Result"

def generate_pin(p_length):
    pin = PinGenerator(p_length)
    st.session_state.pin_result = pin.generate()


def generate_random(r_length, include_numbers, include_symbols):
    r_password = RandomPasswordGenerator(r_length, include_numbers, include_symbols)
    st.session_state.random_result = r_password.generate()


def generate_memorable(number_of_words, seperator, capitalize, random_lower_upper, vocabulary):
    m_password = MemorablePasswordGenerator(number_of_words, seperator, capitalize, random_lower_upper, vocabulary)
    st.session_state.memorable_result = m_password.generate()

st.image("../assets/password.jpg")
st.title("🔐 Password Generator")

col1, col2, col3 = st.columns(3)
col1.code(st.session_state.pin_result)
col2.code(st.session_state.random_result)
col3.code(st.session_state.memorable_result)

password_types = st.multiselect("Choose the type(s) of the password", ['PIN Code', 'Random Password', 'Memorable Password'])

p_gen, r_gen, m_gen = False, False, False

if 'PIN Code' in password_types:
    st.header('PIN Code')
    p_length = st.slider("PIN Length", 1, 50, 8)
    p_gen = True

if 'Random Password' in password_types:
    st.header('Random Password')
    r_length = st.slider("Password Length", 1, 50, 8)
    include_numbers = st.toggle("Include Numbers")
    include_symbols = st.toggle("Include Symbols")
    r_gen = True

if 'Memorable Password' in password_types:
    st.header('Memorable Password')
    number_of_words = st.slider("Number of Words", 1, 50, 4)
    seperator = st.text_input("Choose a Seperator", value= '-')
    capitalize = st.toggle("Capital Words")
    random_lower_upper = st.toggle("Random Upper-Lower Case")

    if st.toggle("Personal Words"):
        vocabulary = [i.strip() for i in st.text_input("Please enter your words.(Separate with ',')").split(',')]
    else:
        vocabulary = None
    m_gen = True

if st.button("Generate"):
    if p_gen:
        generate_pin(p_length)
    if r_gen:
        generate_random(r_length, include_numbers, include_symbols)
    if m_gen:
        generate_memorable(number_of_words, seperator, capitalize, random_lower_upper, vocabulary)
    st.rerun()

