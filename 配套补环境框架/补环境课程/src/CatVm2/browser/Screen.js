var Screen =function Screen()  {//构造函数
    throw new TypeError("Illegal constructor");
};  catvm.safefunction(Screen);

Object.defineProperties(Screen.prototype , {
    [Symbol.toStringTag]: {
        value: "Screen",
        configurable: true
    }
});
////////////////////////////////////////////////////////
Screen.prototype.availWidth  = 1040;
Screen.prototype.availHeight  = 1920;
////////////////////////////////////////////////////////
screen = {};
screen.__proto__ = Screen.prototype;


screen = catvm.proxy(screen);