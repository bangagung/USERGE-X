from pyrogram import Filters, CallbackQuery
from userge import userge, Message, Config
from userge.core.ext import RawClient
@userge.on_cmd("alive", about={
    'header': "Just For Fun"}, allow_channels=False)
async def alive_inline(message: Message):
    bot = await userge.bot.get_me()
    x = await userge.get_inline_bot_results(bot.username, "alive")
    await userge.send_inline_bot_result(chat_id=message.chat.id,
                                        query_id=x.query_id,
                                        result_id=x.results[1].id)
    await message.delete()

if Config.BOT_TOKEN and Config.OWNER_ID:
    if Config.HU_STRING_SESSION:
        ubot = userge.bot
    else:
        ubot = userge

    @ubot.on_callback_query(filters=Filters.regex(pattern=r"^settings_btn$"))
    async def alive_cb(_, callback_query: CallbackQuery):
        alive_settings=f"""
    🕔 Uptime : {userge.uptime}

    • 👥 𝗦𝘂𝗱𝗼 : {_parse_arg(Config.SUDO_ENABLED)}
    • 🚨 𝗔𝗻𝘁𝗶𝘀𝗽𝗮𝗺 : {_parse_arg(Config.ANTISPAM_SENTRY)}
    • ↕️ 𝗗𝘂𝗮𝗹 𝗠𝗼𝗱𝗲 : {_parse_arg(RawClient.DUAL_MODE)}
    • ➕ 𝗘𝘅𝘁𝗿𝗮 𝗣𝗹𝘂𝗴𝗶𝗻𝘀 : {_parse_arg(Config.LOAD_UNOFFICIAL_PLUGINS)}
    """
        await callback_query.answer(alive_settings, show_alert=True)

def _parse_arg(arg: bool) -> str:
    return " ✅ 𝙴𝚗𝚊𝚋𝚕𝚎𝚍" if arg else " ❌ 𝙳𝚒𝚜𝚊𝚋𝚕𝚎𝚍"     
