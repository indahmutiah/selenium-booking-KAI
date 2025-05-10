# Selenium Booking KAI

This repo automates the process of booking train tickets on the KAI (Kereta Api Indonesia) website using Selenium Python WebDriver. This usefull for testing or automating the booking process for train tickets.

## 🎯 Features

- Open the official KAI booking website: https://booking.kai.id/
- Select any origin and destination station
- Choose a national holiday (red dates on the calendar, excluding Saturdays and Sundays)
- Perform a search and simulate clicking the “Book” button (without completing the payment process)

## ⚙️ Tech Stack

1. Python 3.x
2. Selenium Python WebDriver
3. ChromeDriver (or any preferred browser driver)

## 🚀 How to Run

- Clone this repository.
- install the required packages using pip

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate.bat  # Windows
```

```bash
pip install selenium
```

- Run the script using python

```bash
python booking.py
```

📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
