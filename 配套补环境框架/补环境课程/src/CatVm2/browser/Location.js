var Location =function Location()  {//构造函数
    throw new TypeError("Illegal constructor");
};  catvm.safefunction(Location);

Object.defineProperties(Location.prototype , {
    [Symbol.toStringTag]: {
        value: "Location",
        configurable: false
    }
});
////////////////////////////////////////////////////////


location = {};
location.__proto__ = Location.prototype;
location.href = "https://www.douyin.com/user/MS4wLjABAAAANIeYi-Hoc7FKO4-q6_xCPh17UzdI8UAdefnRyYmwUUVrUx98dEKjZtBppy10U1HD?enter_method=video_title&author_id=2471313768191751&group_id=6907805825113279744&log_pb=%7B%22impr_id%22%3A%22021627458130795fdbddc0100fff0030ac23dd00000000938e009%22%7D&enter_from=video_detail";
location.port = "";
location.protocol ="https:";
location.host ="douyin.com";
location.toString = function toString(){return location.href};catvm.safefunction(location.toString);

////////////////////////////////////////////////////////




location = catvm.proxy(location);