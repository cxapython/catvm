


var HTMLDivElement =function HTMLDivElement()  {//构造函数
    throw new TypeError("Illegal constructor");
};  catvm.safefunction(HTMLDivElement);


Object.defineProperties(HTMLDivElement.prototype , {
    [Symbol.toStringTag]: {
        value: "HTMLDivElement",
        configurable: true
    }
});

//navigator = catvm.proxy(navigator);

//真实的div
catvm.memory.htmlelements["div"] = function(){
    var div =  new (function(){});
    /////////////////////////////////////////////
    div.align = "";
    div.host = "pay.qq.com";
    div.addEventListener = function addEventListener(){

    }; catvm.safefunction(div.addEventListener);
    div.setAttribute = function setAttribute(k,v){
        this[k] = v;
    }; catvm.safefunction(div.setAttribute);
    /////////////////////////////////////////////
    div.__proto__ = HTMLDivElement.prototype;
    return catvm.proxy(div);
}
