#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from telegram import *
from telegram.ext import *
import random
import time
from tinydb import *

updater = Updater('8192198859:AAFlFmKDANGsM51kfdAoAYdaBoJjrfDqFXo', use_context=True)
dispatcher = updater.dispatcher

db = TinyDB('players.json')
UserQuery = Query()

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
        'Coins': 500,
        'Essences': 0,
        'Moonshards': 0,
        'max_xp': 100,
        'battles_played': 0,
        'explores_won': 0,
        'explores_lost': 0,
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

def reset_all(update, context):
    user_id = update.effective_user.id

    if user_id not in ADMINS:
        update.message.reply_text("❌ You are not authorized to use this command.")
        return

    db.truncate()
    update.message.reply_text("✅ All user data has been reset.")    
  

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
            
def xp_system(update,context):
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    
    if int(user_info['max_xp']) <= int(user_info['xp']):
        user_info['xp'] -= user_info['max_xp']
        user_info['level'] += 1
        user_info['max_xp'] += 100*user_info['level']
        user_info['max_hp'] += 20*user_info['level']
        user_info['power'] += 10*user_info['level']
        save_user_data(user_info)
        chat_id = update.effective_chat.id
        update.bot.send_message(chat_id = chat_id , text = 'Congratulations! you leveled up')
    
def start(update, context):
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    images = [
    "https://files.catbox.moe/x4ah5l.jpg",  # Replace with actual file_id or direct URL
    "https://files.catbox.moe/lt70jg.jpg"
]

    chosen_image = random.choice(images)

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

def help(update, context):
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    update.message.reply_text(
    """*🤖 Bot Command List*

Here are all the cool things you can do:

• `/start` – 🌟 _Begin your journey!_  
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
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    if update.message.chat.type != 'private':
        update.message.reply_text("❌ Use this command in DM!")
        return
        
     
     
    current_monster = random.choice(list(monster_db.keys()))
     
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

def button(update, context):
    
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    query = update.callback_query
    query.answer()
    answer = query.data
    
    current_monster = context.user_data['current_monster']
    monster_hp = context.user_data['monster_hp']
    monster_dmg = context.user_data['monster_dmg']
    
    
    if answer == 'hunt':
         
        user_info['hp'] -= monster_dmg
        monster_hp -= user_info['power']
        save_user_data(user_info)
        # Update stored HPs
        
        context.user_data['monster_hp'] = monster_hp
        
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
    

        
    
    
def profile(update, context):
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
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
    )

def button2(update, context):
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    query = update.callback_query
    query.answer()
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
    
def handle_quantity(update, context):
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    item = context.user_data['item_to_buy']
    
    try:
        amount = int(update.message.text)
        if amount <= 0:
            update.message.reply_text("❌ Please enter a number greater than 0.")
            return CHOOSE_QUANTITY
    except:
        update.message.reply_text("❌ Please enter a valid number.")
        return CHOOSE_QUANTITY

    if item == 'Essences':
        price = 1000
        if user_info['Coins'] >= amount * price:
            user_info['Coins'] -= amount * price
            user_info['Essences'] += amount
            save_user_data(user_info)
            update.message.reply_text(f"✅ Bought {amount} Essences for {amount * price} coins!")
        else:
            update.message.reply_text("❌ Not enough coins!")

    elif item == 'Moonshards':
        price = 100
        if user_info['Coins'] >= amount * price:
            user_info['Coins'] -= amount * price
            user_info['Moonshards'] += amount
            save_user_data(user_info)
            update.message.reply_text(f"✅ Bought {amount} Moonshards for {amount * price} coins!")
        else:
            update.message.reply_text("❌ Not enough coins!")

    return ConversationHandler.END
    
    
shop_conv = ConversationHandler(
    entry_points=[CallbackQueryHandler(button2, pattern='^Essences|Moonshards$')],
    states={
        CHOOSE_QUANTITY: [MessageHandler(Filters.text & ~Filters.command, handle_quantity)],
    },
    fallbacks=[],
)

guess_num = range(1)

def guess(update,context):
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    if update.message.chat.type != 'private':
        update.message.reply_text(
    text="🕵️‍♂️ *Guessing Game Notice!*\n\nPlease use this command in a *private chat* with me.\nTap my profile and click *'Start'* to play!",
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
    "🎯 *Welcome to the Number Guessing Game!*\n\n"
    "🔢 A number between *1 and 100* has been chosen...\n"
    "❓ Do you want to try and guess it?\n\n"
    "🏆 *Reward:* +100 Coins\n"
    "🕐 *Note:* You can play once every 1 minute.",
    parse_mode=ParseMode.MARKDOWN,
    reply_markup=reply_markup3)
    
def button3(update,context):
    
    
    
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    query=update.callback_query
    query.answer()
    
    user_choice = query.data
    
    
    if user_choice == 'yes':
        query.edit_message_text(
    text="📨 *Great!* Now send me a number between *1 and 100* to guess it.\n\n🎯 Let’s see if you can hit the right number!",
    parse_mode=ParseMode.MARKDOWN
)
        return guess_num
        
    elif user_choice == 'no':
        query.edit_message_text(
    text="🚪 *You chose to walk away...*\nNo worries, come back anytime to test your luck! 🎲😉",
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
            user_info['Coins']+=100
            del context.user_data['number']
            user_info['xp']+=25
            save_user_data(user_info)
            xp_system(update,context)
            update.message.reply_text(
    "🎉 *You guessed it right!* 🎯\n\n💰 You earned *100 Coins* and gained *25 XP*! 🧠🔥\nKeep it up, champion!",
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
    "🎯 *Time to Toss the Coin!*\n\nChoose your side wisely:",
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
    f"🎉 *The coin landed on:* `{context.user_data['bot_option'].capitalize()}`\n"
    "✅ *You won the toss!*\n"
    "💰 You earned *20 coins* and gained *15 XP!*",
    parse_mode=ParseMode.MARKDOWN
)
        user_info['Coins'] += 20
        user_info['xp']+=15
        save_user_data(user_info)
        xp_system(update,context)
        
    else:
        query.edit_message_text(
    f"😢 *The coin landed on:* `{context.user_data['bot_option'].capitalize()}`\n"
    "❌ *You lost the toss!*\n"
    "💸 You lost *10 coins!*",
    parse_mode=ParseMode.MARKDOWN
)
        user_info['Coins']-= 10
        save_user_data(user_info)
        
def stats(update,context):
    user_id = update.effective_user.id
    user_info = init_user(update,context)
    user_data = context.user_data
    
    username = user_info["username"]
    hp = user_info["hp"]
    max_hp = user_info["max_hp"]
    power = user_info["power"]
    level = user_info["level"]
    xp = user_info["xp"]
    max_xp = user_info["max_xp"]
    coins = user_info["Coins"]
    moonshards = user_info["Moonshards"]
    essences = user_info["Essences"]
    
    stats_message = f"""
━━━━━━━━━━━━━━━━━━━━━━  
🏰 *CHARACTER PROFILE* 🏰  
━━━━━━━━━━━━━━━━━━━━━━

👤 *Username:* `@{username}`

━━━━━━━━━━━━━━━━━━━━━━  
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

 *Explores Played:* `{explores_played}`  
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
        keyboard6 = [
    [
        InlineKeyboardButton("⚔️ Battle Stats", callback_data="battle_stats"),
        InlineKeyboardButton("🧭 Explore Stats", callback_data="explore_stats")
    ]
]

        reply_markup6 = InlineKeyboardMarkup(keyboard6)
        
        query.edit_message_text(
        stats_message,
        reply_markup = reply_markup6,
        parse_mode = ParseMode.MARKDOWN)
    
        
        
        
# Handlers
dispatcher.add_handler(CommandHandler('reset_user',reset_user))
dispatcher.add_handler(CommandHandler('reset_all',reset_all))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('explore', explore))
dispatcher.add_handler(CommandHandler('shop', shop))
dispatcher.add_handler(CommandHandler('guess',guess))
dispatcher.add_handler(CommandHandler('toss',toss))
dispatcher.add_handler(CommandHandler('mystats',stats))

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(shop_conv)
dispatcher.add_handler(CallbackQueryHandler(button2,pattern='^(Essences|Moonshards)$'))  # Handles shop buttons
dispatcher.add_handler(CallbackQueryHandler(button,pattern='^(hunt|walk)$'))   # Handles hunt/walk
dispatcher.add_handler(CallbackQueryHandler(button4,pattern='^(heads|tails)$'))
dispatcher.add_handler(CallbackQueryHandler(button6,pattern='^(battle_stats|explore_stats|my_stats)$'))
updater.start_polling()
updater.idle()