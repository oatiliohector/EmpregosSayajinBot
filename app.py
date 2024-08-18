import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from modules.vagas.vagas_scrapping import VagasProgramador
from modules.telegram.telegram_integration import TelegramBot

load_dotenv()

app = Flask(__name__)

@app.route('/bot', methods=['GET'])
def bot():
    channel_id = os.getenv('BOT_CHANNEL_ID')

    if not channel_id:
        return jsonify({'error': 'CHANNEL_ID is missing in environment variables'}), 400

    vagas = VagasProgramador(
        site_name='indeed',
        search_term='programador',
        results_wanted=5,
        location='São Paulo',
        hours_old=24,
        country_indeed='Brazil'
    )

    jobs_df = vagas.pesquisar_vaga()

    if jobs_df.empty:
        message = "Nenhuma vaga encontrada."
    else:
        jobs = jobs_df.to_dict('records')
        message = "\n\n".join([f"{job['title']} - {job['company']} ({job['location']})" for job in jobs])

    telegram_bot = TelegramBot()
    response = telegram_bot.send_message(channel_id, message)

    if 'error' in response:
        return jsonify({'error': response['error']}), 500

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
