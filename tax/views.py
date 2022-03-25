from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telethon import TelegramClient, sync
from telebot import *
import telebot
from .models import *


bot = TeleBot("5131385007:AAGjOh5Xn3qTEmqYZ04oSxq2MU1CKjq8EEM")


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse("Bot Url Page")
    elif request.method == 'POST':
        bot.process_new_updates([
            telebot.types.Update.de_json(
                request.body.decode("utf-8")
            )
        ])
        return HttpResponse(status=200)


@bot.message_handler(commands=['start'])
def greeting(message):
    main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Sudlar haqida ma\'lumot")
    btn2 = types.KeyboardButton("Interaktive xizmatlar")
    btn3 = types.KeyboardButton("Sudga murojaat")
    # btn4 = types.KeyboardButton("Sozlash")
    main_menu.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,
                  'Menyudan kerakli bo\'limni tanlang:\n', reply_markup=main_menu)
   


@bot.message_handler(func=lambda message: True)
def get_info(message):
	step = UserRequest.objects.get(user_id=253953)
	
	regions = ("Navoiy viloyati", "Buxoro viloyati", "Qoraqalpag\'iston Respublikasi", "Xorazm viloyati", "Toshkent viloyati", "Toshkent shahar",
			   "Jizzax viloyati", "Sirdaryo viloyati", "Farg\'ona viloyati", "Samarqand viloyati", "Andijon viloyati", "Namangan viloyati", "Surxondaryo viloyati", "Qashqadaryo viloyati")
	
	main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton("Sudlar haqida ma\'lumot")
	btn2 = types.KeyboardButton("Interaktive xizmatlar")
	btn3 = types.KeyboardButton("Sudga murojaat")
	# btn4 = types.KeyboardButton("Sozlash")
	main_menu.add(btn1, btn2, btn3)

	sud_types = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1_sud_info = types.KeyboardButton("Oliy sud")
	btn2_sud_info = types.KeyboardButton("Jinoyat ishlari bo\'yicha sudlar")
	btn3_sud_info = types.KeyboardButton("Ma\'muriy sudlar")
	btn4_sud_info = types.KeyboardButton("Fuqarolik ishlarni bo\'yicha sudlar")
	btn5_sud_info = types.KeyboardButton("Iqtisodiy sudlar")
	btn6_sud_info = types.KeyboardButton("Orqaga ↩️")
	sud_types.add(btn1_sud_info, btn2_sud_info, btn3_sud_info, btn4_sud_info, btn5_sud_info, btn6_sud_info)

	category = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1_c = types.KeyboardButton("Ishni topish")
	# btn2_c = types.KeyboardButton("Qarorlar to\'plami")
	btn3_c = types.KeyboardButton("Davo namunalari")
	# btn4_c = types.KeyboardButton("Davlar boji kalkulyatori")
	btn5_c = types.KeyboardButton("Orqaga ↩️")
	category.add(btn1_c, btn3_c, btn5_c)

	client_request = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1_cr = types.KeyboardButton("Fuqarolik ishlarni bo\'yicha sudga murojaat")
	btn2_cr = types.KeyboardButton("Iqtisodiy sudga murojaat")
	btn3_cr = types.KeyboardButton("Ma\'muriy sudga murojaat")
	btn4_cr = types.KeyboardButton("Jinoyat ishlari bo\'yicha sudga murojaat")
	btn5_cr = types.KeyboardButton("Axborot texnologiyalari sudiga murojaat")
	btn6_cr = types.KeyboardButton("Korrupsiyaga qarshi kurash sudiga murojaat")
	btn7_cr = types.KeyboardButton("Orqaga ↩️")
	client_request.add(btn1_cr, btn2_cr, btn3_cr, btn4_cr, btn5_cr, btn6_cr, btn7_cr)

	secondary_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1_s = types.KeyboardButton("Bosh menu")
	btn2_s = types.KeyboardButton("Orqaga ↩️")
	secondary_markup.add(btn1_s, btn2_s)

	case_types = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1_case = types.KeyboardButton("Jinoiy ish")
	btn2_case = types.KeyboardButton("Fuqarolik ishi")
	btn3_case = types.KeyboardButton("Ma\'muriy huquqbuzarlik")
	btn4_case = types.KeyboardButton("Iqtisodiy ish")
	case_types.add(btn1_case, btn2_case, btn3_case, btn4_case, btn1_s, btn2_s)

	cancel_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1_cancel = types.KeyboardButton("Bekor qilish 🚫")
	cancel_markup.add(btn1_cancel)

	if message.text == 'Bekor qilish 🚫':
		bot.send_message(message.from_user.id, 'Ishingiz turini tanlang:', reply_markup=case_types)
	
	if message.text == 'Bosh menu':
		bot.send_message(message.from_user.id, 'Menyudan kerakli bo\'limni tanlang:\n', reply_markup=main_menu)

	if message.text == "Sudlar haqida ma\'lumot":
		bot.send_message(message.from_user.id, 'Sud turini tanlang:', reply_markup=sud_types)
		step.step = 1
		step.save()
	
	if message.text == "Interaktive xizmatlar":
		bot.send_message(message.from_user.id, 'Kerakli bo\'limni tanlang:', reply_markup=category)		
		step.step = 1
		step.save()

	if message.text == 'Ishni topish':
		step.step = 3
		step.save()
		bot.send_message(message.from_user.id, 'Ishingiz turini tanlang:', reply_markup=case_types)

	if message.text == 'Jinoiy ish':
		bot.send_message(message.from_user.id, 'Ishingiz raqamini yozing', reply_markup=cancel_markup)

	if message.text == 'Fuqarolik ishi':
		bot.send_message(message.from_user.id, 'Ishingiz raqamini yozing', reply_markup=cancel_markup)

	if message.text == 'Ma\'muriy huquqbuzarlik':
		bot.send_message(message.from_user.id, 'Ishingiz raqamini yozing', reply_markup=cancel_markup)

	if message.text == 'Iqtisodiy ish':
		bot.send_message(message.from_user.id, 'Ishingiz raqamini yozing', reply_markup=cancel_markup)

	if message.text == 'Davo namunalari':
		markup_davo = types.InlineKeyboardMarkup(row_width=1)
		btn1_davo = types.InlineKeyboardButton("Faylni yuklash",  url="https://sud.uz/wp-content/uploads/2019/07/1-aliment-undiris-akida.doc", callback_data=f"kjhvkjgv")
		# markup_davo.add(types.InlineKeyboardButton(f"Fayl", callback_data=f"https://sud.uz/wp-content/uploads/2019/07/1-aliment-undiris-akida.doc"))
		markup_davo.add(btn1_davo)
		bot.send_message(message.from_user.id, 'Aliment undirish haqida', reply_markup=markup_davo)

	if message.text == "Sudga murojaat":
		bot.send_message(message.from_user.id, 'Kerakli bo\'limni tanlang:', reply_markup=client_request)
		step.step = 1
		step.save()
	
	if message.text == "Fuqarolik ishlarni bo\'yicha sudga murojaat":
		step.step = 1
		step.save()
		bot.send_message(message.from_user.id, "Hurmatli foydalanuvchi, ushbu telegram bot orqali faqat ishlarni o'z vaqtida, to'g'ri ko'rish va hal etish, ishlar ko'rilishini asossiz cho'zilishiga baham berish, sudlar faoliyatidagi byurokratiya holatlari va korrupsya bilan kurashishga bog'liq bolgan murojaatlar qabul qilinadi. Savol va takliflarni yozing. Ularni matn (matnning maksimal hajmi 3000 ta belgidan oshmasligi kerak) ko'rinishida yuborishingiz mumkin.", reply_markup=secondary_markup)
	
	if message.text == "Iqtisodiy sudga murojaat":
		step.step = 1
		step.save()
		bot.send_message(message.from_user.id, "Hurmatli foydalanuvchi, ushbu telegram bot orqali faqat ishlarni o'z vaqtida, to'g'ri ko'rish va hal etish, ishlar ko'rilishini asossiz cho'zilishiga baham berish, sudlar faoliyatidagi byurokratiya holatlari va korrupsya bilan kurashishga bog'liq bolgan murojaatlar qabul qilinadi. Savol va takliflarni yozing. Ularni matn (matnning maksimal hajmi 3000 ta belgidan oshmasligi kerak) ko'rinishida yuborishingiz mumkin.", reply_markup=secondary_markup)
	
	if message.text == "Ma'muriy sudga murojaat":
		step.step = 1
		step.save()
		bot.send_message(message.from_user.id, "Hurmatli foydalanuvchi, ushbu telegram bot orqali faqat ishlarni o'z vaqtida, to'g'ri ko'rish va hal etish, ishlar ko'rilishini asossiz cho'zilishiga baham berish, sudlar faoliyatidagi byurokratiya holatlari va korrupsya bilan kurashishga bog'liq bolgan murojaatlar qabul qilinadi. Savol va takliflarni yozing. Ularni matn (matnning maksimal hajmi 3000 ta belgidan oshmasligi kerak) ko'rinishida yuborishingiz mumkin.", reply_markup=secondary_markup)
	
	if message.text == "Jinoyat ishlari bo'yicha sudga murojaat":
		step.step = 1
		step.save()
		bot.send_message(message.from_user.id, "Hurmatli foydalanuvchi, ushbu telegram bot orqali faqat ishlarni o'z vaqtida, to'g'ri ko'rish va hal etish, ishlar ko'rilishini asossiz cho'zilishiga baham berish, sudlar faoliyatidagi byurokratiya holatlari va korrupsya bilan kurashishga bog'liq bolgan murojaatlar qabul qilinadi. Savol va takliflarni yozing. Ularni matn (matnning maksimal hajmi 3000 ta belgidan oshmasligi kerak) ko'rinishida yuborishingiz mumkin.", reply_markup=secondary_markup)
	
	if message.text == "Axborot texnologiyalari sudiga murojaat":
		step.step = 1
		step.save()
		bot.send_message(message.from_user.id, "Hurmatli foydalanuvchi, ushbu telegram bot orqali faqat ishlarni o'z vaqtida, to'g'ri ko'rish va hal etish, ishlar ko'rilishini asossiz cho'zilishiga baham berish, sudlar faoliyatidagi byurokratiya holatlari va korrupsya bilan kurashishga bog'liq bolgan murojaatlar qabul qilinadi. Savol va takliflarni yozing. Ularni matn (matnning maksimal hajmi 3000 ta belgidan oshmasligi kerak) ko'rinishida yuborishingiz mumkin.", reply_markup=secondary_markup)
	
	if message.text == "Korrupsiyaga qarshi kurash sudiga murojaat":
		step.step = 1
		step.save()
		bot.send_message(message.from_user.id, "Hurmatli foydalanuvchi, ushbu telegram bot orqali faqat ishlarni o'z vaqtida, to'g'ri ko'rish va hal etish, ishlar ko'rilishini asossiz cho'zilishiga baham berish, sudlar faoliyatidagi byurokratiya holatlari va korrupsya bilan kurashishga bog'liq bolgan murojaatlar qabul qilinadi. Savol va takliflarni yozing. Ularni matn (matnning maksimal hajmi 3000 ta belgidan oshmasligi kerak) ko'rinishida yuborishingiz mumkin.", reply_markup=secondary_markup)
	
	if message.text == "Orqaga ↩️":
		if step.step == 1:
			bot.send_message(message.from_user.id, 'Kerakli bo\'limni tanlang:', reply_markup=main_menu)
		if step.step == 2:
			step.step = 1
			step.save()
			bot.send_message(message.from_user.id, 'Sud turini tanlang:', reply_markup=sud_types)

		if step.step == 3:
			step.step = 1
			step.save()
			bot.send_message(message.from_user.id, 'Kerakli bo\'limni tanlang:', reply_markup=category)

	if message.text == "Oliy sud":
		step.step = 2
		step.save()
		bot.send_message(message.from_user.id, 'O\'zbekiston Respublikasi Oliy sudi\nManzil\
			1001186, Toshkent shahar, A.Qodiriy ko\'chasi, 1-uy\nTel: (71) 239 02 74\n\
		E-mail: infosupcourt.uz', reply_markup=secondary_markup)
	
	if message.text == "Jinoyat ishlari bo\'yicha sudlar":
		step.step = 2
		step.save()
		markup_regions = types.InlineKeyboardMarkup(row_width=1)
		for region in regions:		
			markup_regions.add(types.InlineKeyboardButton(f"{region}", callback_data=f"{region} jinoiy"))
		bot.send_message(message.from_user.id, 'Hududni tanlang:', reply_markup=markup_regions)

	if message.text == "Ma\'muriy sudlar":
		step.step = 2
		step.save()
		markup_regions = types.InlineKeyboardMarkup(row_width=1)
		for region in regions:
			markup_regions.add(types.InlineKeyboardButton(f"{region}", callback_data=f"{region} mamuriy"))
		bot.send_message(message.from_user.id, 'Hududni tanlang:', reply_markup=markup_regions)

	if message.text == "Fuqarolik ishlarni bo\'yicha sudlar":
		step.step = 2
		step.save()
		markup_regions = types.InlineKeyboardMarkup(row_width=1)
		for region in regions:
			markup_regions.add(types.InlineKeyboardButton(f"{region}", callback_data=f"{region} fuqarolik"))
		bot.send_message(message.from_user.id, 'Hududni tanlang:', reply_markup=markup_regions)

	if message.text == "Iqtisodiy sudlar":
		step.step = 2
		step.save()
		markup_regions = types.InlineKeyboardMarkup(row_width=1)
		for region in regions:
			markup_regions.add(types.InlineKeyboardButton(f"{region}", callback_data=f"{region} iqtisodiy"))
		bot.send_message(message.from_user.id, 'Hududni tanlang:', reply_markup=markup_regions)



@bot.callback_query_handler(func=lambda call: True)
def call_data(call):
	print(call.data)

	secondary_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
	btn1_s = types.KeyboardButton("Bosh menu")
	btn2_s = types.KeyboardButton("Orqaga")
	secondary_markup.add(btn1_s, btn2_s)
	regions = ("Navoiy viloyati", "Buxoro viloyati", "Qoraqalpag\'iston Respublikasi", "Xorazm viloyati", "Toshkent viloyati", "Toshkent shahar",
			   "Jizzax viloyati", "Sirdaryo viloyati", "Farg\'ona viloyati", "Samarqand viloyati", "Andijon viloyati", "Namangan viloyati", "Surxondaryo viloyati", "Qashqadaryo viloyati")
	
	
	# jinoiy sudlar
	if call.data == "Navoiy viloyati jinoiy":
		bot.send_message(call.from_user.id,
                         f"Наманган шаҳри, Н. Намангоний кўчаси, 10 уй, тел.: (369) 227-85-57, 227-81-10, почта индекси 160133, e-mail: j.namangan@sud.uz", reply_markup=secondary_markup)
	if call.data == "Buxoro viloyati jinoiy":
		bot.send_message(call.from_user.id,
                         f"Бухоро шаҳри, Ҳофиз Таниш Бухорий кўчаси, 13 уй, тел.:(65) 221-55-35, 221-53-13, почта индекси 200111, e-mail:j.buxoro@sud.uz", reply_markup=secondary_markup)
	if call.data == "Qoraqalpag\'iston Respublikasi jinoiy":
		bot.send_message(call.from_user.id,
                         f"Нукус шаҳар, «Дослык гузари», МФЙ И.Каримов кўчаси, 122-уй, тел.: (61) 222-02-00, 222-17-00, 222-00-60, почта индекси 230100, e-mail: j.qr@sud.uz", reply_markup=secondary_markup)
	if call.data == "Xorazm viloyati jinoiy":
		bot.send_message(call.from_user.id,
                         f"Урганч шаҳри, Тинчлик кўчаси, 22 уй, тел.: (62) 228-66-22, 228-66-12, почта индекси 220100, e-mail: j.xorazm@sud.uz", reply_markup=secondary_markup)
	if call.data == "Toshkent viloyati jinoiy":
		bot.send_message(call.from_user.id,
                         f"Тошкент шаҳри, Ш. Руставели кўчаси, 93 уй, тел.: (71) 253-79-32, 253-17-60, почта индекси 100059, e-mail: j.toshkent.v@sud.uz", reply_markup=secondary_markup)
	if call.data == "Toshkent shahar jinoiy":
		bot.send_message(call.from_user.id,
                         f"Тошкент шаҳри, А.Навоий кўчаси, 23 уй, тел.: (71) 241-02-51, 244-09-35, почта индекси 100011, e-mail: j.toshkent@sud.uz", reply_markup=secondary_markup)
	if call.data == "Jizzax viloyati jinoiy":
		bot.send_message(call.from_user.id,
                         f"Жиззах шаҳри, Сайилжойи кўчаси, 63 уй, тел.: (72) 226-20-45, 226-57-02, почта индекси 130100, e-mail: j.jizzax@sud.uz", reply_markup=secondary_markup)
	if call.data == "Sirdaryo viloyati jinoiy":
		bot.send_message(call.from_user.id,
                         f"Гулистон шаҳри, А. Навоий шоҳ кўчаси, 47 уй, тел.: (67) 225-35-13, 235-02-04, почта индекси 120100, e-mail: j.sirdaryo@sud.uz", reply_markup=secondary_markup)
	if call.data == "Farg\'ona viloyati jinoiy":
		bot.send_message(call.from_user.id,
                         f"Фарғона шаҳри, Соҳибқирон Темур кўчаси, 30-уй, тел.: (73) 226-69-50, 226-07-75, почта индекси 150100, e-mail: j.fargona@sud.uz", reply_markup=secondary_markup)
	if call.data == "Samarqand viloyati jinoiy":
		bot.send_message(call.from_user.id,
                         f"Самарқанд шаҳри, Мингтут кўчаси, 1 уй, тел.: (66) 234-82-50, 234-26-41, почта индекси 140100, e-mail:j.samarqand@sud.uz", reply_markup=secondary_markup)
	if call.data == "Andijon viloyati jinoiy":
		bot.send_message(call.from_user.id,
                         f"Андижон шаҳри, А. Навоий шоҳ кўчаси, 15 уй, тел.: (74)223-49-04, 223-57-57, почта индекси 170100, e-mail:j.andijon@sud.uz", reply_markup=secondary_markup)
	if call.data == "Namangan viloyati jinoiy":
		bot.send_message(call.from_user.id,
                         f"Наманган шаҳри, Н. Намангоний кўчаси, 10 уй, тел.: (369) 227-85-57, 227-81-10, почта индекси 160133, e-mail: j.namangan@sud.uz", reply_markup=secondary_markup)
	if call.data == "Surxondaryo viloyati jinoiy":
		bot.send_message(call.from_user.id,
                         f"Термиз шаҳри, И.Каримов кўчачи, 40 уй, тел.: (76) 222-47-04, 222-46-07, почта индекси 190106, e-mail: j.surxondaryo@sud.uz", reply_markup=secondary_markup)
	if call.data == "Qashqadaryo viloyati jinoiy":
		bot.send_message(call.from_user.id,
                         f"Қарши шаҳри, О.Турсунов кўчаси, 97 уй, тел.: (75) 221-85-35, 221-01-68, 221-05-58 почта индекси 180000, e-mail: j.qashqadaryo@sud.uz", reply_markup=secondary_markup)
	

	#mamuriy sudlar
	if call.data == "Navoiy viloyati mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-436) 223-11-53	m.navoiy@sud.uz	Navoiy viloyati, Navoiy shahri, Navoiy ko'chasi, 30B-uy, pochta indeksi 210100", reply_markup=secondary_markup)
	if call.data == "Buxoro viloyati mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-365) 221-93-89	m.buxoro@sud.uz	Buxoro viloyati, Buxoro shahri, Yangiobod ko'chasi, 29-uy, pochta indeksi 200101", reply_markup=secondary_markup)
	if call.data == "Qoraqalpag\'iston Respublikasi mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-361) 224-53-75	E-mail: m.qr@sud.uz	Manzil: Qoraqalpag\'iston Respublikasi, Nukus shahri, Chimboy Guzori ko'chasi, raqamsiz uy, pochta indeksi 230100", reply_markup=secondary_markup)
	if call.data == "Xorazm viloyati mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-362) 226-01-54	m.xorazm@sud.uz	Xorazm viloyati, Urganch shahri, Аl-Хorazmiy ko'chasi, 95-uy, pochta indeksi  230200", reply_markup=secondary_markup)
	if call.data == "Toshkent viloyati mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-371) 273-25-93	m.toshkent.v@sud.uz	Toshkent shahri, Yakkasaroy tumani, Shota Rustavelli ko'chasi, 93-uy, pochta indeksi 100059", reply_markup=secondary_markup)
	if call.data == "Toshkent shahar mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (99) 981-22-20	m.toshkent@sud.uz	Toshkent shahri, Yashnobod tumani, Paxlavon Mahmud 1-berk ko'chasi, 8-uy, pochta indeksi 100047", reply_markup=secondary_markup)
	if call.data == "Jizzax viloyati mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-372) 222-35-72	m.jizzax@sud.uz	Jizzah viloyati, Jizzah shahri, Navro'z mahallasi, M. Tursunov ko'chasi, 1-uy, pochta indeksi 130100", reply_markup=secondary_markup)
	if call.data == "Sirdaryo viloyati mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-367) 227-55-33	m.sirdaryo@sud.uz	Sirdaryo viloyati, Guliston shahri, O'zbekiston ko'chasi, 68-uy, pochta indeksi 120100", reply_markup=secondary_markup)
	if call.data == "Farg\'ona viloyati mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-373) 244-67-30	m.fargona@sud.uz	Farg'ona viloyati, Farg'ona shahri, Аl-Farg'oniy ko'chasi, 47-uy, pochta indeksi 150100", reply_markup=secondary_markup)
	if call.data == "Samarqand viloyati mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-366) 235-00-16	m.samarqand@sud.uz	Samarqand viloyati, Samarqand shahri, Ko'ksaroy maydoni ko'chasi, 3-uy, pochta indeksi 140157", reply_markup=secondary_markup)
	if call.data == "Andijon viloyati mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-374) 228-29-07	m.andijon@sud.uz	Andijon viloyati, Andijon shahri, Alisher Navoiy shoh ko'chasi, 15-uy, pochta indeksi 711002", reply_markup=secondary_markup)
	if call.data == "Namangan viloyati mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-369) 227-26-22	m.namangan@sud.uz	Namangan viloyati, Namangan shahri, Lutfiy ko'chasi, 6-uy, pochta indeksi 160136", reply_markup=secondary_markup)
	if call.data == "Surxondaryo viloyati mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-376) 223-10-36	m.surxondaryo@sud.uz	Surxondaryo viloyati, Termiz shahri, Navbog' ko'chasi, 12-uy, pochta indeksi 190100", reply_markup=secondary_markup)
	if call.data == "Qashqadaryo viloyati mamuriy":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-375) 230-14-80	m.qashqadaryo@sud.uz	Qashqadaryo viloyati, Qarshi shahri, Bunyodkorlik ko'chasi, 7-uy, pochta indeksi  180000", reply_markup=secondary_markup)
	

	#fuqarolik sudlari
	if call.data == "Navoiy viloyati fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Навоий шаҳри, С. Айний кўчаси,1 уй, тел.: (36)225-17-74, 225-17-80, 225-17-76, почта индекси 210100, e-mail: f.navoiy@sud.uz", reply_markup=secondary_markup)
	if call.data == "Buxoro viloyati fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Бухоро шаҳар, Янгиҳаёт кўчаси 122-уй, тел.: (65) 224-49-89, 224-59-89, 221-85-93, почта индекси 200111, e-mail: f.buxoro@sud.uz", reply_markup=secondary_markup)
	if call.data == "Qoraqalpag\'iston Respublikasi fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Нукус шаҳар, «Дослык гузари», МФЙ И.Каримов кўчаси, 122-уй, тел.: (61) 224-50-51, 224-38-74, 224-53-66, почта индекси 230100, e-mail:  f.qr@sud.uz", reply_markup=secondary_markup)
	if call.data == "Xorazm viloyati fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Урганч шаҳри, Машъал кўчаси, 3 уй, тел.: (62) 228-12-27,228-12-44,почта индекси 220100, e-mail: f.xorazm@sud.uz", reply_markup=secondary_markup)
	if call.data == "Toshkent viloyati fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Тошкент шаҳри, Ш. Руставели кўчаси, 93 уй, тел.: (71) 253-91-97, 253-89-40, 712539195 почта индекси 100059, e-mail: f.toshkent.v@sud.uz", reply_markup=secondary_markup)
	if call.data == "Toshkent shahar fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Мирзо Улуғбек тумани, Буюк ипак йули кўчаси, 246 уй, тел.: (71) 262-66-45, 262-66-43, 269-08-83, почта индекси 100187, e-mail: f.toshkent@sud.uz", reply_markup=secondary_markup)
	if call.data == "Jizzax viloyati fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Жиззах шаҳри, О.Азимов кўчаси,15 уй, тел.: (72) 222-40-93, 222-40-92, 222-29-43, 222-38-17, почта индекси 708000, e-mail: f.jizzah@sud.uz", reply_markup=secondary_markup)
	if call.data == "Sirdaryo viloyati fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Гулистон шаҳар, И.Каримов кўчаси, 75 уй,тел.: (67) 225-37-47, 225-24-85, 225-48-08 почта индекси 120100, e-mail: f.sirdaryo@sud.uz", reply_markup=secondary_markup)
	if call.data == "Farg\'ona viloyati fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Фарғона шаҳри, Янгисой кўчаси,2 уй, тел.: (73) 243-16-79, 243-16-94, почта индекси 150102, e-mail: f.fargona@sud.uz", reply_markup=secondary_markup)
	if call.data == "Samarqand viloyati fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Tel: (0-366) 235-00-16	m.samarqand@sud.uz	Samarqand viloyati, Samarqand shahri, Ko'ksaroy maydoni ko'chasi, 3-uy, pochta indeksi 140157", reply_markup=secondary_markup)
	if call.data == "Andijon viloyati fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Андижон шаҳри, Бобур шоҳ кўчаси, 26 уй, тел.: (74) 228-38-51, 228-17-19, 228-16-77, 228-39-06 почта индекси 170100,e-mail:  f.andijon@sud.uz", reply_markup=secondary_markup)
	if call.data == "Namangan viloyati fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Наманган шаҳар, Лутфий кўчаси, 6-уй,тел.: (69) 227-30-50, 63 227-30-47, почта индекси 160127, e-mail:  f.namangan@sud.uz", reply_markup=secondary_markup)
	if call.data == "Surxondaryo viloyati fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Термиз шаҳар, И.Каримов кўчаси, 286 б уй, тел.: (76) 221-94-51, 221-94-72, 221-94-64, почта индекси 190111, e-mail: f.surxondaryo@sud.uz", reply_markup=secondary_markup)
	if call.data == "Qashqadaryo viloyati fuqarolik":
		bot.send_message(call.from_user.id,
                         f"Қарши шаҳар, Бунёдкорлик кўчаси, 10-А уй,тел.: (75) 221-03-76, почта индекси 180100, e-mail:f.qashqadaryo@sud.uz", reply_markup=secondary_markup)
	

	#iqtisodiy sudlar
	if call.data == "Navoiy viloyati iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Навоий вилояти, Навоий шаҳар, Навоий кўчаси 11 уй, тел.: (79) 220-22-47, 220-22-46, почта индекси 210100, e-mail: i.navoiy@sud.uz", reply_markup=secondary_markup)
	if call.data == "Buxoro viloyati iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Бухоро вилояти, Бухоро шаҳар, Янгиҳаёт кўчаси 122-уй,тел.: (65) 221-85-93, 221-86-06, почта индекси 200111, e-mail: i.buxoro@sud.uz", reply_markup=secondary_markup)
	if call.data == "Qoraqalpag\'iston Respublikasi iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Қорақалпоғистон Республикаси, Нукус шаҳар, «Дослык гузари», МФЙ И.Каримов кўчаси, 122-уй, тел.: (61) 224-50-51, 224-38-74, 224-53-66, почта индекси 230100, e-mail: i.qr@sud.uz", reply_markup=secondary_markup)
	if call.data == "Xorazm viloyati iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Хоразм вилояти, Урганч шаҳри, Машъал кўчаси, 3 уй, тел.: (62) 226-01-69, 226-01-70,, почта индекси 220100, e-mail: i.xorazm@sud.uz", reply_markup=secondary_markup)
	if call.data == "Toshkent viloyati iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Тошкент шаҳри, Ш. Руставели кўчаси, 93 уй, тел.: (71) 253-24-90, 253-24-47, почта индекси 100059, e-mail: i.toshkent.v@sud.uz", reply_markup=secondary_markup)
	if call.data == "Toshkent shahar iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Тошкент шаҳри, Чилонзор тумани, Чўпон-ота кўчаси, 6 уй, тел.: (71) 273-06-46, 273-32-22 почта индекси 100097, e-mail: i.toshkent@sud.uz", reply_markup=secondary_markup)
	if call.data == "Jizzax viloyati iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Жиззах вилояти, Жиззах шаҳар, Қалия маҳалласи А.Саъдуллаев кўчаси 77 уй, тел.: (72) 224-47-08 почта индекси 130111, e-mail: i.jizzax@sud.uz", reply_markup=secondary_markup)
	if call.data == "Sirdaryo viloyati iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Сирдарё вилояти, Гулистон шаҳар, И.Каримов кўчаси, 75 уй,тел.: (67) 225-45-67, 225-28-28, почта индекси 120100, e-mail: i.sirdaryo@sud.uz", reply_markup=secondary_markup)
	if call.data == "Farg\'ona viloyati iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Фарғона вилояти, Фарғона шаҳри, Янгисой кўчаси,2 уй, тел.: (73) 244-64-12, 244-64-13,, почта индекси 150102, e-mail: i.fargona@sud.uz", reply_markup=secondary_markup)
	if call.data == "Samarqand viloyati iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Самарқанд вилояти, Самарқанд шаҳар, Мингтут кўчаси, 2 уй, тел.: (66) 234-52-46, 234-51-95, почта индекси 140100, e-mail: i.samarqand@sud.uz", reply_markup=secondary_markup)
	if call.data == "Andijon viloyati iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Андижон вилояти, Андижон шаҳри, Алишер Навоий шоҳ кўчаси, 41 уй, тел.: (74) 223-60-37, 223-60-38 почта индекси 170100, e-mail: i.andijon@sud.uz", reply_markup=secondary_markup)
	if call.data == "Namangan viloyati iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Наманган вилояти, Наманган шаҳри, Н.Намангоний кўчаси, 20 уй, тел.: (69) 227-81-38, 227-76-09 почта индекси 160133, e-mail: i.namangan@sud.uz", reply_markup=secondary_markup)
	if call.data == "Surxondaryo viloyati iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Сурхондарё вилояти, Термиз шаҳар, И.Каримов кўчаси, 286 б уй, тел.: (76) 221-94-55, 221-94-61, почта индекси 190111, e-mail: i.surxondaryo@sud.uz", reply_markup=secondary_markup)
	if call.data == "Qashqadaryo viloyati iqtisodiy":
		bot.send_message(call.from_user.id,
                         f"Қашқадарё вилояти, Қарши шаҳар, Бунёдкорлик кўчаси, 10-А уй,тел.: (75) 221-12-82, почта индекси 180100, e-mail: i.qashqadaryo@sud.uz", reply_markup=secondary_markup)
	

bot.polling()
