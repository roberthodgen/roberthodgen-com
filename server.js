var express = require('express');

var app = express();

var OPTIONS = {
  root: './dist/'
};

app.use(express.static('./dist'));

app.get('/bundle.js', function (req, res) {
  res.sendFile('bundle.js', OPTIONS);
});

app.get('*', function (req, res) {
  res.sendFile('app.html', OPTIONS);
});

app.listen(3000, function () {
  console.log('Express server listening on port 3000...')
});
