var Storage =function Storage()  {//构造函数
    throw new TypeError("Illegal constructor");
};  catvm.safefunction(Storage);
Object.defineProperties(Storage.prototype , {
    [Symbol.toStringTag]: {
        value: "Storage",
        configurable: true
    }
});
/////////////////////////////////////

Storage.prototype.length=0;
Storage.prototype.clear=function clear(){
    debugger;
    var temp = Object.keys(this)
    for(var i =0;temp.length>i;i++)
    {
        delete this[temp[i]];
    }
};  catvm.safefunction(Storage.prototype.clear);
Storage.prototype.getItem=function getItem(k){
    debugger;
    return this[k];
};  catvm.safefunction(Storage.prototype.getItem);
Storage.prototype.key=function key(index){
    debugger;
    return Object.keys(this)[index];
};  catvm.safefunction(Storage.prototype.key);
Storage.prototype.removeItem=function removeItem(k){
    debugger;
    delete this[k];
};  catvm.safefunction(Storage.prototype.removeItem);
Storage.prototype.setItem=function setItem(k,v){
    debugger;
    this[k] = v;
};  catvm.safefunction(Storage.prototype.setItem);

/////这里容易被检测
Storage.prototype.__defineGetter__("length",function length(){
    return Object.keys(this).length;
});

/////////////////////////////////////
var localStorage = {}
localStorage.__proto__ = Storage.prototype;
localStorage = catvm.proxy(localStorage);

var sessionStorage = {}
sessionStorage.__proto__ = Storage.prototype;
sessionStorage = catvm.proxy(sessionStorage);