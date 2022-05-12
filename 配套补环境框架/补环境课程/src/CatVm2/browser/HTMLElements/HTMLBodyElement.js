var HTMLBodyElement =function HTMLBodyElement()  {//构造函数
    throw new TypeError("Illegal constructor");
};  catvm.safefunction(HTMLBodyElement);


Object.defineProperties(HTMLBodyElement.prototype , {
    [Symbol.toStringTag]: {
        value: "HTMLBodyElement",
        configurable: true
    }
});

//真实的div
catvm.memory.htmlelements["body"] = function(){
    var body =  new (function(){});
    /////////////////////////////////////////////
    body.align = "";
    body.clientWidth=1920,
    body.clientHeight=1080,
    // body.host = location.host;
    // body.setAttribute = function setAttribute(k,v){
    //     this[k] = v;
    // }; catvm.safefunction(body.setAttribute);
    body.appendChild=function appendChild(e){};catvm.safefunction(body.appendChild);
    body.getAttribute = function getAttribute(e){if(e == 'inited'){return null;}else{debugger}};catvm.safefunction(body.getAttribute);
    /////////////////////////////////////////////
    body.__proto__ = HTMLBodyElement.prototype;
    return catvm.proxy(body);
}
