import requests
from datetime import datetime
import os
city = os.getenv("CITY", "Kochi")

def get_weather(city):
    """
    Fetch weather information from wttr.in
    """

    try:
        url = f"https://wttr.in/{city}?format=3"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.text

        return "Weather data unavailable."

    except Exception as e:
        return f"Weather Error: {e}"


def get_quote():
    """
    Fetch motivational quote
    """

    try:
        url = "https://zenquotes.io/api/random"

        response = requests.get(url, timeout=10)

        data = response.json()

        quote = data[0]["q"]
        author = data[0]["a"]

        return quote, author

    except Exception as e:
        return "Stay positive and keep learning.", "Daily Pulse Bot"


def generate_report(city):
    """
    Generate complete report
    """

    today = datetime.now().strftime("%d-%m-%Y")

    weather = get_weather(city)

    quote, author = get_quote()

    report = f"""
          DAILY PULSE REPORT
=========================================

Date: {today}

Weather Update
--------------
{weather}

Quote of the Day
----------------
"{quote}"

- {author}

=========================================
Generated Automatically by Daily Pulse Bot
"""

    return report


def save_report(report):
    """
    Save report to text file
    """

    with open(
        "daily_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)


def main():

    print("\nDAILY PULSE BOT\n")

    city = input(
        "Enter city name: "
    )

    report = generate_report(city)

    print(report)

    save_report(report)

    print(
        "\nReport saved as daily_report.txt"
    )


if __name__ == "__main__":
    main()
