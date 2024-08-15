const express = require('express');
const serverless = require('serverless-http');
const PDFDocument = require('pdfkit');
const cors = require('cors');

const app = express();

require('dotenv').config();

app.use(cors());
app.use(express.json());

app.post('/', (req, res) => {
  const doc = new PDFDocument();
  let filename = req.body.filename;
  filename = encodeURIComponent(filename) + '.pdf';
  res.setHeader('Content-disposition', 'attachment; filename="' + filename + '"');
  res.setHeader('Content-type', 'application/pdf');
  const content = req.body.content;
  doc.y = 300;
  doc.text(content, 50, 50);
  doc.pipe(res);
  doc.end();
});

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
