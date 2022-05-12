catvm.memory.MimeType = {}

var MimeType =function MimeType()  {//构造函数
    throw new TypeError("Illegal constructor");
};  catvm.safefunction(MimeType);


Object.defineProperties(MimeType.prototype , {
    [Symbol.toStringTag]: {
        value: "MimeType",
        configurable: true
    }
});
/////////////////////////////////
MimeType.prototype.description = "";
MimeType.prototype.enabledPlugin = null;
MimeType.prototype.suffixes = "";
MimeType.prototype.type = "";
for(var pr in MimeType.prototype){
    if(typeof(MimeType.prototype[pr]) != "function"){
        MimeType.prototype.__defineGetter__(pr,function(){
            throw new TypeError("Illegal constructor"); 
        });
    }
}
/////////////////////////////////
catvm.memory.MimeType.new = function(data,initPlugin){
    var mimetype = {};
    if(data!=undefined)
    {
        mimetype.description = data.description;
        mimetype.suffixes = data.suffixes;
        mimetype.type = data.type;
        mimetype.enabledPlugin = initPlugin;
    }

    mimetype.__proto__ = MimeType.prototype;
    return mimetype;
}
