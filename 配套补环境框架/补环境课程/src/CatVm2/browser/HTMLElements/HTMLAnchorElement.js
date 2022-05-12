var HTMLAnchorElement =function HTMLAnchorElement()  {//构造函数
    throw new TypeError("Illegal constructor");
};  catvm.safefunction(HTMLAnchorElement);


Object.defineProperties(HTMLAnchorElement.prototype , {
    [Symbol.toStringTag]: {
        value: "HTMLAnchorElement",
        configurable: true
    }
});

//真实的div
catvm.memory.htmlelements["a"] = function(){
    var a =  new (function(){});
    /////////////////////////////////////////////
    a.setAttribute = function setAttribute(k,v){
        this[k] = v;
    }; catvm.safefunction(a.setAttribute);


    a.host = location.host;
    Object.defineProperty(a,'href',{
        get:function(){
            return location.href;
        }
    });
    /////////////////////////////////////////////
    a.__proto__ = HTMLAnchorElement.prototype;
    return catvm.proxy(a);
}
