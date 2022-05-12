var HTMLLinkElement =function HTMLLinkElement()  {//构造函数
    throw new TypeError("Illegal constructor");
};  catvm.safefunction(HTMLLinkElement);


Object.defineProperties(HTMLLinkElement.prototype , {
    [Symbol.toStringTag]: {
        value: "HTMLLinkElement",
        configurable: true
    }
});

//真实的div
catvm.memory.htmlelements["link"] = function(){
    var link =  new (function(){});
    /////////////////////////////////////////////
    link.relList = catvm.memory.htmlelements["DOMTokenList"]();
    link.host = "pay.qq.com";
    link.setAttribute = function setAttribute(k,v){
        this[k] = v;
    }; catvm.safefunction(link.setAttribute);
    /////////////////////////////////////////////
    link.__proto__ = HTMLLinkElement.prototype;
    return catvm.proxy(link);
}
