var qrImage = require('qr-image');
var fs = require('fs');

qrImage
	.image("http://cagmypctest.wellington.com", {type:'png', size:20})
	.pipe(fs.createWriteStream("MyQRCode.png"));
	
console.log('QR Code Generated !');
