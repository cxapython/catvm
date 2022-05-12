var fs = require('fs');
var catvm2 = require('./CatVm2/catvm2.node.js');
//https://www.npmjs.com/package/vm2   npm install vm2  
const {VM,VMScript} = require('vm2') ;
const { NodeVM } = require('vm2');
var catvm2code = catvm2.run({
    proxy:true,
    print:true
},
`
    catvm.AddPlugin({description:"npAliSSOLogin Plugin",filename:"npalissologin.dll",name:"AliSSOLogin plugin",MimeTypes:[{description: "AliSSOLogin",suffixes: "AliSSOLogin",type: "application/npalissologin"},{description: "AliSSOLogin1",suffixes: "AliSSOLogin",type: "application1/npalissologin"}]});
    catvm.AddPlugin({description:"npAliSSOLogin Plugin",filename:"npalissologin1.dll",name:"AliSSOLogin plugin2",MimeTypes:[{description: "AliSSOLogin",suffixes: "AliSSOLogin",type: "application/npalissologin"},{description: "AliSSOLogin1",suffixes: "AliSSOLogin",type: "application1/npalissologin"}]});
`);
const codefile = `${__dirname}/code1.js`;
const vm = new VM();
debugger
const script = new VMScript(catvm2code + fs.readFileSync(codefile) , `${__dirname}/my.js`);
debugger
console.log(vm.run(script)) 
debugger



