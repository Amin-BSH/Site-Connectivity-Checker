# Website Availability Checker

## Overview

The **Website Availability Checker** is a Streamlit-based web application that allows users to check the availability of websites. Users can input URLs, and the app will verify whether the websites are reachable or not.

## Features

- Add multiple URLs to check their availability.
- Clear all added URLs with a single click.
- Display the status of each URL (reachable or not).
- User-friendly interface built with Streamlit.

## Requirements

To run this project, you need the following:

- Python 3.7 or higher
- The following Python libraries:
  - `streamlit`
  - `requests`

## Installation

1. Clone the repository or download the project files.

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   streamlit run src/app.py
   ```

2. Open the URL displayed in the terminal (usually `http://localhost:8501`) in your web browser.
3. Use the app to:
   - Enter a URL in the input field and click **Add URL**.
   - Click **Check Availability** to verify the status of the added URLs.
   - View the results in the **URLs** and **Status** columns.
   - Clear all URLs by clicking **Clear All URLs**.

## Project Structure

```
4.4_site_connectivity_checher/
│
├── Code/
│   ├── src/
│   │   ├── app.py          # Main application file
│   ├── README.md           # Project documentation
│   ├── requirements.txt    # List of dependencies
```

## Example

1. Enter a URL (e.g., `www.google.com`) and click **Add URL**.
2. Click **Check Availability** to see if the website is reachable.
3. The status will be displayed as:
   - ✅ for reachable websites.
   - ❌ for unreachable websites.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the user interface.
- Uses the [Requests](https://docs.python-requests.org/en/latest/) library for HTTP requests.
