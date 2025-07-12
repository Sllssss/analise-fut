import requests
from telegram import Bot
import time
import os

# === CONFIGURAÇÕES ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def obter_jogos():
    jogos = [
        {"casa": "Flamengo", "fora": "Botafogo", "prob_1_5": 92, "prob_btts": 78},
        {"casa": "Corinthians", "fora": "Santos", "prob_1_5": 81, "prob_btts": 65},
        {"casa": "Chelsea", "fora": "Liverpool", "prob_1_5": 89, "prob_btts": 72},
        {"casa": "Real Madrid", "fora": "Barcelona", "prob_1_5": 95, "prob_btts": 88},
    ]
    return jogos

def filtrar_jogos(jogos):
    return [j for j in jogos if j['prob_1_5'] >= 85 and j['prob_btts'] >= 70]

def enviar_mensagem(bot, jogo):
    mensagem = f"📊 {jogo['casa']} x {jogo['fora']}\n"
    mensagem += f"⚽ +1.5 Gols: {jogo['prob_1_5']}%\n"
    mensagem += f"✉️ Ambos Marcam (BTTS): {jogo['prob_btts']}%"
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=mensagem)

def main():
    print("🔎 Rodando bot de análise...")
    bot = Bot(token=TELEGRAM_TOKEN)
    jogos = obter_jogos()
    selecionados = filtrar_jogos(jogos)
    if not selecionados:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="Nenhum jogo com +1.5 >85% e BTTS >70% encontrado hoje.")
    else:
        for jogo in selecionados:
            enviar_mensagem(bot, jogo)
            time.sleep(1)

if __name__ == '__main__':
    main()
