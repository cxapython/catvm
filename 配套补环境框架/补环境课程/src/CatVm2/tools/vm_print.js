//框架日志功能
catvm.print = {}
catvm.print.open = true;
catvm.memory.print = [];
catvm.print.log = function (logType,target,property,value) {
  
    if (catvm.print.open && catvm.memory.config.print) {
        //开始保存日志
        if( catvm.memory.print.length == 111){
            debugger;
        }
        catvm.memory.print.push({"类型":logType,"调用者":target,"属性":property,"值":value});
    }
}
catvm.print.getall = function () {
    console.table(catvm.memory.print,["类型","调用者","属性","值"]);
}
