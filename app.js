const express = require('express');
const serverless = require('serverless-http');
const axios = require('axios');
const cors = require('cors');
require('dotenv').config();

const app = express();

app.use(cors());
app.use(express.json());

app.get('/bot', async (req, res) => {
  const bot_id = process.env.BOT_SECRET_ID;
  const channel_id = process.env.BOT_CHANNEL_ID;
  const message = 'Im Atilio but you can call me Heck!';
  const url = `https://api.telegram.org/bot${bot_id}/sendMessage`;

  if (!channel_id) {
    return res.status(400).json({ error: 'CHANNEL_ID is missing in environment variables' });
  }

  try {
    const response = await axios.post(url, {
      chat_id: channel_id,
      text: message,
    });
    return res.status(200).json(response.data);
  } catch (error) {
    console.error('Error sending message:', error.response ? error.response.data : error.message);
    return res.status(error.response ? error.response.status : 500).json({
      error: error.response ? error.response.data : 'Error',
    });
  }
});

if (require.main === module) {
  app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
  });
} else {
  module.exports.app = serverless(app);
}
