from pyrogram import Client, filters
from utils import check_user, multi_rec, getChannels

app = Client(
    "Deepika_Love_Bot",
    bot_token = "6144406425:AAGpo7qViUrsJsChanO0105XTO5wmu_YodM",
    api_id = 17038143,
    api_hash = "c1705f4cf711329ea025772dfd7057e0"
)



@app.on_message(filters.incoming & filters.command(['multirec']) & filters.incoming & filters.text)
def multirec_handler(app, message):

    auth_user = check_user(message)
    if auth_user is None:
        return

    if len(message.text.split()) < 3:
        message.reply_text("<b>Syntax: </b>`/multirec [channelName] [duration] | [filename]`")
        return

    multi_rec(app, message)

@app.on_message(filters.incoming & filters.command(['channels']) & filters.text)
def show_channels_handler(app, message):

    auth_user = check_user(message)
    if auth_user is None:
        return


    getChannels(app, message)


@app.on_message(filters.command(['start']) & filters.text)
def start_handler(app, message):

    if len(message.text.split()) < 3:
        message.reply_text("<b>A Telegram Top 1 Bot In India</b>")
        return
    # Don't remove Conan76 from here, Resepct the Developer...
    
app.run()
