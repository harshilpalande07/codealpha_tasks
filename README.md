
---

# 🤖 TASK 1: AI Voice Chatbot System

## 📌 Description
This project is an AI-powered chatbot that:
- Responds to user messages in real-time
- Uses local AI model (Ollama)
- Supports voice output using Windows SAPI engine
- Includes smart responses (jokes, quotes, time, greetings)

## ⚙️ Features
- 💬 Real-time AI conversation
- 🎤 Voice output using system speech engine
- 🧠 Context-aware responses
- 😂 Programming jokes generator
- ⏰ Time & date awareness

## 🧠 Working
1. User enters input in terminal
2. Input is processed through conditional logic
3. If no rule matches → AI model (Ollama) generates response
4. Output is displayed + spoken using voice engine

---

# 📂 TASK 2: File Automation System

## 📌 Description
This project automatically organizes image files from a folder into a structured directory.

## ⚙️ Features
- 📁 Scans a folder for image files
- 🖼 Supports multiple formats (.png, .jpg, .jpeg, .gif, .webp, etc.)
- 🚚 Automatically moves files to destination folder
- 📊 Shows real-time status updates

## 🧠 Working
1. Script scans source directory
2. Checks file extensions
3. Matches supported image formats
4. Moves files into organized folder
5. Displays success/failure logs

---

# 📊 TASK 3: Stock Portfolio Tracker

## 📌 Description
A real-time stock tracking system using Yahoo Finance API.

## ⚙️ Features
- 📈 Live stock price updates
- 💰 Portfolio management system
- 📊 Asset valuation calculation
- 💾 Export portfolio to CSV file

## 🧠 Working
1. User enters stock symbols and quantity
2. System fetches live prices using `yfinance`
3. Calculates total portfolio value
4. Displays formatted financial report
5. Optionally exports data into CSV file

---

# 🧰 REQUIREMENTS

Install all dependencies using:

```bash
pip install ollama pywin32 yfinance
