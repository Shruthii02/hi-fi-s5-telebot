import telebot
from telebot import types

help_msg="""📤let's chat like this

Iam not case sensitive😉😁

/start  👉 Enter start and you can wake me up !!

/help   👉 U see...I don't help you😉😂

/timetable 👉 I can get you S5 timetable

/subject_code 👉 To provide you all resources of S5 subjects --> Syllabus, Notes and Previous year QP's

                           OR

/subject_name in short    eg: (/adc, /lic, /dsp, /mfe ,/dm,/cs)


eg: /ECT303 or /dsp for Digital Signal Processing


/contribute 👉 For contributing any new study material to the bot📑

/suggest 👉 For your suggestions for my improvement😎


I can't reply for incorrect commands or chats🤫


More features will get updated.😎

"""


contribute_msg= """ Thank you for your interest in contributing to Hi-Fi S5!

I will accept anything 🤗 (Notes,You Tube Video links, Previous Year QP's etc...)

Kindly use the following link to share your study materials. 👇
🔗 https://forms.gle/eD6uupDHoWNCmK4m6

Your contribution is greatly appreciated! 📚🙌😄

"""

suggest_msg= """Calling all genius inventors, brainstormers, and enthusiasts!

 Hi-Fi S5 is in need of your superpowers! Have an idea to make this bot even more amazing?

   Don't keep it hidden in your secret lair! Share your mind-boggling suggestions using the mighty link below.
   🔗https://forms.gle/xk8qYCo81p4ABqK8A

   Together, we'll transform this bot into a legendary hero of education! Pow! 💥🦸‍♂️📚😄

"""


welcome_msg="""🤖Welcome to Hi-Fi S5 !🤖

I am eager to help you with anything to reach your goals in this semester..,

Need study materials📚, timetable🗓️, syllabus📄 or other information to help you with your S5??

   Let us study together and achieve academic success!❤️

   Plan ahead!!    Here is the University Sem exam timetable to plan your study👇
/timetable

Need any help??  ➡️/help

You have something new to share with me?🤩 Hurry up!! Click on the link and pass me things..😊 👇
 /contribute

I know., you have got better ideas this time., Suggest your points for my progress..!😁 👇
/suggest


   Hit Continue to explore ➡️/Continue
   """

time_table="""🕰️5th SEM EXAM TIMETABLE

🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽

🗓️Jan 4 (Thursday)    ➡️ Linear Integrated Circulits (ECT301)


🗓️Jan 8 (Monday)      ➡️ Digital Signal Processing (ECT 303)


🗓️Jan 11 (Thursday)   ➡️ Analog And Digital Communication (ECT 305)


🗓️Jan 16 (Tuesday)    ➡️ Control System (ECT 307)


🗓️Jan 19 (Friday)     ➡️ Industrial Economics & Foreign Trade (HUT 300) / Management for Engineers (HUT 310)


🗓️Jan 22 (Monday)     ➡️ Disaster Management (MCN 301)



✨✨Hit Continue to explore✨✨
/Continue
"""

Continue =""" 📔Select the Subject📔

🎯 Linear Integrated Circuits (ECT301) ↙️
 /ECT301


🎯 Digital Signal Processing (ECT 303) ↙️
 /ECT303


🎯 Analog And Digital Communication (ECT 305) ↙️
 /ECT305


🎯 Control System (ECT 307)  ↙️
 /ECT307


🎯 Management for Engineers (HUT 310) ↙️
 /HUT310


🎯 Disaster Management (MCN 301) ↙️
 /MCN301



"""

ECT301= """ 💡 Linear Integrated Circulits (ECT301) 💡
 (No of Credits- 4)


📄Syllabus 👇

https://shorturl.at/qwBC8

📝Notes 👇

https://shorturl.at/evT39


❔Previous year QP's 👇

https://shorturl.at/clFNU

 🎥Videos 👇

https://shorturl.at/fpwZ3

🤖 Contribute a new material 👇
 /contribute


 Any suggestions?🫡
 /suggest


"""

ECT303= """ 🚦 Digital Signal Processing (ECT 303) 🚦
 (No of Credits- 4)


📄Syllabus 👇

 https://rb.gy/8ve1y6

📝Notes 👇

https://rb.gy/dxy7vf

❔Previous year QP's 👇

https://rb.gy/6ahor5

 🎥Videos 👇

https://shorturl.at/zBP78

 🤖 Contribute a new material 👇
 /contribute


 Any suggestions?🫡
 /suggest



"""

ECT305= """ 🖥️ Analog And Digital Communication (ECT 305) 🖥️
 (No of Credits- 4)


📄Syllabus 👇

https://shorturl.at/fsUYZ

📝Notes 👇

https://shorturl.at/GLWY8

❔Previous year QP's 👇

https://shorturl.at/nuzV5

 🎥Videos 👇

https://shorturl.at/swCO5

 🤖 Contribute a new material 👇
 /contribute


 Any suggestions?🫡
 /suggest



"""


ECT307= """📊 Control System (ECT 307)  📊
 (No of Credits- 4)


📄Syllabus 👇

http://surl.li/orkji

📝Notes 👇

http://surl.li/orkjy

❔Previous year QP's 👇

http://surl.li/orkkl

 🎥Videos 👇

http://surl.li/orklg

🤖 Contribute a new material 👇
 /contribute


 Any suggestions?🫡
 /suggest



"""


HUT310= """🤝  Management for Engineers (HUT 310) 🤝
 (No of Credits- 3)


📄Syllabus 👇

http://surl.li/orklq

📝Notes 👇

http://surl.li/orklz

❔Previous year QP's 👇

http://surl.li/orkmo

 🎥Videos 👇

http://surl.li/orknr

 🤖 Contribute a new material 👇
 /contribute


 Any suggestions?🫡
 /suggest



"""

MCN301= """🫡 Disaster Management (MCN 301) 🫡
 (No of Credits- 0)


📄Syllabus 👇

http://surl.li/orkop

📝Notes 👇

 http://surl.li/orkpf

❔Previous year QP's 👇

http://surl.li/orkpu

 🎥Videos 👇

http://surl.li/orkqe

 🤖 Contribute a new material 👇
 /contribute


 Any suggestions?🫡
 /suggest



"""










BOT_TOKEN = 'Give your secert here'

bot = telebot.TeleBot(BOT_TOKEN)
animation_url = "https://media.giphy.com/media/3o7qDJKIO5rSeyHhvO/giphy.gif"

def create_inline1_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton('Continue', callback_data='Continue'))
    return keyboard

def create_inline_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton('Timetable', callback_data='timetable'))
    keyboard.add(types.InlineKeyboardButton('LIC', callback_data='ECT301'))
    keyboard.add(types.InlineKeyboardButton('DSP', callback_data='ECT303'))
    keyboard.add(types.InlineKeyboardButton('ADC', callback_data='ECT305'))
    keyboard.add(types.InlineKeyboardButton('CS', callback_data='ECT307'))
    keyboard.add(types.InlineKeyboardButton('MFE', callback_data='HUT310'))
    keyboard.add(types.InlineKeyboardButton('DM', callback_data='MCN301'))
    return keyboard

@bot.message_handler(commands=['START', 'start', 'Start'])
def send_start(message):
    bot.send_animation(message.chat.id, animation_url, caption=welcome_msg, reply_markup=create_inline_keyboard())

@bot.callback_query_handler(func=lambda call: True)
def handle_inline_buttons(call):

    if call.data == 'timetable':
        bot.send_message(call.message.chat.id, f" {time_table}")
    elif call.data == 'ECT301':
        bot.send_message(call.message.chat.id, f"{ECT301}")
    elif call.data == 'ECT303':
        bot.send_message(call.message.chat.id, f"{ECT303}")
    elif call.data == 'ECT305':
        bot.send_message(call.message.chat.id, f"{ECT305}")
    elif call.data == 'ECT307':
        bot.send_message(call.message.chat.id, f"{ECT307}")
    elif call.data == 'HUT310':
        bot.send_message(call.message.chat.id, f"{HUT310}")
    elif call.data == 'MCN301':
        bot.send_message(call.message.chat.id, f"{MCN301}")
    else :
        bot.send_message(call.message.chat.id, f"{Continue}")



@bot.message_handler(commands=['START', 'start','Start'])
def send_start(message):
    bot.reply_to(message, welcome_msg)

@bot.message_handler(commands=['TIMETABLE', 'timetable','Timetable'])
def send_timetable(message):
    bot.reply_to(message, time_table,reply_markup=create_inline1_keyboard())



@bot.message_handler(commands=['Continue', 'CONTINUE','continue'])
def send_continue(message):
    bot.reply_to(message, Continue)


@bot.message_handler(commands=['ECT301', 'ect301','Ect301','lic',"LIC",'Lic'])
def send_lic(message):
    bot.reply_to(message, ECT301)

@bot.message_handler(commands=['ECT303', 'ect303','Ect303','DSP',"dsp",'Dsp'])
def send_dsp(message):
    bot.reply_to(message, ECT303)

@bot.message_handler(commands=['ECT305', 'ect305','Ect305','ADC',"Adc",'adc'])
def send_adc(message):
    bot.reply_to(message, ECT305)

@bot.message_handler(commands=['ECT307', 'ect307','Ect307','CS',"Cs",'cs'])
def send_cs(message):
    bot.reply_to(message, ECT307)

@bot.message_handler(commands=['HUT310', 'hut310','Hut310','mfe',"MFE",'Mfe'])
def send_mfe(message):
    bot.reply_to(message, HUT310)

@bot.message_handler(commands=['MCN301', 'Mcn301','mcn301','dm',"Dm",'DM'])
def send_dm(message):
    bot.reply_to(message, MCN301)



@bot.message_handler(commands=["HELP","help","Help"])
def send_help(message):
    bot.reply_to(message, help_msg)

@bot.message_handler(commands=['Contribute', 'contribute','CONTRIBUTE'])
def send_contribute(message):
    bot.reply_to(message, contribute_msg,reply_markup=create_inline1_keyboard())

@bot.message_handler(commands=['Suggest', 'SUGGEST','suggest'])
def send_suggest(message):
    bot.reply_to(message, suggest_msg, reply_markup=create_inline1_keyboard())

@bot.message_handler(func=lambda message: True)
def handle_wrong_command(message):
    bot.reply_to(message, "Sorry, wrong command.", reply_markup=create_inline_keyboard())
bot.infinity_polling()

