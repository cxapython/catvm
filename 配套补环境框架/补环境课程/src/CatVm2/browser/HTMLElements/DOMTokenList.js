var DOMTokenList =function DOMTokenList()  {//构造函数
    throw new TypeError("Illegal constructor");
};  catvm.safefunction(DOMTokenList);


Object.defineProperties(DOMTokenList.prototype , {
    [Symbol.toStringTag]: {
        value: "DOMTokenList",
        configurable: true
    }
});

//真实的div
catvm.memory.htmlelements["DOMTokenList"] = function(){
    var dOMTokenList =  new (function(){});
    /////////////////////////////////////////////
    dOMTokenList.setAttribute = function setAttribute(k,v){
        this[k] = v;
    }; catvm.safefunction(dOMTokenList.setAttribute);
    dOMTokenList.host = "pay.qq.com";
    dOMTokenList.supports = function supports(token){debugger;};catvm.safefunction(dOMTokenList.supports);
    /////////////////////////////////////////////
    dOMTokenList.__proto__ = DOMTokenList.prototype;
    return catvm.proxy(dOMTokenList);
}
