var paymentModule = require('iota-payment')
var app = require('express')()
var ps = require('python-shell')


app.get("/", function (req, res) {
    res.send('hello world from 03_events example!');
});

let server = paymentModule.createServer(app)

// Start server with iota-payment module on '/payments'
server.listen(3000, function () {
    console.log(`Server started on http://localhost:3000 `)
})


//Create an event handler which is called, when a payment was successfull
var onPaymentCreated = function (payment) {
    console.log("onPaymentCreated", payment)
    let options = {
        scriptPath: './python/scripts',
        args: [payment.address, payment.amount]
    };

    ps.run('show_qr_code.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
    });
}

//Create an event handler which is called, when a payment was successfull
var onPaymentSuccess = function (payment) {
    console.log("onPaymentSuccess", payment)
    ps.run('python/scripts/show_success.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
    });
}


//Assign the event handler to an event:
paymentModule.on('paymentCreated', onPaymentCreated);
paymentModule.on('paymentSuccess', onPaymentSuccess);

