const express = require('express');
const app = express();

/* Use Helmet
const helmet = require('helmet');
app.use(helmet.hidePoweredBy());
*/
// use only hide-powered-by middleware.
const hidePoweredBy = require("hide-powered-by");
app.use(hidePoweredBy());

// use framegard. Default: SAMEORIGIN.
const frameguard = require("frameguard");
app.use(frameguard({ action: 'deny' }));

// use xssFilter. But this is deprecated. Instead of this, use xXssProtection().
const xXssProtection = require("x-xss-protection");
app.use(xXssProtection());













































module.exports = app;
const api = require('./server.js');
app.use(express.static('public'));
app.disable('strict-transport-security');
app.use('/_api', api);
app.get("/", function (request, response) {
  response.sendFile(__dirname + '/views/index.html');
});
let port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Your app is listening on port ${port}`);
});
