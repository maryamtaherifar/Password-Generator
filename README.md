# 🔐 Password Generator

A simple yet powerful password generator that creates three types of passwords:

- PIN Code – numeric passwords

- Random Password – secure random strings

- Memorable Password – human-friendly word-based passwords

This project includes both a terminal version and an interactive GUI built with Streamlit.
---
## 🚀 How to Run

There are **two ways** to run:

---

### ✅ 1. Terminal Mode

1. Clone this repository and navigate into the project folder.
2. Install dependencies:
   ```bash
   pip install -r requirements1.txt
   ```
3. Run the game:
    ```bash
    python main.py
    ```

### ✅ 2. Web GUI Mode (Streamlit)

1. Clone this repository and navigate into the project folder.

2. Install dependencies:
    ```bash
    pip install -r requirements2.txt
    ```
3. Run the game with Streamlit:
    ```bash
    streamlit run GUI_main.py
    ```
---

## 🧰 Features

1️⃣ PIN Code

Generates numeric passwords of any length.

Example output: 49382016

2️⃣ Random Password

Customizable inclusion of numbers and symbols.

Example output: gH8#lpT1

3️⃣ Memorable Password

Generates word-based passwords that are easy to remember.

Custom options:

- Number of words

- Separator (-, _, etc.)

- Capitalized words

- Randomized letter case

- Custom vocabulary input

Example output: happy-BIRD-ocean-CLOUD

---
## 🗂️ Project Structure

```bash
Password-Generator/
│
├── src/
│   ├── main.py          # Core logic (password generation classes) and Terminal version
│   ├── GUI_main.py      # Web GUI version using Streamlit
│
├── README.md
├── requirements1.txt    # Dependencies for terminal version
├── requirements2.txt    # Dependencies for GUI version
```
