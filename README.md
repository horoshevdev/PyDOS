# **PyDOS**  
_A playful MS-DOS parody written in Python!_

![PyDOS Preview](https://i.postimg.cc/DZMKGqy5/pydor.png)  

---

## **Available Commands**

Below is a list of commands you can use in PyDOS. Each command mimics classic MS-DOS functionality with a modern twist.

| **Command**   | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| `move`        | Move a folder, object, or file to a new location.                               |
| `delete`      | Delete a folder, object, or file.                                              |
| `notepad`     | Open the notepad application for text editing.                                 |
| `browser`     | Launch the browser to explore the web.                                         |
| `dir`         | Display all files and folders in the current directory.                        |
| `copy`        | Copy a file or folder to another location.                                     |
| `ipconfig`    | Retrieve network information, including IP address, gateway, and subnet mask.  |
| `finger`      | Get detailed information about users on the system.                            |
| `attrib`      | Change or view file attributes (e.g., read-only, hidden).                      |
| `cls`         | Clear the console screen for a fresh start.                                    |
| `cmd`         | Open the command prompt for advanced operations.                               |
| `rename`      | Rename a file or folder to a new name.                                         |


---

## **Example Usage (Example IP)**

```plaintext
C:\> ipconfig
IP Address: 192.168.1.10
Gateway: 192.168.1.1
Subnet Mask: 255.255.255.0
```

----
### ***Tested on:***
![Ubuntu](https://img.shields.io/badge/Ubuntu--informational?logo=Ubuntu&style=social&logoColor=ff7300&color=666666&labelColor=999999) 
![Windows](https://img.shields.io/badge/Windows--informational?logo=Wine&style=social&logoColor=000000&color=666666&labelColor=999999)
----

## Translation Example

```json
"en": {
        "welcome": "Welcome to PyDOS!",
        "prompt": "Enter a PyDOS command >>> ",
        "help": {
            "move": "move - Move a folder, object, or file.",
            "delete": "delete - Delete a folder, object, or file.",
            "notepad": "notepad - Opens Notepad.",
            "browser": "browser - Opens the browser.",
            "dir": "dir - Shows all files in the directory.",
            "copy": "copy - Copies a file to another location.",
            "ipconfig": "ipconfig - Retrieves the current IP address, gateway, and subnet.",
            "finger": "finger - Retrieves information about users.",
            "attrib": "attrib - Changes file attributes.",
            "cls": "cls - Clears the console screen.",
            "cmd": "cmd - Opens the command prompt.",
            "rename": "rename - Renames a file.",
        },
        "move": {
            "source": "Enter the file name to move: ",
            "current_dir": "Enter the current directory of the file: ",
            "target_dir": "Enter the target directory: ",
            "success": "File {} successfully moved to {}",
            "error_not_found": "Error: File or directory not found.",
            "error_permission": "Error: Insufficient permissions to move the file.",
        },
        "delete": {
            "path": "Enter the file path: ",
            "name": "Enter the file name: ",
            "success": "File successfully deleted.",
            "error_not_found": "File not found.",
        },
        "notepad": "Opening Notepad...",
        "browser": "Opening the browser...",
        "dir": "List of files in the current directory:",
        "copy": "Copying file...",
        "ipconfig": "Network information:",
        "finger": "Enter the username: ",
        "attrib": "Invalid ATTRIB command format. Allowed commands: '+r', '-r', '+h', '-h'.",
        "cls": "Clearing the screen...",
        "cmd": "Opening the command prompt...",
        "rename": {
            "old_name": "Enter the old file name: ",
            "new_name": "Enter the new file name: ",
            "success": "File {} successfully renamed to {}.",
            "error_not_found": "File not found.",
        },
```
