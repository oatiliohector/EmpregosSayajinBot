const express = require('express');
const serverless = require('serverless-http');

const cors = require('cors');

const app = express();

require('dotenv').config();

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.status(200).send('Hello world!');
})

app.get('/goodbye', (req, res) => {
  res.status(200).send('Goodbye World\n');
});

if (require.main === module) {
  app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
  });
} else {
  module.exports.app = serverless(app);
}
