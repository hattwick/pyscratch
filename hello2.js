// Test web server.  
// Requires npm install network

// "use strict";
var http = require('http');
var server = http.createServer();
// Stick to require statement for bringing modules in.  Node is still working on stabile module implementation

server.on('request', function(req, res)  {
	res.end('Node Server is Listening');
});


// Get public IP

var network = require('network');

network.get_public_ip(function(err, ip) {
  console.log(err || ip); // log public IP address
})


// Get default Gateway address
network.get_gateway_ip(function(err, ip) {
  console.log(err || ip); // err may be 'No active network interface found.'
})

server.listen(8080)
console.log('Server running on http://localhost:9000')

// http
//     .createServer((req, res) => {
//    	res.writeHead(200, {'Content-type': 'text/html'});
//    	res.end('<h1>Infra-TST VPC Reporting Reachable</h1>');
//    })
//    .listen(8080, () => console.log('Server listening on port 8080'));
