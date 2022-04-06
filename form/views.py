from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telethon import TelegramClient, sync
from telebot import *
import telebot
from form.models import *


bot = TeleBot("5023297653:AAEpWWWTJAKpmd7BSaGoggaHT8fA6g8-FR4")


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse("Bot Url My Page")
    elif request.method == 'POST':
        bot.process_new_updates([
            telebot.types.Update.de_json(
                request.body.decode("utf-8")
            )
        ])
        return HttpResponse(status=200)


@bot.message_handler(commands=['start'])
def greeting(message):
    main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton('Anketa to\'ldirish 📝')
    main_markup.add(btn)
    bot.send_message(message.from_user.id,
                  '*Salom.\nBotga xush kelibsiz!\nBot sizga Fortuna Biznes korxonasiga ishga kirishda ro\'yxatdan o\'tishga yordam beradi.*', reply_markup=main_markup, parse_mode='Markdown')
    

@bot.message_handler(func=lambda message: True)
def register_view(message):
    active_users = Applicant.objects.filter(user_id=message.from_user.id)
    
    if len(active_users) == 0:
        client = Applicant.objects.create(
            user_id=message.from_user.id)
        client.active = True
        client.save()
    else:
        client = Applicant.objects.get(user_id=message.from_user.id)
        client.active = True
        client.save()
 
    regions = ("Navoiy viloyati", "Buxoro viloyati", "Qoraqalpag\'iston Respublikasi", "Xorazm viloyati", "Toshkent viloyati", "Toshkent shahar",
               "Jizzax viloyati", "Sirdaryo viloyati", "Farg\'ona viloyati", "Samarqand viloyati", "Andijon viloyati", "Namangan viloyati", "Surxondaryo viloyati", "Qashqadaryo viloyati")
    
    client = Applicant.objects.get(user_id=message.from_user.id)
    
    cancel_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Bekor qilish 🚫")
    cancel_markup.add(btn1)

    main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Bekor qilish 🚫")
    main_markup.add(btn1)

    new_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Anketa to\'ldirish 📝")
    new_markup.add(btn1)

    orders = ['Anketa to\'ldirish 📝']

    if message.text == "Keyingisi":
        client.step += 1
        client.save()

    if message.text == 'Anketa to\'ldirish 📝':
        client.step = 1
        client.save()
        bot.send_message(message.from_user.id,
                  '*Ism familiyangizni kiriting 👤\n*', reply_markup=cancel_markup, parse_mode='Markdown')

    elif message.text == "Tasdiqlash ✅":
        client.step = 0
        client.active = False
        client.save()
        bot.send_message(message.from_user.id,
                  "*Royxatdan muvaffaqiyatli o'tdingiz!*", reply_markup=new_markup, parse_mode='Markdown')
    
    elif message.text == "Bekor qilish 🚫":
        client.delete()
        bot.send_message(message.from_user.id,
                  '*Bekor qilindi.\n*', reply_markup=new_markup, parse_mode='Markdown')
    # if message.text == "Qo'shimcha til kiritish":


    elif client.step == 1:
        client.full_name = message.text
        client.step += 1
        client.save()
        bot.send_message(message.from_user.id,
                  '*📅 Tug‘ilgan sanangiz : \n\nKK.OO.YYYY(16.10.1999) formatida:\n*', reply_markup=cancel_markup, parse_mode='Markdown')
    
    elif client.step == 2:
        client.born_date = message.text
        client.step += 1
        client.save()
        edu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Oliy")
        btn2 = types.KeyboardButton("Magistratura")
        btn3 = types.KeyboardButton("Talaba")
        btn4 = types.KeyboardButton("O\'rta maxsus")
        btn5 = types.KeyboardButton("Bekor qilish 🚫")
        edu_markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id,
                  '*Ma\'lumotingiz turini tanlang 💼 :\n*', reply_markup=edu_markup, parse_mode='Markdown')

    elif client.step == 3:
        client.current_state_education = message.text
        client.step += 1
        client.save() 
        bot.send_message(message.from_user.id,
                  '*Ta\'lim muassasining nomi va bitirgan yilingiz:\n*', reply_markup=main_markup, parse_mode='Markdown')
    
    elif client.step == 4:
        client.education_place = message.text
        client.step += 1
        client.save()
        marital_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Turmush qurgan")
        btn2 = types.KeyboardButton("Turmush qurmagan")
        btn3 = types.KeyboardButton("Bekor qilish 🚫") 
        marital_markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                  '*Oilaviy holatingiz 👨‍👩‍👧‍👦 :\n*', reply_markup=marital_markup, parse_mode='Markdown')

    elif client.step == 5:
        client.marital_status = message.text
        client.step += 1
        client.save()
        province_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3) 
        for region in regions:
            province_markup.add(types.KeyboardButton(f"{region}"))
        cancel = types.KeyboardButton("Bekor qilish 🚫")
        province_markup.add(cancel)
        bot.send_message(message.from_user.id,
                  '*Qaysi viloyatdansiz 🌐:\n*', reply_markup=province_markup, parse_mode='Markdown')
    elif client.step == 6:
        client.address_province = message.text
        client.step += 1
        client.save()
        bot.send_message(message.from_user.id,
                  "*To'liq manzilingizni kiriting (Tuman, MFY, ko'cha) 🌐:\n*", reply_markup=cancel_markup, parse_mode='Markdown')

    elif client.step == 7:
        client.address_region_full = message.text
        client.step += 1
        client.save()
        workplace_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Farg'ona tumani")
        btn2 = types.KeyboardButton("Qo'qon tumani")
        btn3 = types.KeyboardButton("Samarqand tumani")
        btn4 = types.KeyboardButton("Buvayda tumani")
        btn5 = types.KeyboardButton("Bekor qilish 🚫")
        workplace_markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id,
                  "*Qaysi filialda ishlashni xohlaysiz 🏘:\n*", reply_markup=workplace_markup, parse_mode='Markdown')

    elif client.step == 8:
        client.workplace = message.text
        client.step += 1
        client.save()
        rank_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Kredit bo'limi ishchisi")
        btn2 = types.KeyboardButton("Hisobchi")
        btn3 = types.KeyboardButton("Kassa ishchisi")
        btn4 = types.KeyboardButton("Unduruv bo'limi")
        btn5 = types.KeyboardButton("Qabulxonachi")
        btn6 = types.KeyboardButton("Oshpaz")
        btn7 = types.KeyboardButton("Farrosh")
        btn8 = types.KeyboardButton("Bekor qilish 🚫")
        rank_markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id,
                  "*Qaysi lavozimda ishlashni xohlaysiz?:\n*", reply_markup=rank_markup, parse_mode='Markdown')
    
    elif client.step == 9:
        client.rank = message.text
        client.step += 1
        client.save()
        bot.send_message(message.from_user.id,
                  "*Telefon raqamingizni 9xxxxxxxx ko'rinishida kiriting ☎️:\n*", reply_markup=main_markup, parse_mode='Markdown')

    
    elif client.step == 10:
        if str(message.text).isdigit():
            client.tel_number = message.text
            client.step += 1
            client.save()
            bot.send_message(message.from_user.id,
                             '*Avval qayerda ishlagansiz yoki amaliyot qilgansiz?\n\n\n*(Tashkilot nomi va ishlash vaqti davomiyligi)', reply_markup=main_markup, parse_mode='Markdown')
        else:
            bot.send_message(message.from_user.id,
                             '*Iltimos to\'g\'ri ma\'lumot kiriting🙅‍♂️*', parse_mode='Markdown')

    elif client.step == 11:
        client.work_experience = message.text
        client.step += 1
        client.save()
        it_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Boshlang'ich")
        btn2 = types.KeyboardButton("O'rta")
        btn3 = types.KeyboardButton("Yuqori")
        btn4 = types.KeyboardButton("Ekpert")
        btn5 = types.KeyboardButton("Bekor qilish 🚫")
        it_markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id,
                  "*Kompyuterni qaysi darajada bilasiz:*", reply_markup=it_markup, parse_mode='Markdown')

    elif client.step == 12:
        client.it_level = message.text
        client.step += 1
        client.save()
        lan_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Rus tili")
        btn2 = types.KeyboardButton("Ingliz tili")
        btn3 = types.KeyboardButton("Qo'shimcha til kiritish")
        btn5 = types.KeyboardButton("Bekor qilish 🚫")
        lan_markup.add(btn1, btn2, btn3, btn5)
        bot.send_message(message.from_user.id,
                  "*Qo'shimcha qaysi tillarni bilasiz?*", reply_markup=lan_markup, parse_mode='Markdown')

        # if message.text == "Qo'shimcha tilni kiriting:":
        #     bot.send_message(message.from_user.id,
        #           "Qo'shimcha tilni kiriting:", reply_markup=cancel_markup)
        #     client.language = 

    elif client.step == 13:     
        client.language = message.text
        client.step += 1
        client.save()
        confirm_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_confirm = types.KeyboardButton("Tasdiqlash ✅")
        btnc_cancel = types.KeyboardButton("Bekor qilish 🚫")
        confirm_markup.add(btn_confirm, btnc_cancel)
        bot.send_message(message.from_user.id,
              "*Ma\'lumotlar to\'g\'riligini tasdiqlang:\n*", parse_mode='Markdown')
        bot.send_message(message.from_user.id,
                          f"*Ism Familiya:   {client.full_name}\nTug'ilgan sana:     {client.born_date}\nTelefon raqami:     {client.tel_number}\nYashsh manzili:    {client.address_province} {client.address_region_full}\nMa'lumot turi:     {client.current_state_education}\nTa'lim muassasining nomi:     {client.education_place}\nOilayiv holati:     {client.marital_status}\nIshlamoqchi bo'lgan filial:    {client.workplace}\nIshlamoqchi bolgan lavozim:     {client.rank}\nAvval ishlagan yoki amaliyot qilgan joyi:    {client.work_experience}\nKompyuterni bilish darajasi:     {client.it_level}\nQaysi tillarni biladi:   {client.language}*", reply_markup=confirm_markup, parse_mode='Markdown')

    
   
    
    



    
