import telebot
from telebot import types

TOKEN = '8978400880:AAHDE8VhF5LTOsrhEFLw1PmrRUnTnS6D_i8'
bot = telebot.TeleBot(TOKEN)

# رقم الشام كاش الخاص بالمتجر
SHAM_CASH_NUMBER = "4771260739597270"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = types.KeyboardButton('🔥 فري فاير')
    btn2 = types.KeyboardButton('🔫 شدات ببجي')
    btn3 = types.KeyboardButton('💰 تعبئة الرصيد')
    btn4 = types.KeyboardButton('👤 رصيدي')
    btn5 = types.KeyboardButton('🌟 عروض المشاهير والشخصيات')
    btn6 = types.KeyboardButton('🛒 شروط وشحن المتجر')
    btn7 = types.KeyboardButton('📞 الدعم الفني والتواصل')
    
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    markup.add(btn6)
    markup.add(btn7)
    
    welcome_text = (
        "🎮 أهلاً بك من جديد في متجر TopUp Charger\n"
        "اختر الخدمة المطلوبة:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.strip()
    
    if text == '🔥 فري فاير':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('100 + 10 FreeFire'))
        markup.add(types.KeyboardButton('210 + 21 FreeFire'))
        markup.add(types.KeyboardButton('530 + 53 FreeFire'))
        markup.add(types.KeyboardButton('1080 + 108 FreeFire'))
        markup.add(types.KeyboardButton('2200 + 220 FreeFire'))
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "🔥 <b>يرجى اختيار الحزمة المطلوبة من الأسفل:</b>", parse_mode='HTML', reply_markup=markup)
        
    elif text == '100 + 10 FreeFire':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "✅ لقد اخترت حزمة:\n• 100 + 10 FreeFire By ID (السعر: 13,500 ل.س)\n\n📝 يرجى إرسال الـ (ID) الخاص بك الآن في الشات كرسالة نصية لخصم المبلغ والشحن:", reply_markup=markup)
    elif text == '210 + 21 FreeFire':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "✅ لقد اخترت حزمة:\n• 210 + 21 FreeFire By ID (السعر: 27,000 ل.س)\n\n📝 يرجى إرسال الـ (ID) الخاص بك الآن في الشات كرسالة نصية لخصم المبلغ والشحن:", reply_markup=markup)
    elif text == '530 + 53 FreeFire':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "✅ لقد اخترت حزمة:\n• 530 + 53 FreeFire By ID (السعر: 68,000 ل.س)\n\n📝 يرجى إرسال الـ (ID) الخاص بك الآن في الشات كرسالة نصية لخصم المبلغ والشحن:", reply_markup=markup)
    elif text == '1080 + 108 FreeFire':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "✅ لقد اخترت حزمة:\n• 1080 + 108 FreeFire By ID (السعر: 136,000 ل.س)\n\n📝 يرجى إرسال الـ (ID) الخاص بك الآن في الشات كرسالة نصية لخصم المبلغ والشحن:", reply_markup=markup)
    elif text == '2200 + 220 FreeFire':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "✅ لقد اخترت حزمة:\n• 2200 + 220 FreeFire By ID (السعر: 275,000 ل.س)\n\n📝 يرجى إرسال الـ (ID) الخاص بك الآن في الشات كرسالة نصية لخصم المبلغ والشحن:", reply_markup=markup)
        
    elif text == '🔫 شدات ببجي':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('60 شدة روبوت'))
        markup.add(types.KeyboardButton('325 شدة روبوت'))
        markup.add(types.KeyboardButton('660 شدة روبوت'))
        markup.add(types.KeyboardButton('1800 شدة روبوت'))
        markup.add(types.KeyboardButton('3850 شدة روبوت'))
        markup.add(types.KeyboardButton('8100 شدة روبوت'))
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "🔫 <b>اختر حزمة شدات ببجي المطلوبة:</b>", parse_mode='HTML', reply_markup=markup)
        
    elif text == '60 شدة روبوت':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "✅ لقد اخترت حزمة:\n• 60 شدة روبوت (السعر: 12,000 ل.س)\n\n📝 يرجى إرسال الـ (ID) الخاص بك الآن في الشات كرسالة نصية لخصم المبلغ والشحن:", reply_markup=markup)
    elif text == '325 شدة روبوت':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "✅ لقد اخترت حزمة:\n• 325 شدة روبوت (السعر: 65,000 ل.س)\n\n📝 يرجى إرسال الـ (ID) الخاص بك الآن في الشات كرسالة نصية لخصم المبلغ والشحن:", reply_markup=markup)
    elif text == '660 شدة روبوت':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "✅ لقد اخترت حزمة:\n• 660 شدة روبوت (السعر: 132,000 ل.س)\n\n📝 يرجى إرسال الـ (ID) الخاص بك الآن في الشات كرسالة نصية لخصم المبلغ والشحن:", reply_markup=markup)
    elif text == '1800 شدة روبوت':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "✅ لقد اخترت حزمة:\n• 1800 شدة روبوت (السعر: 335,000 ل.س)\n\n📝 يرجى إرسال الـ (ID) الخاص بك الآن في الشات كرسالة نصية لخصم المبلغ والشحن:", reply_markup=markup)
    elif text == '3850 شدة روبوت':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "✅ لقد اخترت حزمة:\n• 3850 شدة روبوت (السعر: 690,000 ل.س)\n\n📝 يرجى إرسال الـ (ID) الخاص بك الآن في الشات كرسالة نصية لخصم المبلغ والشحن:", reply_markup=markup)
    elif text == '8100 شدة روبوت':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "✅ لقد اخترت حزمة:\n• 8100 شدة روبوت (السعر: 1,400,000 ل.س)\n\n📝 يرجى إرسال الـ (ID) الخاص بك الآن في الشات كرسالة نصية لخصم المبلغ والشحن:", reply_markup=markup)
        
    elif text == '💰 تعبئة الرصيد':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('💳 شام كاش'))
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "💳 <b>اختر طريقة تعبئة الرصيد المتاحة:</b>", parse_mode='HTML', reply_markup=markup)
        
    elif text == '💳 شام كاش':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        sham_message = (
            "💳 <b>الشحن عبر شام كاش:</b>\n\n"
            "يرجى التحويل إلى رقم الحساب التالي:\n"
            f"<code>{SHAM_CASH_NUMBER}</code>\n\n"
            "بعد إتمام التحويل، يرجى إرسال <b>رقم العملية (الحوالة)</b> هنا لتتم إضافة الرصيد لحسابك فوراً."
        )
        bot.send_message(message.chat.id, sham_message, parse_mode='HTML', reply_markup=markup)
        
    elif text == '👤 رصيدي':
        bot.send_message(message.chat.id, "👤 رصيدك الحالي: 0 ل.س")
    elif text == '🌟 عروض المشاهير والشخصيات':
        bot.send_message(message.chat.id, "🌟 عروض المشاهير والشخصيات متوفرة حسب الطلب. تواصل مع الدعم للاستفسار.")
    elif text == '🛒 شروط وشحن المتجر':
        bot.send_message(message.chat.id, "🛒 شروط وشحن المتجر:\n1. تأكد من صحة الـ ID قبل الإرسال.\n2. تتم عملية الشحن مباشرة بعد خصم المبلغ.")
    elif text == '📞 الدعم الفني والتواصل':
        bot.send_message(message.chat.id, "📞 للتواصل مع الدعم الفني والمساعدة يرجى مراسلة الإدارة عبر المعرف التالي:\n@ghadeershas", parse_mode='HTML')
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('/start'))
        bot.send_message(message.chat.id, "✅ لقد استلمنا رقم العملية أو الـ (ID) الخاص بك بنجاح وستتم معالجة الطلب.\nللعودة للقائمة الرئيسية اضغط على الزر أدناه:", reply_markup=markup)

bot.infinity_polling()
