"""Minimal Streamlit presentation; no persistence or external calls."""

import streamlit as st

from finance_tracker.config import ConfigurationError, load_configuration


st.set_page_config(page_title="Finance Tracker", page_icon="💰")
st.title("Finance Tracker")

try:
    configuration = load_configuration()
except ConfigurationError as error:
    st.error(str(error))
    st.stop()

for warning in configuration.warnings:
    st.warning(warning)

st.success("Local configuration is valid.")
st.write(
    f"Reporting currency: {configuration.reporting_currency} "
    f"(minor-unit scale: {configuration.minor_unit_scale})"
)
st.write("Gemini: disabled · Telegram: disabled")
st.info("Your local setup is ready. Financial tracking is not available in this version.")
