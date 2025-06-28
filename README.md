# THE SCHEDULER: Zoom & QuickTime Player Automation Bot

## Overview

**THE SCHEDULER** is an interactive Python automation tool for macOS that schedules and automates the process of recording and joining Zoom meetings using QuickTime Player. It leverages mouse and keyboard automation, time-based scheduling, and CSV-based configuration to handle repetitive meeting and recording tasks. The script is especially useful for students, teachers, and professionals who need to automate their online workflow.

---

## Features

- **Automated Screen Recording:** Starts and stops QuickTime Player screen recordings at scheduled times.
- **Automated Zoom Joining:** Joins Zoom meetings automatically using provided Meeting IDs and passwords.
- **Scheduling:** Supports both default (recurring) and custom (one-time) meeting/recording schedules.
- **Mouse Position Setup:** Interactive setup to record the mouse positions for various UI elements.
- **CSV-based Configuration:** Stores timings, meeting details, and mouse positions in CSV files for easy customization.
- **Interactive CLI:** Menu-driven interface for all major actions.
- **Multiple Modes:** Record only, join only, or both; supports multiple meetings per session.

---

## Requirements

- **Operating System:** macOS Catalina or later
- **Python:** Python 3.x (recommended: 3.8+)
- **Python Packages:**  
  - `pyautogui`  
  - `pandas`
- **Applications:**  
  - Zoom (installed in `/Applications/zoom.us.app`)
  - QuickTime Player (default on macOS)
- **Permissions:**  
  - Accessibility permissions for Python (for mouse/keyboard automation)
  - Screen recording permissions for Python and QuickTime Player

### Install Python Packages

```bash
pip3 install pyautogui pandas
```

### Grant Accessibility Permissions

1. Open **System Preferences** > **Security & Privacy** > **Privacy** tab.
2. Select **Accessibility** and **Screen Recording**.
3. Add your Terminal or Python IDE to both lists.

---

## Code Structure

```
.
├── main_script.py                # Main automation script (rename as needed)
├── tinpr.csv                    # Mouse setup timing for automation
├── renp.csv                     # Mouse positions for recording
├── menp.csv                     # Mouse positions for Zoom joining
├── eenp.csv                     # Mouse positions for ending recording
├── dctimings.csv                # Default schedule: start/end recording, number of meetings
├── dtimings.csv                 # Default meeting schedule: time, meeting ID, password
├── itimings.csv                 # Custom (input) meeting schedule
├── dqtimings.csv                # QuickTime recording start time (default)
├── dptimings.csv                # QuickTime recording end time (default)
├── dktimings.csv                # QuickTime start/end times (custom)
├── datimings.csv                # Join-only meeting schedule
└── (other CSVs as generated)
```

---

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Shiven78900/python.git
cd python
```

### 2. Prepare Your System

- Ensure Zoom and QuickTime Player are installed in their default locations.
- Install required Python packages (see above).
- Grant accessibility and screen recording permissions to your Terminal or IDE.

### 3. Run the Script

```bash
python3 main_script.py
```
*(Replace `main_script.py` with the actual filename.)*

### 4. Follow the Interactive Menu

You'll see a menu like:

```
THE SCHEDULER: Zoom and Quick Time Player Automation Bot
1. Delete the previous mouse inputs and/or add another
2. Delete the previous Default Inputs and input new default Time, Meeting ID and Password
3. Record zoom meeting and join the meeting automatically according to the default Time, Meeting ID and Password
4. Record and join the zoom meeting according to your input
5. Start screen Recording
6. End Screen Recording
7. Start and End Screen Recording
8. Join Meeting
9. ENTER ANOTHER OPTION
10. Exit
```

- Enter the number for your desired action.
- Follow prompts to set up mouse positions, schedules, meeting IDs, and passwords.
- The script will automate mouse/keyboard actions at the scheduled times.

### 5. CSV Files

- **Do not delete the CSV files** unless you want to reset your configuration.
- Each CSV stores either timings, meeting details, or mouse positions for automation.

---

## Brief Description

THE SCHEDULER is a robust, menu-driven Python automation tool for macOS that eliminates the hassle of manually starting/stopping recordings and joining Zoom meetings. By combining time scheduling, mouse/keyboard automation, and CSV-based configuration, it ensures you never miss a meeting or recording—ideal for remote workers, students, and teachers.

*For questions, improvements, or issues, please open an issue or pull request on the repository.*

---

## License

This project does not specify a license. Please contact the repository owner for clarification on usage and distribution rights.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to suggest improvements or report bugs.

## Contact

For questions or support, please open an issue on the GitHub repository.