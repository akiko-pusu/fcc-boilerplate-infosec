const express = require('express');
const app = express();

const helmet = require('helmet');

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

// use "dont-sniff-mimetype" instead of helmet.noSniff().
const dontSniffMimetype = require("dont-sniff-mimetype");
app.use(dontSniffMimetype());

// use 'ienoopen' instead of helmet.ieNoOpen().
const ienoopen = require("ienoopen");
app.use(ienoopen());

// use hsts to force https protocol.
const strictTransportSecurity = require("hsts");

// Sets "Strict-Transport-Security: max-age=7776000; includeSubDomains"
app.use(
  strictTransportSecurity({
    maxAge: 7776000, // 90 days in second.
  }),
);

// use 'dns-prefetch-control' instead of helmet.dnsPrefetchControl().
const dnsPrefetchControl = require("dns-prefetch-control");

// Set X-DNS-Prefetch-Control: off
app.use(dnsPrefetchControl());

// use 'nocache' instead of helmet.noCache().
const nocache = require("nocache");
app.use(nocache());


// use 'helmet-csp' instead of helmet.contentSecurityPolicy().
const contentSecurityPolicy = require("helmet-csp");
app.use(contentSecurityPolicy({
  useDefaults: true,
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", 'trusted-cdn.com']
  }
}));










































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
