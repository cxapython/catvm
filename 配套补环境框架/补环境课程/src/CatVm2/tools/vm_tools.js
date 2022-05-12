//更改浏览器的某些参数 常用的
//catvm.memory.Plugin.new({description:"npAliSSOLogin Plugin",filename:"npalissologin.dll",name:"AliSSOLogin plugin",MimeTypes:[{description: "AliSSOLogin",suffixes: "AliSSOLogin",type: "application/npalissologin"},{description: "AliSSOLogin1",suffixes: "AliSSOLogin",type: "application1/npalissologin"}]})

//在此文件下的代码 必须要框架run方法执行后执行
catvm.AddPlugin = function(data){
//{description:"npAliSSOLogin Plugin",filename:"npalissologin.dll",name:"AliSSOLogin plugin",MimeTypes:[{description: "AliSSOLogin",suffixes: "AliSSOLogin",type: "application/npalissologin"},{description: "AliSSOLogin1",suffixes: "AliSSOLogin",type: "application1/npalissologin"}]}
    if(catvm.memory.PluginArray.temp == undefined)
    {
        catvm.memory.PluginArray.temp = []
    }
    catvm.memory.PluginArray.temp.push(data);
}