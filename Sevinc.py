import telethon
from gtts import gTTS
import random
import asyncio
from telethon import Button
from telethon.tl.types import MessageEntityPre
import os
from lazımlılar import log
from telethon.tl.types import InputMediaDice
import base64
from telethon import events, sync, Button
from lazımlılar.config import Sevinc, SUDO_USERS
from Toollar.Fuck import yeni_user, ayrılan_user
from Toollar.yazılacaklar import salam, sağol, sevinc
from Temalar.tema import tema
from oyunlar import *
import time
import youtube_dl
#Getdik Kodlamağa Ey
#Bura Baxma Gijdıllaxx

SAHİB = [5324143657, 2124305832]


##Ayrılma Mesajı
@Sevinc.on(events.ChatAction)
async def handler(event):
	if event.user_left:
		await event.reply(f"{random.choice(ayrılan_user)}")
		
# Bu repo edalet_22 tərəfindən yazılıb
# Öz adına çıxaran peysərdi
# Bu yazıları silmədən işlədin

# t.me/RoBotlarimTg | YouTube: RoBotlarimTg | t.me/EdaletSup
# t.me/aykhan_s | t.me/edalet_22
# GitHub: EdaletRoBot


#@edalet_22 terefindən @RoBotlarimTg üçün yazilib silmədən istifadə edin
@Sevinc.on(events.NewMessage(pattern="^/id ?(.*)"))
async def id(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_id = previous_message.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**Sizin Telegram id:** `{user_id}`")
        else:
            return await event.reply(f"**İstifadəçi id:** `{user_id}`\n**Qrup id:** `{chat_id}`")


#@edalet_22 terefindən @RoBotlarimTg üçün yazilib silmədən istifadə edin
    else:
        user_id = event.sender_id
        chat_id = event.chat_id
        if event.is_private:
            return await event.reply(f"**Sizin Telegram id:** `{user_id}`")
        else:
            return await event.reply(f"**İstifadəçi id:** `{user_id}`\n**Qrup id:** `{chat_id}`")
            



# YouTube downloader ayarları
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(id)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

# /song komutunu işleyen fonksiyon
@Sevinc.on(events.NewMessage(pattern='/song'))
async def handle_song(event):
    song_name = event.message.text.split('/song ')[-1]
    chat = await event.get_chat()
    if song_name:
        message = await event.respond('Şarkı aranıyor...')
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(f"ytsearch:{song_name}", download=False)['entries'][0]
                file_name = f"{info['id']}.{info['ext']}"
                ydl.download([info['webpage_url']])
                await client.send_file(chat.id, file=file_name, caption=f"🎧 Şarkı adı: {info['title']}\n🕒 Süre: {info['duration']}")
        except Exception as e:
            print(str(e))
            await message.edit('Şarkı bulunamadı.')
    else:
        await event.respond('Şarkı adını belirtmediniz.')




##Start Mesajı
@Sevinc.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
		if event.is_private:
		  		async for usr in Sevinc.iter_participants(event.chat_id):
		  			ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
		  			await Sevinc.send_message(-1001596585823, f"Start Verən İstifadəçi - {ad}")
		  			await event.reply(f"Salam, {ad} Mən Ruslan Tərəfindən Hazırlanmış Bir Sadə Botam\nƏraflı Məlumat Üçün @ordayam_5_deqiqeye Hesabına Yazın\n\nÇox Yaxında Yeni Funksiyalar Olacaq", buttons=(
		  			[Button.url('Kodlayan', 'https://t.me/ordayam_5_deqiqeye')],
		  	 	[Button.url('Köməkçi Asistan', 'https://t.me/edalet_22')],
		  	 	[Button.url('Oyun Qurubumuz', 'https://t.me/TheBorzMaf')],
		  	 	[Button.inline(f"Əmrlər", data="help")]
		  			),
		  			link_preview=False)
		  			


@Sevinc.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
		  			await event.edit("Salam Mən Ruslan Tərəfindən Hazırlanmış Bir Sadə Botam\nƏraflı Məlumat Üçün @ordayam_5_deqiqeye Hesabına Yazın\n\nÇox Yaxında Yeni Funksiyalar Olacaq", buttons=(
		  			[Button.url('Kodlayan', 'https://t.me/ordayam_5_deqiqeye')],
		  			[Button.url('Komekci Asistan', 'https://t.me/edalet_22')],
		  			[Button.url('Oyun Qurubumuz', 'https://t.me/TheBorzMaf')],
		  			[Button.inline(f"Əmrlər", data="help")],
		  			),
		  			link_preview=False)
		  			
		  			


@Sevinc.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):
		await event.edit("Salam Aşagıdakı Butonlara Basaraq Əmrlərimə Baxa Bilərsiz", buttons=(
		[
		Button.inline("Əyləncə", data="eylence")
		],
		[
		Button.inline("Process Stop", data="stop")
		],
		[
		Button.inline("Geri", data="start")
		],
		),
		link_preview=False)
		
		
		
@Sevinc.on(events.callbackquery.CallbackQuery(data="stop"))
async def handler(event):
		await event.edit("Tam Hazır Deyiləm", buttons=(
		[
		Button.url('Kodlayan', 'https://t.me/ordayam_5_deqiqeye')],
		[
		Button.inline('Geri', data="start")
		],
		),
		link_preview=False)
		
		
@Sevinc.on(events.callbackquery.CallbackQuery(data="eylence"))
async def handler(event):
		await event.edit("Salam Bu Mənim Əyləncə Əmrlərimdir\n\n/Tema yazaraq Butondan istifadə ede bilersiz\nBu Əm Vasitesile Size Maraqlı Sözler Ata Bilerem", buttons=(
		[Button.inline('Geri', data="help")
		],
		),
		link_preview=False)
		
		

		    
		    
		    
ad = ["1", "2", "3", "4", "5", "6", "7", "8"]

@Sevinc.on(events.NewMessage(pattern="/name"))
async def name(event):
	await event.reply(random.choice(ad), buttons=[
	Button.inline("Dəyiş", data="ad"),
	Button.inline("Geri", data="start")
	])
	
	
@Sevinc.on(events.callbackquery.CallbackQuery(data="ad"))
async def handler(event):
				await event.edit(random.choice(ad), buttons=[
				Button.inline("Dəyiş", data="ad"),
				Button.inline("Geri", data="start")
				
								])				
			
			
@Sevinc.on(events.NewMessage(incoming=True, from_users=SAHİB, pattern="^/Tema ?(.*)"))
async def yeni_mesaj (event:
		events.NewMessage.Event):
			await event.reply(f"{random.choice(tema)}", buttons=[
			Button.inline("Dəyiş", data="Tema"),
			Button.inline("Geri", data="start")
			])
			
@Sevinc.on(events.callbackquery.CallbackQuery(data="Tema"))
async def handler(event):
	await event.edit(f"{random.choice(tema)}", buttons=[
	Button.inline("Dəyiş", data="Tema"),
	Button.inline("Geri", data="start")
	])
	

						
##Başdadıq Kodlamağa Eyy
		
##Ala Yeri Sikdir Yatda
##Saat 01:18
##Və Mən Gıjdıllax Kimi Yatmıram
			
				
@Sevinc.on(events.NewMessage(pattern='/offline'))
async def handler(event):
				if str(event.sender_id) not in SUDO_USERS:
					return await event.reply("Sən Mənim Sahibim Deyilsən")
					await event.reply("Qoz Kimi İsleyirem", buttons=(
					[Button.url('Sahib', 'https://t.me/ordayam_5_deqiqeye')],
					),
					link_preview=False)
					
					


# /online komutunu işleyen fonksiyon
@Sevinc.on(events.NewMessage(pattern='/online'))
async def handle_online(event):
    sender = await event.get_sender()
    if sender.username == 'ordayam_5_deqeye':
        await event.respond('Deyerli Sahibim Ruslan Için Çalışıyorumm')
    else:
        await event.respond('Sən Mənim Sahibim Değilsin. Ben Sadece Ruslan İçin Çalısıyorum')

# Botu çalıştırma 

					

# Resimleri saklamak için bir liste 



		

				
##Ala Mənə Sevinc Lazımdı?
##Gedim Sikdirim Yatımda

##Və Bu Qədər Qalaninı Sabax
##Və Teen Wolf Başlamasina Son 2
#Dayay Sikdirdim
			
##Bu Botu Yaratmaqda Məqsəd Nədi Özümde Bilmirem
##Sencə Niyə? Çünki Gıjdıllağammmm

		
print("Sevinc Botun Bomba İşləyir...")
Sevinc.run_until_disconnected()