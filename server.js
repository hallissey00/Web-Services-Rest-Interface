var hprose = require("hprose");
function ping(name) {
    return "Ping " + name + "!";
}
var server = hprose.Server.create("http://127.0.0.1:5000/");
server.addFunction(ping);
server.start();