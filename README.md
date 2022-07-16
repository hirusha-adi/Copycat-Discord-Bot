# Copycat Discord Bot

this bot will repeat everything you say

# Setup

1. Install `python3`, `git` and a text editor (`nano`)

    ```bash
    sudo apt install python3 python3-pip git nano -y
    ```

2. clone the repo and cd into it / download the tarball with source code, extract, open a cosole in that working directory

    ```bash
    git clone "https://github.com/hirusha-adi/Copycat-Discord-Bot.git"
    cd ./Copycat-Discord-Bot
    ```

3. Install bot dependencies

    ```bash
    python3 -m pip install -r requirements.txt
    ```

4. Set the bot token

    ```bash
    nano token.key
    ```

    1. paste the token (Ctrl+Shift+V)
    2. save the file (Ctrl+S)
    3. exit (Ctrl+X)


5. Edit the `settings.json` to suite your needs

    ```json
    {
        "title": "CopyCat Bot",
        "repo": "https://github.com/hirusha-adi/Copycat-Discord-Bot",
        "prefix": "rb"
    }
    ```

    <table>
    <thead>
    <tr>
        <th>Key Name</th>
        <th>Data Type</th>
        <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>title</td>
        <td>string</td>
        <td>Name of the discord bot</td>
    </tr>
    <tr>
        <td>repo</td>
        <td>string</td>
        <td>Repository link / website link / bot link</td>
    </tr>
    <tr>
        <td>repo</td>
        <td>prefix</td>
        <td>Bot prefix</td>
    </tr>
    </tbody>
    </table>

    - the `settings.json` is already filled with some sample data, make sure to replce them to suite your needs

6. Start the discord bot
    ```bash
    python bot.py
    ```

# Available commands

### `help`

- display the bot help message (send an embed)

### `start`
- start repeating

### `stop`
- stop repeating

### `status`
- Current repeating status - `on`/`off`