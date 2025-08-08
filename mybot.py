#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from telegram import *
from telegram.ext import *
import random
import time
from tinydb import *
<<<<<<< HEAD

=======
import copy
import re
>>>>>>> 0f7a004 (Initial commit)
updater = Updater('8192198859:AAFlFmKDANGsM51kfdAoAYdaBoJjrfDqFXo', use_context=True)
dispatcher = updater.dispatcher

db = TinyDB('players.json')
UserQuery = Query()
<<<<<<< HEAD

=======
#init_user
>>>>>>> 0f7a004 (Initial commit)
def init_user(update,context):
    user_id = update.effective_user.id
    username = update.effective_user.username or update.effective_user.first_name
    user_info = db.get(UserQuery.user_id == user_id)
    
    if user_info is None:
        user_info = {
        'user_id': user_id,
        'username': username,
        'level': 1,
        'xp': 0,
<<<<<<< HEAD
        'Coins': 500,
        'Essences': 0,
        'Moonshards': 0,
=======
        'coins': 1000,
        'essences': 0,
        'moonshards': 0,
>>>>>>> 0f7a004 (Initial commit)
        'max_xp': 100,
        'battles_played': 0,
        'explores_won': 0,
        'explores_lost': 0,
<<<<<<< HEAD
        'power': 50,
        'max_hp': 100,
        'hp': 100,
        'battles_played':0,
        'battles_won':0,
        'battles_lost':0
         }
        db.insert(user_info)
        
    
    else:
        user_info.setdefault('user_id', user_id)
        user_info.setdefault('username',username)
        user_info.setdefault('level', 1)
        user_info.setdefault('xp', 0)
        user_info.setdefault('Coins', 500)
        user_info.setdefault('Essences', 0)
        user_info.setdefault('Moonshards', 0)
        user_info.setdefault('max_xp', 100)
        user_info.setdefault('explores_played', 0)
        user_info.setdefault('explores_won', 0)
        user_info.setdefault('explores_lost', 0)
        user_info.setdefault('power', 50)
        user_info.setdefault('max_hp', 100)
        user_info.setdefault('hp', 100)
        user_info.setdefault('battles_played', 0)
        user_info.setdefault('battles_won', 0)
        user_info.setdefault('battles_lost', 0)
    
        
    return user_info 
    context.user_data.update(user_info)
        
        
monster_db = {
    'lasher': {'hp': 300, 'dmg': 100},
    'slayer': {'hp': 250, 'dmg': 120},
    'gloam': {'hp': 480, 'dmg': 130},
    'razorbeak': {'hp': 100, 'dmg': 90},
    'blightborn': {'hp': 150, 'dmg': 140},
    'shadefang': {'hp': 170, 'dmg': 150},
    'duskmaw': {'hp': 600, 'dmg': 160},
    'hollowroot': {'hp': 660, 'dmg': 170},
    'vilethorn': {'hp': 720, 'dmg': 180},
    'embergut': {'hp': 780, 'dmg': 190},
    'doomcaller': {'hp': 230, 'dmg': 200},
    'rotclaw': {'hp': 200, 'dmg': 210},
    'ashen_wyrm': {'hp': 870, 'dmg': 205},
    'blackvein': {'hp': 190, 'dmg': 195},
    'soulgnaw': {'hp': 750, 'dmg': 185}
}  
     
     

def save_user_data(user_info):
    
    db.upsert(user_info, UserQuery.user_id == user_info['user_id'])
    
ADMINS = [ 6590055256 ,]  # Replace with real Telegram user IDs

=======
        'explores_played':0,
        'power': 50,
        'max_power':50,
        'max_hp': 100,
        'hp': 100,
        'agility':200,
        'max_agility':200,
        'battles_played':0,
        'battles_won':0,
        'battles_lost':0,
        'user_weapons':{},
        'equiped_weapon':None,
         }
    db.upsert(user_info, UserQuery.user_id == user_id)
        
    return user_info 
    context.user_data.update(user_info)

def add_field_to_all_users(field_name, default_value):
    for user in db.all():
        if field_name not in user:
            db.update({field_name: default_value}, UserQuery.user_id == user['user_id'])
 #monster_db       
add_field_to_all_users('magical_items',[])
add_field_to_all_users('explores_played',0)
monster_db = {
    'lasher': {
        'hp': 100, 'dmg': 100, 'agility': 300,
        'photo': "AgACAgUAAxkBAAINfmiV-8k3XKyDaBEh2IpWWyv-Pk0qAAKXxjEbdoyxVEdHn_YxLf4pAQADAgADeQADNgQ"
    },
    'slayer': {
        'hp': 80, 'dmg': 80, 'agility': 260,
        'photo': "AgACAgUAAxkBAAINf2iV-8kXZj7um1j_sZBco8BWji03AAKYxjEbdoyxVAxhQ1-X5-AhAQADAgADeQADNgQ"
    },
    'gloam': {
        'hp': 75, 'dmg': 95, 'agility': 210,
        'photo': "AgACAgUAAxkBAAINgGiV-8nQxkd2bUwJecopBB6iXYoDAAKZxjEbdoyxVLuVEDkg189iAQADAgADeQADNgQ"
    },
    'razorbeak': {
        'hp': 50, 'dmg': 90, 'agility': 240,
        'photo': "AgACAgUAAxkBAAINgWiV-8lElhjVKwPmCjVmh5lMg345AAKaxjEbdoyxVF1wBfcmGhN3AQADAgADeAADNgQ"
    },
    'blightborn': {
        'hp': 30, 'dmg': 40, 'agility': 100,
        'photo': "AgACAgUAAxkBAAINgmiV-8mSo4DBhhjPhGJXrQie0nJ8AAKbxjEbdoyxVPAm76E_YObYAQADAgADeQADNgQ"
    },
    'shadefang': {
        'hp': 40, 'dmg': 50, 'agility': 170,
        'photo': "AgACAgUAAxkBAAINg2iV-8l1BwvKyjCL4L7tKROpIMvqAAKexjEbdoyxVBvB4eUZo6KKAQADAgADeQADNgQ"
    },
    'duskmaw': {
        'hp': 60, 'dmg': 60, 'agility': 155,
        'photo': "AgACAgUAAxkBAAINhGiV-8kAAeytiXeU21wRv5xa_-n1HgACn8YxG3aMsVTgRAgO89dufgEAAwIAA3kAAzYE"
    },
    'hollowroot': {
        'hp': 65, 'dmg': 70, 'agility': 150,
        'photo': "AgACAgUAAxkBAAINhWiV-8nALq4cH4ltO8zZr1GKXogHAAKgxjEbdoyxVBPCqXnhr2k_AQADAgADeAADNgQ"
    },
    'vilethorn': {
        'hp': 70, 'dmg': 80, 'agility': 165,
        'photo': "AgACAgUAAxkBAAINhmiV-8lcxBmij39Ut0N7WbuICwbVAAKhxjEbdoyxVBTBrYof85srAQADAgADeQADNgQ"
    },
    'embergut': {
        'hp': 85, 'dmg': 75, 'agility': 175,
        'photo': "AgACAgUAAxkBAAINh2iV-8nOKrlknIfAgPeLpJyG5WQAA6TGMRt2jLFUjjODUhhGY9cBAAMCAAN5AAM2BA"
    },
    'doomcaller': {
        'hp': 90, 'dmg': 35, 'agility': 170,
        'photo': "AgACAgUAAxkBAAINiGiV-8nwXWbRGvL0Vln4fYZJxjVhAAKlxjEbdoyxVHP_wG3Tc-qwAQADAgADeQADNgQ"
    },
    'rotclaw': {
        'hp': 30, 'dmg': 20, 'agility': 135,
        'photo': "AgACAgUAAxkBAAINiWiV-8m_p_K_lyWFQUrxT_DAt55YAAKmxjEbdoyxVKBT_bN8PPphAQADAgADeAADNgQ"
    },
    'ashen_wyrm': {
        'hp': 95, 'dmg': 25, 'agility': 160,
        'photo': "AgACAgUAAxkBAAINimiV-8kobB-FsztMEEoLPXLIpuU_AAKnxjEbdoyxVC64FTmHN2xQAQADAgADeAADNgQ"
    },
    'blackvein': {
        'hp': 65, 'dmg': 35, 'agility': 130,
        'photo': "AgACAgUAAxkBAAINi2iV-8nxncjEJAYjHH-Srv1Eid0uAAKoxjEbdoyxVOWvG8_fEMOfAQADAgADeAADNgQ"
    },
    'soulgnaw': {
        'hp': 60, 'dmg': 30, 'agility': 125,
        'photo': "AgACAgUAAxkBAAINjGiV-8ndgtf5IKqnKgfCKm5f7w_nAAKpxjEbdoyxVFDClP7XytlEAQADAgADeQADNgQ"
    },
    'thornfiend': {
        'hp': 55, 'dmg': 65, 'agility': 145,
        'photo': "AgACAgUAAxkBAAINjWiV-8mdsoO7e6pCATXudUAYSn_lAAKqxjEbdoyxVHQiW9zfwJvYAQADAgADeAADNgQ"
    },
    'voidlurker': {
        'hp': 100, 'dmg': 110, 'agility': 195,
        'photo': "AgACAgUAAxkBAAINjmiV-8m9tSa6z9gr4yB9Xg92St_WAAKsxjEbdoyxVA7TtZyIF4GXAQADAgADeQADNgQ"
    },
    'nethermaw': {
        'hp': 120, 'dmg': 85, 'agility': 185,
        'photo': "AgACAgUAAxkBAAINj2iV-8kGpxysKWBZYJkAAVvuGt0qnQACrcYxG3aMsVSeRKlUTIREewEAAwIAA3gAAzYE"
    },
    'cragjaw': {
        'hp': 80, 'dmg': 45, 'agility': 115,
        'photo': "AgACAgUAAxkBAAINkGiV-8ntOsj6T6DG7IgUG5vGQ8MjAAKuxjEbdoyxVAE7aSVD2V2XAQADAgADeQADNgQ"
    },
    'stormhide': {
        'hp': 90, 'dmg': 95, 'agility': 200,
        'photo': "AgACAgUAAxkBAAINkWiV-8kLxR9TyhJJMovs7RVH9jKcAAKwxjEbdoyxVL6AgFWi5JSOAQADAgADeAADNgQ"
    },
    'skyripper': {
        'hp': 120, 'dmg': 60, 'agility': 200,
        'photo': "AgACAgUAAxkBAAINkmiV-8n5UCPhLD4VtOyhHyIm4FHjAAKyxjEbdoyxVJIsS33zoo-wAQADAgADeQADNgQ"
    },
    'deathbloom': {
        'hp': 110, 'dmg': 75, 'agility': 210,
        'photo': "AgACAgUAAxkBAAINk2iV-8lIEi635A6ilNIfA79RUcnnAAKzxjEbdoyxVAuBViFY2YbqAQADAgADeAADNgQ"
    },
    'pyrelord': {
        'hp': 110, 'dmg': 120, 'agility': 240,
        'photo': "AgACAgUAAxkBAAINlGiV-8mbOejOOtA56mV39tfxLyheAAK1xjEbdoyxVO2RCH7tETBCAQADAgADeQADNgQ"
    },
    'glarefang': {
        'hp': 80, 'dmg': 100, 'agility': 420,
        'photo': "AgACAgUAAxkBAAINlWiV-8ljphR7pzWTtFIi8u8GRCnXAAK4xjEbdoyxVMIp2AGB2zKbAQADAgADeAADNgQ"
    },
    'timbergnash': {
        'hp': 240, 'dmg': 55, 'agility': 300,
        'photo': "AgACAgUAAxkBAAINlmiV-8neiS7joBQpHVdVr64FY-kuAAK5xjEbdoyxVCfLYl6YKDXaAQADAgADeQADNgQ"
    }
}
     
weapon_list = {
    'Bronze Sword': {
        'name': 'Bronze Sword',
        'bonus_power': 10,
        'bonus_hp': 5,
        'price': 1,
        'rarity': 'Common',
        'bonus_agility': 50,
        'weapon_level': 1,
        'weapon_xp': 0,
        'weapon_max_xp': 150,
        'photo':"AgACAgUAAxkBAAINR2iV5xqtiKk7dUCyX_Fe-g7m5_6DAAKmyjEbsDKwVPy0UV1aOCAXAQADAgADeQADNgQ"
    },
    'Iron Blade': {
        'name': 'Iron Blade',
        'bonus_power': 20,
        'bonus_hp': 15,
        'price': 5,
        'rarity': 'Common',
        'bonus_agility': 75,
        'weapon_level': 1,
        'weapon_xp': 0,
        'weapon_max_xp': 150,
        'photo':"AgACAgUAAxkBAAINQ2iV5xWGX5YHGPSAbkS68hVlrsv2AAKqyjEbsDKwVAoh22qI3RGlAQADAgADeQADNgQ"
    },
    'Crystal Lance': {
        'name': 'Crystal Lance',
        'bonus_power': 30,
        'bonus_hp': 20,
        'price': 10,
        'rarity': 'Uncommon',
        'bonus_agility': 100,
        'weapon_level': 1,
        'weapon_xp': 0,
        'weapon_max_xp': 150,
        'photo':"AgACAgUAAxkBAAINQWiV5xOqqIqJCpsX9dG3hN2AOncGAAKoyjEbsDKwVA9o3H25EL4aAQADAgADeQADNgQ"
    },
    'Void Edge': {
        'name': 'Void Edge',
        'bonus_power': 50,
        'bonus_hp': 40,
        'price': 20,
        'rarity': 'Rare',
        'bonus_agility': 200,
        'weapon_level': 1,
        'weapon_xp': 0,
        'weapon_max_xp': 150,
        'photo':"AgACAgUAAxkBAAINRWiV5xgjov4p49ex0UOUD40-MJErAAKpyjEbsDKwVPTgPUSRux_yAQADAgADeAADNgQ"
    }
}
#save_user_data
def save_user_data(user_info):
    
    if user_info['coins'] <= 0:
      user_info['coins'] = 0
    db.upsert(user_info, UserQuery.user_id == user_info['user_id'])
    
    
ADMINS = [ 6590055256 ,]  # Replace with real Telegram user IDs
#reset_all
>>>>>>> 0f7a004 (Initial commit)
def reset_all(update, context):
    user_id = update.effective_user.id

    if user_id not in ADMINS:
        update.message.reply_text("❌ You are not authorized to use this command.")
        return

    db.truncate()
    update.message.reply_text("✅ All user data has been reset.")    
<<<<<<< HEAD
  

=======


def escape_markdown(text: str) -> str:
    return re.sub(r'([_*\[\]()~`>#+\-=|{}.!])', r'\\\1', text) 
    
#reset_user
>>>>>>> 0f7a004 (Initial commit)
def reset_user(update, context):
    if update.effective_user.id not in ADMINS:
        update.message.reply_text('❌ You are not authorized to use this command.')
        return

    if not context.args:
        update.message.reply_text("⚠️ Please give a user ID.\nExample: `/reset_user 123456789`", parse_mode='Markdown')
        return

    try:
        user_id = int(context.args[0])  # convert to int

        # ✅ Check if user exists
        if db.search(UserQuery.user_id == user_id):
            db.remove(UserQuery.user_id == user_id)
            update.message.reply_text(f"✅ User `{user_id}` has been removed!", parse_mode='Markdown')
        else:
            update.message.reply_text("⚠️ User not found in database.")
    
    except Exception as e:
        update.message.reply_text(f"❌ Invalid ID! Error: `{e}`", parse_mode='Markdown')
<<<<<<< HEAD
            
=======
 #xp           
>>>>>>> 0f7a004 (Initial commit)
def xp_system(update,context):
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
<<<<<<< HEAD
    
    if int(user_info['max_xp']) <= int(user_info['xp']):
        user_info['xp'] -= user_info['max_xp']
        user_info['level'] += 1
        user_info['max_xp'] += 100*user_info['level']
        user_info['max_hp'] += 20*user_info['level']
        user_info['power'] += 10*user_info['level']
        save_user_data(user_info)
        chat_id = update.effective_chat.id
        update.bot.send_message(chat_id = chat_id , text = 'Congratulations! you leveled up')
    
=======
    leveled_up = False
    # Add earned XP before this check
    while user_info['xp'] >= user_info['max_xp']:
      user_info['xp'] = user_info['xp'] - user_info['max_xp']  # Explicit subtraction
      user_info['level'] += 1
      user_info['max_xp'] += 50 * user_info['level']
      user_info['hp'] += 10 * user_info['level']
      user_info['power'] += 5 * user_info['level']
      user_info['agility'] += 20 * user_info['level']
      leveled_up = True
      save_user_data(user_info)

    if leveled_up:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"""🌟 Level Up! 🌟  
Congratulations, brave adventurer!
    
🧍 You’ve reached <b>Level {user_info['level']}</b>!  
Keep exploring, battling, and rising to greatness!"""
        , parse_mode = ParseMode.HTML)
      
    save_user_data(user_info)
    
def weapon_xp_system(update,context):
  user_id = update.effective_user.id
  user_info = init_user(update,context)
  user_data = context.user_data
   
  user_info['user_weapons'][user_info['equiped_weapon']]['weapon_xp'] += 30
    
  if user_info['user_weapons'][user_info['equiped_weapon']]['weapon_xp'] >= user_info['user_weapons'][user_info['equiped_weapon']]['weapon_max_xp']:
    user_info['user_weapons'][user_info['equiped_weapon']]['weapon_xp'] -= user_info['user_weapons'][user_info['equiped_weapon']]['weapon_max_xp']
    user_info['user_weapons'][user_info['equiped_weapon']]['weapon_level'] += 1
    user_info['user_weapons'][user_info['equiped_weapon']]['weapon_max_xp'] += 50*user_info['user_weapons'][user_info['equiped_weapon']]['weapon_level']
    user_info['user_weapons'][user_info['equiped_weapon']]['bonus_hp'] += 10*user_info['user_weapons'][user_info['equiped_weapon']]['weapon_level']
    user_info['user_weapons'][user_info['equiped_weapon']]['bonus_power'] += 5*user_info['user_weapons'][user_info['equiped_weapon']]['weapon_level']
    user_info['user_weapons'][user_info['equiped_weapon']]['bonus_agility'] += 20*user_info['user_weapons'][user_info['equiped_weapon']]['weapon_level']
    
    
    
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id = chat_id , text = f'''⚔️✨ Your weapon has leveled up! ✨⚔️

🔹 <b>Name:</b> {user_info['equiped_weapon']}  
🔹 <b>New Level:</b> {user_info['user_weapons'][user_info['equiped_weapon']]['weapon_level']}
🔹 <b>Weapon XP:</b> {user_info['user_weapons'][user_info['equiped_weapon']]['weapon_xp']} / {user_info['user_weapons'][user_info['equiped_weapon']]['weapon_max_xp']}

🔥 Keep battling to make it even stronger!''',
parse_mode = ParseMode.HTML)

  save_user_data(user_info)
  
#start    
>>>>>>> 0f7a004 (Initial commit)
def start(update, context):
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
<<<<<<< HEAD
=======
    username = user_info['username']
>>>>>>> 0f7a004 (Initial commit)
    
    images = [
    "https://files.catbox.moe/x4ah5l.jpg",  # Replace with actual file_id or direct URL
    "https://files.catbox.moe/lt70jg.jpg"
]

    chosen_image = random.choice(images)

<<<<<<< HEAD
    caption = (
    "🕹️ *Welcome to DOMAIN ARCADE!*\n\n"
    "🌌 *Enter a realm beyond time and space...*\n"
    "⚔️ Hunt monsters, collect loot, level up, and become a legend.\n"
    "🎲 Play mini-games, challenge your luck, and earn rewards!\n\n"
    "📜 Use /help to begin your journey!"
)

    context.bot.send_photo(
    chat_id=update.effective_chat.id,
    photo=chosen_image,
    caption=caption,
    parse_mode=ParseMode.MARKDOWN)

=======
    caption = f"""
━━━━━━━━━━━━━━━━━━━━━━  
🌌 *WELCOME TO THE REALM* 🌌  
━━━━━━━━━━━━━━━━━━━━━━  

👤 *User:* `@{username}`

You awaken beneath a fading sky, the scent of old magic thick in the air...  
Ancient whispers call your name — the realm has been waiting.

From forgotten ruins to shadowed forests, from arcane towers to cursed seas...  
your path is unwritten, your legacy yet to form.

Will you rise as a hero, fall as a legend, or vanish in silence?

━━━━━━━━━━━━━━━━━━━━━━  
📝 _The journey begins — may your choices echo through eternity._  
━━━━━━━━━━━━━━━━━━━━━━
"""

    update.message.reply_photo(
    photo=chosen_image,
    caption=caption,
    parse_mode=ParseMode.MARKDOWN)
    
#help
>>>>>>> 0f7a004 (Initial commit)
def help(update, context):
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    update.message.reply_text(
    """*🤖 Bot Command List*
<<<<<<< HEAD
=======
━━━━━━━━━━━━━━━━━━━━━━
>>>>>>> 0f7a004 (Initial commit)

Here are all the cool things you can do:

• `/start` – 🌟 _Begin your journey!_  
<<<<<<< HEAD
• `/profile` – 📜 _View your stats and items_  
• `/explore` – 🧭 _Go on an adventure and fight monsters_  
• `/guess` – 🎯 _Play the number guessing game to win coins_  
• `/toss` – 🪙 _Toss a coin and test your luck_  
• `/shop` – 🛒 _Buy items like Essences and Moonshards_  
• `/help` – ❓ _Show this help message again_

*✨ Have fun playing!*  
_The adventure is just beginning..._""",
    parse_mode=ParseMode.MARKDOWN
)

def explore(update, context):
    
    init_user(update,context)
=======
• `/mystats` – 🧍‍♂️ _View your full character profile_  
• `/explore` – 🧭 _Go on an adventure and fight monsters_  
• `/guess` – 🎯 _Play the number guessing game to win coins_  
• `/toss` – 🎲 _Toss a coin and test your luck_  
• `/shop` – 🛒 _Buy Essences, weapons, and more_  
• `/myinventory` – 🎒 _Check your collected items_  
• `/mygear` – ⚔️ _View your equipped battle gear_  
• `/view <weapon>` – 🔍 _See detailed stats of a weapon available in-game_  
• `/help` – ❓ _Show this help message again_
• `/give` - _To give an item to another user_

━━━━━━━━━━━━━━━━━━━━━━  
*✨ Enjoy your adventure, hero!*  
_The realm awaits your next move..._
""",
    parse_mode=ParseMode.MARKDOWN
)

#explore 
def explore(update, context):
    
    
>>>>>>> 0f7a004 (Initial commit)
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
<<<<<<< HEAD
=======
    
>>>>>>> 0f7a004 (Initial commit)
    if update.message.chat.type != 'private':
        update.message.reply_text("❌ Use this command in DM!")
        return
        
     
     
    current_monster = random.choice(list(monster_db.keys()))
<<<<<<< HEAD
     
    context.user_data['current_monster'] = current_monster
    
    user_info['explores_played'] += 1
    save_user_data(user_info)    
    current_monster = context.user_data['current_monster']
    monster_stats = monster_db[current_monster]
    context.user_data['monster_hp'] = monster_stats['hp']
    context.user_data['monster_dmg'] = monster_stats['dmg']
    
    
     
    keyboard = [
    [InlineKeyboardButton('⚔️ Attack the Monster', callback_data='hunt')],
    [InlineKeyboardButton('🚶 Walk Away Silently', callback_data='walk')]
]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
    f"*👾 A wild {current_monster} appeared!*\n\n"
    "What will you do, brave adventurer?",
    reply_markup=reply_markup,
    parse_mode=ParseMode.MARKDOWN)

=======
    context.user_data['current_monster'] = current_monster
    
    user_info['explores_played'] += 1
    save_user_data(user_info)   
    
    monster_stats = monster_db[current_monster]
    context.user_data['monster_hp'] = monster_stats['hp']
    context.user_data['monster_dmg'] = monster_stats['dmg']
    context.user_data['monster_agility'] = monster_stats['agility']
    monster_photo = monster_db[current_monster]['photo']
    monster_level = random.randint(1,int(user_info['level']))
    context.user_data['monster_level'] = monster_level
    context.user_data['monster_hp'] = context.user_data['monster_hp'] * monster_level
    context.user_data['monster_dmg'] = context.user_data['monster_dmg'] * monster_level
    context.user_data['monster_agility'] = context.user_data['monster_agility'] * monster_level
    keyboard = [
    [InlineKeyboardButton('⚔️ Hunt the Monster', callback_data='hunt')]
]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_photo(photo = monster_photo,
    caption=
    f"""
    🌫️ The air thickens with mystery...  
⚠️ You feel a powerful presence nearby.  

━━━━━━━━━━━━━━━━━━━━━━ 

✨ *A Wild {current_monster} Has Appeared!* ✨  
*Level:* `{monster_level}`

*Monster HP:* {context.user_data['monster_hp']}
*Monster Power:* {context.user_data['monster_dmg']}
*Monster Agility:* {context.user_data['monster_agility']}

🧝 *Brave adventurer*, what will you do?

━━━━━━━━━━━━━━━━━━━━━━  
⚔️ *Hunt* — Face the beast head-on  
━━━━━━━━━━━━━━━━━━━━━━""",
    reply_markup=reply_markup,
    parse_mode=ParseMode.MARKDOWN
)
def explore_button(update,context):
  user_info = init_user(update,context)
  user_data = context.user_data
  
  query = update.callback_query
  query.answer()
  explore_option = query.data
  
  if explore_option == 'hunt':
    current_monster = context.user_data['current_monster']
    monster_hp = context.user_data['monster_hp']
    monster_dmg = context.user_data['monster_dmg']
    monster_agility = context.user_data['monster_agility']
    query.edit_message_caption(
      caption = (
      f'''
⚔️─────────────⚔️
        
<b>You chose to attack the {current_monster}!</b>
         
───────────────
         
👾 <b>Monster HP:</b> {monster_hp}
💥 <b>Monster Damage:</b> {monster_dmg}
⚡ <b>Monster Agility:</b> {monster_agility}
        
───────────────
🔥<b> Prepare for battle!</b>
⚔️ <b>Attack</b> — Face the beast head-on  
🚶 <b>Retreat</b> — Live to fight another day
⚔️─────────────⚔️
    '''),
    parse_mode = ParseMode.HTML,
    reply_markup = InlineKeyboardMarkup(
      [
        [InlineKeyboardButton('⚔️ Attack the Monster',callback_data='attack')],
        [InlineKeyboardButton('🚶 Retreat Silently',callback_data='retreat')]
      ]
    )
  )
        
>>>>>>> 0f7a004 (Initial commit)
def button(update, context):
    
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    query = update.callback_query
    query.answer()
    answer = query.data
    
<<<<<<< HEAD
    current_monster = context.user_data['current_monster']
    monster_hp = context.user_data['monster_hp']
    monster_dmg = context.user_data['monster_dmg']
    
    
    if answer == 'hunt':
         
        user_info['hp'] -= monster_dmg
        monster_hp -= user_info['power']
        save_user_data(user_info)
=======
    monster_level = context.user_data['monster_level']
    current_monster = context.user_data['current_monster']
    monster_hp = context.user_data['monster_hp']
    monster_dmg = context.user_data['monster_dmg']
    monster_agility = context.user_data['monster_agility']
    equiped_weapon = user_info['equiped_weapon']
    
    if not equiped_weapon or equiped_weapon not in user_info['user_weapons']:
      total_hp = user_info['hp']
      user_battle_power = user_info['power']
      user_battle_agility = user_info['agility']
    else:
      total_hp = user_info['hp'] + user_info['user_weapons'][equiped_weapon]['bonus_hp']
      user_battle_power = user_info['power'] + user_info['user_weapons'][equiped_weapon]['bonus_power']
      user_battle_agility = user_info['agility'] + user_info['user_weapons'][equiped_weapon]['bonus_agility']

# 🩹 Use or create current_hp if not there yet
    if 'current_hp' not in user_info:
      user_info['current_hp'] = total_hp
    
    user_battle_hp = user_info['current_hp']
    
    if answer == 'attack':
      
      explore_log = ""
      if user_battle_agility >= monster_agility:
        monster_hp -= user_battle_power
        context.user_data['monster_hp'] = monster_hp
        explore_log += f"👤 You attacked first and dealt <b>{user_battle_power}</b> damage!\n"
        
        if monster_hp > 0:
          user_battle_hp -= monster_dmg
          user_info['current_hp'] = user_battle_hp 
          save_user_data(user_info)
          
          explore_log += f"👾 {current_monster} struck back and dealt <b>{monster_dmg}</b> damage!\n"
            
      if user_battle_agility < monster_agility:
        user_battle_hp -= monster_dmg
        user_info['current_hp'] = user_battle_hp
        save_user_data(user_info)
        explore_log += f"👾 {current_monster} attacked first and dealt <b>{monster_dmg}</b> damage!\n"
        
        if user_battle_hp > 0:
          monster_hp -= user_battle_power
          context.user_data['monster_hp'] = monster_hp
          explore_log += f"👤 You struck back and dealt <b>{user_battle_power}</b> damage!\n"
        
        
>>>>>>> 0f7a004 (Initial commit)
        # Update stored HPs
        
        context.user_data['monster_hp'] = monster_hp
        
<<<<<<< HEAD
        if monster_hp <= 0:
            query.edit_message_text(f"🏆 *Victory!*\n\nYou defeated *{current_monster}* in a fierce battle!\n\n🪙 You earned *+20 Coins*\n✨ Gained *+15 XP*\n\n🎮 Use /explore to battle more monsters!",parse_mode = ParseMode.MARKDOWN)
            user_info['Coins']+=20
            user_info['xp']+=15
            user_info['explores_won'] += 1
            user_info['hp'] = user_info['max_hp']
            xp_system(update,context)
            del user_data['current_monster']
            del user_data['monster_hp']
            del user_data['monster_dmg']
            save_user_data(user_info)
            
        elif user_info['hp'] <= 0:
            query.edit_message_text(f"💀 *Defeat...*\n\nYou fought bravely, but *{current_monster}* was too strong.\n\n🧍 You have fallen in battle.\n🪙 You dropped *10 coins*.\nYou get *5 XP*.\n\n🔁 Use /explore to try again and redeem your honor!",parse_mode = ParseMode.MARKDOWN)
            user_info['Coins'] -= 10
            user_info['xp'] += 5
            user_info['explores_lost'] += 1
            user_info['hp'] = user_info['max_hp']
            xp_system(update,context)
            del user_data['current_monster']
            del user_data['monster_hp']
            del user_data['monster_dmg']
            save_user_data(user_info)
        
        else:
            keyboard5 = [
    [InlineKeyboardButton('⚔️ Attack Again', callback_data='hunt')],
    [InlineKeyboardButton('🚶 Give Up', callback_data='walk')]
]
            reply_markup5 = InlineKeyboardMarkup(keyboard5)

            query.edit_message_text(
    f"⚔️ You chose to attack *{current_monster}*!\n\n"
    f"💥 You dealt *{user_info['power']}* damage!\n"
    f"🩸 {current_monster} dealt *{monster_dmg}* damage back!\n\n"
    f"👾 {current_monster} has *{monster_hp} HP* left.\n"
    f"❤️ You have *{user_info['hp']} HP* left.",
    reply_markup=reply_markup5,
    parse_mode=ParseMode.MARKDOWN
)
       
        
    elif answer == 'walk':
        query.edit_message_text(
            "🚶‍♂️ *You walked away...*\n\n"
            "Sometimes, retreat is the wisest choice.\n"
            "_Live to fight another day, brave soul._",
            parse_mode=ParseMode.MARKDOWN
        )
=======
      if monster_hp <= 0:
        user_info['coins']+=20
        user_info['xp']+=15
        user_info['explores_won'] += 1
        user_info['current_hp'] = total_hp
        save_user_data(user_info)
        xp_system(update,context)
        if not equiped_weapon or equiped_weapon not in user_info['user_weapons']:
          weapon_xp_msg = ''
          pass
        else:
          
          weapon_xp_system(update,context)
          
          weapon_xp_msg = '<b>🗡️ Weapon XP Gained:</b> +30'
          
        
        query.edit_message_caption(
          caption =
    f"""⚔️ <b>Battle Log</b>  
━━━━━━━━━━━━━━━━━━━━━━  

{explore_log}

🏆 <b>Victory!</b>  
━━━━━━━━━━━━━━━━━━━━━━  
You defeated <b>{current_monster}</b> in a fierce battle!

🪙 <b>Coins Earned:</b> +20  
✨ <b>XP Gained:</b> +15
{weapon_xp_msg}
   
━━━━━━━━━━━━━━━━━━━━━━  
🎮 Use /explore to battle more monsters!""",
    parse_mode=ParseMode.HTML
)
        
        
        
        
        
        del user_data['current_monster']
        del user_data['monster_hp']
        del user_data['monster_dmg']
        del user_data['monster_agility']
          # full HP again
        
        
      elif user_info['current_hp'] <= 0:
        user_info['coins'] -= 10
        user_info['xp'] += 5
        user_info['explores_lost'] += 1
        user_info['current_hp'] = total_hp
        save_user_data(user_info)
        xp_system(update,context)
        if not equiped_weapon or equiped_weapon not in user_info['user_weapons']:
          weapon_xp_msg = ''
          pass
        else:
          
        
          weapon_xp_system(update,context)
          
          weapon_xp_msg = '<b>Weapon XP Gained:</b> +30'
          
        query.edit_message_caption(
          caption=
    f"""⚔️ <b>Battle Log</b>  
━━━━━━━━━━━━━━━━━━━━━━  

{explore_log}

💀 <b>Defeat...</b>  
━━━━━━━━━━━━━━━━━━━━━━  
You fought bravely, but <b>{current_monster}</b> was too strong.

🧍‍♂️ You have fallen in battle.  
🪙 <b>Coins Lost:</b> 10  
✨ <b>XP Gained:</b>+5  
   {weapon_xp_msg}
━━━━━━━━━━━━━━━━━━━━━━  
🔁 Use /explore to try again and redeem your honor!
""",
    parse_mode=ParseMode.HTML
)
        
        
        
        
        
        
        
        del user_data['current_monster']
        del user_data['monster_hp']
        del user_data['monster_dmg']
        del user_data['monster_agility']
          # full HP again
        
        
      else:
        keyboard5 = [
    [InlineKeyboardButton('⚔️ Attack Again', callback_data='attack')],
    [InlineKeyboardButton('🚶 Retreat', callback_data='retreat')]
]
        reply_markup5 = InlineKeyboardMarkup(keyboard5)

        query.edit_message_caption(
          caption =
    f"""⚔️ <b>Attack Turn</b>  
━━━━━━━━━━━━━━━━━━━━━━  

{explore_log}

━━━━━━━━━━━━━━━━━━━━━━  
📉 <b>{current_monster}'s HP:</b> <code>{monster_hp}</code>  
❤️ <b>Your HP:</b> <code>{user_battle_hp}</code>

━━━━━━━━━━━━━━━━━━━━━━""",
    reply_markup=reply_markup5,
    parse_mode=ParseMode.HTML
)
       
        
    elif answer == 'retreat':
      query.edit_message_caption(
        caption =
  """🚶‍♂️ *You Chose to Retreat*  
━━━━━━━━━━━━━━━━━━━━━━  
Sometimes, retreat is the wisest choice.  
Your journey doesn’t end here...

📜 _Live to fight another day, brave soul._  
━━━━━━━━━━━━━━━━━━━━━━""",
  parse_mode=ParseMode.MARKDOWN
)
>>>>>>> 0f7a004 (Initial commit)
    

        
    
<<<<<<< HEAD
    
def profile(update, context):
=======
#inventory    
def inventory(update, context):
>>>>>>> 0f7a004 (Initial commit)
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
<<<<<<< HEAD
    
    update.message.reply_text(
    f"*📜 Your Profile*\n\n"
    f"🏅 *Level:* {user_info['level']}\n"
    f"✨ *XP:* {user_info['xp']} / {user_info['max_xp']}\n"
    f"💰 *Coins:* {user_info['Coins']}\n"
    f"🔮 *Essences:* {user_info['Essences']}\n"
    f"🐚 *Moonshards:* {user_info['Moonshards']}",
    parse_mode=ParseMode.MARKDOWN
)

CHOOSE_QUANTITY = range(1)

def shop(update, context):
    image = "https://files.catbox.moe/pzmbvd.jpg"  # Replace with your image URL or file_id

    caption = (
        "🛒 *Welcome to the Arcade Shop!*\n\n"
        "✨ Buy powerful items to help you in battle!\n"
        "💰 Use your coins wisely to level up faster.\n\n"
        "🧩 *Available Items:*\n"
        "• Essences — 1000 Coins\n"
        "• Moonshards — 100 Coins"
    )

    keyboard4 = [
        [InlineKeyboardButton('💥 Buy Essences (1000 🪙)', callback_data='Essences')],
        [InlineKeyboardButton('🧿 Buy Moonshards (100 🪙)', callback_data='Moonshards')]
    ]
    reply_markup2 = InlineKeyboardMarkup(keyboard4)

    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=image,
        caption=caption,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=reply_markup2#
=======
    username = user_info['username'] or user_info['first_name']
    
    inv_markup = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("⚔️ Weapons", callback_data='inv_weapons'),
        InlineKeyboardButton("✨ Magical Items", callback_data='inv_magic')
    ]
])
    update.message.reply_text(
    f"*👤 Your Inventory*\n\n"
    f"`Username:` `{username}`\n\n"
    f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
    f"💰 *Coins:* {user_info['coins']}\n"
    f"🔮 *Essences:* {user_info['essences']}\n"
    f"🐚 *Moonshards:* {user_info['moonshards']}\n\n"
    f"━━━━━━━━━━━━━━━━━━━━━━",
    parse_mode=ParseMode.MARKDOWN,
    reply_markup = inv_markup
)

def inv_button(update,context):
  
  user_info = init_user(update,context)
  user_id = user_info['user_id']
  username = user_info['username'] or user_info['first_name']
  user_data = context.user_data
  
  query = update.callback_query
  query.answer()
  
  inv_chosen = query.data
  
  if inv_chosen == 'inv_weapons':
    inv_weapons_markup = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("📦 Inventory", callback_data='inv_main'),
        InlineKeyboardButton("✨ Magical Items", callback_data='inv_magic')
    ]
])
    if not user_info['user_weapons']:
      query.edit_message_text(
      text=(
          "⚔️ *Weapon Inventory*\n"
          "━━━━━━━━━━━━━━━━━━━━━━\n"
          "You open your worn-out satchel... 🧳\n"
          "_It's empty... for now._\n\n"
          "You haven’t discovered any weapons yet.\n"
          "Explore the world or win battles to find powerful gear!\n"
          "━━━━━━━━━━━━━━━━━━━━━━"
      ),
      parse_mode=ParseMode.MARKDOWN,
      reply_markup = inv_weapons_markup
  )
  
    else:
      user_wp_list = "\n".join([f"🗡️ {wp}" for wp in user_info["user_weapons"].keys()])
      
      message = f"""
🧰 <b>YOUR INVENTORY</b>

✨ Here are all your equipped and owned weapons:

━━━━━━━━━━━━━━━━━━━━

{user_wp_list}

━━━━━━━━━━━━━━━━━━━━

💡 <b>Tip:</b> Use /mygear to view your equipped weapon!
"""
      query.edit_message_text(message,
        reply_markup = inv_weapons_markup,
        parse_mode = ParseMode.HTML)
        
  elif inv_chosen == 'inv_magic':
    inv_magic_markup = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("📦 Inventory", callback_data='inv_main'),
        InlineKeyboardButton("⚔️ Weapons", callback_data='inv_weapons')
    ]
])
    query.edit_message_text(
    text=(
        "✨ *Magical Items*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "You gaze into your enchanted pouch... 🔮\n"
        "_But it's silent and empty..._\n\n"
        "No magical items have been discovered yet.\n"
        "Seek out mystical places, defeat bosses, or unlock ancient chests!\n"
        "━━━━━━━━━━━━━━━━━━━━━━"
    ),
    parse_mode=ParseMode.MARKDOWN,
    reply_markup = inv_magic_markup
)
  elif inv_chosen == 'inv_main':
    inv_main_markup = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("⚔️ Weapons", callback_data='inv_weapons'),
        InlineKeyboardButton("✨ Magical Items", callback_data='inv_magic')
    ]
])
    query.edit_message_text(
    f"*👤 Your Inventory*\n"
    f"`Username:` `{username}`\n"
    f"━━━━━━━━━━━━━━━━━━━━━━\n"
    f"💰 *Coins:* {user_info['coins']}\n"
    f"🔮 *Essences:* {user_info['essences']}\n"
    f"🐚 *Moonshards:* {user_info['moonshards']}\n"
    f"━━━━━━━━━━━━━━━━━━━━━━",
    parse_mode=ParseMode.MARKDOWN,
    reply_markup = inv_main_markup
)

BUY_WEAPON = range(1)
CHOOSE_QUANTITY = range(1)

def cancel(update, context):
    update.message.reply_text("❌ Purchase cancelled. You can /shop again anytime!")
    return ConversationHandler.end
    
#shop
def shop(update, context):
    user_info = init_user(update,context)
  
    if update.message.chat.type != 'private':
        update.message.reply_text("❌ Use this command in DM!")
        return
  
    image = "AgACAgUAAxkBAAIPKWiWR8bCk2-C5LXjUr6jLKdjoTnUAAKf0zEb5V-wVFwym1zA70KmAQADAgADeAADNgQ"  # Replace with your image URL or file_id

    caption = f"""
━━━━━━━━━━━━━━━━━━━━━━  
🏪 *THE GRAND SHOP*  
━━━━━━━━━━━━━━━━━━━━━━

Step into a world of trades and treasures.  
Choose where you want to browse:

🪙 *Resource Shop*  
Buy *Moonshards* and rare *Essences* to boost your power.

🗡️ *Weapon Shop*  
*Buy Amazing And powerful Weapons to increase your gear power*

⭐ *Magic Shop*  
🔒 Locked — *Coming soon...*

━━━━━━━━━━━━━━━━━━━━━━  
📜 _New shops will open as your journey unfolds..._
"""

    keyboard7 = [
    [InlineKeyboardButton("🎒 Resource Shop", callback_data="resource_shop")],
    [InlineKeyboardButton("🛡️ Weapon Shop", callback_data="weapon_shop")],
    [InlineKeyboardButton("🌟 Magic Shop", callback_data="magic_shop")]
    
]

    reply_markup7 = InlineKeyboardMarkup(keyboard7)

    update.message.reply_photo(
        photo=image,
        caption=caption,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=reply_markup7
>>>>>>> 0f7a004 (Initial commit)
    )

def button2(update, context):
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    query = update.callback_query
    query.answer()
<<<<<<< HEAD
    context.user_data['item_to_buy'] = query.data
    
    
    query.edit_message_caption(
    caption=(
        "🛒 *Shop Purchase*\n\n"
        "🧾 You selected to buy an item.\n"
        "💬 _Please enter how many you want to buy._\n\n"
        "⚠️ *Make sure you have enough coins!*\n"
        "💡 Example: `3`, `10`, `25`"
    ),
    parse_mode=ParseMode.MARKDOWN
)
 
    return CHOOSE_QUANTITY
=======
    context.user_data['chosen_shop'] = query.data
    
    if context.user_data['chosen_shop'] == 'resource_shop':
      keyboard4 = [
        [InlineKeyboardButton('💥 Buy Essences (1000 🪙)', callback_data='essences')],
        [InlineKeyboardButton('🧿 Buy Moonshards (100 🪙)', callback_data='moonshards')]
    ]
      reply_markup2 = InlineKeyboardMarkup(keyboard4)
      
      query.edit_message_caption(
      caption = ( """
🎒 *Resource Shop*  
━━━━━━━━━━━━━━━━━━━━━━  
Here you'll find rare materials that fuel your journey:  

🪙 Coins — Common trade currency  
🔮 Essences — Crystallized magical energy  
🐚 Moonshards — Fragments of ancient power

💡 _Spend wisely, traveler. These items are more than they appear..._
"""
    ),reply_markup = reply_markup2,
    parse_mode=ParseMode.MARKDOWN
)
 
      
      
    elif context.user_data['chosen_shop'] == 'weapon_shop':
      query.edit_message_caption(
        caption = (
    """
🏰 *Welcome to the Weapon Shop!* 🏰  
━━━━━━━━━━━━━━━━━━━━━━  
🛒 Choose your blade and forge your destiny!

`Bronze Sword`  
💰 Price: 1 Essence 🎖️ Rarity: Common  

`Iron Blade`  
💰 Price: 5 Essence 🎖️ Rarity :Common  

`Crystal Lance`  
💰 Price: 10 Essence 🎖️ Rarity :Uncommon

`Void Edge`  
💰 Price: 20 Essence 🎖️ Rarity: Rare  

━━━━━━━━━━━━━━━━━━━━━━  
📝 *Send the name of the weapon you want to buy.*
*use /cancel to cancel the purchase *
"""
),
parse_mode  = ParseMode.MARKDOWN)

      return BUY_WEAPON 
      

    elif context.user_data['chosen_shop'] == 'magic_shop':
      query.edit_message_caption(
        caption = ("""
✨ *Magic Shop - Not Yet Awakened* ✨  
━━━━━━━━━━━━━━━━━━━━━━  
📦 Enchanted tomes remain sealed...  
🔮 Mystic lights flicker behind dusty shelves...  
🧙‍♂️ The magician has yet to return from his arcane journey.

📜 *Patience, young adventurer — true magic takes time.*  
━━━━━━━━━━━━━━━━━━━━━━
"""),
parse_mode = ParseMode.MARKDOWN)

def button7(update,context):
  
  user_info = init_user(update,context)
  user_data = context.user_data
  
  query = update.callback_query
  query.answer()
  
  context.user_data['item_to_buy'] = query.data
  item_name = context.user_data.get("item_to_buy", "Unknown Item")
  currency_emoji = '🪙'
  item_to_buy = context.user_data['item_to_buy']

  if item_to_buy == "essences":
    item_price = 1000
  elif item_to_buy == "moonshards":
    item_price = 100
    
  query.edit_message_caption(
    caption = (f"""
🛒 <b>Purchase Menu</b>  
━━━━━━━━━━━━━━━━━━━━━━  
✨ You have selected: <b>{item_name}</b>  
💰 <b>Price:</b> {item_price} {currency_emoji} per unit  
📦 <b>Stock:</b> Unlimited

🧮 <i>How many would you like to buy?</i>  
<b>Send the quantity below.</b>  
<b>Send /cancel to cancel purchase.</b>
━━━━━━━━━━━━━━━━━━━━━━
"""),
parse_mode = ParseMode.HTML
)
  return CHOOSE_QUANTITY
>>>>>>> 0f7a004 (Initial commit)
    
def handle_quantity(update, context):
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    item = context.user_data['item_to_buy']
    
<<<<<<< HEAD
=======
    if not update.effective_user:
      update.message.reply_text('not you')
>>>>>>> 0f7a004 (Initial commit)
    try:
        amount = int(update.message.text)
        if amount <= 0:
            update.message.reply_text("❌ Please enter a number greater than 0.")
            return CHOOSE_QUANTITY
    except:
        update.message.reply_text("❌ Please enter a valid number.")
        return CHOOSE_QUANTITY

<<<<<<< HEAD
    if item == 'Essences':
        price = 1000
        if user_info['Coins'] >= amount * price:
            user_info['Coins'] -= amount * price
            user_info['Essences'] += amount
=======
    if item == 'essences':
        price = 1000
        if user_info['coins'] >= amount * price:
            user_info['coins'] -= amount * price
            user_info['essences'] += amount
>>>>>>> 0f7a004 (Initial commit)
            save_user_data(user_info)
            update.message.reply_text(f"✅ Bought {amount} Essences for {amount * price} coins!")
        else:
            update.message.reply_text("❌ Not enough coins!")

<<<<<<< HEAD
    elif item == 'Moonshards':
        price = 100
        if user_info['Coins'] >= amount * price:
            user_info['Coins'] -= amount * price
            user_info['Moonshards'] += amount
=======
    elif item == 'moonshards':
        price = 100
        if user_info['coins'] >= amount * price:
            user_info['coins'] -= amount * price
            user_info['moonshards'] += amount
>>>>>>> 0f7a004 (Initial commit)
            save_user_data(user_info)
            update.message.reply_text(f"✅ Bought {amount} Moonshards for {amount * price} coins!")
        else:
            update.message.reply_text("❌ Not enough coins!")

    return ConversationHandler.END
    
    
shop_conv = ConversationHandler(
<<<<<<< HEAD
    entry_points=[CallbackQueryHandler(button2, pattern='^Essences|Moonshards$')],
    states={
        CHOOSE_QUANTITY: [MessageHandler(Filters.text & ~Filters.command, handle_quantity)],
    },
    fallbacks=[],
)

guess_num = range(1)

=======
    entry_points=[CallbackQueryHandler(button7, pattern='^(essences|moonshards)$')],
    states={
        CHOOSE_QUANTITY: [MessageHandler(Filters.text & ~Filters.command, handle_quantity)],
    },
    fallbacks=[CommandHandler('cancel',cancel)],
)
# This is your cancel handler – works for the whole conversation

    
def buy_wp(update,context):
  user_info = init_user(update,context)
  
  user_wp_name = update.message.text
  
  if user_wp_name not in list(weapon_list.keys()):
    update.message.reply_text(
    "⚠️ *No such weapon found!*\n"
    "Please double-check the name and try again.\n\n"
    "💡 *Tip:* Long press the weapon name in the list to copy it easily.",
    parse_mode=ParseMode.MARKDOWN
)
    return BUY_WEAPON
    
  elif user_wp_name in list(weapon_list.keys()):
    if user_wp_name not in list(user_info['user_weapons'].keys()):
      if user_info['essences'] >= weapon_list[user_wp_name]['price']:
        user_info['user_weapons'][user_wp_name] = copy.deepcopy(weapon_list[user_wp_name])
        user_info['essences'] -= weapon_list[user_wp_name]['price']
        save_user_data(user_info)
        update.message.reply_text(
      f"""
  ━━━━━━━━━━━━━━━━━━━━━━  
  ✅ You have successfully purchased ``{user_wp_name}``  
  💰 Price: {weapon_list[user_wp_name]['price']} Essences  
  ━━━━━━━━━━━━━━━━━━━━━━  
  🧰 The weapon has been added to your inventory.  
  ⚙️ Equip it using `/mygear` to use it in battle!  
  ━━━━━━━━━━━━━━━━━━━━━━
  """,
      parse_mode=ParseMode.MARKDOWN
  )
        return ConversationHandler.END
      
      else:
        update.message.reply_text(
    "🚫 Not Enough Essences!\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "You don’t have enough 💠 *Essences* to buy that weapon.\n"
    "Keep exploring and defeating monsters to earn more!\n\n"
    "💡 *Tip:* Stronger monsters drop more essences.\n"
    "━━━━━━━━━━━━━━━━━━━━━━",
    parse_mode=ParseMode.MARKDOWN
)
        return ConversationHandler.END

  
    elif user_wp_name in list(user_info['user_weapons'].keys()):
      update.message.reply_text(
    "⚠️ You Already Own This Weapon!\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "You already have this weapon in your inventory.\n"
    "Check it out using /mygear!\n\n"
    "💡 <b>Tip:</b>You can only buy each weapon once.\n"
    "━━━━━━━━━━━━━━━━━━━━━━",
    parse_mode=ParseMode.HTML
)
      return ConversationHandler.END
  
weapon_conv_handler = ConversationHandler(
      entry_points=[CallbackQueryHandler(button2, pattern='^(weapon_shop)$')],
      states={
          BUY_WEAPON: [MessageHandler(Filters.text & ~Filters.command, buy_wp)],
      },
      fallbacks=[CommandHandler('cancel',cancel)]  # No fallback used in your case
  )
    
    
  
guess_num = range(1)
#guess 
>>>>>>> 0f7a004 (Initial commit)
def guess(update,context):
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    if update.message.chat.type != 'private':
        update.message.reply_text(
<<<<<<< HEAD
    text="🕵️‍♂️ *Guessing Game Notice!*\n\nPlease use this command in a *private chat* with me.\nTap my profile and click *'Start'* to play!",
=======
    text="""
🕵️‍♂️ *Guessing Game Notice*  
━━━━━━━━━━━━━━━━━━━━━━  
This game can only be played in *private chat* with me.

👤 Tap my profile and press *Start* to begin your challenge!
━━━━━━━━━━━━━━━━━━━━━━  
""",
>>>>>>> 0f7a004 (Initial commit)
    parse_mode=ParseMode.MARKDOWN
)
        return
        
    # Check if user is on cooldown
      
        
    now = time.time()
    cooldown = context.user_data.get('guess_cooldown', 0)
    
    if now < cooldown:
         wait_time = int(cooldown - now)
         update.message.reply_text(
    text="⏳ *Please wait!* \n\nYou're on cooldown. Try again in *{} seconds*!".format(wait_time),
    parse_mode=ParseMode.MARKDOWN
)
         return ConversationHandler.END
    
        # Set new cooldown (60 seconds from now)
    context.user_data['guess_cooldown'] = now + 60
    
    
    context.user_data['number']= random.randint(1,100)
    
    keyboard2 = [
    [InlineKeyboardButton("✅ Yes! Let's Play", callback_data='yes')],
    [InlineKeyboardButton("❌ No, Maybe Later", callback_data='no')]
]
    
    reply_markup3 = InlineKeyboardMarkup(keyboard2)
    
    update.message.reply_text(
<<<<<<< HEAD
    "🎯 *Welcome to the Number Guessing Game!*\n\n"
    "🔢 A number between *1 and 100* has been chosen...\n"
    "❓ Do you want to try and guess it?\n\n"
    "🏆 *Reward:* +100 Coins\n"
    "🕐 *Note:* You can play once every 1 minute.",
    parse_mode=ParseMode.MARKDOWN,
    reply_markup=reply_markup3)
=======
    "🎯 *Welcome to the Number Guessing Game!*  \n"
    "━━━━━━━━━━━━━━━━━━━━━━  \n"
    "🔢 A number between *1 and 100* has been chosen...  \n"
    "❓ Can you guess it right?  \n\n"
    "🏆 *Reward:* +100 Coins  \n"
    "⏱️ *Note:* Play once every 1 minute.  \n"
    "━━━━━━━━━━━━━━━━━━━━━━",
    parse_mode=ParseMode.MARKDOWN,
    reply_markup=reply_markup3
)
>>>>>>> 0f7a004 (Initial commit)
    
def button3(update,context):
    
    
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    query=update.callback_query
    query.answer()
    
    user_choice = query.data
    
    
    if user_choice == 'yes':
        query.edit_message_text(
<<<<<<< HEAD
    text="📨 *Great!* Now send me a number between *1 and 100* to guess it.\n\n🎯 Let’s see if you can hit the right number!",
=======
    text="🎯 *Great!* Let's begin the challenge!  \n"
         "━━━━━━━━━━━━━━━━━━━━━━  \n"
         "📨 Send me a number between *1 and 100* to make your guess.  \n"
         "💡 Trust your instincts and take a shot!  \n"
         "━━━━━━━━━━━━━━━━━━━━━━",
>>>>>>> 0f7a004 (Initial commit)
    parse_mode=ParseMode.MARKDOWN
)
        return guess_num
        
    elif user_choice == 'no':
        query.edit_message_text(
<<<<<<< HEAD
    text="🚪 *You chose to walk away...*\nNo worries, come back anytime to test your luck! 🎲😉",
=======
    text="🚪 *You chose to walk away...*  \n"
         "━━━━━━━━━━━━━━━━━━━━━━  \n"
         "Sometimes, a wise retreat is better than a risky gamble.  \n"
         "🎲 Come back anytime to test your luck again! 😉  \n"
         "━━━━━━━━━━━━━━━━━━━━━━",
>>>>>>> 0f7a004 (Initial commit)
    parse_mode=ParseMode.MARKDOWN
)
        return ConversationHandler.END
        
def guess_numb(update,context):
     
        user_id = update.effective_user.id
        user_info = init_user(update,context)
        user_data = context.user_data
        
        
        user_ans = int(update.message.text)
        correct_ans = int(context.user_data['number'])
            
         
    
    
        if user_ans == correct_ans:
<<<<<<< HEAD
            user_info['Coins']+=100
=======
            user_info['coins']+=100
>>>>>>> 0f7a004 (Initial commit)
            del context.user_data['number']
            user_info['xp']+=25
            save_user_data(user_info)
            xp_system(update,context)
            update.message.reply_text(
<<<<<<< HEAD
    "🎉 *You guessed it right!* 🎯\n\n💰 You earned *100 Coins* and gained *25 XP*! 🧠🔥\nKeep it up, champion!",
=======
    "🎉 *You guessed it right!* 🎯  \n"
    "━━━━━━━━━━━━━━━━━━━━━━  \n"
    "💰 *Reward:* +100 Coins  \n"
    "✨ *XP Gained:* +25 XP  \n"
    "━━━━━━━━━━━━━━━━━━━━━━  \n"
    "Keep it up, champion! 🧠🔥",
>>>>>>> 0f7a004 (Initial commit)
    parse_mode=ParseMode.MARKDOWN
)
            return ConversationHandler.END
            
        elif user_ans >= correct_ans:
            update.message.reply_text(
    "❌ *Wrong answer!*\nYour guess is *too high* 📈\nTry a smaller number!",
    parse_mode=ParseMode.MARKDOWN
)
            return guess_num
            
            
        elif user_ans <= correct_ans:
            update.message.reply_text(
    "❌ *Wrong answer!*\nYour guess is *too low* 📉\nTry a bigger number!",
    parse_mode=ParseMode.MARKDOWN
)
            return guess_num
            
conv_handler = ConversationHandler(
        entry_points =[CallbackQueryHandler(button3,pattern='^yes|no$')],
        states = {
                        guess_num: [MessageHandler(Filters.text & ~Filters.command , guess_numb )]
                        },
                        fallbacks = []
                        )        
   
<<<<<<< HEAD
   
=======
 #toss  
>>>>>>> 0f7a004 (Initial commit)
def toss(update,context):
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    # Check if user is on cooldown
    now = time.time()
    cooldown = context.user_data.get('toss_cooldown', 0)

    if now < cooldown:
        wait_time = int(cooldown - now)
        update.message.reply_text(
    text=f"⏳ *Whoa there!* You just tossed the coin!\n\n🪙 Please wait *{wait_time} seconds* before trying again!",
    parse_mode=ParseMode.MARKDOWN
)
        return

    # Set new cooldown (60 seconds from now)
    context.user_data['toss_cooldown'] = now + 30
    
    
    two_option = ['heads','tails']
    bot_option = random.choice(two_option)
    context.user_data['bot_option'] = bot_option
    
    keyboard3 = [
    [
        InlineKeyboardButton("🪙 Heads", callback_data='heads'),
        InlineKeyboardButton("🐢 Tails", callback_data='tails')
    ]
]
    reply_markup4 = InlineKeyboardMarkup(keyboard3)
    
    update.message.reply_text(
<<<<<<< HEAD
    "🎯 *Time to Toss the Coin!*\n\nChoose your side wisely:",
=======
    "🪙 *Time to Toss the Coin!* 🎯  \n"
    "━━━━━━━━━━━━━━━━━━━━━━  \n"
    "Choose your side wisely:  \n"
    "Heads or Tails? 🤔",
>>>>>>> 0f7a004 (Initial commit)
    reply_markup=reply_markup4,
    parse_mode=ParseMode.MARKDOWN
)
    
    
def button4(update,context):
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    query = update.callback_query
    query.answer()
    
    chosen_option = query.data
    
    if chosen_option == context.user_data['bot_option']:
        query.edit_message_text(
<<<<<<< HEAD
    f"🎉 *The coin landed on:* `{context.user_data['bot_option'].capitalize()}`\n"
    "✅ *You won the toss!*\n"
    "💰 You earned *20 coins* and gained *15 XP!*",
    parse_mode=ParseMode.MARKDOWN
)
        user_info['Coins'] += 20
=======
    f"🪙 *Coin Toss Result!* 🎯\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n"
    f"🎉 The coin landed on: *{context.user_data['bot_option'].capitalize()}*\n"
    "✅ *You won the toss!*\n"
    "🪙 *Reward:* +20 Coins\n"
    "✨ *XP Gained:* +15",
    parse_mode=ParseMode.MARKDOWN
)
        user_info['coins'] += 20
>>>>>>> 0f7a004 (Initial commit)
        user_info['xp']+=15
        save_user_data(user_info)
        xp_system(update,context)
        
    else:
        query.edit_message_text(
<<<<<<< HEAD
    f"😢 *The coin landed on:* `{context.user_data['bot_option'].capitalize()}`\n"
    "❌ *You lost the toss!*\n"
    "💸 You lost *10 coins!*",
    parse_mode=ParseMode.MARKDOWN
)
        user_info['Coins']-= 10
        save_user_data(user_info)
        
=======
    f"🪙 *Coin Toss Result!* 🎯\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n"
    f"😢 The coin landed on: *{context.user_data['bot_option'].capitalize()}*\n"
    "❌ *You lost the toss!*\n"
    "💸 *Penalty:* -10 Coins",
    parse_mode=ParseMode.MARKDOWN
)
        user_info['coins']-= 10
        save_user_data(user_info)
  #stats      
>>>>>>> 0f7a004 (Initial commit)
def stats(update,context):
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    username = user_info["username"]
    hp = user_info["hp"]
<<<<<<< HEAD
    max_hp = user_info["max_hp"]
    power = user_info["power"]
    level = user_info["level"]
    xp = user_info["xp"]
    max_xp = user_info["max_xp"]
    coins = user_info["Coins"]
    moonshards = user_info["Moonshards"]
    essences = user_info["Essences"]
=======
    max_hp = user_info["hp"]
    power = user_info["power"]
    level = user_info["level"]
    agility = user_info["agility"]
    xp = user_info["xp"]
    max_xp = user_info["max_xp"]
    coins = user_info["coins"]
    moonshards = user_info["moonshards"]
    essences = user_info["essences"]
    equiped_weapon = user_info['equiped_weapon'] or 'No weapons or not equiped one'
    

    if not equiped_weapon or equiped_weapon not in user_info['user_weapons']:
      bonus_hp = 0
      bonus_power = 0
      bonus_agility = 0
      
    else:
      bonus_hp = user_info['user_weapons'][equiped_weapon].get('bonus_hp', 0)
      bonus_power = user_info['user_weapons'][user_info['equiped_weapon']]['bonus_power']
      bonus_agility = user_info['user_weapons'][user_info['equiped_weapon']]['bonus_agility']
     
>>>>>>> 0f7a004 (Initial commit)
    
    stats_message = f"""
━━━━━━━━━━━━━━━━━━━━━━  
🏰 *CHARACTER PROFILE* 🏰  
━━━━━━━━━━━━━━━━━━━━━━

👤 *Username:* `@{username}`

━━━━━━━━━━━━━━━━━━━━━━  
<<<<<<< HEAD
🎚️ *LEVEL & XP*  
Level: *{level}*  
XP: *{xp} / {max_xp}*

━━━━━━━━━━━━━━━━━━━━━━  
❤️ *STATS*  
HP: *{hp} / {max_hp}*  
Power: *{power}*

━━━━━━━━━━━━━━━━━━━━━━  
     *RESOURCES*  
🪙 Coins: `{coins}`  
🔮 Orbs: `{essences}`  
🐚 Sea Shells: `{moonshards}`

━━━━━━━━━━━━━━━━━━━━━━  
📝 *Play more to grow stronger — the realm remembers those who act.*  
━━━━━━━━━━━━━━━━━━━━━━
=======

🎚️ *LEVEL & XP*  
*Level:* *{level}*  
*XP:* *{xp} / {max_xp}*

━━━━━━━━━━━━━━━━━━━━━━  

❤️ *STATS*  
*HP:* *{hp}* *(+{bonus_hp})*
*Power:* *{power}* *(+{bonus_power})*
*Agility:* *{agility}* *(+{bonus_agility})*
*Equiped Weapon:* *{equiped_weapon} *

━━━━━━━━━━━━━━━━━━━━━━  
📝 *Play more to grow stronger — the realm remembers those who act.*  
━━━━━━━━━━━━━━━━━━━━━━"""
>>>>>>> 0f7a004 (Initial commit)
    
    
    
    keyboard6 = [
    [
        InlineKeyboardButton("⚔️ Battle Stats", callback_data="battle_stats"),
        InlineKeyboardButton("🧭 Explore Stats", callback_data="explore_stats")
    ]
]

    reply_markup6 = InlineKeyboardMarkup(keyboard6)


    
    update.message.reply_text(stats_message,     reply_markup = reply_markup6 , 
parse_mode = ParseMode.MARKDOWN)

def button6(update,context):
    user_info = init_user(update,context)
    user_data = context.user_data
    
    query = update.callback_query
    query.answer()
    
    chosen_stats = query.data
    
    if chosen_stats == 'battle_stats':
        
        battles_played = user_info['battles_played']
        battles_won = user_info['battles_won']
        battles_lost = user_info['battles_lost']
        
        battle_text = f"""
*BATTLE STATS*

Battles Played: `{battles_played}`  
Battles Won: `{battles_won}`  
Battles Lost: `{battles_lost}`

_Keep fighting, warrior!_
"""
        reply_markup7=InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🎯 My Stats", callback_data="my_stats"),
        InlineKeyboardButton("🧭 Explore Stats", callback_data="explore_stats")
    ]
])

        query.edit_message_text(
        battle_text,
        reply_markup = reply_markup7,
        parse_mode = ParseMode.MARKDOWN)
        
    elif chosen_stats == 'explore_stats':
        
        explores_played = user_info['explores_played']
        explores_won = user_info['explores_won']
        explores_lost = user_info['explores_lost']
        
        explore_text = f"""
* EXPLORE STATS*

<<<<<<< HEAD
 *Explores Played:* `{explores_played}`  
=======
 *Explores Done:* `{explores_played}`  
>>>>>>> 0f7a004 (Initial commit)
 *Victories:* `{explores_won}`  
 *Defeats:* `{explores_lost}`

_Keep exploring, adventurer! _
"""
        reply_markup8=InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🎯 My Stats", callback_data="my_stats"),
        InlineKeyboardButton("⚔️ Battle Stats", callback_data="battle_stats")
    ]
])

        query.edit_message_text(
        explore_text,
        reply_markup=reply_markup8,
        parse_mode = ParseMode.MARKDOWN)
        
        
    elif chosen_stats == 'my_stats':
        
        username = user_info["username"]
        hp = user_info["hp"]
<<<<<<< HEAD
        max_hp = user_info["max_hp"]
        power = user_info["power"]
        level = user_info["level"]
        xp = user_info["xp"]
        max_xp = user_info["max_xp"]
        coins = user_info["Coins"]
        moonshards = user_info["Moonshards"]
        essences = user_info["Essences"]
        
        stats_message = f"""
`━━━━━━━━━━━━━━━━━━━━━━`
🏰 *CHARACTER PROFILE*
`━━━━━━━━━━━━━━━━━━━━━━`

👤 *Username:* @{username}

🏅 *Level:* `{level}`
📊 *XP:* `{xp}` / `{max_xp}`

❤️ *HP:* `{hp}` / `{max_hp}`
⚔️ *Power:* `{power}`

`━━━━━━━━━━━━━━━━━━━━━━`
🪙 *Coins:* `{coins}`
🔮 *Orbs:* `{essences}`
🐚 *Sea Shells:* `{moonshards}`

`━━━━━━━━━━━━━━━━━━━━━━`
📜 _Play more to grow stronger, hero._
"""
=======
        max_hp = user_info["hp"]
        power = user_info["power"]
        level = user_info["level"]
        agility = user_info["agility"]
        xp = user_info['xp']
        max_xp = user_info['max_xp']
        coins = user_info["coins"]
        moonshards = user_info["moonshards"]
        essences = user_info["essences"]
        equiped_weapon = user_info['equiped_weapon'] or 'No weapons or not equiped one'
        if not equiped_weapon or equiped_weapon not in user_info['user_weapons']:
          bonus_hp = 0
          bonus_power = 0
          bonus_agility = 0
      
        else:
          bonus_hp = user_info['user_weapons'][equiped_weapon].get('bonus_hp', 0)
          bonus_power = user_info['user_weapons'][user_info['equiped_weapon']]['bonus_power']
          bonus_agility = user_info['user_weapons'][user_info['equiped_weapon']]['bonus_agility']

        stats_message = f"""
━━━━━━━━━━━━━━━━━━━━━━
🏰 <b>CHARACTER PROFILE</b> 🏰
━━━━━━━━━━━━━━━━━━━━━━

👤 <b>Username:</b> @{username}

━━━━━━━━━━━━━━━━━━━━━━

🎚️ <b>LEVEL & XP</b>
<b>Level:</b> {level}
<b>XP:</b> {xp} / {max_xp}

━━━━━━━━━━━━━━━━━━━━━━

❤️ <b>STATS</b>
<b>HP:</b> {hp} (+{bonus_hp})
<b>Power:</b> {power} (+{bonus_power})
<b>Agility:</b> {agility} (+{bonus_agility})
<b>Equiped Weapon:</b> {equiped_weapon or 'No Weapon'}

━━━━━━━━━━━━━━━━━━━━━━

📝 <i>Play more to grow stronger — the realm remembers those who act.</i>
━━━━━━━━━━━━━━━━━━━━━━
"""



        
>>>>>>> 0f7a004 (Initial commit)
        keyboard6 = [
    [
        InlineKeyboardButton("⚔️ Battle Stats", callback_data="battle_stats"),
        InlineKeyboardButton("🧭 Explore Stats", callback_data="explore_stats")
    ]
]
<<<<<<< HEAD

        reply_markup6 = InlineKeyboardMarkup(keyboard6)
        
        query.edit_message_text(
        stats_message,
        reply_markup = reply_markup6,
        parse_mode = ParseMode.MARKDOWN)
    
        
        
        
# Handlers
=======
        reply_markup6 = InlineKeyboardMarkup(keyboard6)

        query.edit_message_text(
    text=stats_message,
    reply_markup=reply_markup6,
    parse_mode=ParseMode.HTML
)
 
def add(update,context):
  
  user_info = init_user(update,context)
  if update.effective_user.id not in ADMINS:
    update.message.reply_text('You are not authorized for this cmd ')
    return
  
  if  len(context.args) < 3:
    update.message.reply_text(
      '''*Please provide*
*Username* :- _The user to which you want item to add_
*Item* :- _The item you want to add_
*Amount* :- _How much you want to add_
      ''',
      parse_mode='Markdown')
    return
      
  target_userid = int(context.args[0])
  target_user_item = context.args[1]
  item_amount = int(context.args[2])
  target_user_item = target_user_item
  
  result = db.search(UserQuery.user_id == target_userid )
  
  
      
  if not result:
    update.message.reply_text(f'No user with {target_userid} found. ')
    return 
  
  user_data = result[0]
  new_value = user_data.get(target_user_item,0) + item_amount
  db.update({target_user_item:new_value},UserQuery.user_id == target_userid)
  
  
  update.message.reply_text(f"""
🎁 *Item Successfully Added!*

━━━━━━━━━━━━━━━━━━━━
👤 *User:* `{target_userid}`
📦 *Item:* `{target_user_item}`
➕ *Amount Added:* `{item_amount}`
📊 *New Total:* `{new_value}`
━━━━━━━━━━━━━━━━━━━━
""", parse_mode="Markdown")
  
def remove(update,context):
  
  user_info = init_user(update,context)
  if update.effective_user.id not in ADMINS:
    update.message.reply_text('You are not authorized for this cmd ')
    return
  
  if  len(context.args) < 3:
    update.message.reply_text(
      '''*Please provide*
*Username* :- _The user to which you want item to remove_
*Item* :- _The item you want to remove_
*Amount* :- _How much you want to remove_
      ''',
      parse_mode='Markdown')
    return
      
  target_userid = int(context.args[0])
  target_user_item = context.args[1]
  item_amount = int(context.args[2])
  target_user_item = target_user_item
  
  result = db.search(UserQuery.user_id == target_userid )
  
  
      
  if not result:
    update.message.reply_text(f'No user with {target_userid} found. ')
    return 
  
  user_data = result[0]
  new_value = user_data.get(target_user_item,0) - item_amount
  db.update({target_user_item:new_value},UserQuery.user_id == target_userid)
  
  
  update.message.reply_text(f"""
 *Item Successfully removed!*

━━━━━━━━━━━━━━━━━━━━
👤 *User:* `{target_userid}`
📦 *Item:* `{target_user_item}`
➕ *Amount Removed* `{item_amount}`
📊 *New Total:* `{new_value}`
━━━━━━━━━━━━━━━━━━━━
""", parse_mode="Markdown")  


EQUIP_WEAPON = range(0)


#my_gear
def my_gear(update,context):
  chat_type = update.effective_chat.type
  user_info = init_user(update,context)
  user_data = context.user_data
  
  if chat_type in ['group','supergroup']:
    update.message.reply_text(
      f"""
  🛡️ <b>Your Battle Gear</b>
  
  ━━━━<b> Your equiped weapon </b>━━━━
  
  🔹 <b>Equipped Weapon:</b> {user_info['equiped_weapon']}
  
  ━━━━ 🧪 <b>Magical Items </b>🧪 ━━━━
  
  <i>Coming Soon...</i>
  
  ━━━━━━━━━━━━━━━━━━━━
  <b> Use /mygear in DM to edit your gear </b>
  
  """,
      parse_mode=ParseMode.HTML
  )
  
  
  else:
    
    my_gear_keyboard = [
      [InlineKeyboardButton("🗡️ Equip Weapon", callback_data='equip_weapon')],
      [InlineKeyboardButton("🧪 Edit Magical Items", callback_data='edit_magic')]
  ]
  
    my_gear_markup = InlineKeyboardMarkup(my_gear_keyboard)
    
    update.message.reply_text(
      f"""
  🛡️ *Your Battle Gear*
  
  ━━━━<b> Your equiped Weapon </b>━━━━
  
  🔹 *Equipped Weapon:* {user_info['equiped_weapon']}
  
  ━━━━ 🧪 *Magical Items* 🧪 ━━━━
  
  _Coming Soon..._
  
  ━━━━━━━━━━━━━━━━━━━━
  """,
      parse_mode="Markdown",
      reply_markup = my_gear_markup
  )
    return ConversationHandler.END

def my_gear_button(update,context):
  
  user_info = init_user(update,context)
  
  query = update.callback_query
  query.answer()
  
  my_gear_option = query.data
  
  if my_gear_option == 'edit_magic':
    query.edit_message_text(
    f"""
🧪 *Edit Magical Items*

━━━━━━━━━━━━━━━━━━━━

✨ This feature is *coming soon*...
Get ready to enhance your powers!

━━━━━━━━━━━━━━━━━━━━
""",
    parse_mode="Markdown"
)

  elif my_gear_option == 'equip_weapon':
    user_weapons = user_info['user_weapons']
    weapons_list = '\n'.join([f"🔸 `{w}`" for w in user_weapons])  # Replace `user_weapons` with your weapon list variable

    query.edit_message_text(
    f"""
🗡️ *Equip Weapon*

━━━━━━━━━━━━━━━━━━━━

Here are your available weapons:

{weapons_list if weapons_list else "You have no weapons yet."}

━━━━━━━━━━━━━━━━━━━━
📤 Send the *weapon name* to equip it.
━━━━━━━━━━━━━━━━━━━━
""",
    parse_mode="Markdown"
)
    return EQUIP_WEAPON

def equip_weapon(update,context):
  
  sent_weapon_name = update.message.text.title()
  user_info = init_user(update,context)
  
  if sent_weapon_name in list(weapon_list.keys()):
    if sent_weapon_name not in list(user_info['user_weapons'].keys()):
      update.message.reply_text(
      """
  🚫 *Oops!*
  
  ━━━━━━━━━━━━━━━━━━━━
  
  You do *not* own this weapon.
  
  Please check your inventory and try again with a valid weapon name.
  
  ━━━━━━━━━━━━━━━━━━━━
  """,
      parse_mode="Markdown"
  )
      return EQUIP_WEAPON
    
    else:
      user_info['equiped_weapon'] = sent_weapon_name
      save_user_data(user_info)
      update.message.reply_text(
      f"""
  ✅ *Weapon Equipped!*
  
  ━━━━━━━━━━━━━━━━━━━━
  
  You have successfully equipped the weapon:
  🗡️ *{sent_weapon_name.title()}*
  
  Get ready for battle, warrior!
  
  ━━━━━━━━━━━━━━━━━━━━
  """,
      parse_mode="Markdown"
  )
      return ConversationHandler.END
      
  else:
    update.message.reply_text(
    f"""
❌ *Invalid Weapon Name!*

━━━━━━━━━━━━━━━━━━━━

There is no such weapon .
Please double-check and send the correct weapon name.

━━━━━━━━━━━━━━━━━━━━
""",
    parse_mode="Markdown"
)
    return EQUIP_WEAPON
    
    

gear_conv_handler = ConversationHandler(
    entry_points=[
        CallbackQueryHandler(my_gear_button, pattern='^(equip_weapon)$')
    ],
    states={
        EQUIP_WEAPON: [
            MessageHandler(Filters.text & ~Filters.command, equip_weapon)
        ],
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)
  
  
def view(update,context):
  user_info = init_user(update,context)
  
  
  
  if len(context.args)<1:
    update.message.reply_text(
    """🚫 *Oops! You're not using this command correctly.*

📌 Here's how to use it:
`/view <weapon>`

🧪 *Example:*
`/view Bronze Sword`

Try again using the correct format! 😊""",
    parse_mode="Markdown"
)
    return 
  item_to_view = ' '.join(context.args).title()
  
  
  
  if item_to_view not in list(weapon_list.keys()):
    update.message.reply_text(
    """❌ *Invalid Weapon Name!*

━━━━━━━━━━━━━━━━━━━━
It seems like the item you're trying to view doesn't exist.

🧠 *Tip:* Use the command like this:  
`/view Bronze Sword`
━━━━━━━━━━━━━━━━━━━━
""",
    parse_mode="Markdown"
)
  else:
    if item_to_view not in list(user_info['user_weapons'].keys()):
      weapon_hp = weapon_list[item_to_view]['bonus_hp']
      weapon_power = weapon_list[item_to_view]['bonus_power']
      weapon_agility=weapon_list[item_to_view]['bonus_agility']
      weapon_rarity = weapon_list[item_to_view]['rarity']
      weapon_photo = weapon_list[item_to_view]['photo']
      update.message.reply_photo(photo = weapon_photo , caption = 
    f"""
🗡️ *Item Info*

━━━━━━━━━━━━━━━━━━━━

🔹 *Item:* `{item_to_view}`
🌟 *Rarity:* `{weapon_list[item_to_view]["rarity"].title()}`

━━ ⚔️ *Weapon Stats* ⚔️ ━━

💥 *Power:* `{weapon_list[item_to_view]["bonus_power"]}`
❤️ *HP:* `{weapon_list[item_to_view]["bonus_hp"]}`
🏃 *Agility:* `{weapon_list[item_to_view]["bonus_agility"]}`

━━━━━━━━━━━━━━━━━━━━
""",
    parse_mode="Markdown"
)
    else :
      weapon_photo = weapon_list[item_to_view]['photo']
      user_weapon_data = user_info["user_weapons"].get(item_to_view)

      update.message.reply_photo(photo = weapon_photo,
      caption=
    f"""
🗡️ *Item Info*

━━━━━━━━━━━━━━━━━━━━

🔹 *Item:* {item_to_view}
🌟 *Rarity:* {weapon_list[item_to_view]["rarity"].title()}

━━ ⚔️ *Weapon Stats* ⚔️ ━━

💥 *Power:* {user_info['user_weapons'][item_to_view]["bonus_power"]}
❤️ *HP:* {user_info['user_weapons'][item_to_view]["bonus_hp"]}
🏃 *Agility:* {user_info['user_weapons'][item_to_view]["bonus_agility"]}

━━🧪 *Progress Stats* 🧪 ━━

📈 *Level:* {user_info['user_weapons'][item_to_view]["weapon_level"]}
🔸 *XP:* {user_info['user_weapons'][item_to_view]["weapon_xp"]}/{user_info['user_weapons'][item_to_view]["weapon_max_xp"]}

━━━━━━━━━━━━━━━━━━━━
""",
    parse_mode="Markdown"
)
      
def give(update, context):
    user_info = init_user(update, context)
   
    if len(context.args) < 2:
        update.message.reply_text(
            '''❌ **Oops! You used the command the wrong way.**  
To give an item, please use this format:  
➡️ /give item amount  

For example: /give essences 3  

Try again! ''')
        return
  
    if not update.message.reply_to_message:
        update.message.reply_text(
            '''You didn’t reply to anyone’s message.
Please reply to a message to use this command!''')
        return
  
    taker = update.message.reply_to_message.from_user
    giver = update.effective_user
  
    taker_data = db.search(UserQuery.user_id == taker.id)
    if not taker_data:
        update.message.reply_text(
            '''The user you replied to has not started the bot yet!
Please reply to a person who has started the bot.''')
        return
    
    item_to_give = context.args[0]
    
    if item_to_give not in ['essences', 'essence', 'moonshard', 'moonshards', 'coins', 'coin']:
      update.message.reply_text('You cannot give this item!')
      return

    if item_to_give in ['essence', 'moonshard', 'coin']:
      item_to_give += 's'
      pass
    try:
        amount_to_give = int(context.args[1])  # Convert amount to integer
    except ValueError:
        update.message.reply_text("❌ The amount must be a number!")
        return
  
    # Check if giver has enough items
    if user_info.get(item_to_give, 0) < amount_to_give:
        update.message.reply_text(
            f'''You do not have enough {item_to_give}''')
        return
    
    # Reduce giver's items
    user_info[item_to_give] -= amount_to_give

    # Get taker's full data (assuming taker_data is a list of dicts)
    taker_info = taker_data[0]

    # Add to taker's items
    taker_info[item_to_give] = taker_info.get(item_to_give, 0) + amount_to_give

    # Save both users' data (You need a function to update both in your DB)
    save_user_data(user_info)          # Save giver's updated data
    db.update(taker_info, UserQuery.user_id == taker.id)  # Save taker's updated data

    update.message.reply_text(
        f'Sent {amount_to_give} {item_to_give} to {taker.first_name}!')
        
def get_file_id(update, context):
    photo = update.message.photo[-1]  # get highest resolution photo
    file_id = photo.file_id
    update.message.reply_text(f"File ID: <code>{file_id}</code>",parse_mode=ParseMode.HTML)

def open_keyboard(update, context):
    # One persistent button
    explore_button = [[KeyboardButton("/explore")],[KeyboardButton("/mygear"),KeyboardButton("/close")]]
    
    open_markup = ReplyKeyboardMarkup(
        explore_button, 
        resize_keyboard=True,
        one_time_keyboard=False
    )
    
    update.message.reply_text(
        "Opened keyboard!",
        reply_markup=open_markup
    )



def remove_keyboard(update, context):
    update.message.reply_text(
        "Keyboard removed ✅",
        reply_markup=ReplyKeyboardRemove()
    )
  
#Handlers
>>>>>>> 0f7a004 (Initial commit)
dispatcher.add_handler(CommandHandler('reset_user',reset_user))
dispatcher.add_handler(CommandHandler('reset_all',reset_all))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('explore', explore))
dispatcher.add_handler(CommandHandler('shop', shop))
dispatcher.add_handler(CommandHandler('guess',guess))
dispatcher.add_handler(CommandHandler('toss',toss))
dispatcher.add_handler(CommandHandler('mystats',stats))
<<<<<<< HEAD

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(shop_conv)
dispatcher.add_handler(CallbackQueryHandler(button2,pattern='^(Essences|Moonshards)$'))  # Handles shop buttons
dispatcher.add_handler(CallbackQueryHandler(button,pattern='^(hunt|walk)$'))   # Handles hunt/walk
dispatcher.add_handler(CallbackQueryHandler(button4,pattern='^(heads|tails)$'))
dispatcher.add_handler(CallbackQueryHandler(button6,pattern='^(battle_stats|explore_stats|my_stats)$'))
=======
dispatcher.add_handler(CommandHandler('myinventory',inventory))
dispatcher.add_handler(CommandHandler('add',add))
dispatcher.add_handler(CommandHandler('remove',remove))
dispatcher.add_handler(CommandHandler('view',view))
dispatcher.add_handler(CommandHandler('mygear',my_gear))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, get_file_id))
dispatcher.add_handler(CommandHandler("open", open_keyboard))
dispatcher.add_handler(CommandHandler("close",remove_keyboard))
dispatcher.add_handler(conv_handler)
dispatcher.add_handler(shop_conv)
dispatcher.add_handler(weapon_conv_handler)
dispatcher.add_handler(gear_conv_handler)
dispatcher.add_handler(CommandHandler('give',give))
dispatcher.add_handler(CallbackQueryHandler(inv_button,pattern='^(inv_weapons|inv_magic|inv_main)$'))
dispatcher.add_handler(CallbackQueryHandler(button2,pattern='^(resource_shop|weapon_shop|magic_shop)$'))  # Handles shop buttons
dispatcher.add_handler(CallbackQueryHandler(button,pattern='^(attack|retreat)$'))   # Handles hunt/walk
dispatcher.add_handler(CallbackQueryHandler(explore_button,pattern='^(hunt)$'))
dispatcher.add_handler(CallbackQueryHandler(button4,pattern='^(heads|tails)$'))
dispatcher.add_handler(CallbackQueryHandler(button6,pattern='^(battle_stats|explore_stats|my_stats)$'))
dispatcher.add_handler(CallbackQueryHandler(my_gear_button,pattern='^(equip_weapon|edit_magic)$'))
>>>>>>> 0f7a004 (Initial commit)
updater.start_polling()
updater.idle()