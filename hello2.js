// "use strict";
var http = require('http');
// Stick to require statement for bringing modules in.  Node is still working on stabile module implementation

http
    .createServer((req, res) => {
    	res.writeHead(200, {'Content-type': 'text/html'});
    	res.end('<h1>Infra-TST VPC Reporting Reachable</h1>');
    })
    .listen(8080, () => console.log('Server listening on port 8080'));
