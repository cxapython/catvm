var fs = require('fs');


function GetCode(){
    var code = "";
    code += fs.readFileSync(`${__dirname}/DOMTokenList.js`) + "\r\n"
    code += fs.readFileSync(`${__dirname}/HTMLDivElement.js`) + "\r\n"
    code += fs.readFileSync(`${__dirname}/HTMLBodyElement.js`) + "\r\n"
    code += fs.readFileSync(`${__dirname}/HTMLLinkElement.js`) + "\r\n"
    code += fs.readFileSync(`${__dirname}/HTMLScriptElement.js`) + "\r\n"
    code += fs.readFileSync(`${__dirname}/HTMLAnchorElement.js`) + "\r\n"
    return code;
}

module.exports = {
    GetCode
}