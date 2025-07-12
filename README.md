# Bot de Análise de Futebol

Este bot analisa jogos de futebol e envia os melhores palpites no Telegram.

### Filtros usados:
- +1.5 gols com probabilidade acima de 85%
- Ambos marcam (BTTS) acima de 70%

## Como usar no Railway

1. Crie uma conta em [https://railway.app](https://railway.app)
2. Crie um novo projeto e conecte este repositório
3. Adicione as variáveis de ambiente:
   - `TELEGRAM_TOKEN` = seu token do bot
   - `TELEGRAM_CHAT_ID` = seu ID de Telegram
4. Configure para rodar automaticamente (via cron job ou loop contínuo)
