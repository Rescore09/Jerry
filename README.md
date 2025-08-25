
# Jerry


## 📌 Overview

Jerry is a discord bot I build long ago with malicous intents of giving an easy way to steal minecraft sessions tokens. I have long since stopped, and decided to release the source to the public, I hope you do not use this for any malicous intents, However it has the malicious capabilities.

This bot is built on [`discord.py`](https://github.com/Rapptz/discord.py) and acts as a **build manager** inside Discord.  
It allows authorized users to:

- Control access via an **admin-only allowlist**
- Generate builds (currently malware stubs – should be replaced with safe builds)
- Log build history per user
- Upload build artifacts to remote services
- Provide a **modern Rich-based CLI dashboard** when the bot starts

While originally designed for unsafe purposes, the framework is highly reusable for enterprise-grade tooling. With minimal refactor, it can be turned into:

- ✅ CI/CD build trigger bot
- ✅ Deployment artifact uploader (AWS S3, Google Drive, etc.)
- ✅ Secure access-controlled tool distribution bot

---

## 🛠️ Features

- **Access Control**  
  Admins can add/remove users who are allowed to run `/build`.

- **Build Command**  
  Authorized users can trigger a build (currently compiles a malicious stub, but can be reworked to trigger a real build system).

- **Build Logging**  
  Logs each build to a JSON file for accountability.

- **Upload Handling**  
  Uses `aiohttp` to upload artifacts to external file hosts (replace with enterprise storage).

- **Error Handling & Embeds**  
  All errors and outputs are returned as rich Discord embeds for clarity.

- **CLI Dashboard**  
  On startup, the bot shows a styled dashboard using `rich` with status messages and progress bars.

---

## 🚀 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/rescore09/jerry/
   cd repo
   ```
2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Core dependencies:

   * `discord.py`
   * `aiohttp`
   * `rich`
   * `colorama`
   * `cryptography`

3. **Configure the bot**

   * Set your Discord bot token in the source (replace placeholder in `bot.run("TOKEN")`).

4. **Run the bot**

   ```bash
   python main.py
   ```


## Task list
This project was made some time ago and was kept private. I have decided to release it as a way to educate others on how to create a discord bot that builds malware and returns the original. This project was built on the  [`Nyx Builder`](https://github.com/rescore09/nyx) project. The discord bot's source code is a direct 1:1 with it's logic with some updates. I have plans to update this along with its source. Here are the short term plans:
 
* Implement a proper encryption for the `source.py`
* Rewrite the `main.py` to use cogs as a way to organize files efficently.
* Replace the `allowed.rsc` and the `blacklisted.rsc` with a proper `users.db`.
* Currently the `source.py` only extracts Minecraft Session Tokens if any instance of minecraft or a modified client is running. However, I plan on adding a system that works without the presence of a minecraft instance.
* Improve build times for faster responses
* Replace all requests in `source.py` that use `requests` library with a custom undetectable one.

## ⚠️ Legal & Ethical Warning

* Do **not** use this bot to build or distribute malware.
* This project should only be used as a **learning resource** for Discord bot development and DevOps automation.
* The maintainer of this repository are **not responsible** for misuse.

---

## 📚 License

This project is under the protection of the MIT License, You are allowed to install and distribute this. However, claiming this as your own will be an act of dishonering the License.