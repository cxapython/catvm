var EventTarget =function EventTarget()  //构造函数
{
};  catvm.safefunction(EventTarget);

Object.defineProperties(EventTarget.prototype , {
     [Symbol.toStringTag]: {
         value: "EventTarget",
         configurable: true
     }
});
EventTarget.prototype.addEventListener = function addEventListener(type, callback){
    
    if(!(type in catvm.memory.listeners)) {
        catvm.memory.listeners[type] = [];
      }
      catvm.memory.listeners[type].push(callback);
}; catvm.safefunction(EventTarget.prototype.addEventListener);

EventTarget.prototype.dispatchEvent = function dispatchEvent(event_){
    if(event_[type] == undefined || event_[type] == "")
    {
        return ;
    }
    if(catvm.memory.listeners[event_[type]] != undefined )
    {
        return ;
    }
    for(var i=0; catvm.memory.listeners[event_[type]].length > i;i++)
    {
        catvm.memory.listeners[event_[type]][i].apply(this,event_);
    }
    debugger;
}; catvm.safefunction(EventTarget.prototype.dispatchEvent);

EventTarget.prototype.removeEventListener = function removeEventListener(){
    debugger;
}; catvm.safefunction(EventTarget.prototype.removeEventListener);


