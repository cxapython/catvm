function xx(pr,fo,name_) {
    var code = "";
    switch (typeof (pr[fo])) {
       
        case "function":
            var temp = name_+".prototype."+ fo;
            code = temp + "=" +"function "+fo+"(){debugger;};  catvm.safefunction("+temp+");";
            break;
        case "object":
            var temp = name_+".prototype."+ fo;
            code = temp + "=" +"catvm.proxy(class "+fo+"{});"
            break;
        default:
            code = name_+".prototype."+ fo + "=" +pr[fo] +";";
            break;
    }
    return code;
}

function getcode(pr,name_) {
    var code = "";
    for (var fo in pr.__proto__) {
        code += xx(pr,fo,name_) + "\r\n";
    }
    return code;
}