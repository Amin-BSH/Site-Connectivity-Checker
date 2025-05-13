import concurrent.futures
import time
from typing import List

import requests
import streamlit as st


def format_url(url: str) -> str:
    """
    Formats a given URL to ensure it starts with 'https://www.'.

    :param url: The URL to format.
    :return: The formatted URL.
    """
    if url.startswith("http://"):
        url = url[len("http://") :]

    if url.startswith("https://"):
        url = url[len("https://") :]

    if url.startswith("www."):
        url = url[len("www.") :]

    url = "https://www." + url

    return url


def check_site_connectivity(url: str) -> bool:
    """
    Checks the connectivity of a given website.

    :param url: The URL of the website to check.
    :return: True if the website is reachable, False otherwise.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }
        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False


def alert_message(message: str, timer: int = False) -> None:
    """
    Displays a warning message in the Streamlit app.

    :param message: The message to display.
    :param timer: The duration (in seconds) to display the message. If False, the message persists.
    :type timer: int or bool
    """
    alert = st.warning(f"{message}")
    if timer:
        time.sleep(timer)
        alert.empty()


def main() -> None:
    """
    The main function to run the Streamlit app for checking website availability.

    """
    st.title(":zap: Website Availability Checker")

    if "urls" not in st.session_state:
        st.session_state.urls: List[str] = []

    url = st.text_input(label="Enter a url:", placeholder="For example: www.google.com")
    url = format_url(url=url)

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button(label="Add url", use_container_width=True):
            if url and url not in st.session_state.urls:
                st.session_state.urls.append(url)
            else:
                alert_message("URL IS NOT VALID or YOU HAVE ALREADY ADDED!", timer=3)

    with col2:
        if st.button(label="Clear all urls", use_container_width=True):
            st.session_state.urls = []

    if st.button(label="Check Availability", use_container_width=True):
        if st.session_state.urls:
            for idx, url in enumerate(st.session_state.urls):
                with st.spinner(f"Checking {url}"):
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        futures = {executor.submit(check_site_connectivity, url): idx}

                for future in concurrent.futures.as_completed(futures):
                    idx = futures[future]
                    st.session_state[f"status_{idx}"] = future.result()

        else:
            alert_message("First Enter a URL", timer=3)

    if st.session_state.urls:
        col1, col2 = st.columns([1, 1], vertical_alignment="center")
        with col1:
            st.subheader("URLs")
            for idx, i in enumerate(st.session_state.urls):
                st.write(i)

        with col2:
            st.subheader("Status")
            for idx, url in enumerate(st.session_state.urls):
                if st.session_state.get(f"status_{idx}") is True:
                    st.write(":white_check_mark:")
                elif st.session_state.get(f"status_{idx}") is False:
                    st.write(":x:")
                else:
                    st.write("")
    else:
        alert_message("Please Enter a Url")


main()
