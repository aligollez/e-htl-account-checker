import concurrent.futures
import requests
import telegram
from telegram.ext import Updater

updater = Updater("Bot_Tokeninizi_Giriniz", use_context=True)

def do(domain):
  try:
    url = requests.get('http://' + domain, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'}, timeout=3).url
    if url.endswith('/wp-admin/setup-config.php') or url.endswith('/wp-admin/install.php'):
      updater.bot.send_message(chat_id="Grubunuzun_veya_kendi_chatIDnizi_yazmaniz_lazim", text=url)
  except:
    pass
    
with open('domain-names.txt') as f:
  domain_list = f.read().splitlines()


updater.bot.send_message(chat_id="Grubunuzun_veya_kendi_chatIDnizi_yazmaniz_lazim", text="İşlem başlatıldı.")

with concurrent.futures.ThreadPoolExecutor(max_workers=32) as worker:
  for i in domain_list:
    worker.submit(do, i)

updater.bot.send_message(chat_id="Grubunuzun_veya_kendi_chatIDnizi_yazmaniz_lazim", text="İşlem tamamlandı.")
