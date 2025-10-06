import telebot
from telebot import types
import logging

# === Configuration du log (mode debug) ===
telebot.logger.setLevel(logging.DEBUG)
logger = telebot.logger

# === Ton token ===
TOKEN = "8402955738:AAGAp2Z0Lyr8DDccr3p5a5Q5UmdWhuQBFOQ"
bot = telebot.TeleBot(TOKEN)

# === Liens et code promo ===
AFFILIATE_LINK = "https://1wvdmy.life/?p=fo84"
PROMO_CODE = "80VIP"

# === Image et message de présentation ===
WELCOME_IMAGE = "https://www.google.com/imgres?imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D433057215785552&imgrefurl=https%3A%2F%2Fwww.facebook.com%2Fgroups%2F1501485943767666%2F&h=1099&w=1152&tbnid=DKIVQPWogT9sdM&source=sh%2Fx%2Fsaves%2Fuv%2Fm5%2F3&tbnh=436&tbnw=458&usg=AI4_-kSAxFdigSsyX2Gp3az5orr7j3psAQ&vet=1&docid=k05AwQYtq9x_fM&kgs=d4799e556a74004f"
WELCOME_CAPTION = (
    f"🔥 Bienvenue sur le bot officiel 1WIN 🔥\n\n"
    f"💰 Utilise le code promo : {PROMO_CODE}\n"
    "et profite de ton bonus exclusif !"
)

print("[SYSTEM] Initialisation du bot 1WIN...")

# === Gestion de la commande /start ===
@bot.message_handler(commands=["start"])
def handle_start(message):
    print(f"[INFO] L'utilisateur {message.from_user.username} a démarré le bot.")

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("📝 S’inscrire maintenant", url=AFFILIATE_LINK)
    btn2 = types.InlineKeyboardButton("✅ Vérifier mon inscription", callback_data="verify")
    markup.add(btn1)
    markup.add(btn2)

    bot.send_photo(
        message.chat.id,
        photo=WELCOME_IMAGE,
        caption=(
            f"Bienvenue {message.from_user.first_name or 'cher utilisateur'} 👋\n\n"
            f"💰 Utilise le code promo : {PROMO_CODE}\n\n"
            "👇 Clique ci-dessous pour t’inscrire :"
        ),
        reply_markup=markup,
    )

# === Gestion du bouton de vérification ===
@bot.callback_query_handler(func=lambda call: call.data == "verify")
def handle_verify(call):
    print(f"[INFO] Vérification d’inscription demandée par {call.from_user.username}")
    bot.answer_callback_query(call.id, "Vérification en cours...")
    bot.send_message(
        call.message.chat.id,
        "🔍 Vérification en cours...\n\n"
        "❌ Aucun compte trouvé avec le code promo 80VIP.\n\n"
        "➡️ Réessaie de t’inscrire ici : " + AFFILIATE_LINK,
    )

# === Démarrage du bot ===
print("[SYSTEM] Bot 1WIN lancé avec succès ✅")
print("[SYSTEM] En attente d'interactions...")

bot.infinity_polling(skip_pending=True)
