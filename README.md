# Random Quote Generator
This is a Python-based application that fetches and displays random quotes. It includes a GUI with functionality to retrieve a new quote and an option to read the quote aloud using text-to-speech. 

## Instructions for Self-Deployment / Setup
### Dependencies
#### PyQt5
- Created by: Riverbank Computing in 1998
- Purpose: PyQt5 provides a toolkit for creating a GUI in Python, specifically designed to resemble a native app experience.
- How It Works: PyQt5 wraps Qt, a robust framework for GUI design, allowing Python to control the window, buttons, and display.

#### pyttsx3
- Created by: Peter Parente, later maintained by contributors
- Purpose: pyttsx3 provides text-to-speech capabilities, converting quote text into speech.
- How It Works: The library utilizes your system’s TTS (Text-to-Speech) engine to render quotes audibly.


### Understanding Python Versions and Compatibility
Recommended Python Version
- The ideal version for this project is Python 3.8.x, though it will work with Python versions 3.7 and above. Python 3.8, released on October 14, 2019, is optimized for performance and compatibility with external libraries.

Why Python 3.8?
Python 3.8 introduced improvements in:

- Assignment expressions (:=) to enhance code readability.
- Position-only parameters for improved function design.
- New math functions that improve computation in GUI-related applications.

> [!CAUTION]
> Ensure you avoid Python 2.x, which reached its end-of-life on January 1, 2020 and lacks compatibility with modern libraries used in this project.


### Installing Python and Setting Up Environment
Ensure Python 3.8+ is installed.

#### Windows:
- Download from the Python website.
- Run the installer and check “Add Python to PATH.”

#### MacOS:
Install Python using Homebrew (if you don’t have it installed, see below):

```
brew install python
```
> This command finds and installs Python from the Homebrew package repository. Homebrew automatically downloads and compiles the package for easy use on macOS, reducing dependency and compatibility issues often encountered with traditional manual installations.

The command brew install is used on macOS to install software packages via the Homebrew package manager, which simplifies installing and managing software. Homebrew was created in 2009 by Max Howell, aiming to bring Linux-style package management to macOS.

- `brew`: The primary command-line tool for Homebrew, which manages software installation, removal, and updates.
- `install`: Specifies the action to install a package.


#### Linux:
Most distributions come with Python pre-installed, but to upgrade or install:

```
sudo apt-get install python3
```
> This command locates and installs Python from the system's package repositories.

The command sudo apt-get install is a package management command used primarily on Debian-based Linux distributions (such as Ubuntu) to install software. It was created by Debian project contributors in the 1990s as part of the Advanced Packaging Tool (APT) system.

- `sudo`: Temporarily grants superuser (root) privileges, allowing the user to perform administrative tasks.
- `apt-get`: A command-line tool used to handle packages, including installation, updates, and removal.
- `install`: Specifies the action to install a package.

### Downloading the Project Files
#### Cloning or Downloading the Repository
There are two primary ways to download project files from GitHub: cloning the repository via Git and downloading the files as a ZIP archive. Both approaches allow you to obtain the full set of project files, but they serve different purposes and have distinct processes.

##### Option 1: Cloning the Repository Using Git
Git is a distributed version control system, created by Linus Torvalds in 2005, primarily for managing and tracking code changes in collaborative software projects. When you clone a repository with Git, you’re creating a local copy of all the project files and the entire commit history, including branches, tags, and version control metadata. This is particularly useful if you want to keep the repository updated or make contributions.

1. Ensure Git is Installed:
- macOS: Install Git using brew install git if Homebrew is installed.
- Linux: Use sudo apt-get install git (details on apt-get in prior steps).
- Windows: Download the installer from the Git official website.

2. Using the Git Clone Command:
```
git clone https://github.com/UMD-Mehdiyev/deployment-exercise.git
```
- `git`: The command-line interface for Git, enabling commands like cloning, committing, and pushing.
- `clone`: Copies an entire Git repository, including all files and version history, to your local system.
`https://github.com/UMD-Mehdiyev/deployment-exercise.git`: The URL for the remote GitHub repository. Git uses this URL to locate and download the repository files. 

3. What Cloning Does:
- Creates a directory named `deployment-exercise` on your local system.
- Adds a `.git` folder inside the directory, which stores the version history.
- Sets up a connection to the GitHub repository, so you can later pull updates or push changes if you have write access.

4. Git Advantages:
- Tracking Changes: Git tracks modifications, allowing you to revert to previous versions.
- Collaboration: When working on teams, Git enables multiple people to work on different branches and merge changes efficiently.
- Updating Your Local Repository: Use git pull to fetch and merge the latest changes from the GitHub repository without needing to re-download the whole repository.

##### Option 2: Downloading as a ZIP Archive
If you’re not interested in tracking version history or contributing to the repository and simply want to use the code, downloading a ZIP file might be easier and faster.

1. How to Download as a ZIP:

- Go to the repository's main page on GitHub.
- Click on the green "Code" button, then select "Download ZIP".
- This downloads the entire repository as a ZIP archive.

2. Extracting the ZIP:
Once downloaded, extract the ZIP file to a desired location on your computer:
- macOS: Double-click the file to extract.
- Linux: Use unzip (e.g., unzip deployment-exercise.zip).
- Windows: Right-click and select "Extract All."

3. Advantages of the ZIP Method:
- Quick Setup: No additional software is needed to access the project files.
- Lightweight: The ZIP file doesn’t contain Git history or metadata, so it takes up less space and is simpler if you don’t need version control.

4. Limitations of the ZIP Method:
- Static Snapshot: The ZIP file is a single snapshot of the repository at the time of download; it won’t receive updates or reflect any changes made to the repository afterward.
- No Commit History: Without Git, you won’t have access to the project’s commit history or branches.

> Both methods achieve the goal of downloading project files, but Git is typically preferred in software development for its flexibility, version control, and collaborative features. Choose the option that best suits your project needs!

### Installing Required Libraries and Explanation
#### Command Syntax
The `pip` command is Python’s package manager, created by The Python Packaging Authority in 2008, to facilitate easy installation of libraries.
```
pip install <package_name>
```

The command `pip install pyttsx3` installs the **pyttsx3** library. Each `pip install` command goes to Python’s official package repository, **PyPI (Python Package Index)**, and installs the latest version of the specified library.
```
pip install PyQt5 requests pyttsx3
```

#### Install Breakdown
- PyQt5: Adds GUI components to your environment.
- pyttsx3: Allows text-to-speech functionality.


### Running the Application: Detailed Commands
#### Opening a Terminal
- Windows: Open PowerShell or Command Prompt.
- MacOS: Open Terminal.
- Linux: Open Terminal with Ctrl+Alt+T.

#### Navigating to Project Directory
1. Open your terminal.
2. Use `cd` (change directory) to enter the folder:
```
cd path/to/deployment-exercise
```

#### Running the Application
Run the main script:
```
python app.py
```
> The python main.py command interprets and runs the main.py script, where the program is defined, including the GUI and all functionality.
