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

