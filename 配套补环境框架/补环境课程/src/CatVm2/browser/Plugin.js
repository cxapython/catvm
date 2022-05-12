catvm.memory.Plugin = {}

var Plugin =function Plugin()  {//构造函数
    throw new TypeError("Illegal constructor");
};  catvm.safefunction(Plugin);

catvm.memory.Plugin.iterator = function values(){
    debugger;
    return {
        next:function(){
            if(this.index_ == undefined)
            {
                this.index_ = 0;
            }
            var temp = this.self_[this.index_];
            this.index_++;
            if(temp!=undefined)
            {
                return {done:false,falvalue:temp};
            }
            else
            {
                return {done:true,falvalue:temp};
            }
        },
        self_:this
    }
};  catvm.safefunction(catvm.memory.Plugin.iterator);

Object.defineProperties(Plugin.prototype , {
    [Symbol.toStringTag]: {
        value: "Plugin",
        configurable: true
    },
    [Symbol.iterator]: {
        value: catvm.memory.Plugin.iterator,
        configurable: true
    }
});
///////////////////////////////////////
Plugin.prototype.description = "";
Plugin.prototype.filename = "";
Plugin.prototype.name = "";
Plugin.prototype.length = 0;

Plugin.prototype.item = function item(index){
    
    return this[index];
}; catvm.safefunction(Plugin.prototype.item);
Plugin.prototype.namedItem = function namedItem(key){
   
    return this[key];
}; catvm.safefunction(Plugin.prototype.namedItem);

for(var pr in Plugin.prototype){
    if(typeof(Plugin.prototype[pr]) != "function"){
        Plugin.prototype.__defineGetter__(pr,function(){
            throw new TypeError("Illegal constructor"); 
        });
    }
}
/////////////////////////////////////////
//{description:"npAliSSOLogin Plugin",filename:"npalissologin.dll",name:"AliSSOLogin plugin",MimeTypes:[{description: "AliSSOLogin",suffixes: "AliSSOLogin",type: "application/npalissologin"},{description: "AliSSOLogin1",suffixes: "AliSSOLogin",type: "application1/npalissologin"}]}
catvm.memory.Plugin.new = function(data){
    var plugin = {};
    
    if(data != undefined)
    {
        plugin.description = data.description;
        plugin.filename =  data.filename;
        plugin.name = data.name;
        //MimeType
        if(data.MimeTypes != undefined)
        {
            for (let mtindex = 0; mtindex < data.MimeTypes.length; mtindex++) {
                var mimeTypedata = data.MimeTypes[mtindex];
                ///////
                var mimeType = catvm.memory.MimeType.new(mimeTypedata,plugin);

                plugin[mtindex] = mimeType;
                //plugin[mimeType.type] = mimeType;
                Object.defineProperty(plugin,mimeType.type, {
                    value: mimeType

                });
            }

            plugin.length = data.MimeTypes.length;
        }
    }
  
    plugin.__proto__ = Plugin.prototype;
    return plugin;
}