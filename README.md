# 🔏 passperclip
## 🔐 Password Generator

A simple Python script to generate secure 16-character passwords, copy them to the clipboard, and log them with a timestamp and website/app name. Ideal for creating unique passwords for various accounts while keeping a record for reference. 🚀

## ✨ Features

- ✅ Generates a 16-character password with a mix of uppercase letters, lowercase letters, digits, and special characters.
- 📋 Copies the password to the system clipboard for easy pasting.
- 📝 Logs each password with a timestamp and user-provided website/app name to `password_log.txt`.
- ⚡ Lightweight and easy to use from the command line.

## 🛠️ Requirements

- 🐍 Python 3.x
- 📦 `pyperclip` library (`pip install pyperclip`)

## 📥 Installation

1. **Clone the Repository** 📂:

   ```bash
   git clone https://github.com/spidbitx/passperclip.git
   cd passperclip
   ```

2. **Install Dependencies** ⚙️:

   ```bash
   pip install pyperclip
   ```

3. **Verify Python Installation** 🔍: Ensure Python 3 is installed by running:

   ```bash
   python --version
   ```

   or

   ```bash
   python3 --version
   ```

## 🚀 Usage

1. **Run the Script** ▶️:

   ```bash
   python passperclip.py
   ```

   or

   ```bash
   python3 passperclip.py
   ```

2. **Enter Website/App Name** ✍️: When prompted, input the website or app name (e.g., `Gmail`).

3. **Output** 📤:

   - The script generates a 16-character password (e.g., `K7@mP9#nL2$xQ8rT`).
   - The password is copied to the clipboard (paste with `Ctrl+V` or `Cmd+V`).
   - The password, timestamp, and website/app name are logged to `password_log.txt`.

4. **Example Log Entry** in `password_log.txt` 📜:

   ```
   2025-04-20 23:53:45 - Description: Gmail, Password: K7@mP9#nL2$xQ8rT
   ```

## ⚡ Boosting Productivity with This Script

To maximize productivity, integrate this script into your workflow with these best practices:

- 🔄 **Batch Password Updates**: Use the script to generate new passwords for multiple accounts in one session. The clipboard feature allows quick pasting into password fields, and the log file keeps all details organized.
- 🔒 **Secure Storage**: Move `password_log.txt` to a secure, encrypted location (e.g., a VeraCrypt container) after each session to protect sensitive data.
- 🖥️ **Alias for Quick Access**: Create a shell alias to run the script faster:
  - On Windows (PowerShell):

    ```powershell
    echo "Set-Alias passgen 'python $HOME\path\to\passperclip.py'" >> $PROFILE
    ```

  - On macOS/Linux (bash/zsh):

    ```bash
    echo "alias passgen='python3 ~/path/to/passperclip.py'" >> ~/.bashrc
    ```

    Then run `passgen` to launch the script.

- 🎯 **Desktop Shortcut with Keybinding**: Set up a desktop shortcut with a global keybinding (e.g., `Ctrl+Shift+P`) to launch the script from anywhere. This eliminates navigating to the script’s directory, making password generation instant. See the "Creating a Desktop Shortcut" section below for setup steps.
- 🔗 **Combine with Password Managers**: Use the generated passwords in a password manager like Bitwarden or 1Password. Paste the password from the clipboard and store the website/app name from the log for reference.
- 📅 **Regular Log Review**: Periodically review `password_log.txt` to ensure all accounts have unique passwords. Use the timestamp to track when passwords were created and plan updates (e.g., every 6 months).

## 🖼️ Creating a Desktop Shortcut (Windows)

To boost productivity, create a desktop shortcut for the script and bind it to `Ctrl+Shift+P` for instant access from anywhere on Windows.

### Steps to Create a Shortcut

1. **Locate the Script** 📍: Ensure `passperclip.py` is in a permanent location (e.g., `C:\Users\YourUsername\Documents\passperclip`).

2. **Create the Shortcut** 🛠️:

   - Right-click on the desktop and select **New > Shortcut**.
   - In the location field, enter:

     ```
     python "C:\path\to\passperclip.py"
     ```

     Replace `C:\path\to\passperclip.py` with the full path to the script. If Python is not in your PATH, use the full path to Python (e.g., `C:\Python39\python.exe`).

   - Click **Next**, name the shortcut `Password Generator`, and click **Finish**.

3. **Set the Keybinding** ⌨️:

   - Right-click the shortcut on the desktop and select **Properties**.
   - In the **Shortcut** tab, find the **Shortcut key** field.
   - Click in the field and press `Ctrl+Shift+P`. It should display `Ctrl + Shift + P`.
   - Click **Apply** and **OK**.

4. **(Optional) Set Working Directory** 🗂️:

   - In the shortcut’s **Properties**, set the **Start in** field to the script’s directory (e.g., `C:\Users\YourUsername\Documents\passperclip`) to ensure `password_log.txt` is created in the correct location.

### How It Works

- **After Setup**:

  - Press `Ctrl+Shift+P` from anywhere (e.g., browser, desktop, or another app).
  - A terminal window opens, running the script.
  - Enter the website/app name when prompted.
  - The 16-character password is generated, copied to the clipboard, and logged to `password_log.txt`.
  - Paste the password (e.g., `Ctrl+V`) into the desired password field.
  - The terminal displays the password and log confirmation, then stays open until you close it.

- **Productivity Benefit**:

  - The keybinding eliminates the need to navigate to the script or open a terminal manually.
  - Instant access speeds up password generation during account creation or updates.
  - The log file ensures you never lose track of generated passwords.

## ⚠️ Security Notes

- **Plain-Text Log**: `password_log.txt` stores passwords in plain text, which is insecure. Consider:

  - 🔐 Encrypting the log file using a library like `cryptography`.
  - 🔑 Storing passwords in a secure password manager instead of a log file.

- **Randomness**: The script uses Python’s `secrets` module for cryptographically secure password generation, ensuring high security for generated passwords. Example:

  ```python
  import secrets
  password = ''.join(secrets.choice(all_chars) for _ in range(16))
  ```

- **File Permissions**: Ensure `password_log.txt` is only accessible to your user account.

## 🤝 Contributing

Feel free to fork the repository, add features (e.g., GUI, encryption, cross-platform shortcuts), and submit pull requests. Issues and feature requests are welcome! 🌟
