window = this;
var Window = function Window(){
    //容易被检测到的  堆栈
    throw new TypeError("Illegal constructor");
}; catvm.safefunction(Window);
Object.defineProperties(Window.prototype , {
    [Symbol.toStringTag]: {
        value: "Window",
        configurable: true
    }
});
//////////////////////////////////
window.setTimeout = function setTimeout(x,d)
{
    //x 有可能是方法 也有可能是文本
    typeof(x) == "function"?x():undefined;
    typeof(x) == "string"?eval(x) :undefined;
    //正确应该 生成UUID  并且保存到内存
    return 0;
};   catvm.safefunction(window.setTimeout);
window.setInterval = function setTimeout(x,d)
{
    //x 有可能是方法 也有可能是文本
    typeof(x) == "function"?x():undefined;
    typeof(x) == "string"?eval(x) :undefined;
    //正确应该 生成UUID  并且保存到内存
    return 0;
};   catvm.safefunction(window.setInterval);
window.clearTimeout = function(){

};   catvm.safefunction(window.clearTimeout);
Window.prototype.PERSISTENT = 1;
Window.prototype.TEMPORARY = 0;
window.open = function open(){debugger;}; catvm.safefunction(window.open);
window.chrome = catvm.proxy(class chrome{});
window.DeviceOrientationEvent = function DeviceOrientationEvent(){debugger;}; catvm.safefunction(window.DeviceOrientationEvent);
window.DeviceMotionEvent= function DeviceMotionEvent(){debugger;}; catvm.safefunction(window.DeviceMotionEvent);
window.top = window;
window.frames = window;
window.onload = e => { };
window.length = 0;
window.onfocus = null;
window.fetch = function fetch(){

};   catvm.safefunction(window.fetch);


/////////////////////////////////


//window.localStorage =  class localStorage{};
//window.localStorage.getItem = function getItem(){debugger;};catvm.safefunction(window.localStorage.getItem);
//window.localStorage.setItem= function setItem(){debugger;};catvm.safefunction(window.localStorage.setItem);
//window.localStorage = catvm.proxy(window.localStorage)
/////////////////////////////////
Window.prototype.__proto__ = WindowProperties.prototype;


window.__proto__ = Window.prototype;

Window.prototype = catvm.proxy(Window.prototype)
window = catvm.proxy(window)