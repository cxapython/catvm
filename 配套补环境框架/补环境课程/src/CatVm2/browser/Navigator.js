catvm.memory.navigator = {}

var Navigator =function Navigator()  {//构造函数
    throw new TypeError("Illegal constructor");
};  catvm.safefunction(Navigator);

Object.defineProperties(Navigator.prototype , {
    [Symbol.toStringTag]: {
        value: "Navigator",
        configurable: true
    }
});
////////////////////////////////////////////////////////
Navigator.prototype.plugins = [];
Navigator.prototype.languages = ["zh-CN", "zh"];
Navigator.prototype.userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36";
Navigator.prototype.appVersion = "5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36";
Navigator.prototype.vendor = "Google Inc.";
Navigator.prototype.appName = "Netscape";
Navigator.prototype.appCodeName = "Mozilla";
Navigator.prototype.javaEnabled = function javaEnabled(){
    return true
};catvm.safefunction(Navigator.prototype.javaEnabled);

Navigator.prototype.getBattery = function getBattery(){

}; catvm.safefunction(Navigator.prototype.getBattery);

navigator = {};
navigator.__proto__ = Navigator.prototype;


for (catvm.memory.navigator.temp in Navigator.prototype) {
    navigator[catvm.memory.navigator.temp] = Navigator.prototype[catvm.memory.navigator.temp];
    Navigator.prototype.__defineGetter__(catvm.memory.navigator.temp, function() {
        throw new TypeError("Illegal constructor"); 
    });
}

////////////////////////////////////////////////////////




navigator = catvm.proxy(navigator);