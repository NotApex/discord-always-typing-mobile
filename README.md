# discord-always-typing-mobile
Makes you always show as typing in a specific discord channel this is for termux btw
video tut https://youtu.be/IjP-v2wfEhE

# how to setup
```bash
git clone https://github.com/NotApex/discord-always-typing-mobile/
```

```bash
pip install requests
```

```bash
python main.py
```
# how to get your discord token
On pc you need to go to the discord website once the website is loaded you need to type 
```bash
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```
now on mobile it's a bit different you need to download [Kiwi browser](https://play.google.com/store/apps/details?id=com.kiwibrowser.browser) once you have downloaded Kiwi browser go to discord.com and click the 3 dots in the top right corner scroll down till you see desktop site and click it then login to your discord account once you login click the 3 dots scroll down all the way and click Developer tools once the dev tools open swipe to the right to get to the dev tools tab at the top click the 2 arrows then click Console then paste this in
```bash
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```
copy the token and the id of the channel you want to always type in and start the script
