# Pomodoro Timer

A simple Pomodoro timer I built using Python and Tkinter. It helps me focus better by using work sessions and break sessions — all shown inside a small GUI app with a tomato graphic.

# What This App Does

Runs a 25-minute work timer

Automatically switches to:

5-minute short break

20-minute long break after 4 cycles

Shows checkmarks (✓) after each completed work session

Includes a Reset button to restart everything

Works through a clean and simple Tkinter interface

# How It Works

# Timer System

The app uses a cycle counter called reps:

Odd reps → Work session

Even reps → Short break

Every 8th rep → Long break

This repeats automatically.

# Countdown

The countdown updates every second using window.after().
When time reaches zero, it starts the next session on its own.

# Reset Button

Reset:

Stops the running timer

Clears all checkmarks

Sets the timer text back to 00:00

Resets cycles

# Features in the UI

Tomato timer image

"START" and "RESET" buttons

Large, readable time display

Checkmarks to show progress

Soft color theme (green, yellow, red, pink)

# Technologies I Used

Python

Tkinter

# Why I Built This

I built this project to practice Python GUI development and to make a simple tool that improves my focus.
It helped me learn:

how countdown timers work

how to manage repeated events

how to update UI elements dynamically

how to structure a full functional Tkinter app
