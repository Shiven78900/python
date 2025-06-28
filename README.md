THE SCHEDULER: Zoom & QuickTime Player Automation Bot
Overview
THE SCHEDULER is an advanced Python automation tool for macOS that streamlines the process of recording and joining Zoom meetings using QuickTime Player. It leverages mouse automation, time scheduling, and CSV-based configuration to automate repetitive meeting tasks. The script is ideal for users who frequently record and join Zoom meetings and want to minimize manual intervention.

Features
Automates screen recording using QuickTime Player.

Automates joining Zoom meetings at scheduled times.

Supports scheduling multiple meetings with different IDs and passwords.

Customizable mouse input setup for various UI elements.

Interactive CLI menu for all major functions.

Stores and manages timings and meeting details using CSV files.

Requirements
Operating System: macOS Catalina or later

Python: Python 3.x (recommended: 3.8+)

Python Packages:

pyautogui

pandas

Applications:

Zoom (installed in /Applications/zoom.us.app)

QuickTime Player (default on macOS)

Permissions:

Accessibility permissions for Python (needed for mouse automation)

Screen recording permissions for Python and QuickTime Player

Install Required Python Packages
bash
pip3 install pyautogui pandas
Grant Accessibility Permissions
Open System Preferences > Security & Privacy > Privacy tab.

Select Accessibility from the sidebar.

Click the lock to make changes.

Add your Terminal or Python IDE to the list (e.g., Terminal, iTerm, PyCharm, VS Code).

Repeat for Screen Recording if needed.

Setup & Usage
1. Clone the Repository
bash
git clone https://github.com/Shiven78900/python.git
cd python
2. Prepare the Environment
Ensure Zoom and QuickTime Player are installed in their default locations.

Make sure you have the required Python packages installed (see above).

Run the script from Terminal or your preferred Python IDE.

3. Run the Script
bash
python3 <script_name>.py
Replace <script_name>.py with the actual filename.

4. Using THE SCHEDULER
Upon running, you'll see a menu like:

text
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
Choose an option by entering the corresponding number.

Follow the on-screen prompts to configure timings, meeting IDs, passwords, and mouse positions.

The script will automate mouse movements and keyboard input as required.

5. CSV Files
The script uses several CSV files to store timings, meeting details, and mouse positions:

tinpr.csv, renp.csv, menp.csv, eenp.csv: For mouse position and timing setup.

dctimings.csv, dtimings.csv, itimings.csv, etc.: For storing scheduled meeting and recording times.

Do not delete these files unless resetting the configuration.

How to Easily Implement on Your Mac
Install Python 3 and required packages.

Grant Accessibility and Screen Recording permissions to your Terminal or IDE.

Clone the repository and navigate into it.

Run the script and follow the interactive prompts.

Keep Zoom and QuickTime Player installed in their default locations.

Do not use the mouse/keyboard for other tasks while automation is running.

Brief Description
THE SCHEDULER is a robust automation solution for users who need to record and join Zoom meetings on a schedule. By combining Python automation, mouse/keyboard control, and CSV-based scheduling, it eliminates repetitive manual work and ensures you never miss a meeting or recording. The script is highly interactive and customizable, making it suitable for both power users and those new to automation.

For questions, improvements, or issues, please open an issue or pull request on the repository.
