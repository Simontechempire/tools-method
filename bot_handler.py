from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json
from modules.toolset import Toolset

with open('config/settings.json') as f:
    config = json.load(f)

tools = Toolset()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ("🚀 *DARKLORD COMMAND CENTER*\n\n"
            "/banwa [num] - Ban WhatsApp\n"
            "/bangwagroup [id] - Ban WA Group\n"
            "/bantiktok [user] - Ban TikTok\n"
            "/bantg [user] - Ban Telegram\n"
            "/ubanwa [num] - Unban WhatsApp\n"
            "/ubantg [user] - Unban Telegram\n"
            "/hack [target] - Session Hack\n"
            "/ddos [ip] - DDoS Attack\n"
            "/ipgrab [target] - IP Grabber\n"
            "/leak [target] - Data Leak\n")
    await update.message.reply_text(text, parse_mode="Markdown")

async def handle_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE, func):
    if update.effective_user.id != config['admin_id']: return
    target = context.args[0] if context.args else None
    if not target: 
        await update.message.reply_text("Target missing!")
        return
    await update.message.reply_text(f"Executing tool on {target}...")
    res = func(target)
    await update.message.reply_text(f"Result: {res}")

async def banwa(u, c): await handle_cmd(u, c, tools.tool_ban_wa)
async def bangwa(u, c): await handle_cmd(u, c, tools.tool_ban_wa_group)
async def bantiktok(u, c): await handle_cmd(u, c, tools.tool_ban_tiktok)
async def bantg(u, c): await handle_cmd(u, c, tools.tool_ban_tg)
async def ubanwa(u, c): await handle_cmd(u, c, tools.tool_uban_wa)
async def ubantg(u, c): await handle_cmd(u, c, tools.tool_uban_tg)
async def hack(u, c): await handle_cmd(u, c, tools.tool_hack_session)
async def ddos(u, c): await handle_cmd(u, c, tools.tool_dDoS)
async def ipgrab(u, c): await handle_cmd(u, c, tools.tool_ip_grab)
async def leak(u, c): await handle_cmd(u, c, tools.tool_leak_data)

if __name__ == '__main__':
    app = ApplicationBuilder().token(config['bot_token']).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("banwa", banwa))
    app.add_handler(CommandHandler("bangwagroup", bangwa))
    app.add_handler(CommandHandler("bantiktok", bantiktok))
    app.add_handler(CommandHandler("bantg", bantg))
    app.add_handler(CommandHandler("ubanwa", ubanwa))
    app.add_handler(CommandHandler("ubantg", ubantg))
    app.add_handler(CommandHandler("hack", hack))
    app.add_handler(CommandHandler("ddos", ddos))
    app.add_handler(CommandHandler("ipgrab", ipgrab))
    app.add_handler(CommandHandler("leak", leak))
    app.run_polling()
