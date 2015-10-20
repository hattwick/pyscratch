var qrImage = require('qr-image');
var fs = require('fs');

qrImage
	.image("This is what you get with a two pizza team, Jack", {type:'png', size:20})
	.pipe(fs.createWriteStream("MyQRCode.png"));
	
console.log('QR Code Generated !');
