var Document = function Document() {//构造函数

}; catvm.safefunction(Document);
Object.defineProperties(Document.prototype, {
    [Symbol.toStringTag]: {
        value: "HTMLDocument",
        configurable: true
    }
});
document = {};

document.__proto__ = Document.prototype;
////////////////////////////////////////////////////////
document.head = catvm.proxy({});
document.body = catvm.memory.htmlelements["body"]();
document.cookie = "douyin.com; douyin.com; passport_csrf_token_default=ce1b7db9b04bf7ed1d101b9db1d3000f; passport_csrf_token=ce1b7db9b04bf7ed1d101b9db1d3000f; s_v_web_id=verify_c10e4cfe73d00ecc425e345df7393eba; MONITOR_WEB_ID=81102dbb-5909-47e8-af74-4da4c111b407";
document.referrer = location?.href || "";
document.getElementsByTagName = function getElementsByTagName(name_){
debugger;
return catvm.proxy({});

};  catvm.safefunction(document.getElementsByTagName);


document.getElementById = function getElementById(id) {
    debugger;
    switch (id) {
        case "xMidasToken":
            return (new class {
                get value() {
                    return window.__xMidasToken

                }
            })
        case "xMidasVersion":
            return (new class {
                getAttribute(e) {
                    if (e == 'width') {
                        return '325';
                    }
                }
            })
        default:
            const ele = catvm.memory.RunElementList.filter(t => t.id == id)[0];
            if (!ele) debugger;
            return ele;
    }
    //用id匹配当前环境内存种已有的Element
    //return catvm.memory.RunElementList.filter(t => t.id == id)[0];
}; catvm.safefunction(document.getElementById);

document.addEventListener = function addEventListener(type, listener, options, useCapture) {
    debugger
}; catvm.safefunction(document.addEventListener);

document.createElement = function createElement(tagName) {
    debugger
    var tagname = tagName.toLowerCase() + "";
    var ele;
    if (catvm.memory.htmlelements[tagname] == undefined) {
        ele = catvm.proxy(new class createElement { });
    } else {
        ele = catvm.memory.htmlelements[tagname]();
    }
    catvm.memory.RunElementList.push(ele);
    return ele;
}; catvm.safefunction(document.createElement);

////////////////////////////////////////////////////////

document = catvm.proxy(document);