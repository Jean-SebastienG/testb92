import streamlit as st
from streamlit.testing.v1 import AppTest

def test_title():
    # Create an instance of AppTest
    at = AppTest.from_file("app.py")

    # Run the app
    at.run(timeout=10)

    # Check if the title is correct
    assert at.title[0].value == "Car Sales Data analysis"

