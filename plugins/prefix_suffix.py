from pyrogram import Client, filters, enums
from helper.database import seximodbots


@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_caption(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Give The Prefix__\n\nExample:- `/set_prefix @sexi_mod`**")
    prefix = message.text.split(" ", 1)[1]
    sexi_mod = await message.reply_text("Please Wait ...")
    await seximodbots.set_prefix(message.from_user.id, prefix)
    await sexi_mod.edit("**Prefix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):

    sexi_mod = await message.reply_text("Please Wait ...")
    prefix = await seximodbots.get_prefix(message.from_user.id)
    if not prefix:
        return await sexi_mod.edit("**You Don't Have Any Prefix ❌**")
    await seximodbots.set_prefix(message.from_user.id, None)
    await sexi_mod.edit("**Prefix Deleted Successfully 🗑️**")


@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_caption(client, message):

    sexi_mod = await message.reply_text("Please Wait ...")
    prefix = await seximodbots.get_prefix(message.from_user.id)
    if prefix:
        await sexi_mod.edit(f"**Your Prefix :-**\n\n`{prefix}`")
    else:
        await sexi_mod.edit("**You Don't Have Any Prefix ❌**")


# SUFFIX
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_csuffix(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Give The Suffix__\n\nExample:- `/set_suffix @sexi_mod`**")
    suffix = message.text.split(" ", 1)[1]
    sexi_mod = await message.reply_text("Please Wait ...")
    await seximodbots.set_suffix(message.from_user.id, suffix)
    await sexi_mod.edit("**Suffix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):

    sexi_mod = await message.reply_text("Please Wait ...")
    suffix = await seximodbots.get_suffix(message.from_user.id)
    if not suffix:
        return await sexi_mod.edit("**You Don't Have Any Suffix ❌**")
    await seximodbots.set_suffix(message.from_user.id, None)
    await sexi_mod.edit("**Suffix Deleted Successfully ✅**")


@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_csuffix(client, message):

    sexi_mod = await message.reply_text("Please Wait ...")
    suffix = await seximodbots.get_suffix(message.from_user.id)
    if suffix:
        await sexi_mod.edit(f"**Your Suffix :-**\n\n`{suffix}`")
    else:
        await sexi_mod.edit("**You Don't Have Any Suffix ❌**")
       
      
     
    
   
   
