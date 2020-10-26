# Among Us Discord Bot

This is an Among Us Discord bot that mutes and unmutes players with a single command, without anyone needing to mute themselves manually.

## Installation and setup

Please bare with the setup of this process, it will take a moment so make sure to follow each step carefully. <br />
Note: make sure you have python3 and pip3 already installed on your windows machine

1) Download the Among Us Bot [here](https://bit.ly/3kvgYnV)
2) Extract the files from zip.
3) Navigate to the extracted folder through your command prompt.
4) Create a `.env` file.
5) Add the following lines to `.env`.
    ```
    DISCORD_TOKEN={your-bot-token}
    DISCORD_GUILD={your-guild-token}
    ```
    >NOTE: Make sure remove the angular brackets after replacing with tokens.

    >*Refer to point 13 for more details* 
6) In your command prompt, type the following command.
    ```
    $ pipenv --three
    or
    $ pipenv --python 3.8
7) Spawns the shell within the virtualenv by typing the following command.
    ```
    $ pipenv shell
    ```
8) Once the shell has started, run the below command to install the packages.
    ```
    $ pipenv install
    ```
9) Go to https://discord.com/developers/applications and create a new application and add a new bot in the bot panel
10) Navigate to the Bot panel and enable `PRESENCE INTENT` and `SERVER MEMBERS INTENT
`
11) Navigate to the OAuth2 panel and in scopes, click bot. Then scroll down and choose "Mute members" and "Deafen members" or simply give "Adminstrator" as the permissions of the bot. Copy the link and paste it onto another tab and authorize this bot to your server
    >NOTE: Giving "Adminstrator" permission is a security risk in case somebody gets their hands on your bot token.  
12) Copy the bot token in the bot panel.
13) Go to the `.env` file and edit it. Change the `DISCORD_TOKEN` to your discord bot token and `GUILD_TOKEN` to the `client id` mentioned in General Information panel and save it.
    ```
    DISCORD_TOKEN=NzY5OTY3ODg1NTAyMTE5OTM3.X5WueQ.0L29H_6UN6_wTqm2zi-3lr7AA2c
    DISCORD_GUILD=829065885500510997
    ```
14) Now go to your command prompt and run `bot.py`
    ```
    $ python bot.py
    ``` 
14) To complete the setup, read the text below

# Set up discord server

The the bot will mute/unmute everyone in the same voice channel as the one who triggered the command.

1) Make sure the bot has come online.
2) Now type `.help` to get list of all the commands available.

>NOTE: When a member dies, they must type `.dead` in discord so they will be muted until the end of the game. Also someone can instead type `.kill @User1 @User2` instead so not everyone needs to type `.dead`