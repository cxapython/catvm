var arry = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
];


var aaa;
!function(e) {
    var n = {}
      , a = {
        share: 0
    }
      , o = [];
    function s(t) {
        if (n[t])
            return n[t].exports;
        var i = n[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        return e[t].call(i.exports, i, i.exports, s),
        i.l = !0,
        i.exports
    };
    aaa = s;
}({
    "js_encrypt":function (e) {
//         function R(e, t, n, r) {
//                 t < 0 && (t = 65535 + t + 1);
//                 for (var i = 0, o = Math.min(e.length - n, 2); i < o; ++i)
//                     e[n + i] = (t & 255 << 8 * (r ? i : 1 - i)) >>> 8 * (r ? i : 1 - i)
//             };
//         function readInt8(e, t) {
//                 return t || undefined,
//                 128 & this[e] ? -1 * (255 - this[e] + 1) : this[e]
//             };
//         function writeInt8(e, t, n) {
//                 return e = +e,
//                 t |= 0,
//                 n || undefined,
//                 (e = Math.floor(e)),
//                 e < 0 && (e = 255 + e + 1),
//                 this[t] = 255 & e,
//                 t + 1
//             };
//         function readInt16LE(e, t) {
//                 t || undefined;
//                 var n = this[e] | this[e + 1] << 8;
//                 return 32768 & n ? 4294901760 | n : n
//             };
//         function readInt16BE(e, t) {
//                 t || undefined;
//                 var n = this[e + 1] | this[e] << 8;
//                 return 32768 & n ? 4294901760 | n : n
//             };
//         function writeInt16LE(e, t, n) {
//                 return e = +e,
//                 t |= 0,
//                 n || undefined,
//                 true ? (this[t] = 255 & e,
//                 this[t + 1] = e >>> 8) : R(this, e, t, !0),
//                 t + 2
//             };
//         function writeInt16BE(e, t, n) {
//                 return e = +e,
//                 t |= 0,
//                 n || I(this, e, t, 2, 32767, -32768),
//                 u.TYPED_ARRAY_SUPPORT ? (this[t] = e >>> 8,
//                 this[t + 1] = 255 & e) : R(this, e, t, !1),
//                 t + 2
//             };
//         function readUInt16LE(e, t) {
//                 return t || undefined,
//                 this[e] | this[e + 1] << 8
//             };
//         function readUInt16BE(e, t) {
//                 return t || undefined,
//                 this[e] << 8 | this[e + 1]
//             };
//         function writeUInt16LE(e, t, n) {
//                 return e = +e,
//                 t |= 0,
//                 n || undefined,
//                 true ? (this[t] = 255 & e,
//                 this[t + 1] = e >>> 8) : R(this, e, t, !0),
//                 t + 2
//             };
//         function writeUInt16BE(e, t, n) {
//                 return e = +e,
//                 t |= 0,
//                 n || undefined,
//                 true ? (this[t] = e >>> 8,
//                 this[t + 1] = 255 & e) : R(this, e, t, !1),
//                 t + 2
//             };
//         function readInt32LE(e, t) {
//                 return t || undefined,
//                 this[e] | this[e + 1] << 8 | this[e + 2] << 16 | this[e + 3] << 24
//             };
//         function writeInt32LE(e, t, n) {
//                 return e = +e,
//                 t |= 0,
//                 n || undefined,
//                 true ? (this[t] = 255 & e,
//                 this[t + 1] = e >>> 8,
//                 this[t + 2] = e >>> 16,
//                 this[t + 3] = e >>> 24) : j(this, e, t, !0),
//                 t + 4
//             };
//         function readUInt32LE(e, t) {
//                 return t || undefined,
//                 (this[e] | this[e + 1] << 8 | this[e + 2] << 16) + 16777216 * this[e + 3]
//             };
//         function writeUInt32LE(e, t, n) {
//                 return e = +e,
//                 t |= 0,
//                 n || undefined,
//                 true ? (this[t + 3] = e >>> 24,
//                 this[t + 2] = e >>> 16,
//                 this[t + 1] = e >>> 8,
//                 this[t] = 255 & e) : j(this, e, t, !0),
//                 t + 4
//             };
//         var i = aaa("9152");
//         function readFloatLE(e, t) {
//                 return t || undefined,
//                 i.read(this, e, !0, 23, 4)
//             };
//         function readFloatBE(e, t) {
//                 return t || undefined,
//                 i.read(this, e, !1, 23, 4)
//             };
//         function N(e, t, n, r, o) {
//                 return o || undefined,
//                 i.write(e, t, n, r, 23, 4),
//                 n + 4
//             }
//         function writeFloatLE(e, t, n) {
//                 return N(this, e, t, !0, n)
//             };
//         function writeFloatBE(e, t, n) {
//                 return N(this, e, t, !1, n)
//             };
//         function readDoubleLE(e, t) {
//                 return t || undefined,
//                 i.read(this, e, !0, 52, 8)
//             };
//         function readDoubleBE(e, t) {
//                 return t || undefined,
//                 i.read(this, e, !1, 52, 8)
//             };
//         function D(e, t, n, r, o) {
//                 return o || undefined,
//                 i.write(e, t, n, r, 52, 8),
//                 n + 8
//             }
//         function writeDoubleLE(e, t, n) {
//                 return D(this, e, t, !0, n)
//             };
//         function writeDoubleBE(e, t, n) {
//                 return D(this, e, t, !1, n)
//             };
//         function fromBits(e, t, n) {
//             return new r(e,t,n)
//         };
//         function fromNumber(e, t) {
//             if (isNaN(e))
//                 return t ? m : y;
//             if (t) {
//                 if (e < 0)
//                     return m;
//                 if (e >= p)
//                     return E
//             } else {
//                 if (e <= -v)
//                     return x;
//                 if (e + 1 >= v)
//                     return S
//             }
//             return e < 0 ? u(-e, t).neg() : c(e % h | 0, e / h | 0, t)
//         }
//         function c(e, t, n) {
//             return new r(e,t,n)
//         }
//         var OO = {
//     "x": [
//         1,
//         1,
//         null,
//         null
//     ],
//     "c": [
//         1,
//         1,
//         function(e, t) {
//                         return String.fromCharCode(e[t])
//                     }
//                     , function(e, t, n) {
//                         t[n] = e.charCodeAt(0)
//                     }
//     ],
//     "b": [
//         1,
//         1,
//         function(e, t) {
//                         return readInt8(t)
//                     }
//                     , function(e, t, n) {
//                         writeInt8(e, n, !0)
//                     }
//     ],
//     "B": [
//         1,
//         1,
//         function(e, t) {
//                         return e[t]
//                     }
//                     , function(e, t, n) {
//                         t[n] = e
//                     }
//     ],
//     "h": [
//         2,
//         2,
//         true ? function(e, t) {
//                         return readInt16LE(t)
//                     }
//                     : function(e, t) {
//                         return readInt16BE(t)
//                     }
//                     , true ? function(e, t, n) {
//                         return writeInt16LE(e, n, !0)
//                     }
//                     : function(e, t, n) {
//                         return writeInt16BE(e, n, !0)
//                     }
//     ],
//     "H": [
//         2,
//         2,
//         true ? function(e, t) {
//                         return readUInt16LE(t)
//                     }
//                     : function(e, t) {
//                         return readUInt16BE(t)
//                     }
//                     , true ? function(e, t, n) {
//                         return writeUInt16LE(e, n, !0)
//                     }
//                     : function(e, t, n) {
//                         return writeUInt16BE(e, n, !0)
//                     }
//     ],
//     "i": [
//         4,
//         4,
//         function(e, t) {
//                 return readInt32LE(t, !0)
//             },
//         function(e, t, n) {
//                 writeInt32LE(e, n, !0)
//             }
//     ],
//     "I": [
//         4,
//         4,
//         function(e, t) {
//                 return readUInt32LE(t, !0)
//             },
//         function(e, t, n) {
//                 writeUInt32LE(e, n, !0)
//             }
//     ],
//     "l": [
//         4,
//         4,
//         function(e, t) {
//                 return readInt32LE(t, !0)
//             },
//         function(e, t, n) {
//                 writeInt32LE(e, n, !0)
//             }
//     ],
//     "L": [
//         4,
//         4,
//         function(e, t) {
//                 return readUInt32LE(t, !0)
//             },
//         function(e, t, n) {
//                 writeUInt32LE(e, n, !0)
//             }
//     ],
//     "f": [
//         4,
//         4,
//         true ? function(e, t) {
//                         return readFloatLE(t)
//                     }
//                     : function(e, t) {
//                         return readFloatBE(t)
//                     }
//                     , true ? function(e, t, n) {
//                         return writeFloatLE(e, n, !0)
//                     }
//                     : function(e, t, n) {
//                         return writeFloatBE(e, n, !0)
//                     }
//     ],
//     "d": [
//         8,
//         8,
//         true ? function(e, t) {
//                         return readDoubleLE(t)
//                     }
//                     : function(e, t) {
//                         return readDoubleBE(t)
//                     }
//                     , true ? function(e, t, n) {
//                         return writeDoubleLE(e, n, !0)
//                     }
//                     : function(e, t, n) {
//                         return writeDoubleBE(e, n, !0)
//                     }
//     ],
//     "s": [
//         1,
//         1,
//         function(e, t, n) {
//                 var r = e.indexOf(0, t)
//                   , i = Math.min(t + n, -1 === r ? e.length : r);
//                 return e.slice(t, i).toString("utf8")
//             },
//         function(e, t, n, r) {
//                 var i = t.write(e, n, r, "utf8");
//                 i < r && t.fill(0, n + i, n + r)
//             }
//     ],
//     "p": [
//         1,
//         1,
//         function(e, t, n) {
//                 var r = e[0];
//                 return r >= n && (r = n - 1),
//                 t++,
//                 e.slice(t, t + r).toString("utf8")
//             },
//         function(e, n, r, i) {
//                 var o = t.alloc(e, "utf8")
//                   , a = o.length;
//                 a >= i && (a = i - 1),
//                 a > 255 && (a = 255),
//                 o[r] = a,
//                 o.copy(n, r + 1, 0, a),
//                 n.fill(0, r + 1 + a, r + i)
//             }
//     ],
//     "P": [
//         8,
//         8,
//         function(e, t) {
//                 return fromBits(readInt32LE(t), readInt32LE(t + 4), !0)
//             },
//         function(e, t, n) {
//             writeInt32LE(0, n, !0),
//             writeInt32LE(e, n + 4, !0)
//         }
//     ],
//     "q": [
//         8,
//         8,
//         function(e, t) {
//                 return r.fromBits(readInt32LE(t), readInt32LE(t + 4), !1)
//             },
//         function(e, t, n) {
//             writeInt32LE(0, n, !0),
//             writeInt32LE(e, n + 4, !0)
//         }
//     ],
//     "Q": [
//         8,
//         8,
//         function(e, t) {
//                 return r.fromBits(readInt32LE(t), readInt32LE(t + 4), !0)
//             },
//         function(e, t, n) {
//             writeInt32LE(0, n, !0),
//             writeInt32LE(e, n + 4, !0)
//         }
//     ],
//     "?": [
//         1,
//         1,
//         function(e, t) {
//                         return 0 !== e[t]
//                     },
//         function(e, t, n) {
//                         t[n] = e ? 1 : 0
//                     }
//     ]
// }
//         C = function(e) {
//                     var t = e[0]
//                       , r = !0
//                       , i = OO;
//                     switch (t) {
//                     case ">":
//                     }
//                     return {
//                         map: i,
//                         skipFirst: r
//                     }
//                 }
//         function unpackFrom(e, t, n, r) {
//                             var i = []
//                               , o = null
//                               , a = 0
//                               , s = C(e)
//                               , u = s.map;
//                             true && a++;
//                             for (var c = e.length; a < c; a++) {
//                                 var l = e[a];
//                                 if (l >= "0" && l <= "9")
//                                     o = null === o ? l : o + l;
//                                 else {
//                                     var f = u[l];
//                                     if (f) {
//                                         var d = f[0]
//                                           , h = f[1];
//                                         h > 1 && (r = Math.ceil(r / h) * h),
//                                         o = o ? parseInt(o, 10) : 0;
//                                         var p = void 0;
//                                         "s" === l ? (p = 1,
//                                         d = o) : "p" === l ? (p = 1,
//                                         d = o || 1) : p = o || 1;
//                                         for (var v = f[2]; p > 0; ) {
//                                             if (v) {
//                                                 if (n && r + d >= t.length)
//                                                     throw new Error("Reached end of buffer, can't unpack anymore data.");
//                                                 i.push(v(t, r, o))
//                                             }
//                                             r += d,
//                                             p--
//                                         }
//                                         o = null
//                                     }
//                                 }
//                             }
//                             return i
//                         }
        var x = {
            'unpack': function(e, t) {
                console.log(t)
                        function readUInt32BE(e) {
                            return 16777216 * t[e] + (t[e + 1] << 16 | t[e + 2] << 8 | t[e + 3])
                        }
                        var result = [readUInt32BE(0, !0)]
                    return result
                        },
            'pack': function (e, t, n) {
                function writeInt32BE(e, t, n) {
   
                    return  (arry[t] = e >>> 24,
                        arry[t + 1] = e >>> 16,
                        arry[t + 2] = e >>> 8,
                        arry[t + 3] = 255 & e)
                };
                writeInt32BE(0, n, !0),
                writeInt32BE(e, n + 4, !0)
                return new Uint8Array(t)
            }
        }

          , O = aaa("1a2a");
        function A(e) {
            return 128 & e ? 255 & (e << 1 ^ 27) : e << 1
        }
        function y(e) {
            return A(e) ^ e
        }
        function C(e) {
            return y(A(e))
        }
        function k(e) {
            return C(y(A(e)))
        }
        function j(e) {
            return k(e) ^ C(e) ^ y(e)
        }
        function SS() {
            for (var i = "/".concat('/bbs/app/api/share/data/'.split("/").filter((function(e) {
                return e
            }
            )).join("/"), "/"), n = "", a = "BCDFGHJKMNPQRTVWXY23456789", o = x.pack( Math.round(new Date().getTime()/1000), arry, 0), s = O("sha1", 'L2Jicy9hcHAvYXBpL3NoYXJlL2RhdGEv').update(o).digest(), r = 15 & s.slice(19, 20)[0], c = 2147483647 & x.unpack(">I", s.slice(r, r + 4))[0], l = 0; l < 5; l++) {
                var u = c % a.length;
                c = ~~(c / a.length),
                n += a[u]
            }
            var d = "".concat(function(e) {
                return e.reduce((function(e, t, i) {
                    return e + t
                }
                ))
            }(function(e) {
                var t = [0, 0, 0, 0];
                return t[0] = j(e[0]) ^ k(e[1]) ^ C(e[2]) ^ y(e[3]),
                t[1] = y(e[0]) ^ j(e[1]) ^ k(e[2]) ^ C(e[3]),
                t[2] = C(e[0]) ^ y(e[1]) ^ j(e[2]) ^ k(e[3]),
                t[3] = k(e[0]) ^ C(e[1]) ^ y(e[2]) ^ j(e[3]),
                e[0] = t[0],
                e[1] = t[1],
                e[2] = t[2],
                e[3] = t[3],
                e
            }(n.slice(-4).split("").map((function(e) {
                return e.charCodeAt()
            }
            )))) % 100);
            return d.length < 2 && (d = 0 + d),
            d = n + d

        }
            e.exports = {
            SS
        }
    },
    "3fb5": function(e, t) {
        "function" == typeof Object.create ? e.exports = function(e, t) {
            t && (e.super_ = t,
            e.prototype = Object.create(t.prototype, {
                constructor: {
                    value: e,
                    enumerable: !1,
                    writable: !0,
                    configurable: !0
                }
            }))
        }
        : e.exports = function(e, t) {
            if (t) {
                e.super_ = t;
                var n = function() {};
                n.prototype = t.prototype,
                e.prototype = new n,
                e.prototype.constructor = e
            }
        }
    },
    d424: function(e, t, n) {
        "use strict";
        var r = n("3fb5")
          , i = n("8707").Buffer
          , o = n("6430")
          , a = i.alloc(128)
          , s = 64;
        function u(e, t) {
            o.call(this, "digest"),
            "string" == typeof t && (t = i.from(t)),
            this._alg = e,
            this._key = t,
            t.length > s ? t = e(t) : t.length < s && (t = i.concat([t, a], s));
            for (var n = this._ipad = i.allocUnsafe(s), r = this._opad = i.allocUnsafe(s), u = 0; u < s; u++)
                n[u] = 54 ^ t[u],
                r[u] = 92 ^ t[u];
            this._hash = [n]
        }
        r(u, o),
        u.prototype._update = function(e) {
            this._hash.push(e)
        }
        ,
        u.prototype._final = function() {
            var e = this._alg(i.concat(this._hash));
            return this._alg(i.concat([this._opad, e]))
        }
        ,
        e.exports = u
    },
    8707: function(e, t, n) {
        var r = n("b639")
          , i = r.Buffer;
        function o(e, t) {
            for (var n in e)
                t[n] = e[n]
        }
        function a(e, t, n) {
            return i(e, t, n)
        }
        i.from && i.alloc && i.allocUnsafe && i.allocUnsafeSlow ? e.exports = r : (o(r, t),
        t.Buffer = a),
        a.prototype = Object.create(i.prototype),
        o(i, a),
        a.from = function(e, t, n) {
            if ("number" == typeof e)
                throw new TypeError("Argument must not be a number");
            return i(e, t, n)
        }
        ,
        a.alloc = function(e, t, n) {
            if ("number" != typeof e)
                throw new TypeError("Argument must be a number");
            var r = i(e);
            return void 0 !== t ? "string" == typeof n ? r.fill(t, n) : r.fill(t) : r.fill(0),
            r
        }
        ,
        a.allocUnsafe = function(e) {
            if ("number" != typeof e)
                throw new TypeError("Argument must be a number");
            return i(e)
        }
        ,
        a.allocUnsafeSlow = function(e) {
            if ("number" != typeof e)
                throw new TypeError("Argument must be a number");
            return r.SlowBuffer(e)
        }
    },
    b639: function(e, t, n) {
        "use strict";
        (function(e) {
            var r = n("1fb5")
              , i = n("9152")
              , o = n("e3db");
            function a() {
                return u.TYPED_ARRAY_SUPPORT ? 2147483647 : 1073741823
            }
            function s(e, t) {
                if (a() < t)
                    throw new RangeError("Invalid typed array length");
                return u.TYPED_ARRAY_SUPPORT ? (e = new Uint8Array(t)).__proto__ = u.prototype : (null === e && (e = new u(t)),
                e.length = t),
                e
            }
            function u(e, t, n) {
                if (!(u.TYPED_ARRAY_SUPPORT || this instanceof u))
                    return new u(e,t,n);
                if ("number" == typeof e) {
                    if ("string" == typeof t)
                        throw new Error("If encoding is specified then the first argument must be a string");
                    return f(this, e)
                }
                return c(this, e, t, n)
            }
            function c(e, t, n, r) {
                if ("number" == typeof t)
                    throw new TypeError('"value" argument must not be a number');
                return "undefined" != typeof ArrayBuffer && t instanceof ArrayBuffer ? function(e, t, n, r) {
                    if (t.byteLength,
                    n < 0 || t.byteLength < n)
                        throw new RangeError("'offset' is out of bounds");
                    if (t.byteLength < n + (r || 0))
                        throw new RangeError("'length' is out of bounds");
                    return t = void 0 === n && void 0 === r ? new Uint8Array(t) : void 0 === r ? new Uint8Array(t,n) : new Uint8Array(t,n,r),
                    u.TYPED_ARRAY_SUPPORT ? (e = t).__proto__ = u.prototype : e = d(e, t),
                    e
                }(e, t, n, r) : "string" == typeof t ? function(e, t, n) {
                    if ("string" == typeof n && "" !== n || (n = "utf8"),
                    !u.isEncoding(n))
                        throw new TypeError('"encoding" must be a valid string encoding');
                    var r = 0 | p(t, n)
                      , i = (e = s(e, r)).write(t, n);
                    return i !== r && (e = e.slice(0, i)),
                    e
                }(e, t, n) : function(e, t) {
                    if (u.isBuffer(t)) {
                        var n = 0 | h(t.length);
                        return 0 === (e = s(e, n)).length || t.copy(e, 0, 0, n),
                        e
                    }
                    if (t) {
                        if ("undefined" != typeof ArrayBuffer && t.buffer instanceof ArrayBuffer || "length"in t)
                            return "number" != typeof t.length || function(e) {
                                return e != e
                            }(t.length) ? s(e, 0) : d(e, t);
                        if ("Buffer" === t.type && o(t.data))
                            return d(e, t.data)
                    }
                    throw new TypeError("First argument must be a string, Buffer, ArrayBuffer, Array, or array-like object.")
                }(e, t)
            }
            function l(e) {
                if ("number" != typeof e)
                    throw new TypeError('"size" argument must be a number');
                if (e < 0)
                    throw new RangeError('"size" argument must not be negative')
            }
            function f(e, t) {
                if (l(t),
                e = s(e, t < 0 ? 0 : 0 | h(t)),
                !u.TYPED_ARRAY_SUPPORT)
                    for (var n = 0; n < t; ++n)
                        e[n] = 0;
                return e
            }
            function d(e, t) {
                var n = t.length < 0 ? 0 : 0 | h(t.length);
                e = s(e, n);
                for (var r = 0; r < n; r += 1)
                    e[r] = 255 & t[r];
                return e
            }
            function h(e) {
                if (e >= a())
                    throw new RangeError("Attempt to allocate Buffer larger than maximum size: 0x" + a().toString(16) + " bytes");
                return 0 | e
            }
            function p(e, t) {
                if (u.isBuffer(e))
                    return e.length;
                if ("undefined" != typeof ArrayBuffer && "function" == typeof ArrayBuffer.isView && (ArrayBuffer.isView(e) || e instanceof ArrayBuffer))
                    return e.byteLength;
                "string" != typeof e && (e = "" + e);
                var n = e.length;
                if (0 === n)
                    return 0;
                for (var r = !1; ; )
                    switch (t) {
                    case "ascii":
                    case "latin1":
                    case "binary":
                        return n;
                    case "utf8":
                    case "utf-8":
                    case void 0:
                        return $(e).length;
                    case "ucs2":
                    case "ucs-2":
                    case "utf16le":
                    case "utf-16le":
                        return 2 * n;
                    case "hex":
                        return n >>> 1;
                    case "base64":
                        return W(e).length;
                    default:
                        if (r)
                            return $(e).length;
                        t = ("" + t).toLowerCase(),
                        r = !0
                    }
            }
            function v(e, t, n) {
                var r = !1;
                if ((void 0 === t || t < 0) && (t = 0),
                t > this.length)
                    return "";
                if ((void 0 === n || n > this.length) && (n = this.length),
                n <= 0)
                    return "";
                if ((n >>>= 0) <= (t >>>= 0))
                    return "";
                for (e || (e = "utf8"); ; )
                    switch (e) {
                    case "hex":
                        return P(this, t, n);
                    case "utf8":
                    case "utf-8":
                        return O(this, t, n);
                    case "ascii":
                        return A(this, t, n);
                    case "latin1":
                    case "binary":
                        return C(this, t, n);
                    case "base64":
                        return T(this, t, n);
                    case "ucs2":
                    case "ucs-2":
                    case "utf16le":
                    case "utf-16le":
                        return M(this, t, n);
                    default:
                        if (r)
                            throw new TypeError("Unknown encoding: " + e);
                        e = (e + "").toLowerCase(),
                        r = !0
                    }
            }
            function g(e, t, n) {
                var r = e[t];
                e[t] = e[n],
                e[n] = r
            }
            function y(e, t, n, r, i) {
                if (0 === e.length)
                    return -1;
                if ("string" == typeof n ? (r = n,
                n = 0) : n > 2147483647 ? n = 2147483647 : n < -2147483648 && (n = -2147483648),
                n = +n,
                isNaN(n) && (n = i ? 0 : e.length - 1),
                n < 0 && (n = e.length + n),
                n >= e.length) {
                    if (i)
                        return -1;
                    n = e.length - 1
                } else if (n < 0) {
                    if (!i)
                        return -1;
                    n = 0
                }
                if ("string" == typeof t && (t = u.from(t, r)),
                u.isBuffer(t))
                    return 0 === t.length ? -1 : m(e, t, n, r, i);
                if ("number" == typeof t)
                    return t &= 255,
                    u.TYPED_ARRAY_SUPPORT && "function" == typeof Uint8Array.prototype.indexOf ? i ? Uint8Array.prototype.indexOf.call(e, t, n) : Uint8Array.prototype.lastIndexOf.call(e, t, n) : m(e, [t], n, r, i);
                throw new TypeError("val must be string, number or Buffer")
            }
            function m(e, t, n, r, i) {
                var o, a = 1, s = e.length, u = t.length;
                if (void 0 !== r && ("ucs2" === (r = String(r).toLowerCase()) || "ucs-2" === r || "utf16le" === r || "utf-16le" === r)) {
                    if (e.length < 2 || t.length < 2)
                        return -1;
                    a = 2,
                    s /= 2,
                    u /= 2,
                    n /= 2
                }
                function c(e, t) {
                    return 1 === a ? e[t] : e.readUInt16BE(t * a)
                }
                if (i) {
                    var l = -1;
                    for (o = n; o < s; o++)
                        if (c(e, o) === c(t, -1 === l ? 0 : o - l)) {
                            if (-1 === l && (l = o),
                            o - l + 1 === u)
                                return l * a
                        } else
                            -1 !== l && (o -= o - l),
                            l = -1
                } else
                    for (n + u > s && (n = s - u),
                    o = n; o >= 0; o--) {
                        for (var f = !0, d = 0; d < u; d++)
                            if (c(e, o + d) !== c(t, d)) {
                                f = !1;
                                break
                            }
                        if (f)
                            return o
                    }
                return -1
            }
            function b(e, t, n, r) {
                n = Number(n) || 0;
                var i = e.length - n;
                r ? (r = Number(r)) > i && (r = i) : r = i;
                var o = t.length;
                if (o % 2 != 0)
                    throw new TypeError("Invalid hex string");
                r > o / 2 && (r = o / 2);
                for (var a = 0; a < r; ++a) {
                    var s = parseInt(t.substr(2 * a, 2), 16);
                    if (isNaN(s))
                        return a;
                    e[n + a] = s
                }
                return a
            }
            function w(e, t, n, r) {
                return z($(t, e.length - n), e, n, r)
            }
            function _(e, t, n, r) {
                return z(function(e) {
                    for (var t = [], n = 0; n < e.length; ++n)
                        t.push(255 & e.charCodeAt(n));
                    return t
                }(t), e, n, r)
            }
            function S(e, t, n, r) {
                return _(e, t, n, r)
            }
            function E(e, t, n, r) {
                return z(W(t), e, n, r)
            }
            function x(e, t, n, r) {
                return z(function(e, t) {
                    for (var n, r, i, o = [], a = 0; a < e.length && !((t -= 2) < 0); ++a)
                        r = (n = e.charCodeAt(a)) >> 8,
                        i = n % 256,
                        o.push(i),
                        o.push(r);
                    return o
                }(t, e.length - n), e, n, r)
            }
            function T(e, t, n) {
                return 0 === t && n === e.length ? r.fromByteArray(e) : r.fromByteArray(e.slice(t, n))
            }
            function O(e, t, n) {
                n = Math.min(e.length, n);
                for (var r = [], i = t; i < n; ) {
                    var o, a, s, u, c = e[i], l = null, f = c > 239 ? 4 : c > 223 ? 3 : c > 191 ? 2 : 1;
                    if (i + f <= n)
                        switch (f) {
                        case 1:
                            c < 128 && (l = c);
                            break;
                        case 2:
                            128 == (192 & (o = e[i + 1])) && ((u = (31 & c) << 6 | 63 & o) > 127 && (l = u));
                            break;
                        case 3:
                            o = e[i + 1],
                            a = e[i + 2],
                            128 == (192 & o) && 128 == (192 & a) && ((u = (15 & c) << 12 | (63 & o) << 6 | 63 & a) > 2047 && (u < 55296 || u > 57343) && (l = u));
                            break;
                        case 4:
                            o = e[i + 1],
                            a = e[i + 2],
                            s = e[i + 3],
                            128 == (192 & o) && 128 == (192 & a) && 128 == (192 & s) && ((u = (15 & c) << 18 | (63 & o) << 12 | (63 & a) << 6 | 63 & s) > 65535 && u < 1114112 && (l = u))
                        }
                    null === l ? (l = 65533,
                    f = 1) : l > 65535 && (l -= 65536,
                    r.push(l >>> 10 & 1023 | 55296),
                    l = 56320 | 1023 & l),
                    r.push(l),
                    i += f
                }
                return function(e) {
                    var t = e.length;
                    if (t <= k)
                        return String.fromCharCode.apply(String, e);
                    var n = ""
                      , r = 0;
                    for (; r < t; )
                        n += String.fromCharCode.apply(String, e.slice(r, r += k));
                    return n
                }(r)
            }
            t.Buffer = u,
            t.SlowBuffer = function(e) {
                return +e != e && (e = 0),
                u.alloc(+e)
            }
            ,
            t.INSPECT_MAX_BYTES = 50,
            u.TYPED_ARRAY_SUPPORT = void 0 !== e.TYPED_ARRAY_SUPPORT ? e.TYPED_ARRAY_SUPPORT : function() {
                try {
                    var e = new Uint8Array(1);
                    return e.__proto__ = {
                        __proto__: Uint8Array.prototype,
                        foo: function() {
                            return 42
                        }
                    },
                    42 === e.foo() && "function" == typeof e.subarray && 0 === e.subarray(1, 1).byteLength
                } catch (e) {
                    return !1
                }
            }(),
            t.kMaxLength = a(),
            u.poolSize = 8192,
            u._augment = function(e) {
                return e.__proto__ = u.prototype,
                e
            }
            ,
            u.from = function(e, t, n) {
                return c(null, e, t, n)
            }
            ,
            u.TYPED_ARRAY_SUPPORT && (u.prototype.__proto__ = Uint8Array.prototype,
            u.__proto__ = Uint8Array,
            "undefined" != typeof Symbol && Symbol.species && u[Symbol.species] === u && Object.defineProperty(u, Symbol.species, {
                value: null,
                configurable: !0
            })),
            u.alloc = function(e, t, n) {
                return function(e, t, n, r) {
                    return l(t),
                    t <= 0 ? s(e, t) : void 0 !== n ? "string" == typeof r ? s(e, t).fill(n, r) : s(e, t).fill(n) : s(e, t)
                }(null, e, t, n)
            }
            ,
            u.allocUnsafe = function(e) {
                return f(null, e)
            }
            ,
            u.allocUnsafeSlow = function(e) {
                return f(null, e)
            }
            ,
            u.isBuffer = function(e) {
                return !(null == e || !e._isBuffer)
            }
            ,
            u.compare = function(e, t) {
                if (!u.isBuffer(e) || !u.isBuffer(t))
                    throw new TypeError("Arguments must be Buffers");
                if (e === t)
                    return 0;
                for (var n = e.length, r = t.length, i = 0, o = Math.min(n, r); i < o; ++i)
                    if (e[i] !== t[i]) {
                        n = e[i],
                        r = t[i];
                        break
                    }
                return n < r ? -1 : r < n ? 1 : 0
            }
            ,
            u.isEncoding = function(e) {
                switch (String(e).toLowerCase()) {
                case "hex":
                case "utf8":
                case "utf-8":
                case "ascii":
                case "latin1":
                case "binary":
                case "base64":
                case "ucs2":
                case "ucs-2":
                case "utf16le":
                case "utf-16le":
                    return !0;
                default:
                    return !1
                }
            }
            ,
            u.concat = function(e, t) {
                if (!o(e))
                    throw new TypeError('"list" argument must be an Array of Buffers');
                if (0 === e.length)
                    return u.alloc(0);
                var n;
                if (void 0 === t)
                    for (t = 0,
                    n = 0; n < e.length; ++n)
                        t += e[n].length;
                var r = u.allocUnsafe(t)
                  , i = 0;
                for (n = 0; n < e.length; ++n) {
                    var a = e[n];
                    if (!u.isBuffer(a))
                        throw new TypeError('"list" argument must be an Array of Buffers');
                    a.copy(r, i),
                    i += a.length
                }
                return r
            }
            ,
            u.byteLength = p,
            u.prototype._isBuffer = !0,
            u.prototype.swap16 = function() {
                var e = this.length;
                if (e % 2 != 0)
                    throw new RangeError("Buffer size must be a multiple of 16-bits");
                for (var t = 0; t < e; t += 2)
                    g(this, t, t + 1);
                return this
            }
            ,
            u.prototype.swap32 = function() {
                var e = this.length;
                if (e % 4 != 0)
                    throw new RangeError("Buffer size must be a multiple of 32-bits");
                for (var t = 0; t < e; t += 4)
                    g(this, t, t + 3),
                    g(this, t + 1, t + 2);
                return this
            }
            ,
            u.prototype.swap64 = function() {
                var e = this.length;
                if (e % 8 != 0)
                    throw new RangeError("Buffer size must be a multiple of 64-bits");
                for (var t = 0; t < e; t += 8)
                    g(this, t, t + 7),
                    g(this, t + 1, t + 6),
                    g(this, t + 2, t + 5),
                    g(this, t + 3, t + 4);
                return this
            }
            ,
            u.prototype.toString = function() {
                var e = 0 | this.length;
                return 0 === e ? "" : 0 === arguments.length ? O(this, 0, e) : v.apply(this, arguments)
            }
            ,
            u.prototype.equals = function(e) {
                if (!u.isBuffer(e))
                    throw new TypeError("Argument must be a Buffer");
                return this === e || 0 === u.compare(this, e)
            }
            ,
            u.prototype.inspect = function() {
                var e = ""
                  , n = t.INSPECT_MAX_BYTES;
                return this.length > 0 && (e = this.toString("hex", 0, n).match(/.{2}/g).join(" "),
                this.length > n && (e += " ... ")),
                "<Buffer " + e + ">"
            }
            ,
            u.prototype.compare = function(e, t, n, r, i) {
                if (!u.isBuffer(e))
                    throw new TypeError("Argument must be a Buffer");
                if (void 0 === t && (t = 0),
                void 0 === n && (n = e ? e.length : 0),
                void 0 === r && (r = 0),
                void 0 === i && (i = this.length),
                t < 0 || n > e.length || r < 0 || i > this.length)
                    throw new RangeError("out of range index");
                if (r >= i && t >= n)
                    return 0;
                if (r >= i)
                    return -1;
                if (t >= n)
                    return 1;
                if (this === e)
                    return 0;
                for (var o = (i >>>= 0) - (r >>>= 0), a = (n >>>= 0) - (t >>>= 0), s = Math.min(o, a), c = this.slice(r, i), l = e.slice(t, n), f = 0; f < s; ++f)
                    if (c[f] !== l[f]) {
                        o = c[f],
                        a = l[f];
                        break
                    }
                return o < a ? -1 : a < o ? 1 : 0
            }
            ,
            u.prototype.includes = function(e, t, n) {
                return -1 !== this.indexOf(e, t, n)
            }
            ,
            u.prototype.indexOf = function(e, t, n) {
                return y(this, e, t, n, !0)
            }
            ,
            u.prototype.lastIndexOf = function(e, t, n) {
                return y(this, e, t, n, !1)
            }
            ,
            u.prototype.write = function(e, t, n, r) {
                if (void 0 === t)
                    r = "utf8",
                    n = this.length,
                    t = 0;
                else if (void 0 === n && "string" == typeof t)
                    r = t,
                    n = this.length,
                    t = 0;
                else {
                    if (!isFinite(t))
                        throw new Error("Buffer.write(string, encoding, offset[, length]) is no longer supported");
                    t |= 0,
                    isFinite(n) ? (n |= 0,
                    void 0 === r && (r = "utf8")) : (r = n,
                    n = void 0)
                }
                var i = this.length - t;
                if ((void 0 === n || n > i) && (n = i),
                e.length > 0 && (n < 0 || t < 0) || t > this.length)
                    throw new RangeError("Attempt to write outside buffer bounds");
                r || (r = "utf8");
                for (var o = !1; ; )
                    switch (r) {
                    case "hex":
                        return b(this, e, t, n);
                    case "utf8":
                    case "utf-8":
                        return w(this, e, t, n);
                    case "ascii":
                        return _(this, e, t, n);
                    case "latin1":
                    case "binary":
                        return S(this, e, t, n);
                    case "base64":
                        return E(this, e, t, n);
                    case "ucs2":
                    case "ucs-2":
                    case "utf16le":
                    case "utf-16le":
                        return x(this, e, t, n);
                    default:
                        if (o)
                            throw new TypeError("Unknown encoding: " + r);
                        r = ("" + r).toLowerCase(),
                        o = !0
                    }
            }
            ,
            u.prototype.toJSON = function() {
                return {
                    type: "Buffer",
                    data: Array.prototype.slice.call(this._arr || this, 0)
                }
            }
            ;
            var k = 4096;
            function A(e, t, n) {
                var r = "";
                n = Math.min(e.length, n);
                for (var i = t; i < n; ++i)
                    r += String.fromCharCode(127 & e[i]);
                return r
            }
            function C(e, t, n) {
                var r = "";
                n = Math.min(e.length, n);
                for (var i = t; i < n; ++i)
                    r += String.fromCharCode(e[i]);
                return r
            }
            function P(e, t, n) {
                var r = e.length;
                (!t || t < 0) && (t = 0),
                (!n || n < 0 || n > r) && (n = r);
                for (var i = "", o = t; o < n; ++o)
                    i += U(e[o]);
                return i
            }
            function M(e, t, n) {
                for (var r = e.slice(t, n), i = "", o = 0; o < r.length; o += 2)
                    i += String.fromCharCode(r[o] + 256 * r[o + 1]);
                return i
            }
            function L(e, t, n) {
                if (e % 1 != 0 || e < 0)
                    throw new RangeError("offset is not uint");
                if (e + t > n)
                    throw new RangeError("Trying to access beyond buffer length")
            }
            function I(e, t, n, r, i, o) {
                if (!u.isBuffer(e))
                    throw new TypeError('"buffer" argument must be a Buffer instance');
                if (t > i || t < o)
                    throw new RangeError('"value" argument is out of bounds');
                if (n + r > e.length)
                    throw new RangeError("Index out of range")
            }
            function R(e, t, n, r) {
                t < 0 && (t = 65535 + t + 1);
                for (var i = 0, o = Math.min(e.length - n, 2); i < o; ++i)
                    e[n + i] = (t & 255 << 8 * (r ? i : 1 - i)) >>> 8 * (r ? i : 1 - i)
            }
            function j(e, t, n, r) {
                t < 0 && (t = 4294967295 + t + 1);
                for (var i = 0, o = Math.min(e.length - n, 4); i < o; ++i)
                    e[n + i] = t >>> 8 * (r ? i : 3 - i) & 255
            }
            function B(e, t, n, r, i, o) {
                if (n + r > e.length)
                    throw new RangeError("Index out of range");
                if (n < 0)
                    throw new RangeError("Index out of range")
            }
            function N(e, t, n, r, o) {
                return o || B(e, 0, n, 4),
                i.write(e, t, n, r, 23, 4),
                n + 4
            }
            function D(e, t, n, r, o) {
                return o || B(e, 0, n, 8),
                i.write(e, t, n, r, 52, 8),
                n + 8
            }
            u.prototype.slice = function(e, t) {
                var n, r = this.length;
                if ((e = ~~e) < 0 ? (e += r) < 0 && (e = 0) : e > r && (e = r),
                (t = void 0 === t ? r : ~~t) < 0 ? (t += r) < 0 && (t = 0) : t > r && (t = r),
                t < e && (t = e),
                u.TYPED_ARRAY_SUPPORT)
                    (n = this.subarray(e, t)).__proto__ = u.prototype;
                else {
                    var i = t - e;
                    n = new u(i,void 0);
                    for (var o = 0; o < i; ++o)
                        n[o] = this[o + e]
                }
                return n
            }
            ,
            u.prototype.readUIntLE = function(e, t, n) {
                e |= 0,
                t |= 0,
                n || L(e, t, this.length);
                for (var r = this[e], i = 1, o = 0; ++o < t && (i *= 256); )
                    r += this[e + o] * i;
                return r
            }
            ,
            u.prototype.readUIntBE = function(e, t, n) {
                e |= 0,
                t |= 0,
                n || L(e, t, this.length);
                for (var r = this[e + --t], i = 1; t > 0 && (i *= 256); )
                    r += this[e + --t] * i;
                return r
            }
            ,
            u.prototype.readUInt8 = function(e, t) {
                return t || L(e, 1, this.length),
                this[e]
            }
            ,
            u.prototype.readUInt16LE = function(e, t) {
                return t || L(e, 2, this.length),
                this[e] | this[e + 1] << 8
            }
            ,
            u.prototype.readUInt16BE = function(e, t) {
                return t || L(e, 2, this.length),
                this[e] << 8 | this[e + 1]
            }
            ,
            u.prototype.readUInt32LE = function(e, t) {
                return t || L(e, 4, this.length),
                (this[e] | this[e + 1] << 8 | this[e + 2] << 16) + 16777216 * this[e + 3]
            }
            ,
            u.prototype.readUInt32BE = function(e, t) {
                return t || L(e, 4, this.length),
                16777216 * this[e] + (this[e + 1] << 16 | this[e + 2] << 8 | this[e + 3])
            }
            ,
            u.prototype.readIntLE = function(e, t, n) {
                e |= 0,
                t |= 0,
                n || L(e, t, this.length);
                for (var r = this[e], i = 1, o = 0; ++o < t && (i *= 256); )
                    r += this[e + o] * i;
                return r >= (i *= 128) && (r -= Math.pow(2, 8 * t)),
                r
            }
            ,
            u.prototype.readIntBE = function(e, t, n) {
                e |= 0,
                t |= 0,
                n || L(e, t, this.length);
                for (var r = t, i = 1, o = this[e + --r]; r > 0 && (i *= 256); )
                    o += this[e + --r] * i;
                return o >= (i *= 128) && (o -= Math.pow(2, 8 * t)),
                o
            }
            ,
            u.prototype.readInt8 = function(e, t) {
                return t || L(e, 1, this.length),
                128 & this[e] ? -1 * (255 - this[e] + 1) : this[e]
            }
            ,
            u.prototype.readInt16LE = function(e, t) {
                t || L(e, 2, this.length);
                var n = this[e] | this[e + 1] << 8;
                return 32768 & n ? 4294901760 | n : n
            }
            ,
            u.prototype.readInt16BE = function(e, t) {
                t || L(e, 2, this.length);
                var n = this[e + 1] | this[e] << 8;
                return 32768 & n ? 4294901760 | n : n
            }
            ,
            u.prototype.readInt32LE = function(e, t) {
                return t || L(e, 4, this.length),
                this[e] | this[e + 1] << 8 | this[e + 2] << 16 | this[e + 3] << 24
            }
            ,
            u.prototype.readInt32BE = function(e, t) {
                return t || L(e, 4, this.length),
                this[e] << 24 | this[e + 1] << 16 | this[e + 2] << 8 | this[e + 3]
            }
            ,
            u.prototype.readFloatLE = function(e, t) {
                return t || L(e, 4, this.length),
                i.read(this, e, !0, 23, 4)
            }
            ,
            u.prototype.readFloatBE = function(e, t) {
                return t || L(e, 4, this.length),
                i.read(this, e, !1, 23, 4)
            }
            ,
            u.prototype.readDoubleLE = function(e, t) {
                return t || L(e, 8, this.length),
                i.read(this, e, !0, 52, 8)
            }
            ,
            u.prototype.readDoubleBE = function(e, t) {
                return t || L(e, 8, this.length),
                i.read(this, e, !1, 52, 8)
            }
            ,
            u.prototype.writeUIntLE = function(e, t, n, r) {
                (e = +e,
                t |= 0,
                n |= 0,
                r) || I(this, e, t, n, Math.pow(2, 8 * n) - 1, 0);
                var i = 1
                  , o = 0;
                for (this[t] = 255 & e; ++o < n && (i *= 256); )
                    this[t + o] = e / i & 255;
                return t + n
            }
            ,
            u.prototype.writeUIntBE = function(e, t, n, r) {
                (e = +e,
                t |= 0,
                n |= 0,
                r) || I(this, e, t, n, Math.pow(2, 8 * n) - 1, 0);
                var i = n - 1
                  , o = 1;
                for (this[t + i] = 255 & e; --i >= 0 && (o *= 256); )
                    this[t + i] = e / o & 255;
                return t + n
            }
            ,
            u.prototype.writeUInt8 = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || I(this, e, t, 1, 255, 0),
                u.TYPED_ARRAY_SUPPORT || (e = Math.floor(e)),
                this[t] = 255 & e,
                t + 1
            }
            ,
            u.prototype.writeUInt16LE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || I(this, e, t, 2, 65535, 0),
                u.TYPED_ARRAY_SUPPORT ? (this[t] = 255 & e,
                this[t + 1] = e >>> 8) : R(this, e, t, !0),
                t + 2
            }
            ,
            u.prototype.writeUInt16BE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || I(this, e, t, 2, 65535, 0),
                u.TYPED_ARRAY_SUPPORT ? (this[t] = e >>> 8,
                this[t + 1] = 255 & e) : R(this, e, t, !1),
                t + 2
            }
            ,
            u.prototype.writeUInt32LE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || I(this, e, t, 4, 4294967295, 0),
                u.TYPED_ARRAY_SUPPORT ? (this[t + 3] = e >>> 24,
                this[t + 2] = e >>> 16,
                this[t + 1] = e >>> 8,
                this[t] = 255 & e) : j(this, e, t, !0),
                t + 4
            }
            ,
            u.prototype.writeUInt32BE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || I(this, e, t, 4, 4294967295, 0),
                u.TYPED_ARRAY_SUPPORT ? (this[t] = e >>> 24,
                this[t + 1] = e >>> 16,
                this[t + 2] = e >>> 8,
                this[t + 3] = 255 & e) : j(this, e, t, !1),
                t + 4
            }
            ,
            u.prototype.writeIntLE = function(e, t, n, r) {
                if (e = +e,
                t |= 0,
                !r) {
                    var i = Math.pow(2, 8 * n - 1);
                    I(this, e, t, n, i - 1, -i)
                }
                var o = 0
                  , a = 1
                  , s = 0;
                for (this[t] = 255 & e; ++o < n && (a *= 256); )
                    e < 0 && 0 === s && 0 !== this[t + o - 1] && (s = 1),
                    this[t + o] = (e / a >> 0) - s & 255;
                return t + n
            }
            ,
            u.prototype.writeIntBE = function(e, t, n, r) {
                if (e = +e,
                t |= 0,
                !r) {
                    var i = Math.pow(2, 8 * n - 1);
                    I(this, e, t, n, i - 1, -i)
                }
                var o = n - 1
                  , a = 1
                  , s = 0;
                for (this[t + o] = 255 & e; --o >= 0 && (a *= 256); )
                    e < 0 && 0 === s && 0 !== this[t + o + 1] && (s = 1),
                    this[t + o] = (e / a >> 0) - s & 255;
                return t + n
            }
            ,
            u.prototype.writeInt8 = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || I(this, e, t, 1, 127, -128),
                u.TYPED_ARRAY_SUPPORT || (e = Math.floor(e)),
                e < 0 && (e = 255 + e + 1),
                this[t] = 255 & e,
                t + 1
            }
            ,
            u.prototype.writeInt16LE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || I(this, e, t, 2, 32767, -32768),
                u.TYPED_ARRAY_SUPPORT ? (this[t] = 255 & e,
                this[t + 1] = e >>> 8) : R(this, e, t, !0),
                t + 2
            }
            ,
            u.prototype.writeInt16BE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || I(this, e, t, 2, 32767, -32768),
                u.TYPED_ARRAY_SUPPORT ? (this[t] = e >>> 8,
                this[t + 1] = 255 & e) : R(this, e, t, !1),
                t + 2
            }
            ,
            u.prototype.writeInt32LE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || I(this, e, t, 4, 2147483647, -2147483648),
                u.TYPED_ARRAY_SUPPORT ? (this[t] = 255 & e,
                this[t + 1] = e >>> 8,
                this[t + 2] = e >>> 16,
                this[t + 3] = e >>> 24) : j(this, e, t, !0),
                t + 4
            }
            ,
            u.prototype.writeInt32BE = function(e, t, n) {
                return e = +e,
                t |= 0,
                n || I(this, e, t, 4, 2147483647, -2147483648),
                e < 0 && (e = 4294967295 + e + 1),
                u.TYPED_ARRAY_SUPPORT ? (this[t] = e >>> 24,
                this[t + 1] = e >>> 16,
                this[t + 2] = e >>> 8,
                this[t + 3] = 255 & e) : j(this, e, t, !1),
                t + 4
            }
            ,
            u.prototype.writeFloatLE = function(e, t, n) {
                return N(this, e, t, !0, n)
            }
            ,
            u.prototype.writeFloatBE = function(e, t, n) {
                return N(this, e, t, !1, n)
            }
            ,
            u.prototype.writeDoubleLE = function(e, t, n) {
                return D(this, e, t, !0, n)
            }
            ,
            u.prototype.writeDoubleBE = function(e, t, n) {
                return D(this, e, t, !1, n)
            }
            ,
            u.prototype.copy = function(e, t, n, r) {
                if (n || (n = 0),
                r || 0 === r || (r = this.length),
                t >= e.length && (t = e.length),
                t || (t = 0),
                r > 0 && r < n && (r = n),
                r === n)
                    return 0;
                if (0 === e.length || 0 === this.length)
                    return 0;
                if (t < 0)
                    throw new RangeError("targetStart out of bounds");
                if (n < 0 || n >= this.length)
                    throw new RangeError("sourceStart out of bounds");
                if (r < 0)
                    throw new RangeError("sourceEnd out of bounds");
                r > this.length && (r = this.length),
                e.length - t < r - n && (r = e.length - t + n);
                var i, o = r - n;
                if (this === e && n < t && t < r)
                    for (i = o - 1; i >= 0; --i)
                        e[i + t] = this[i + n];
                else if (o < 1e3 || !u.TYPED_ARRAY_SUPPORT)
                    for (i = 0; i < o; ++i)
                        e[i + t] = this[i + n];
                else
                    Uint8Array.prototype.set.call(e, this.subarray(n, n + o), t);
                return o
            }
            ,
            u.prototype.fill = function(e, t, n, r) {
                if ("string" == typeof e) {
                    if ("string" == typeof t ? (r = t,
                    t = 0,
                    n = this.length) : "string" == typeof n && (r = n,
                    n = this.length),
                    1 === e.length) {
                        var i = e.charCodeAt(0);
                        i < 256 && (e = i)
                    }
                    if (void 0 !== r && "string" != typeof r)
                        throw new TypeError("encoding must be a string");
                    if ("string" == typeof r && !u.isEncoding(r))
                        throw new TypeError("Unknown encoding: " + r)
                } else
                    "number" == typeof e && (e &= 255);
                if (t < 0 || this.length < t || this.length < n)
                    throw new RangeError("Out of range index");
                if (n <= t)
                    return this;
                var o;
                if (t >>>= 0,
                n = void 0 === n ? this.length : n >>> 0,
                e || (e = 0),
                "number" == typeof e)
                    for (o = t; o < n; ++o)
                        this[o] = e;
                else {
                    var a = u.isBuffer(e) ? e : $(new u(e,r).toString())
                      , s = a.length;
                    for (o = 0; o < n - t; ++o)
                        this[o + t] = a[o % s]
                }
                return this
            }
            ;
            var F = /[^+\/0-9A-Za-z-_]/g;
            function U(e) {
                return e < 16 ? "0" + e.toString(16) : e.toString(16)
            }
            function $(e, t) {
                var n;
                t = t || 1 / 0;
                for (var r = e.length, i = null, o = [], a = 0; a < r; ++a) {
                    if ((n = e.charCodeAt(a)) > 55295 && n < 57344) {
                        if (!i) {
                            if (n > 56319) {
                                (t -= 3) > -1 && o.push(239, 191, 189);
                                continue
                            }
                            if (a + 1 === r) {
                                (t -= 3) > -1 && o.push(239, 191, 189);
                                continue
                            }
                            i = n;
                            continue
                        }
                        if (n < 56320) {
                            (t -= 3) > -1 && o.push(239, 191, 189),
                            i = n;
                            continue
                        }
                        n = 65536 + (i - 55296 << 10 | n - 56320)
                    } else
                        i && (t -= 3) > -1 && o.push(239, 191, 189);
                    if (i = null,
                    n < 128) {
                        if ((t -= 1) < 0)
                            break;
                        o.push(n)
                    } else if (n < 2048) {
                        if ((t -= 2) < 0)
                            break;
                        o.push(n >> 6 | 192, 63 & n | 128)
                    } else if (n < 65536) {
                        if ((t -= 3) < 0)
                            break;
                        o.push(n >> 12 | 224, n >> 6 & 63 | 128, 63 & n | 128)
                    } else {
                        if (!(n < 1114112))
                            throw new Error("Invalid code point");
                        if ((t -= 4) < 0)
                            break;
                        o.push(n >> 18 | 240, n >> 12 & 63 | 128, n >> 6 & 63 | 128, 63 & n | 128)
                    }
                }
                return o
            }
            function W(e) {
                return r.toByteArray(function(e) {
                    if ((e = function(e) {
                        return e.trim ? e.trim() : e.replace(/^\s+|\s+$/g, "")
                    }(e).replace(F, "")).length < 2)
                        return "";
                    for (; e.length % 4 != 0; )
                        e += "=";
                    return e
                }(e))
            }
            function z(e, t, n, r) {
                for (var i = 0; i < r && !(i + n >= t.length || i >= e.length); ++i)
                    t[i + n] = e[i];
                return i
            }
        }
        ).call(this, n("c8ba"))
    },
    c8ba: function(e, t) {
        var n;
        n = function() {
            return this
        }();
        try {
            n = n || new Function("return this")()
        } catch (e) {
            "object" == typeof window && (n = window)
        }
        e.exports = n
    },
    "1fb5": function(e, t, n) {
        "use strict";
        t.byteLength = function(e) {
            var t = c(e)
              , n = t[0]
              , r = t[1];
            return 3 * (n + r) / 4 - r
        }
        ,
        t.toByteArray = function(e) {
            var t, n, r = c(e), a = r[0], s = r[1], u = new o(function(e, t, n) {
                return 3 * (t + n) / 4 - n
            }(0, a, s)), l = 0, f = s > 0 ? a - 4 : a;
            for (n = 0; n < f; n += 4)
                t = i[e.charCodeAt(n)] << 18 | i[e.charCodeAt(n + 1)] << 12 | i[e.charCodeAt(n + 2)] << 6 | i[e.charCodeAt(n + 3)],
                u[l++] = t >> 16 & 255,
                u[l++] = t >> 8 & 255,
                u[l++] = 255 & t;
            return 2 === s && (t = i[e.charCodeAt(n)] << 2 | i[e.charCodeAt(n + 1)] >> 4,
            u[l++] = 255 & t),
            1 === s && (t = i[e.charCodeAt(n)] << 10 | i[e.charCodeAt(n + 1)] << 4 | i[e.charCodeAt(n + 2)] >> 2,
            u[l++] = t >> 8 & 255,
            u[l++] = 255 & t),
            u
        }
        ,
        t.fromByteArray = function(e) {
            for (var t, n = e.length, i = n % 3, o = [], a = 16383, s = 0, u = n - i; s < u; s += a)
                o.push(f(e, s, s + a > u ? u : s + a));
            return 1 === i ? (t = e[n - 1],
            o.push(r[t >> 2] + r[t << 4 & 63] + "==")) : 2 === i && (t = (e[n - 2] << 8) + e[n - 1],
            o.push(r[t >> 10] + r[t >> 4 & 63] + r[t << 2 & 63] + "=")),
            o.join("")
        }
        ;
        for (var r = [], i = [], o = "undefined" != typeof Uint8Array ? Uint8Array : Array, a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", s = 0, u = a.length; s < u; ++s)
            r[s] = a[s],
            i[a.charCodeAt(s)] = s;
        function c(e) {
            var t = e.length;
            if (t % 4 > 0)
                throw new Error("Invalid string. Length must be a multiple of 4");
            var n = e.indexOf("=");
            return -1 === n && (n = t),
            [n, n === t ? 0 : 4 - n % 4]
        }
        function l(e) {
            return r[e >> 18 & 63] + r[e >> 12 & 63] + r[e >> 6 & 63] + r[63 & e]
        }
        function f(e, t, n) {
            for (var r, i = [], o = t; o < n; o += 3)
                r = (e[o] << 16 & 16711680) + (e[o + 1] << 8 & 65280) + (255 & e[o + 2]),
                i.push(l(r));
            return i.join("")
        }
        i["-".charCodeAt(0)] = 62,
        i["_".charCodeAt(0)] = 63
    },
    9152: function(e, t) {
        t.read = function(e, t, n, r, i) {
            var o, a, s = 8 * i - r - 1, u = (1 << s) - 1, c = u >> 1, l = -7, f = n ? i - 1 : 0, d = n ? -1 : 1, h = e[t + f];
            for (f += d,
            o = h & (1 << -l) - 1,
            h >>= -l,
            l += s; l > 0; o = 256 * o + e[t + f],
            f += d,
            l -= 8)
                ;
            for (a = o & (1 << -l) - 1,
            o >>= -l,
            l += r; l > 0; a = 256 * a + e[t + f],
            f += d,
            l -= 8)
                ;
            if (0 === o)
                o = 1 - c;
            else {
                if (o === u)
                    return a ? NaN : 1 / 0 * (h ? -1 : 1);
                a += Math.pow(2, r),
                o -= c
            }
            return (h ? -1 : 1) * a * Math.pow(2, o - r)
        }
        ,
        t.write = function(e, t, n, r, i, o) {
            var a, s, u, c = 8 * o - i - 1, l = (1 << c) - 1, f = l >> 1, d = 23 === i ? Math.pow(2, -24) - Math.pow(2, -77) : 0, h = r ? 0 : o - 1, p = r ? 1 : -1, v = t < 0 || 0 === t && 1 / t < 0 ? 1 : 0;
            for (t = Math.abs(t),
            isNaN(t) || t === 1 / 0 ? (s = isNaN(t) ? 1 : 0,
            a = l) : (a = Math.floor(Math.log(t) / Math.LN2),
            t * (u = Math.pow(2, -a)) < 1 && (a--,
            u *= 2),
            (t += a + f >= 1 ? d / u : d * Math.pow(2, 1 - f)) * u >= 2 && (a++,
            u /= 2),
            a + f >= l ? (s = 0,
            a = l) : a + f >= 1 ? (s = (t * u - 1) * Math.pow(2, i),
            a += f) : (s = t * Math.pow(2, f - 1) * Math.pow(2, i),
            a = 0)); i >= 8; e[n + h] = 255 & s,
            h += p,
            s /= 256,
            i -= 8)
                ;
            for (a = a << i | s,
            c += i; c > 0; e[n + h] = 255 & a,
            h += p,
            a /= 256,
            c -= 8)
                ;
            e[n + h - p] |= 128 * v
        }
    },
    e3db: function(e, t) {
        var n = {}.toString;
        e.exports = Array.isArray || function(e) {
            return "[object Array]" == n.call(e)
        }
    },
    6430: function(e, t, n) {
        var r = n("8707").Buffer
          , i = n("d485").Transform
          , o = n("7d72").StringDecoder;
        function a(e) {
            i.call(this),
            this.hashMode = "string" == typeof e,
            this.hashMode ? this[e] = this._finalOrDigest : this.final = this._finalOrDigest,
            this._final && (this.__final = this._final,
            this._final = null),
            this._decoder = null,
            this._encoding = null
        }
        n("3fb5")(a, i),
        a.prototype.update = function(e, t, n) {
            "string" == typeof e && (e = r.from(e, t));
            var i = this._update(e);
            return this.hashMode ? this : (n && (i = this._toString(i, n)),
            i)
        }
        ,
        a.prototype.setAutoPadding = function() {}
        ,
        a.prototype.getAuthTag = function() {
            throw new Error("trying to get auth tag in unsupported state")
        }
        ,
        a.prototype.setAuthTag = function() {
            throw new Error("trying to set auth tag in unsupported state")
        }
        ,
        a.prototype.setAAD = function() {
            throw new Error("trying to set aad in unsupported state")
        }
        ,
        a.prototype._transform = function(e, t, n) {
            var r;
            try {
                this.hashMode ? this._update(e) : this.push(this._update(e))
            } catch (e) {
                r = e
            } finally {
                n(r)
            }
        }
        ,
        a.prototype._flush = function(e) {
            var t;
            try {
                this.push(this.__final())
            } catch (e) {
                t = e
            }
            e(t)
        }
        ,
        a.prototype._finalOrDigest = function(e) {
            var t = this.__final() || r.alloc(0);
            return e && (t = this._toString(t, e, !0)),
            t
        }
        ,
        a.prototype._toString = function(e, t, n) {
            if (this._decoder || (this._decoder = new o(t),
            this._encoding = t),
            this._encoding !== t)
                throw new Error("can't switch encodings");
            var r = this._decoder.write(e);
            return n && (r += this._decoder.end()),
            r
        }
        ,
        e.exports = a
    },
    d485: function(e, t, n) {
        e.exports = i;
        var r = n("faa1").EventEmitter;
        function i() {
            r.call(this)
        }
        n("3fb5")(i, r),
        i.Readable = n("0ac3"),
        i.Writable = n("af7e"),
        i.Duplex = n("7c16"),
        i.Transform = n("89fd"),
        i.PassThrough = n("51a2"),
        i.Stream = i,
        i.prototype.pipe = function(e, t) {
            var n = this;
            function i(t) {
                e.writable && !1 === e.write(t) && n.pause && n.pause()
            }
            function o() {
                n.readable && n.resume && n.resume()
            }
            n.on("data", i),
            e.on("drain", o),
            e._isStdio || t && !1 === t.end || (n.on("end", s),
            n.on("close", u));
            var a = !1;
            function s() {
                a || (a = !0,
                e.end())
            }
            function u() {
                a || (a = !0,
                "function" == typeof e.destroy && e.destroy())
            }
            function c(e) {
                if (l(),
                0 === r.listenerCount(this, "error"))
                    throw e
            }
            function l() {
                n.removeListener("data", i),
                e.removeListener("drain", o),
                n.removeListener("end", s),
                n.removeListener("close", u),
                n.removeListener("error", c),
                e.removeListener("error", c),
                n.removeListener("end", l),
                n.removeListener("close", l),
                e.removeListener("close", l)
            }
            return n.on("error", c),
            e.on("error", c),
            n.on("end", l),
            n.on("close", l),
            e.on("close", l),
            e.emit("pipe", n),
            e
        }
    },
    faa1: function(e, t, n) {
        "use strict";
        var r, i = "object" == typeof Reflect ? Reflect : null, o = i && "function" == typeof i.apply ? i.apply : function(e, t, n) {
            return Function.prototype.apply.call(e, t, n)
        }
        ;
        r = i && "function" == typeof i.ownKeys ? i.ownKeys : Object.getOwnPropertySymbols ? function(e) {
            return Object.getOwnPropertyNames(e).concat(Object.getOwnPropertySymbols(e))
        }
        : function(e) {
            return Object.getOwnPropertyNames(e)
        }
        ;
        var a = Number.isNaN || function(e) {
            return e != e
        }
        ;
        function s() {
            s.init.call(this)
        }
        e.exports = s,
        e.exports.once = function(e, t) {
            return new Promise((function(n, r) {
                function i(n) {
                    e.removeListener(t, o),
                    r(n)
                }
                function o() {
                    "function" == typeof e.removeListener && e.removeListener("error", i),
                    n([].slice.call(arguments))
                }
                y(e, t, o, {
                    once: !0
                }),
                "error" !== t && function(e, t, n) {
                    "function" == typeof e.on && y(e, "error", t, n)
                }(e, i, {
                    once: !0
                })
            }
            ))
        }
        ,
        s.EventEmitter = s,
        s.prototype._events = void 0,
        s.prototype._eventsCount = 0,
        s.prototype._maxListeners = void 0;
        var u = 10;
        function c(e) {
            if ("function" != typeof e)
                throw new TypeError('The "listener" argument must be of type Function. Received type ' + typeof e)
        }
        function l(e) {
            return void 0 === e._maxListeners ? s.defaultMaxListeners : e._maxListeners
        }
        function f(e, t, n, r) {
            var i, o, a;
            if (c(n),
            void 0 === (o = e._events) ? (o = e._events = Object.create(null),
            e._eventsCount = 0) : (void 0 !== o.newListener && (e.emit("newListener", t, n.listener ? n.listener : n),
            o = e._events),
            a = o[t]),
            void 0 === a)
                a = o[t] = n,
                ++e._eventsCount;
            else if ("function" == typeof a ? a = o[t] = r ? [n, a] : [a, n] : r ? a.unshift(n) : a.push(n),
            (i = l(e)) > 0 && a.length > i && !a.warned) {
                a.warned = !0;
                var s = new Error("Possible EventEmitter memory leak detected. " + a.length + " " + String(t) + " listeners added. Use emitter.setMaxListeners() to increase limit");
                s.name = "MaxListenersExceededWarning",
                s.emitter = e,
                s.type = t,
                s.count = a.length,
                console && console.warn
            }
            return e
        }
        function d() {
            if (!this.fired)
                return this.target.removeListener(this.type, this.wrapFn),
                this.fired = !0,
                0 === arguments.length ? this.listener.call(this.target) : this.listener.apply(this.target, arguments)
        }
        function h(e, t, n) {
            var r = {
                fired: !1,
                wrapFn: void 0,
                target: e,
                type: t,
                listener: n
            }
              , i = d.bind(r);
            return i.listener = n,
            r.wrapFn = i,
            i
        }
        function p(e, t, n) {
            var r = e._events;
            if (void 0 === r)
                return [];
            var i = r[t];
            return void 0 === i ? [] : "function" == typeof i ? n ? [i.listener || i] : [i] : n ? function(e) {
                for (var t = new Array(e.length), n = 0; n < t.length; ++n)
                    t[n] = e[n].listener || e[n];
                return t
            }(i) : g(i, i.length)
        }
        function v(e) {
            var t = this._events;
            if (void 0 !== t) {
                var n = t[e];
                if ("function" == typeof n)
                    return 1;
                if (void 0 !== n)
                    return n.length
            }
            return 0
        }
        function g(e, t) {
            for (var n = new Array(t), r = 0; r < t; ++r)
                n[r] = e[r];
            return n
        }
        function y(e, t, n, r) {
            if ("function" == typeof e.on)
                r.once ? e.once(t, n) : e.on(t, n);
            else {
                if ("function" != typeof e.addEventListener)
                    throw new TypeError('The "emitter" argument must be of type EventEmitter. Received type ' + typeof e);
                e.addEventListener(t, (function i(o) {
                    r.once && e.removeEventListener(t, i),
                    n(o)
                }
                ))
            }
        }
        Object.defineProperty(s, "defaultMaxListeners", {
            enumerable: !0,
            get: function() {
                return u
            },
            set: function(e) {
                if ("number" != typeof e || e < 0 || a(e))
                    throw new RangeError('The value of "defaultMaxListeners" is out of range. It must be a non-negative number. Received ' + e + ".");
                u = e
            }
        }),
        s.init = function() {
            void 0 !== this._events && this._events !== Object.getPrototypeOf(this)._events || (this._events = Object.create(null),
            this._eventsCount = 0),
            this._maxListeners = this._maxListeners || void 0
        }
        ,
        s.prototype.setMaxListeners = function(e) {
            if ("number" != typeof e || e < 0 || a(e))
                throw new RangeError('The value of "n" is out of range. It must be a non-negative number. Received ' + e + ".");
            return this._maxListeners = e,
            this
        }
        ,
        s.prototype.getMaxListeners = function() {
            return l(this)
        }
        ,
        s.prototype.emit = function(e) {
            for (var t = [], n = 1; n < arguments.length; n++)
                t.push(arguments[n]);
            var r = "error" === e
              , i = this._events;
            if (void 0 !== i)
                r = r && void 0 === i.error;
            else if (!r)
                return !1;
            if (r) {
                var a;
                if (t.length > 0 && (a = t[0]),
                a instanceof Error)
                    throw a;
                var s = new Error("Unhandled error." + (a ? " (" + a.message + ")" : ""));
                throw s.context = a,
                s
            }
            var u = i[e];
            if (void 0 === u)
                return !1;
            if ("function" == typeof u)
                o(u, this, t);
            else {
                var c = u.length
                  , l = g(u, c);
                for (n = 0; n < c; ++n)
                    o(l[n], this, t)
            }
            return !0
        }
        ,
        s.prototype.addListener = function(e, t) {
            return f(this, e, t, !1)
        }
        ,
        s.prototype.on = s.prototype.addListener,
        s.prototype.prependListener = function(e, t) {
            return f(this, e, t, !0)
        }
        ,
        s.prototype.once = function(e, t) {
            return c(t),
            this.on(e, h(this, e, t)),
            this
        }
        ,
        s.prototype.prependOnceListener = function(e, t) {
            return c(t),
            this.prependListener(e, h(this, e, t)),
            this
        }
        ,
        s.prototype.removeListener = function(e, t) {
            var n, r, i, o, a;
            if (c(t),
            void 0 === (r = this._events))
                return this;
            if (void 0 === (n = r[e]))
                return this;
            if (n === t || n.listener === t)
                0 == --this._eventsCount ? this._events = Object.create(null) : (delete r[e],
                r.removeListener && this.emit("removeListener", e, n.listener || t));
            else if ("function" != typeof n) {
                for (i = -1,
                o = n.length - 1; o >= 0; o--)
                    if (n[o] === t || n[o].listener === t) {
                        a = n[o].listener,
                        i = o;
                        break
                    }
                if (i < 0)
                    return this;
                0 === i ? n.shift() : function(e, t) {
                    for (; t + 1 < e.length; t++)
                        e[t] = e[t + 1];
                    e.pop()
                }(n, i),
                1 === n.length && (r[e] = n[0]),
                void 0 !== r.removeListener && this.emit("removeListener", e, a || t)
            }
            return this
        }
        ,
        s.prototype.off = s.prototype.removeListener,
        s.prototype.removeAllListeners = function(e) {
            var t, n, r;
            if (void 0 === (n = this._events))
                return this;
            if (void 0 === n.removeListener)
                return 0 === arguments.length ? (this._events = Object.create(null),
                this._eventsCount = 0) : void 0 !== n[e] && (0 == --this._eventsCount ? this._events = Object.create(null) : delete n[e]),
                this;
            if (0 === arguments.length) {
                var i, o = Object.keys(n);
                for (r = 0; r < o.length; ++r)
                    "removeListener" !== (i = o[r]) && this.removeAllListeners(i);
                return this.removeAllListeners("removeListener"),
                this._events = Object.create(null),
                this._eventsCount = 0,
                this
            }
            if ("function" == typeof (t = n[e]))
                this.removeListener(e, t);
            else if (void 0 !== t)
                for (r = t.length - 1; r >= 0; r--)
                    this.removeListener(e, t[r]);
            return this
        }
        ,
        s.prototype.listeners = function(e) {
            return p(this, e, !0)
        }
        ,
        s.prototype.rawListeners = function(e) {
            return p(this, e, !1)
        }
        ,
        s.listenerCount = function(e, t) {
            return "function" == typeof e.listenerCount ? e.listenerCount(t) : v.call(e, t)
        }
        ,
        s.prototype.listenerCount = v,
        s.prototype.eventNames = function() {
            return this._eventsCount > 0 ? r(this._events) : []
        }
    },
    "0ac3": function(e, t, n) {
        (t = e.exports = n("6f2e")).Stream = t,
        t.Readable = t,
        t.Writable = n("6ffa"),
        t.Duplex = n("d6dd"),
        t.Transform = n("dcd0"),
        t.PassThrough = n("aa69")
    },
    "6f2e": function(e, t, n) {
        "use strict";
        (function(t, r) {
            var i = n("966d");
            e.exports = w;
            var o, a = n("e3db");
            w.ReadableState = b,
            n("faa1").EventEmitter;
            var s = function(e, t) {
                return e.listeners(t).length
            }
              , u = n("2aaa")
              , c = n("f60b").Buffer
              , l = t.Uint8Array || function() {}
            ;
            var f = Object.create(n("3a7c"));
            f.inherits = n("3fb5");
            var d = n(1)
              , h = void 0;
            h = d && d.debuglog ? d.debuglog("stream") : function() {}
            ;
            var p, v = n("9b54"), g = n("c4c0");
            f.inherits(w, u);
            var y = ["error", "close", "destroy", "pause", "resume"];
            function m(e, t, n) {
                if ("function" == typeof e.prependListener)
                    return e.prependListener(t, n);
                e._events && e._events[t] ? a(e._events[t]) ? e._events[t].unshift(n) : e._events[t] = [n, e._events[t]] : e.on(t, n)
            }
            function b(e, t) {
                e = e || {};
                var r = t instanceof (o = o || n("d6dd"));
                this.objectMode = !!e.objectMode,
                r && (this.objectMode = this.objectMode || !!e.readableObjectMode);
                var i = e.highWaterMark
                  , a = e.readableHighWaterMark
                  , s = this.objectMode ? 16 : 16384;
                this.highWaterMark = i || 0 === i ? i : r && (a || 0 === a) ? a : s,
                this.highWaterMark = Math.floor(this.highWaterMark),
                this.buffer = new v,
                this.length = 0,
                this.pipes = null,
                this.pipesCount = 0,
                this.flowing = null,
                this.ended = !1,
                this.endEmitted = !1,
                this.reading = !1,
                this.sync = !0,
                this.needReadable = !1,
                this.emittedReadable = !1,
                this.readableListening = !1,
                this.resumeScheduled = !1,
                this.destroyed = !1,
                this.defaultEncoding = e.defaultEncoding || "utf8",
                this.awaitDrain = 0,
                this.readingMore = !1,
                this.decoder = null,
                this.encoding = null,
                e.encoding && (p || (p = n("7d72").StringDecoder),
                this.decoder = new p(e.encoding),
                this.encoding = e.encoding)
            }
            function w(e) {
                if (o = o || n("d6dd"),
                !(this instanceof w))
                    return new w(e);
                this._readableState = new b(e,this),
                this.readable = !0,
                e && ("function" == typeof e.read && (this._read = e.read),
                "function" == typeof e.destroy && (this._destroy = e.destroy)),
                u.call(this)
            }
            function _(e, t, n, r, i) {
                var o, a = e._readableState;
                return null === t ? (a.reading = !1,
                function(e, t) {
                    if (!t.ended) {
                        if (t.decoder) {
                            var n = t.decoder.end();
                            n && n.length && (t.buffer.push(n),
                            t.length += t.objectMode ? 1 : n.length)
                        }
                        t.ended = !0,
                        T(e)
                    }
                }(e, a)) : (i || (o = function(e, t) {
                    var n;
                    return function(e) {
                        return c.isBuffer(e) || e instanceof l
                    }(t) || "string" == typeof t || void 0 === t || e.objectMode || (n = new TypeError("Invalid non-string/buffer chunk")),
                    n
                }(a, t)),
                o ? e.emit("error", o) : a.objectMode || t && t.length > 0 ? ("string" == typeof t || a.objectMode || Object.getPrototypeOf(t) === c.prototype || (t = function(e) {
                    return c.from(e)
                }(t)),
                r ? a.endEmitted ? e.emit("error", new Error("stream.unshift() after end event")) : S(e, a, t, !0) : a.ended ? e.emit("error", new Error("stream.push() after EOF")) : (a.reading = !1,
                a.decoder && !n ? (t = a.decoder.write(t),
                a.objectMode || 0 !== t.length ? S(e, a, t, !1) : k(e, a)) : S(e, a, t, !1))) : r || (a.reading = !1)),
                function(e) {
                    return !e.ended && (e.needReadable || e.length < e.highWaterMark || 0 === e.length)
                }(a)
            }
            function S(e, t, n, r) {
                t.flowing && 0 === t.length && !t.sync ? (e.emit("data", n),
                e.read(0)) : (t.length += t.objectMode ? 1 : n.length,
                r ? t.buffer.unshift(n) : t.buffer.push(n),
                t.needReadable && T(e)),
                k(e, t)
            }
            Object.defineProperty(w.prototype, "destroyed", {
                get: function() {
                    return void 0 !== this._readableState && this._readableState.destroyed
                },
                set: function(e) {
                    this._readableState && (this._readableState.destroyed = e)
                }
            }),
            w.prototype.destroy = g.destroy,
            w.prototype._undestroy = g.undestroy,
            w.prototype._destroy = function(e, t) {
                this.push(null),
                t(e)
            }
            ,
            w.prototype.push = function(e, t) {
                var n, r = this._readableState;
                return r.objectMode ? n = !0 : "string" == typeof e && ((t = t || r.defaultEncoding) !== r.encoding && (e = c.from(e, t),
                t = ""),
                n = !0),
                _(this, e, t, !1, n)
            }
            ,
            w.prototype.unshift = function(e) {
                return _(this, e, null, !0, !1)
            }
            ,
            w.prototype.isPaused = function() {
                return !1 === this._readableState.flowing
            }
            ,
            w.prototype.setEncoding = function(e) {
                return p || (p = n("7d72").StringDecoder),
                this._readableState.decoder = new p(e),
                this._readableState.encoding = e,
                this
            }
            ;
            var E = 8388608;
            function x(e, t) {
                return e <= 0 || 0 === t.length && t.ended ? 0 : t.objectMode ? 1 : e != e ? t.flowing && t.length ? t.buffer.head.data.length : t.length : (e > t.highWaterMark && (t.highWaterMark = function(e) {
                    return e >= E ? e = E : (e--,
                    e |= e >>> 1,
                    e |= e >>> 2,
                    e |= e >>> 4,
                    e |= e >>> 8,
                    e |= e >>> 16,
                    e++),
                    e
                }(e)),
                e <= t.length ? e : t.ended ? t.length : (t.needReadable = !0,
                0))
            }
            function T(e) {
                var t = e._readableState;
                t.needReadable = !1,
                t.emittedReadable || (h("emitReadable", t.flowing),
                t.emittedReadable = !0,
                t.sync ? i.nextTick(O, e) : O(e))
            }
            function O(e) {
                h("emit readable"),
                e.emit("readable"),
                M(e)
            }
            function k(e, t) {
                t.readingMore || (t.readingMore = !0,
                i.nextTick(A, e, t))
            }
            function A(e, t) {
                for (var n = t.length; !t.reading && !t.flowing && !t.ended && t.length < t.highWaterMark && (h("maybeReadMore read 0"),
                e.read(0),
                n !== t.length); )
                    n = t.length;
                t.readingMore = !1
            }
            function C(e) {
                h("readable nexttick read 0"),
                e.read(0)
            }
            function P(e, t) {
                t.reading || (h("resume read 0"),
                e.read(0)),
                t.resumeScheduled = !1,
                t.awaitDrain = 0,
                e.emit("resume"),
                M(e),
                t.flowing && !t.reading && e.read(0)
            }
            function M(e) {
                var t = e._readableState;
                for (h("flow", t.flowing); t.flowing && null !== e.read(); )
                    ;
            }
            function L(e, t) {
                return 0 === t.length ? null : (t.objectMode ? n = t.buffer.shift() : !e || e >= t.length ? (n = t.decoder ? t.buffer.join("") : 1 === t.buffer.length ? t.buffer.head.data : t.buffer.concat(t.length),
                t.buffer.clear()) : n = function(e, t, n) {
                    var r;
                    return e < t.head.data.length ? (r = t.head.data.slice(0, e),
                    t.head.data = t.head.data.slice(e)) : r = e === t.head.data.length ? t.shift() : n ? function(e, t) {
                        var n = t.head
                          , r = 1
                          , i = n.data;
                        e -= i.length;
                        for (; n = n.next; ) {
                            var o = n.data
                              , a = e > o.length ? o.length : e;
                            if (a === o.length ? i += o : i += o.slice(0, e),
                            0 === (e -= a)) {
                                a === o.length ? (++r,
                                n.next ? t.head = n.next : t.head = t.tail = null) : (t.head = n,
                                n.data = o.slice(a));
                                break
                            }
                            ++r
                        }
                        return t.length -= r,
                        i
                    }(e, t) : function(e, t) {
                        var n = c.allocUnsafe(e)
                          , r = t.head
                          , i = 1;
                        r.data.copy(n),
                        e -= r.data.length;
                        for (; r = r.next; ) {
                            var o = r.data
                              , a = e > o.length ? o.length : e;
                            if (o.copy(n, n.length - e, 0, a),
                            0 === (e -= a)) {
                                a === o.length ? (++i,
                                r.next ? t.head = r.next : t.head = t.tail = null) : (t.head = r,
                                r.data = o.slice(a));
                                break
                            }
                            ++i
                        }
                        return t.length -= i,
                        n
                    }(e, t),
                    r
                }(e, t.buffer, t.decoder),
                n);
                var n
            }
            function I(e) {
                var t = e._readableState;
                if (t.length > 0)
                    throw new Error('"endReadable()" called on non-empty stream');
                t.endEmitted || (t.ended = !0,
                i.nextTick(R, t, e))
            }
            function R(e, t) {
                e.endEmitted || 0 !== e.length || (e.endEmitted = !0,
                t.readable = !1,
                t.emit("end"))
            }
            function j(e, t) {
                for (var n = 0, r = e.length; n < r; n++)
                    if (e[n] === t)
                        return n;
                return -1
            }
            w.prototype.read = function(e) {
                h("read", e),
                e = parseInt(e, 10);
                var t = this._readableState
                  , n = e;
                if (0 !== e && (t.emittedReadable = !1),
                0 === e && t.needReadable && (t.length >= t.highWaterMark || t.ended))
                    return h("read: emitReadable", t.length, t.ended),
                    0 === t.length && t.ended ? I(this) : T(this),
                    null;
                if (0 === (e = x(e, t)) && t.ended)
                    return 0 === t.length && I(this),
                    null;
                var r, i = t.needReadable;
                return h("need readable", i),
                (0 === t.length || t.length - e < t.highWaterMark) && h("length less than watermark", i = !0),
                t.ended || t.reading ? h("reading or ended", i = !1) : i && (h("do read"),
                t.reading = !0,
                t.sync = !0,
                0 === t.length && (t.needReadable = !0),
                this._read(t.highWaterMark),
                t.sync = !1,
                t.reading || (e = x(n, t))),
                null === (r = e > 0 ? L(e, t) : null) ? (t.needReadable = !0,
                e = 0) : t.length -= e,
                0 === t.length && (t.ended || (t.needReadable = !0),
                n !== e && t.ended && I(this)),
                null !== r && this.emit("data", r),
                r
            }
            ,
            w.prototype._read = function(e) {
                this.emit("error", new Error("_read() is not implemented"))
            }
            ,
            w.prototype.pipe = function(e, t) {
                var n = this
                  , o = this._readableState;
                switch (o.pipesCount) {
                case 0:
                    o.pipes = e;
                    break;
                case 1:
                    o.pipes = [o.pipes, e];
                    break;
                default:
                    o.pipes.push(e)
                }
                o.pipesCount += 1,
                h("pipe count=%d opts=%j", o.pipesCount, t);
                var a = (!t || !1 !== t.end) && e !== r.stdout && e !== r.stderr ? c : w;
                function u(e, t) {
                    h("onunpipe"),
                    e === n && t && !1 === t.hasUnpiped && (t.hasUnpiped = !0,
                    d())
                }
                function c() {
                    h("onend"),
                    e.end()
                }
                o.endEmitted ? i.nextTick(a) : n.once("end", a),
                e.on("unpipe", u);
                var l = function(e) {
                    return function() {
                        var t = e._readableState;
                        h("pipeOnDrain", t.awaitDrain),
                        t.awaitDrain && t.awaitDrain--,
                        0 === t.awaitDrain && s(e, "data") && (t.flowing = !0,
                        M(e))
                    }
                }(n);
                e.on("drain", l);
                var f = !1;
                function d() {
                    h("cleanup"),
                    e.removeListener("close", y),
                    e.removeListener("finish", b),
                    e.removeListener("drain", l),
                    e.removeListener("error", g),
                    e.removeListener("unpipe", u),
                    n.removeListener("end", c),
                    n.removeListener("end", w),
                    n.removeListener("data", v),
                    f = !0,
                    !o.awaitDrain || e._writableState && !e._writableState.needDrain || l()
                }
                var p = !1;
                function v(t) {
                    h("ondata"),
                    p = !1,
                    !1 !== e.write(t) || p || ((1 === o.pipesCount && o.pipes === e || o.pipesCount > 1 && -1 !== j(o.pipes, e)) && !f && (h("false write response, pause", n._readableState.awaitDrain),
                    n._readableState.awaitDrain++,
                    p = !0),
                    n.pause())
                }
                function g(t) {
                    h("onerror", t),
                    w(),
                    e.removeListener("error", g),
                    0 === s(e, "error") && e.emit("error", t)
                }
                function y() {
                    e.removeListener("finish", b),
                    w()
                }
                function b() {
                    h("onfinish"),
                    e.removeListener("close", y),
                    w()
                }
                function w() {
                    h("unpipe"),
                    n.unpipe(e)
                }
                return n.on("data", v),
                m(e, "error", g),
                e.once("close", y),
                e.once("finish", b),
                e.emit("pipe", n),
                o.flowing || (h("pipe resume"),
                n.resume()),
                e
            }
            ,
            w.prototype.unpipe = function(e) {
                var t = this._readableState
                  , n = {
                    hasUnpiped: !1
                };
                if (0 === t.pipesCount)
                    return this;
                if (1 === t.pipesCount)
                    return e && e !== t.pipes || (e || (e = t.pipes),
                    t.pipes = null,
                    t.pipesCount = 0,
                    t.flowing = !1,
                    e && e.emit("unpipe", this, n)),
                    this;
                if (!e) {
                    var r = t.pipes
                      , i = t.pipesCount;
                    t.pipes = null,
                    t.pipesCount = 0,
                    t.flowing = !1;
                    for (var o = 0; o < i; o++)
                        r[o].emit("unpipe", this, n);
                    return this
                }
                var a = j(t.pipes, e);
                return -1 === a || (t.pipes.splice(a, 1),
                t.pipesCount -= 1,
                1 === t.pipesCount && (t.pipes = t.pipes[0]),
                e.emit("unpipe", this, n)),
                this
            }
            ,
            w.prototype.on = function(e, t) {
                var n = u.prototype.on.call(this, e, t);
                if ("data" === e)
                    !1 !== this._readableState.flowing && this.resume();
                else if ("readable" === e) {
                    var r = this._readableState;
                    r.endEmitted || r.readableListening || (r.readableListening = r.needReadable = !0,
                    r.emittedReadable = !1,
                    r.reading ? r.length && T(this) : i.nextTick(C, this))
                }
                return n
            }
            ,
            w.prototype.addListener = w.prototype.on,
            w.prototype.resume = function() {
                var e = this._readableState;
                return e.flowing || (h("resume"),
                e.flowing = !0,
                function(e, t) {
                    t.resumeScheduled || (t.resumeScheduled = !0,
                    i.nextTick(P, e, t))
                }(this, e)),
                this
            }
            ,
            w.prototype.pause = function() {
                return h("call pause flowing=%j", this._readableState.flowing),
                !1 !== this._readableState.flowing && (h("pause"),
                this._readableState.flowing = !1,
                this.emit("pause")),
                this
            }
            ,
            w.prototype.wrap = function(e) {
                var t = this
                  , n = this._readableState
                  , r = !1;
                for (var i in e.on("end", (function() {
                    if (h("wrapped end"),
                    n.decoder && !n.ended) {
                        var e = n.decoder.end();
                        e && e.length && t.push(e)
                    }
                    t.push(null)
                }
                )),
                e.on("data", (function(i) {
                    (h("wrapped data"),
                    n.decoder && (i = n.decoder.write(i)),
                    n.objectMode && null == i || !(n.objectMode || i && i.length)) || (t.push(i) || (r = !0,
                    e.pause()))
                }
                )),
                e)
                    void 0 === this[i] && "function" == typeof e[i] && (this[i] = function(t) {
                        return function() {
                            return e[t].apply(e, arguments)
                        }
                    }(i));
                for (var o = 0; o < y.length; o++)
                    e.on(y[o], this.emit.bind(this, y[o]));
                return this._read = function(t) {
                    h("wrapped _read", t),
                    r && (r = !1,
                    e.resume())
                }
                ,
                this
            }
            ,
            Object.defineProperty(w.prototype, "readableHighWaterMark", {
                enumerable: !1,
                get: function() {
                    return this._readableState.highWaterMark
                }
            }),
            w._fromList = L
        }
        ).call(this, n("c8ba"), n("f28c"))
    },
    f28c: function(e, t) {
        var n, r, i = e.exports = {};
        function o() {
            throw new Error("setTimeout has not been defined")
        }
        function a() {
            throw new Error("clearTimeout has not been defined")
        }
        function s(e) {
            if (n === setTimeout)
                return setTimeout(e, 0);
            if ((n === o || !n) && setTimeout)
                return n = setTimeout,
                setTimeout(e, 0);
            try {
                return n(e, 0)
            } catch (t) {
                try {
                    return n.call(null, e, 0)
                } catch (t) {
                    return n.call(this, e, 0)
                }
            }
        }
        !function() {
            try {
                n = "function" == typeof setTimeout ? setTimeout : o
            } catch (e) {
                n = o
            }
            try {
                r = "function" == typeof clearTimeout ? clearTimeout : a
            } catch (e) {
                r = a
            }
        }();
        var u, c = [], l = !1, f = -1;
        function d() {
            l && u && (l = !1,
            u.length ? c = u.concat(c) : f = -1,
            c.length && h())
        }
        function h() {
            if (!l) {
                var e = s(d);
                l = !0;
                for (var t = c.length; t; ) {
                    for (u = c,
                    c = []; ++f < t; )
                        u && u[f].run();
                    f = -1,
                    t = c.length
                }
                u = null,
                l = !1,
                function(e) {
                    if (r === clearTimeout)
                        return clearTimeout(e);
                    if ((r === a || !r) && clearTimeout)
                        return r = clearTimeout,
                        clearTimeout(e);
                    try {
                        r(e)
                    } catch (t) {
                        try {
                            return r.call(null, e)
                        } catch (t) {
                            return r.call(this, e)
                        }
                    }
                }(e)
            }
        }
        function p(e, t) {
            this.fun = e,
            this.array = t
        }
        function v() {}
        i.nextTick = function(e) {
            var t = new Array(arguments.length - 1);
            if (arguments.length > 1)
                for (var n = 1; n < arguments.length; n++)
                    t[n - 1] = arguments[n];
            c.push(new p(e,t)),
            1 !== c.length || l || s(h)
        }
        ,
        p.prototype.run = function() {
            this.fun.apply(null, this.array)
        }
        ,
        i.title = "browser",
        i.browser = !0,
        i.env = {},
        i.argv = [],
        i.version = "",
        i.versions = {},
        i.on = v,
        i.addListener = v,
        i.once = v,
        i.off = v,
        i.removeListener = v,
        i.removeAllListeners = v,
        i.emit = v,
        i.prependListener = v,
        i.prependOnceListener = v,
        i.listeners = function(e) {
            return []
        }
        ,
        i.binding = function(e) {
            throw new Error("process.binding is not supported")
        }
        ,
        i.cwd = function() {
            return "/"
        }
        ,
        i.chdir = function(e) {
            throw new Error("process.chdir is not supported")
        }
        ,
        i.umask = function() {
            return 0
        }
    },
    "966d": function(e, t, n) {
        "use strict";
        (function(t) {
            void 0 === t || !t.version || 0 === t.version.indexOf("v0.") || 0 === t.version.indexOf("v1.") && 0 !== t.version.indexOf("v1.8.") ? e.exports = {
                nextTick: function(e, n, r, i) {
                    if ("function" != typeof e)
                        throw new TypeError('"callback" argument must be a function');
                    var o, a, s = arguments.length;
                    switch (s) {
                    case 0:
                    case 1:
                        return t.nextTick(e);
                    case 2:
                        return t.nextTick((function() {
                            e.call(null, n)
                        }
                        ));
                    case 3:
                        return t.nextTick((function() {
                            e.call(null, n, r)
                        }
                        ));
                    case 4:
                        return t.nextTick((function() {
                            e.call(null, n, r, i)
                        }
                        ));
                    default:
                        for (o = new Array(s - 1),
                        a = 0; a < o.length; )
                            o[a++] = arguments[a];
                        return t.nextTick((function() {
                            e.apply(null, o)
                        }
                        ))
                    }
                }
            } : e.exports = t
        }
        ).call(this, n("f28c"))
    },
    "2aaa": function(e, t, n) {
        e.exports = n("faa1").EventEmitter
    },
    f60b: function(e, t, n) {
        var r = n("b639")
          , i = r.Buffer;
        function o(e, t) {
            for (var n in e)
                t[n] = e[n]
        }
        function a(e, t, n) {
            return i(e, t, n)
        }
        i.from && i.alloc && i.allocUnsafe && i.allocUnsafeSlow ? e.exports = r : (o(r, t),
        t.Buffer = a),
        o(i, a),
        a.from = function(e, t, n) {
            if ("number" == typeof e)
                throw new TypeError("Argument must not be a number");
            return i(e, t, n)
        }
        ,
        a.alloc = function(e, t, n) {
            if ("number" != typeof e)
                throw new TypeError("Argument must be a number");
            var r = i(e);
            return void 0 !== t ? "string" == typeof n ? r.fill(t, n) : r.fill(t) : r.fill(0),
            r
        }
        ,
        a.allocUnsafe = function(e) {
            if ("number" != typeof e)
                throw new TypeError("Argument must be a number");
            return i(e)
        }
        ,
        a.allocUnsafeSlow = function(e) {
            if ("number" != typeof e)
                throw new TypeError("Argument must be a number");
            return r.SlowBuffer(e)
        }
    },
    "3a7c": function(e, t, n) {
        function r(e) {
            return Object.prototype.toString.call(e)
        }
        t.isArray = function(e) {
            return Array.isArray ? Array.isArray(e) : "[object Array]" === r(e)
        }
        ,
        t.isBoolean = function(e) {
            return "boolean" == typeof e
        }
        ,
        t.isNull = function(e) {
            return null === e
        }
        ,
        t.isNullOrUndefined = function(e) {
            return null == e
        }
        ,
        t.isNumber = function(e) {
            return "number" == typeof e
        }
        ,
        t.isString = function(e) {
            return "string" == typeof e
        }
        ,
        t.isSymbol = function(e) {
            return "symbol" == typeof e
        }
        ,
        t.isUndefined = function(e) {
            return void 0 === e
        }
        ,
        t.isRegExp = function(e) {
            return "[object RegExp]" === r(e)
        }
        ,
        t.isObject = function(e) {
            return "object" == typeof e && null !== e
        }
        ,
        t.isDate = function(e) {
            return "[object Date]" === r(e)
        }
        ,
        t.isError = function(e) {
            return "[object Error]" === r(e) || e instanceof Error
        }
        ,
        t.isFunction = function(e) {
            return "function" == typeof e
        }
        ,
        t.isPrimitive = function(e) {
            return null === e || "boolean" == typeof e || "number" == typeof e || "string" == typeof e || "symbol" == typeof e || void 0 === e
        }
        ,
        t.isBuffer = n("b639").Buffer.isBuffer
    },
    1: function(e, t) {},
    "9b54": function(e, t, n) {
        "use strict";
        var r = n("f60b").Buffer
          , i = n(2);
        function o(e, t, n) {
            e.copy(t, n)
        }
        e.exports = function() {
            function e() {
                (function(e, t) {
                    if (!(e instanceof t))
                        throw new TypeError("Cannot call a class as a function")
                }
                )(this, e),
                this.head = null,
                this.tail = null,
                this.length = 0
            }
            return e.prototype.push = function(e) {
                var t = {
                    data: e,
                    next: null
                };
                this.length > 0 ? this.tail.next = t : this.head = t,
                this.tail = t,
                ++this.length
            }
            ,
            e.prototype.unshift = function(e) {
                var t = {
                    data: e,
                    next: this.head
                };
                0 === this.length && (this.tail = t),
                this.head = t,
                ++this.length
            }
            ,
            e.prototype.shift = function() {
                if (0 !== this.length) {
                    var e = this.head.data;
                    return 1 === this.length ? this.head = this.tail = null : this.head = this.head.next,
                    --this.length,
                    e
                }
            }
            ,
            e.prototype.clear = function() {
                this.head = this.tail = null,
                this.length = 0
            }
            ,
            e.prototype.join = function(e) {
                if (0 === this.length)
                    return "";
                for (var t = this.head, n = "" + t.data; t = t.next; )
                    n += e + t.data;
                return n
            }
            ,
            e.prototype.concat = function(e) {
                if (0 === this.length)
                    return r.alloc(0);
                if (1 === this.length)
                    return this.head.data;
                for (var t = r.allocUnsafe(e >>> 0), n = this.head, i = 0; n; )
                    o(n.data, t, i),
                    i += n.data.length,
                    n = n.next;
                return t
            }
            ,
            e
        }(),
        i && i.inspect && i.inspect.custom && (e.exports.prototype[i.inspect.custom] = function() {
            var e = i.inspect({
                length: this.length
            });
            return this.constructor.name + " " + e
        }
        )
    },
    2: function(e, t) {},
    c4c0: function(e, t, n) {
        "use strict";
        var r = n("966d");
        function i(e, t) {
            e.emit("error", t)
        }
        e.exports = {
            destroy: function(e, t) {
                var n = this
                  , o = this._readableState && this._readableState.destroyed
                  , a = this._writableState && this._writableState.destroyed;
                return o || a ? (t ? t(e) : !e || this._writableState && this._writableState.errorEmitted || r.nextTick(i, this, e),
                this) : (this._readableState && (this._readableState.destroyed = !0),
                this._writableState && (this._writableState.destroyed = !0),
                this._destroy(e || null, (function(e) {
                    !t && e ? (r.nextTick(i, n, e),
                    n._writableState && (n._writableState.errorEmitted = !0)) : t && t(e)
                }
                )),
                this)
            },
            undestroy: function() {
                this._readableState && (this._readableState.destroyed = !1,
                this._readableState.reading = !1,
                this._readableState.ended = !1,
                this._readableState.endEmitted = !1),
                this._writableState && (this._writableState.destroyed = !1,
                this._writableState.ended = !1,
                this._writableState.ending = !1,
                this._writableState.finished = !1,
                this._writableState.errorEmitted = !1)
            }
        }
    },
    "6ffa": function(e, t, n) {
        "use strict";
        (function(t, r) {
            var i = n("966d");
            function o(e) {
                var t = this;
                this.next = null,
                this.entry = null,
                this.finish = function() {
                    !function(e, t, n) {
                        var r = e.entry;
                        e.entry = null;
                        for (; r; ) {
                            var i = r.callback;
                            t.pendingcb--,
                            i(n),
                            r = r.next
                        }
                        t.corkedRequestsFree ? t.corkedRequestsFree.next = e : t.corkedRequestsFree = e
                    }(t, e)
                }
            }
            e.exports = y;
            var a, s = !t.browser && ["v0.10", "v0.9."].indexOf(t.version.slice(0, 5)) > -1 ? setImmediate : i.nextTick;
            y.WritableState = g;
            var u = Object.create(n("3a7c"));
            u.inherits = n("3fb5");
            var c = {
                deprecate: n("b7d1")
            }
              , l = n("2aaa")
              , f = n("f60b").Buffer
              , d = r.Uint8Array || function() {}
            ;
            var h, p = n("c4c0");
            function v() {}
            function g(e, t) {
                a = a || n("d6dd"),
                e = e || {};
                var r = t instanceof a;
                this.objectMode = !!e.objectMode,
                r && (this.objectMode = this.objectMode || !!e.writableObjectMode);
                var i = e.highWaterMark
                  , s = e.writableHighWaterMark
                  , u = this.objectMode ? 16 : 16384;
                this.highWaterMark = i || 0 === i ? i : r && (s || 0 === s) ? s : u,
                this.highWaterMark = Math.floor(this.highWaterMark),
                this.finalCalled = !1,
                this.needDrain = !1,
                this.ending = !1,
                this.ended = !1,
                this.finished = !1,
                this.destroyed = !1;
                var c = !1 === e.decodeStrings;
                this.decodeStrings = !c,
                this.defaultEncoding = e.defaultEncoding || "utf8",
                this.length = 0,
                this.writing = !1,
                this.corked = 0,
                this.sync = !0,
                this.bufferProcessing = !1,
                this.onwrite = function(e) {
                    E(t, e)
                }
                ,
                this.writecb = null,
                this.writelen = 0,
                this.bufferedRequest = null,
                this.lastBufferedRequest = null,
                this.pendingcb = 0,
                this.prefinished = !1,
                this.errorEmitted = !1,
                this.bufferedRequestCount = 0,
                this.corkedRequestsFree = new o(this)
            }
            function y(e) {
                if (a = a || n("d6dd"),
                !(h.call(y, this) || this instanceof a))
                    return new y(e);
                this._writableState = new g(e,this),
                this.writable = !0,
                e && ("function" == typeof e.write && (this._write = e.write),
                "function" == typeof e.writev && (this._writev = e.writev),
                "function" == typeof e.destroy && (this._destroy = e.destroy),
                "function" == typeof e.final && (this._final = e.final)),
                l.call(this)
            }
            function m(e, t) {
                var n = new Error("write after end");
                e.emit("error", n),
                i.nextTick(t, n)
            }
            function b(e, t, n, r) {
                var o = !0
                  , a = !1;
                return null === n ? a = new TypeError("May not write null values to stream") : "string" == typeof n || void 0 === n || t.objectMode || (a = new TypeError("Invalid non-string/buffer chunk")),
                a && (e.emit("error", a),
                i.nextTick(r, a),
                o = !1),
                o
            }
            function w(e, t, n, r, i, o) {
                if (!n) {
                    var a = function(e, t, n) {
                        return e.objectMode || !1 === e.decodeStrings || "string" != typeof t || (t = f.from(t, n)),
                        t
                    }(t, r, i);
                    r !== a && (n = !0,
                    i = "buffer",
                    r = a)
                }
                var s = t.objectMode ? 1 : r.length;
                t.length += s;
                var u = t.length < t.highWaterMark;
                if (u || (t.needDrain = !0),
                t.writing || t.corked) {
                    var c = t.lastBufferedRequest;
                    t.lastBufferedRequest = {
                        chunk: r,
                        encoding: i,
                        isBuf: n,
                        callback: o,
                        next: null
                    },
                    c ? c.next = t.lastBufferedRequest : t.bufferedRequest = t.lastBufferedRequest,
                    t.bufferedRequestCount += 1
                } else
                    _(e, t, !1, s, r, i, o);
                return u
            }
            function _(e, t, n, r, i, o, a) {
                t.writelen = r,
                t.writecb = a,
                t.writing = !0,
                t.sync = !0,
                n ? e._writev(i, t.onwrite) : e._write(i, o, t.onwrite),
                t.sync = !1
            }
            function S(e, t, n, r, o) {
                --t.pendingcb,
                n ? (i.nextTick(o, r),
                i.nextTick(A, e, t),
                e._writableState.errorEmitted = !0,
                e.emit("error", r)) : (o(r),
                e._writableState.errorEmitted = !0,
                e.emit("error", r),
                A(e, t))
            }
            function E(e, t) {
                var n = e._writableState
                  , r = n.sync
                  , i = n.writecb;
                if (function(e) {
                    e.writing = !1,
                    e.writecb = null,
                    e.length -= e.writelen,
                    e.writelen = 0
                }(n),
                t)
                    S(e, n, r, t, i);
                else {
                    var o = O(n);
                    o || n.corked || n.bufferProcessing || !n.bufferedRequest || T(e, n),
                    r ? s(x, e, n, o, i) : x(e, n, o, i)
                }
            }
            function x(e, t, n, r) {
                n || function(e, t) {
                    0 === t.length && t.needDrain && (t.needDrain = !1,
                    e.emit("drain"))
                }(e, t),
                t.pendingcb--,
                r(),
                A(e, t)
            }
            function T(e, t) {
                t.bufferProcessing = !0;
                var n = t.bufferedRequest;
                if (e._writev && n && n.next) {
                    var r = t.bufferedRequestCount
                      , i = new Array(r)
                      , a = t.corkedRequestsFree;
                    a.entry = n;
                    for (var s = 0, u = !0; n; )
                        i[s] = n,
                        n.isBuf || (u = !1),
                        n = n.next,
                        s += 1;
                    i.allBuffers = u,
                    _(e, t, !0, t.length, i, "", a.finish),
                    t.pendingcb++,
                    t.lastBufferedRequest = null,
                    a.next ? (t.corkedRequestsFree = a.next,
                    a.next = null) : t.corkedRequestsFree = new o(t),
                    t.bufferedRequestCount = 0
                } else {
                    for (; n; ) {
                        var c = n.chunk
                          , l = n.encoding
                          , f = n.callback;
                        if (_(e, t, !1, t.objectMode ? 1 : c.length, c, l, f),
                        n = n.next,
                        t.bufferedRequestCount--,
                        t.writing)
                            break
                    }
                    null === n && (t.lastBufferedRequest = null)
                }
                t.bufferedRequest = n,
                t.bufferProcessing = !1
            }
            function O(e) {
                return e.ending && 0 === e.length && null === e.bufferedRequest && !e.finished && !e.writing
            }
            function k(e, t) {
                e._final((function(n) {
                    t.pendingcb--,
                    n && e.emit("error", n),
                    t.prefinished = !0,
                    e.emit("prefinish"),
                    A(e, t)
                }
                ))
            }
            function A(e, t) {
                var n = O(t);
                return n && (function(e, t) {
                    t.prefinished || t.finalCalled || ("function" == typeof e._final ? (t.pendingcb++,
                    t.finalCalled = !0,
                    i.nextTick(k, e, t)) : (t.prefinished = !0,
                    e.emit("prefinish")))
                }(e, t),
                0 === t.pendingcb && (t.finished = !0,
                e.emit("finish"))),
                n
            }
            u.inherits(y, l),
            g.prototype.getBuffer = function() {
                for (var e = this.bufferedRequest, t = []; e; )
                    t.push(e),
                    e = e.next;
                return t
            }
            ,
            function() {
                try {
                    Object.defineProperty(g.prototype, "buffer", {
                        get: c.deprecate((function() {
                            return this.getBuffer()
                        }
                        ), "_writableState.buffer is deprecated. Use _writableState.getBuffer instead.", "DEP0003")
                    })
                } catch (e) {}
            }(),
            "function" == typeof Symbol && Symbol.hasInstance && "function" == typeof Function.prototype[Symbol.hasInstance] ? (h = Function.prototype[Symbol.hasInstance],
            Object.defineProperty(y, Symbol.hasInstance, {
                value: function(e) {
                    return !!h.call(this, e) || this === y && e && e._writableState instanceof g
                }
            })) : h = function(e) {
                return e instanceof this
            }
            ,
            y.prototype.pipe = function() {
                this.emit("error", new Error("Cannot pipe, not readable"))
            }
            ,
            y.prototype.write = function(e, t, n) {
                var r = this._writableState
                  , i = !1
                  , o = !r.objectMode && function(e) {
                    return f.isBuffer(e) || e instanceof d
                }(e);
                return o && !f.isBuffer(e) && (e = function(e) {
                    return f.from(e)
                }(e)),
                "function" == typeof t && (n = t,
                t = null),
                o ? t = "buffer" : t || (t = r.defaultEncoding),
                "function" != typeof n && (n = v),
                r.ended ? m(this, n) : (o || b(this, r, e, n)) && (r.pendingcb++,
                i = w(this, r, o, e, t, n)),
                i
            }
            ,
            y.prototype.cork = function() {
                this._writableState.corked++
            }
            ,
            y.prototype.uncork = function() {
                var e = this._writableState;
                e.corked && (e.corked--,
                e.writing || e.corked || e.finished || e.bufferProcessing || !e.bufferedRequest || T(this, e))
            }
            ,
            y.prototype.setDefaultEncoding = function(e) {
                if ("string" == typeof e && (e = e.toLowerCase()),
                !(["hex", "utf8", "utf-8", "ascii", "binary", "base64", "ucs2", "ucs-2", "utf16le", "utf-16le", "raw"].indexOf((e + "").toLowerCase()) > -1))
                    throw new TypeError("Unknown encoding: " + e);
                return this._writableState.defaultEncoding = e,
                this
            }
            ,
            Object.defineProperty(y.prototype, "writableHighWaterMark", {
                enumerable: !1,
                get: function() {
                    return this._writableState.highWaterMark
                }
            }),
            y.prototype._write = function(e, t, n) {
                n(new Error("_write() is not implemented"))
            }
            ,
            y.prototype._writev = null,
            y.prototype.end = function(e, t, n) {
                var r = this._writableState;
                "function" == typeof e ? (n = e,
                e = null,
                t = null) : "function" == typeof t && (n = t,
                t = null),
                null != e && this.write(e, t),
                r.corked && (r.corked = 1,
                this.uncork()),
                r.ending || r.finished || function(e, t, n) {
                    t.ending = !0,
                    A(e, t),
                    n && (t.finished ? i.nextTick(n) : e.once("finish", n)),
                    t.ended = !0,
                    e.writable = !1
                }(this, r, n)
            }
            ,
            Object.defineProperty(y.prototype, "destroyed", {
                get: function() {
                    return void 0 !== this._writableState && this._writableState.destroyed
                },
                set: function(e) {
                    this._writableState && (this._writableState.destroyed = e)
                }
            }),
            y.prototype.destroy = p.destroy,
            y.prototype._undestroy = p.undestroy,
            y.prototype._destroy = function(e, t) {
                this.end(),
                t(e)
            }
        }
        ).call(this, n("f28c"), n("c8ba"))
    },
    b7d1: function(e, t, n) {
        (function(t) {
            function n(e) {
                try {
                    if (!t.localStorage)
                        return !1
                } catch (e) {
                    return !1
                }
                var n = t.localStorage[e];
                return null != n && "true" === String(n).toLowerCase()
            }
            e.exports = function(e, t) {
                if (n("noDeprecation"))
                    return e;
                var r = !1;
                return function() {
                    if (!r) {
                        if (n("throwDeprecation"))
                            throw new Error(t);
                        n("traceDeprecation"),
                        r = !0
                    }
                    return e.apply(this, arguments)
                }
            }
        }
        ).call(this, n("c8ba"))
    },
    d6dd: function(e, t, n) {
        "use strict";
        var r = n("966d")
          , i = Object.keys || function(e) {
            var t = [];
            for (var n in e)
                t.push(n);
            return t
        }
        ;
        e.exports = f;
        var o = Object.create(n("3a7c"));
        o.inherits = n("3fb5");
        var a = n("6f2e")
          , s = n("6ffa");
        o.inherits(f, a);
        for (var u = i(s.prototype), c = 0; c < u.length; c++) {
            var l = u[c];
            f.prototype[l] || (f.prototype[l] = s.prototype[l])
        }
        function f(e) {
            if (!(this instanceof f))
                return new f(e);
            a.call(this, e),
            s.call(this, e),
            e && !1 === e.readable && (this.readable = !1),
            e && !1 === e.writable && (this.writable = !1),
            this.allowHalfOpen = !0,
            e && !1 === e.allowHalfOpen && (this.allowHalfOpen = !1),
            this.once("end", d)
        }
        function d() {
            this.allowHalfOpen || this._writableState.ended || r.nextTick(h, this)
        }
        function h(e) {
            e.end()
        }
        Object.defineProperty(f.prototype, "writableHighWaterMark", {
            enumerable: !1,
            get: function() {
                return this._writableState.highWaterMark
            }
        }),
        Object.defineProperty(f.prototype, "destroyed", {
            get: function() {
                return void 0 !== this._readableState && void 0 !== this._writableState && this._readableState.destroyed && this._writableState.destroyed
            },
            set: function(e) {
                void 0 !== this._readableState && void 0 !== this._writableState && (this._readableState.destroyed = e,
                this._writableState.destroyed = e)
            }
        }),
        f.prototype._destroy = function(e, t) {
            this.push(null),
            this.end(),
            r.nextTick(t, e)
        }
    },
    dcd0: function(e, t, n) {
        "use strict";
        e.exports = a;
        var r = n("d6dd")
          , i = Object.create(n("3a7c"));
        function o(e, t) {
            var n = this._transformState;
            n.transforming = !1;
            var r = n.writecb;
            if (!r)
                return this.emit("error", new Error("write callback called multiple times"));
            n.writechunk = null,
            n.writecb = null,
            null != t && this.push(t),
            r(e);
            var i = this._readableState;
            i.reading = !1,
            (i.needReadable || i.length < i.highWaterMark) && this._read(i.highWaterMark)
        }
        function a(e) {
            if (!(this instanceof a))
                return new a(e);
            r.call(this, e),
            this._transformState = {
                afterTransform: o.bind(this),
                needTransform: !1,
                transforming: !1,
                writecb: null,
                writechunk: null,
                writeencoding: null
            },
            this._readableState.needReadable = !0,
            this._readableState.sync = !1,
            e && ("function" == typeof e.transform && (this._transform = e.transform),
            "function" == typeof e.flush && (this._flush = e.flush)),
            this.on("prefinish", s)
        }
        function s() {
            var e = this;
            "function" == typeof this._flush ? this._flush((function(t, n) {
                u(e, t, n)
            }
            )) : u(this, null, null)
        }
        function u(e, t, n) {
            if (t)
                return e.emit("error", t);
            if (null != n && e.push(n),
            e._writableState.length)
                throw new Error("Calling transform done when ws.length != 0");
            if (e._transformState.transforming)
                throw new Error("Calling transform done when still transforming");
            return e.push(null)
        }
        i.inherits = n("3fb5"),
        i.inherits(a, r),
        a.prototype.push = function(e, t) {
            return this._transformState.needTransform = !1,
            r.prototype.push.call(this, e, t)
        }
        ,
        a.prototype._transform = function(e, t, n) {
            throw new Error("_transform() is not implemented")
        }
        ,
        a.prototype._write = function(e, t, n) {
            var r = this._transformState;
            if (r.writecb = n,
            r.writechunk = e,
            r.writeencoding = t,
            !r.transforming) {
                var i = this._readableState;
                (r.needTransform || i.needReadable || i.length < i.highWaterMark) && this._read(i.highWaterMark)
            }
        }
        ,
        a.prototype._read = function(e) {
            var t = this._transformState;
            null !== t.writechunk && t.writecb && !t.transforming ? (t.transforming = !0,
            this._transform(t.writechunk, t.writeencoding, t.afterTransform)) : t.needTransform = !0
        }
        ,
        a.prototype._destroy = function(e, t) {
            var n = this;
            r.prototype._destroy.call(this, e, (function(e) {
                t(e),
                n.emit("close")
            }
            ))
        }
    },
    aa69: function(e, t, n) {
        "use strict";
        e.exports = o;
        var r = n("dcd0")
          , i = Object.create(n("3a7c"));
        function o(e) {
            if (!(this instanceof o))
                return new o(e);
            r.call(this, e)
        }
        i.inherits = n("3fb5"),
        i.inherits(o, r),
        o.prototype._transform = function(e, t, n) {
            n(null, e)
        }
    },
    af7e: function(e, t, n) {
        e.exports = n("6ffa")
    },
    "7c16": function(e, t, n) {
        e.exports = n("d6dd")
    },
    "89fd": function(e, t, n) {
        e.exports = n("0ac3").Transform
    },
    "51a2": function(e, t, n) {
        e.exports = n("0ac3").PassThrough
    },
    "7d72": function(e, t, n) {
        "use strict";
        var r = n("8707").Buffer
          , i = r.isEncoding || function(e) {
            switch ((e = "" + e) && e.toLowerCase()) {
            case "hex":
            case "utf8":
            case "utf-8":
            case "ascii":
            case "binary":
            case "base64":
            case "ucs2":
            case "ucs-2":
            case "utf16le":
            case "utf-16le":
            case "raw":
                return !0;
            default:
                return !1
            }
        }
        ;
        function o(e) {
            var t;
            switch (this.encoding = function(e) {
                var t = function(e) {
                    if (!e)
                        return "utf8";
                    for (var t; ; )
                        switch (e) {
                        case "utf8":
                        case "utf-8":
                            return "utf8";
                        case "ucs2":
                        case "ucs-2":
                        case "utf16le":
                        case "utf-16le":
                            return "utf16le";
                        case "latin1":
                        case "binary":
                            return "latin1";
                        case "base64":
                        case "ascii":
                        case "hex":
                            return e;
                        default:
                            if (t)
                                return;
                            e = ("" + e).toLowerCase(),
                            t = !0
                        }
                }(e);
                if ("string" != typeof t && (r.isEncoding === i || !i(e)))
                    throw new Error("Unknown encoding: " + e);
                return t || e
            }(e),
            this.encoding) {
            case "utf16le":
                this.text = u,
                this.end = c,
                t = 4;
                break;
            case "utf8":
                this.fillLast = s,
                t = 4;
                break;
            case "base64":
                this.text = l,
                this.end = f,
                t = 3;
                break;
            default:
                return this.write = d,
                void (this.end = h)
            }
            this.lastNeed = 0,
            this.lastTotal = 0,
            this.lastChar = r.allocUnsafe(t)
        }
        function a(e) {
            return e <= 127 ? 0 : e >> 5 == 6 ? 2 : e >> 4 == 14 ? 3 : e >> 3 == 30 ? 4 : e >> 6 == 2 ? -1 : -2
        }
        function s(e) {
            var t = this.lastTotal - this.lastNeed
              , n = function(e, t, n) {
                if (128 != (192 & t[0]))
                    return e.lastNeed = 0,
                    "�";
                if (e.lastNeed > 1 && t.length > 1) {
                    if (128 != (192 & t[1]))
                        return e.lastNeed = 1,
                        "�";
                    if (e.lastNeed > 2 && t.length > 2 && 128 != (192 & t[2]))
                        return e.lastNeed = 2,
                        "�"
                }
            }(this, e);
            return void 0 !== n ? n : this.lastNeed <= e.length ? (e.copy(this.lastChar, t, 0, this.lastNeed),
            this.lastChar.toString(this.encoding, 0, this.lastTotal)) : (e.copy(this.lastChar, t, 0, e.length),
            void (this.lastNeed -= e.length))
        }
        function u(e, t) {
            if ((e.length - t) % 2 == 0) {
                var n = e.toString("utf16le", t);
                if (n) {
                    var r = n.charCodeAt(n.length - 1);
                    if (r >= 55296 && r <= 56319)
                        return this.lastNeed = 2,
                        this.lastTotal = 4,
                        this.lastChar[0] = e[e.length - 2],
                        this.lastChar[1] = e[e.length - 1],
                        n.slice(0, -1)
                }
                return n
            }
            return this.lastNeed = 1,
            this.lastTotal = 2,
            this.lastChar[0] = e[e.length - 1],
            e.toString("utf16le", t, e.length - 1)
        }
        function c(e) {
            var t = e && e.length ? this.write(e) : "";
            if (this.lastNeed) {
                var n = this.lastTotal - this.lastNeed;
                return t + this.lastChar.toString("utf16le", 0, n)
            }
            return t
        }
        function l(e, t) {
            var n = (e.length - t) % 3;
            return 0 === n ? e.toString("base64", t) : (this.lastNeed = 3 - n,
            this.lastTotal = 3,
            1 === n ? this.lastChar[0] = e[e.length - 1] : (this.lastChar[0] = e[e.length - 2],
            this.lastChar[1] = e[e.length - 1]),
            e.toString("base64", t, e.length - n))
        }
        function f(e) {
            var t = e && e.length ? this.write(e) : "";
            return this.lastNeed ? t + this.lastChar.toString("base64", 0, 3 - this.lastNeed) : t
        }
        function d(e) {
            return e.toString(this.encoding)
        }
        function h(e) {
            return e && e.length ? this.write(e) : ""
        }
        t.StringDecoder = o,
        o.prototype.write = function(e) {
            if (0 === e.length)
                return "";
            var t, n;
            if (this.lastNeed) {
                if (void 0 === (t = this.fillLast(e)))
                    return "";
                n = this.lastNeed,
                this.lastNeed = 0
            } else
                n = 0;
            return n < e.length ? t ? t + this.text(e, n) : this.text(e, n) : t || ""
        }
        ,
        o.prototype.end = function(e) {
            var t = e && e.length ? this.write(e) : "";
            return this.lastNeed ? t + "�" : t
        }
        ,
        o.prototype.text = function(e, t) {
            var n = function(e, t, n) {
                var r = t.length - 1;
                if (r < n)
                    return 0;
                var i = a(t[r]);
                return i >= 0 ? (i > 0 && (e.lastNeed = i - 1),
                i) : --r < n || -2 === i ? 0 : (i = a(t[r])) >= 0 ? (i > 0 && (e.lastNeed = i - 2),
                i) : --r < n || -2 === i ? 0 : (i = a(t[r])) >= 0 ? (i > 0 && (2 === i ? i = 0 : e.lastNeed = i - 3),
                i) : 0
            }(this, e, t);
            if (!this.lastNeed)
                return e.toString("utf8", t);
            this.lastTotal = n;
            var r = e.length - (n - this.lastNeed);
            return e.copy(this.lastChar, 0, r),
            e.toString("utf8", t, r)
        }
        ,
        o.prototype.fillLast = function(e) {
            if (this.lastNeed <= e.length)
                return e.copy(this.lastChar, this.lastTotal - this.lastNeed, 0, this.lastNeed),
                this.lastChar.toString(this.encoding, 0, this.lastTotal);
            e.copy(this.lastChar, this.lastTotal - this.lastNeed, 0, e.length),
            this.lastNeed -= e.length
        }
    },
    "5a76": function(e, t, n) {
        var r = n("f576");
        e.exports = function(e) {
            return (new r).update(e).digest()
        }
    },
    f576: function(e, t, n) {
        "use strict";
        var r = n("3fb5")
          , i = n("93e6")
          , o = n("8707").Buffer
          , a = new Array(16);
        function s() {
            i.call(this, 64),
            this._a = 1732584193,
            this._b = 4023233417,
            this._c = 2562383102,
            this._d = 271733878
        }
        function u(e, t) {
            return e << t | e >>> 32 - t
        }
        function c(e, t, n, r, i, o, a) {
            return u(e + (t & n | ~t & r) + i + o | 0, a) + t | 0
        }
        function l(e, t, n, r, i, o, a) {
            return u(e + (t & r | n & ~r) + i + o | 0, a) + t | 0
        }
        function f(e, t, n, r, i, o, a) {
            return u(e + (t ^ n ^ r) + i + o | 0, a) + t | 0
        }
        function d(e, t, n, r, i, o, a) {
            return u(e + (n ^ (t | ~r)) + i + o | 0, a) + t | 0
        }
        r(s, i),
        s.prototype._update = function() {
            for (var e = a, t = 0; t < 16; ++t)
                e[t] = this._block.readInt32LE(4 * t);
            var n = this._a
              , r = this._b
              , i = this._c
              , o = this._d;
            n = c(n, r, i, o, e[0], 3614090360, 7),
            o = c(o, n, r, i, e[1], 3905402710, 12),
            i = c(i, o, n, r, e[2], 606105819, 17),
            r = c(r, i, o, n, e[3], 3250441966, 22),
            n = c(n, r, i, o, e[4], 4118548399, 7),
            o = c(o, n, r, i, e[5], 1200080426, 12),
            i = c(i, o, n, r, e[6], 2821735955, 17),
            r = c(r, i, o, n, e[7], 4249261313, 22),
            n = c(n, r, i, o, e[8], 1770035416, 7),
            o = c(o, n, r, i, e[9], 2336552879, 12),
            i = c(i, o, n, r, e[10], 4294925233, 17),
            r = c(r, i, o, n, e[11], 2304563134, 22),
            n = c(n, r, i, o, e[12], 1804603682, 7),
            o = c(o, n, r, i, e[13], 4254626195, 12),
            i = c(i, o, n, r, e[14], 2792965006, 17),
            n = l(n, r = c(r, i, o, n, e[15], 1236535329, 22), i, o, e[1], 4129170786, 5),
            o = l(o, n, r, i, e[6], 3225465664, 9),
            i = l(i, o, n, r, e[11], 643717713, 14),
            r = l(r, i, o, n, e[0], 3921069994, 20),
            n = l(n, r, i, o, e[5], 3593408605, 5),
            o = l(o, n, r, i, e[10], 38016083, 9),
            i = l(i, o, n, r, e[15], 3634488961, 14),
            r = l(r, i, o, n, e[4], 3889429448, 20),
            n = l(n, r, i, o, e[9], 568446438, 5),
            o = l(o, n, r, i, e[14], 3275163606, 9),
            i = l(i, o, n, r, e[3], 4107603335, 14),
            r = l(r, i, o, n, e[8], 1163531501, 20),
            n = l(n, r, i, o, e[13], 2850285829, 5),
            o = l(o, n, r, i, e[2], 4243563512, 9),
            i = l(i, o, n, r, e[7], 1735328473, 14),
            n = f(n, r = l(r, i, o, n, e[12], 2368359562, 20), i, o, e[5], 4294588738, 4),
            o = f(o, n, r, i, e[8], 2272392833, 11),
            i = f(i, o, n, r, e[11], 1839030562, 16),
            r = f(r, i, o, n, e[14], 4259657740, 23),
            n = f(n, r, i, o, e[1], 2763975236, 4),
            o = f(o, n, r, i, e[4], 1272893353, 11),
            i = f(i, o, n, r, e[7], 4139469664, 16),
            r = f(r, i, o, n, e[10], 3200236656, 23),
            n = f(n, r, i, o, e[13], 681279174, 4),
            o = f(o, n, r, i, e[0], 3936430074, 11),
            i = f(i, o, n, r, e[3], 3572445317, 16),
            r = f(r, i, o, n, e[6], 76029189, 23),
            n = f(n, r, i, o, e[9], 3654602809, 4),
            o = f(o, n, r, i, e[12], 3873151461, 11),
            i = f(i, o, n, r, e[15], 530742520, 16),
            n = d(n, r = f(r, i, o, n, e[2], 3299628645, 23), i, o, e[0], 4096336452, 6),
            o = d(o, n, r, i, e[7], 1126891415, 10),
            i = d(i, o, n, r, e[14], 2878612391, 15),
            r = d(r, i, o, n, e[5], 4237533241, 21),
            n = d(n, r, i, o, e[12], 1700485571, 6),
            o = d(o, n, r, i, e[3], 2399980690, 10),
            i = d(i, o, n, r, e[10], 4293915773, 15),
            r = d(r, i, o, n, e[1], 2240044497, 21),
            n = d(n, r, i, o, e[8], 1873313359, 6),
            o = d(o, n, r, i, e[15], 4264355552, 10),
            i = d(i, o, n, r, e[6], 2734768916, 15),
            r = d(r, i, o, n, e[13], 1309151649, 21),
            n = d(n, r, i, o, e[4], 4149444226, 6),
            o = d(o, n, r, i, e[11], 3174756917, 10),
            i = d(i, o, n, r, e[2], 718787259, 15),
            r = d(r, i, o, n, e[9], 3951481745, 21),
            this._a = this._a + n | 0,
            this._b = this._b + r | 0,
            this._c = this._c + i | 0,
            this._d = this._d + o | 0
        }
        ,
        s.prototype._digest = function() {
            this._block[this._blockOffset++] = 128,
            this._blockOffset > 56 && (this._block.fill(0, this._blockOffset, 64),
            this._update(),
            this._blockOffset = 0),
            this._block.fill(0, this._blockOffset, 56),
            this._block.writeUInt32LE(this._length[0], 56),
            this._block.writeUInt32LE(this._length[1], 60),
            this._update();
            var e = o.allocUnsafe(16);
            return e.writeInt32LE(this._a, 0),
            e.writeInt32LE(this._b, 4),
            e.writeInt32LE(this._c, 8),
            e.writeInt32LE(this._d, 12),
            e
        }
        ,
        e.exports = s
    },
    "93e6": function(e, t, n) {
        "use strict";
        var r = n("8707").Buffer
          , i = n("e372").Transform;
        function o(e) {
            i.call(this),
            this._block = r.allocUnsafe(e),
            this._blockSize = e,
            this._blockOffset = 0,
            this._length = [0, 0, 0, 0],
            this._finalized = !1
        }
        n("3fb5")(o, i),
        o.prototype._transform = function(e, t, n) {
            var r = null;
            try {
                this.update(e, t)
            } catch (e) {
                r = e
            }
            n(r)
        }
        ,
        o.prototype._flush = function(e) {
            var t = null;
            try {
                this.push(this.digest())
            } catch (e) {
                t = e
            }
            e(t)
        }
        ,
        o.prototype.update = function(e, t) {
            if (function(e, t) {
                if (!r.isBuffer(e) && "string" != typeof e)
                    throw new TypeError(t + " must be a string or a buffer")
            }(e, "Data"),
            this._finalized)
                throw new Error("Digest already called");
            r.isBuffer(e) || (e = r.from(e, t));
            for (var n = this._block, i = 0; this._blockOffset + e.length - i >= this._blockSize; ) {
                for (var o = this._blockOffset; o < this._blockSize; )
                    n[o++] = e[i++];
                this._update(),
                this._blockOffset = 0
            }
            for (; i < e.length; )
                n[this._blockOffset++] = e[i++];
            for (var a = 0, s = 8 * e.length; s > 0; ++a)
                this._length[a] += s,
                (s = this._length[a] / 4294967296 | 0) > 0 && (this._length[a] -= 4294967296 * s);
            return this
        }
        ,
        o.prototype._update = function() {
            throw new Error("_update is not implemented")
        }
        ,
        o.prototype.digest = function(e) {
            if (this._finalized)
                throw new Error("Digest already called");
            this._finalized = !0;
            var t = this._digest();
            void 0 !== e && (t = t.toString(e)),
            this._block.fill(0),
            this._blockOffset = 0;
            for (var n = 0; n < 4; ++n)
                this._length[n] = 0;
            return t
        }
        ,
        o.prototype._digest = function() {
            throw new Error("_digest is not implemented")
        }
        ,
        e.exports = o
    },
    e372: function(e, t, n) {
        (t = e.exports = n("ad71")).Stream = t,
        t.Readable = t,
        t.Writable = n("dc14"),
        t.Duplex = n("b19a"),
        t.Transform = n("27bf"),
        t.PassThrough = n("780f"),
        t.finished = n("903c"),
        t.pipeline = n("5d1c")
    },
    ad71: function(e, t, n) {
        "use strict";
        (function(t, r) {
            var i;
            e.exports = T,
            T.ReadableState = x,
            n("faa1").EventEmitter;
            var o = function(e, t) {
                return e.listeners(t).length
            }
              , a = n("429b")
              , s = n("b639").Buffer
              , u = t.Uint8Array || function() {}
            ;
            var c, l = n(3);
            c = l && l.debuglog ? l.debuglog("stream") : function() {}
            ;
            var f, d, h, p = n("c6ae"), v = n("4681"), g = n("0db6").getHighWaterMark, y = n("c9b8").codes, m = y.ERR_INVALID_ARG_TYPE, b = y.ERR_STREAM_PUSH_AFTER_EOF, w = y.ERR_METHOD_NOT_IMPLEMENTED, _ = y.ERR_STREAM_UNSHIFT_AFTER_END_EVENT;
            n("3fb5")(T, a);
            var S = v.errorOrDestroy
              , E = ["error", "close", "destroy", "pause", "resume"];
            function x(e, t, r) {
                i = i || n("b19a"),
                e = e || {},
                "boolean" != typeof r && (r = t instanceof i),
                this.objectMode = !!e.objectMode,
                r && (this.objectMode = this.objectMode || !!e.readableObjectMode),
                this.highWaterMark = g(this, e, "readableHighWaterMark", r),
                this.buffer = new p,
                this.length = 0,
                this.pipes = null,
                this.pipesCount = 0,
                this.flowing = null,
                this.ended = !1,
                this.endEmitted = !1,
                this.reading = !1,
                this.sync = !0,
                this.needReadable = !1,
                this.emittedReadable = !1,
                this.readableListening = !1,
                this.resumeScheduled = !1,
                this.paused = !0,
                this.emitClose = !1 !== e.emitClose,
                this.autoDestroy = !!e.autoDestroy,
                this.destroyed = !1,
                this.defaultEncoding = e.defaultEncoding || "utf8",
                this.awaitDrain = 0,
                this.readingMore = !1,
                this.decoder = null,
                this.encoding = null,
                e.encoding && (f || (f = n("7d72").StringDecoder),
                this.decoder = new f(e.encoding),
                this.encoding = e.encoding)
            }
            function T(e) {
                if (i = i || n("b19a"),
                !(this instanceof T))
                    return new T(e);
                var t = this instanceof i;
                this._readableState = new x(e,this,t),
                this.readable = !0,
                e && ("function" == typeof e.read && (this._read = e.read),
                "function" == typeof e.destroy && (this._destroy = e.destroy)),
                a.call(this)
            }
            function O(e, t, n, r, i) {
                c("readableAddChunk", t);
                var o, a = e._readableState;
                if (null === t)
                    a.reading = !1,
                    function(e, t) {
                        if (c("onEofChunk"),
                        !t.ended) {
                            if (t.decoder) {
                                var n = t.decoder.end();
                                n && n.length && (t.buffer.push(n),
                                t.length += t.objectMode ? 1 : n.length)
                            }
                            t.ended = !0,
                            t.sync ? P(e) : (t.needReadable = !1,
                            t.emittedReadable || (t.emittedReadable = !0,
                            M(e)))
                        }
                    }(e, a);
                else if (i || (o = function(e, t) {
                    var n;
                    return function(e) {
                        return s.isBuffer(e) || e instanceof u
                    }(t) || "string" == typeof t || void 0 === t || e.objectMode || (n = new m("chunk",["string", "Buffer", "Uint8Array"],t)),
                    n
                }(a, t)),
                o)
                    S(e, o);
                else if (a.objectMode || t && t.length > 0)
                    if ("string" == typeof t || a.objectMode || Object.getPrototypeOf(t) === s.prototype || (t = function(e) {
                        return s.from(e)
                    }(t)),
                    r)
                        a.endEmitted ? S(e, new _) : k(e, a, t, !0);
                    else if (a.ended)
                        S(e, new b);
                    else {
                        if (a.destroyed)
                            return !1;
                        a.reading = !1,
                        a.decoder && !n ? (t = a.decoder.write(t),
                        a.objectMode || 0 !== t.length ? k(e, a, t, !1) : L(e, a)) : k(e, a, t, !1)
                    }
                else
                    r || (a.reading = !1,
                    L(e, a));
                return !a.ended && (a.length < a.highWaterMark || 0 === a.length)
            }
            function k(e, t, n, r) {
                t.flowing && 0 === t.length && !t.sync ? (t.awaitDrain = 0,
                e.emit("data", n)) : (t.length += t.objectMode ? 1 : n.length,
                r ? t.buffer.unshift(n) : t.buffer.push(n),
                t.needReadable && P(e)),
                L(e, t)
            }
            Object.defineProperty(T.prototype, "destroyed", {
                enumerable: !1,
                get: function() {
                    return void 0 !== this._readableState && this._readableState.destroyed
                },
                set: function(e) {
                    this._readableState && (this._readableState.destroyed = e)
                }
            }),
            T.prototype.destroy = v.destroy,
            T.prototype._undestroy = v.undestroy,
            T.prototype._destroy = function(e, t) {
                t(e)
            }
            ,
            T.prototype.push = function(e, t) {
                var n, r = this._readableState;
                return r.objectMode ? n = !0 : "string" == typeof e && ((t = t || r.defaultEncoding) !== r.encoding && (e = s.from(e, t),
                t = ""),
                n = !0),
                O(this, e, t, !1, n)
            }
            ,
            T.prototype.unshift = function(e) {
                return O(this, e, null, !0, !1)
            }
            ,
            T.prototype.isPaused = function() {
                return !1 === this._readableState.flowing
            }
            ,
            T.prototype.setEncoding = function(e) {
                f || (f = n("7d72").StringDecoder);
                var t = new f(e);
                this._readableState.decoder = t,
                this._readableState.encoding = this._readableState.decoder.encoding;
                for (var r = this._readableState.buffer.head, i = ""; null !== r; )
                    i += t.write(r.data),
                    r = r.next;
                return this._readableState.buffer.clear(),
                "" !== i && this._readableState.buffer.push(i),
                this._readableState.length = i.length,
                this
            }
            ;
            var A = 1073741824;
            function C(e, t) {
                return e <= 0 || 0 === t.length && t.ended ? 0 : t.objectMode ? 1 : e != e ? t.flowing && t.length ? t.buffer.head.data.length : t.length : (e > t.highWaterMark && (t.highWaterMark = function(e) {
                    return e >= A ? e = A : (e--,
                    e |= e >>> 1,
                    e |= e >>> 2,
                    e |= e >>> 4,
                    e |= e >>> 8,
                    e |= e >>> 16,
                    e++),
                    e
                }(e)),
                e <= t.length ? e : t.ended ? t.length : (t.needReadable = !0,
                0))
            }
            function P(e) {
                var t = e._readableState;
                c("emitReadable", t.needReadable, t.emittedReadable),
                t.needReadable = !1,
                t.emittedReadable || (c("emitReadable", t.flowing),
                t.emittedReadable = !0,
                r.nextTick(M, e))
            }
            function M(e) {
                var t = e._readableState;
                c("emitReadable_", t.destroyed, t.length, t.ended),
                t.destroyed || !t.length && !t.ended || (e.emit("readable"),
                t.emittedReadable = !1),
                t.needReadable = !t.flowing && !t.ended && t.length <= t.highWaterMark,
                N(e)
            }
            function L(e, t) {
                t.readingMore || (t.readingMore = !0,
                r.nextTick(I, e, t))
            }
            function I(e, t) {
                for (; !t.reading && !t.ended && (t.length < t.highWaterMark || t.flowing && 0 === t.length); ) {
                    var n = t.length;
                    if (c("maybeReadMore read 0"),
                    e.read(0),
                    n === t.length)
                        break
                }
                t.readingMore = !1
            }
            function R(e) {
                var t = e._readableState;
                t.readableListening = e.listenerCount("readable") > 0,
                t.resumeScheduled && !t.paused ? t.flowing = !0 : e.listenerCount("data") > 0 && e.resume()
            }
            function j(e) {
                c("readable nexttick read 0"),
                e.read(0)
            }
            function B(e, t) {
                c("resume", t.reading),
                t.reading || e.read(0),
                t.resumeScheduled = !1,
                e.emit("resume"),
                N(e),
                t.flowing && !t.reading && e.read(0)
            }
            function N(e) {
                var t = e._readableState;
                for (c("flow", t.flowing); t.flowing && null !== e.read(); )
                    ;
            }
            function D(e, t) {
                return 0 === t.length ? null : (t.objectMode ? n = t.buffer.shift() : !e || e >= t.length ? (n = t.decoder ? t.buffer.join("") : 1 === t.buffer.length ? t.buffer.first() : t.buffer.concat(t.length),
                t.buffer.clear()) : n = t.buffer.consume(e, t.decoder),
                n);
                var n
            }
            function F(e) {
                var t = e._readableState;
                c("endReadable", t.endEmitted),
                t.endEmitted || (t.ended = !0,
                r.nextTick(U, t, e))
            }
            function U(e, t) {
                if (c("endReadableNT", e.endEmitted, e.length),
                !e.endEmitted && 0 === e.length && (e.endEmitted = !0,
                t.readable = !1,
                t.emit("end"),
                e.autoDestroy)) {
                    var n = t._writableState;
                    (!n || n.autoDestroy && n.finished) && t.destroy()
                }
            }
            function $(e, t) {
                for (var n = 0, r = e.length; n < r; n++)
                    if (e[n] === t)
                        return n;
                return -1
            }
            T.prototype.read = function(e) {
                c("read", e),
                e = parseInt(e, 10);
                var t = this._readableState
                  , n = e;
                if (0 !== e && (t.emittedReadable = !1),
                0 === e && t.needReadable && ((0 !== t.highWaterMark ? t.length >= t.highWaterMark : t.length > 0) || t.ended))
                    return c("read: emitReadable", t.length, t.ended),
                    0 === t.length && t.ended ? F(this) : P(this),
                    null;
                if (0 === (e = C(e, t)) && t.ended)
                    return 0 === t.length && F(this),
                    null;
                var r, i = t.needReadable;
                return c("need readable", i),
                (0 === t.length || t.length - e < t.highWaterMark) && c("length less than watermark", i = !0),
                t.ended || t.reading ? c("reading or ended", i = !1) : i && (c("do read"),
                t.reading = !0,
                t.sync = !0,
                0 === t.length && (t.needReadable = !0),
                this._read(t.highWaterMark),
                t.sync = !1,
                t.reading || (e = C(n, t))),
                null === (r = e > 0 ? D(e, t) : null) ? (t.needReadable = t.length <= t.highWaterMark,
                e = 0) : (t.length -= e,
                t.awaitDrain = 0),
                0 === t.length && (t.ended || (t.needReadable = !0),
                n !== e && t.ended && F(this)),
                null !== r && this.emit("data", r),
                r
            }
            ,
            T.prototype._read = function(e) {
                S(this, new w("_read()"))
            }
            ,
            T.prototype.pipe = function(e, t) {
                var n = this
                  , i = this._readableState;
                switch (i.pipesCount) {
                case 0:
                    i.pipes = e;
                    break;
                case 1:
                    i.pipes = [i.pipes, e];
                    break;
                default:
                    i.pipes.push(e)
                }
                i.pipesCount += 1,
                c("pipe count=%d opts=%j", i.pipesCount, t);
                var a = (!t || !1 !== t.end) && e !== r.stdout && e !== r.stderr ? u : y;
                function s(e, t) {
                    c("onunpipe"),
                    e === n && t && !1 === t.hasUnpiped && (t.hasUnpiped = !0,
                    d())
                }
                function u() {
                    c("onend"),
                    e.end()
                }
                i.endEmitted ? r.nextTick(a) : n.once("end", a),
                e.on("unpipe", s);
                var l = function(e) {
                    return function() {
                        var t = e._readableState;
                        c("pipeOnDrain", t.awaitDrain),
                        t.awaitDrain && t.awaitDrain--,
                        0 === t.awaitDrain && o(e, "data") && (t.flowing = !0,
                        N(e))
                    }
                }(n);
                e.on("drain", l);
                var f = !1;
                function d() {
                    c("cleanup"),
                    e.removeListener("close", v),
                    e.removeListener("finish", g),
                    e.removeListener("drain", l),
                    e.removeListener("error", p),
                    e.removeListener("unpipe", s),
                    n.removeListener("end", u),
                    n.removeListener("end", y),
                    n.removeListener("data", h),
                    f = !0,
                    !i.awaitDrain || e._writableState && !e._writableState.needDrain || l()
                }
                function h(t) {
                    c("ondata");
                    var r = e.write(t);
                    c("dest.write", r),
                    !1 === r && ((1 === i.pipesCount && i.pipes === e || i.pipesCount > 1 && -1 !== $(i.pipes, e)) && !f && (c("false write response, pause", i.awaitDrain),
                    i.awaitDrain++),
                    n.pause())
                }
                function p(t) {
                    c("onerror", t),
                    y(),
                    e.removeListener("error", p),
                    0 === o(e, "error") && S(e, t)
                }
                function v() {
                    e.removeListener("finish", g),
                    y()
                }
                function g() {
                    c("onfinish"),
                    e.removeListener("close", v),
                    y()
                }
                function y() {
                    c("unpipe"),
                    n.unpipe(e)
                }
                return n.on("data", h),
                function(e, t, n) {
                    if ("function" == typeof e.prependListener)
                        return e.prependListener(t, n);
                    e._events && e._events[t] ? Array.isArray(e._events[t]) ? e._events[t].unshift(n) : e._events[t] = [n, e._events[t]] : e.on(t, n)
                }(e, "error", p),
                e.once("close", v),
                e.once("finish", g),
                e.emit("pipe", n),
                i.flowing || (c("pipe resume"),
                n.resume()),
                e
            }
            ,
            T.prototype.unpipe = function(e) {
                var t = this._readableState
                  , n = {
                    hasUnpiped: !1
                };
                if (0 === t.pipesCount)
                    return this;
                if (1 === t.pipesCount)
                    return e && e !== t.pipes || (e || (e = t.pipes),
                    t.pipes = null,
                    t.pipesCount = 0,
                    t.flowing = !1,
                    e && e.emit("unpipe", this, n)),
                    this;
                if (!e) {
                    var r = t.pipes
                      , i = t.pipesCount;
                    t.pipes = null,
                    t.pipesCount = 0,
                    t.flowing = !1;
                    for (var o = 0; o < i; o++)
                        r[o].emit("unpipe", this, {
                            hasUnpiped: !1
                        });
                    return this
                }
                var a = $(t.pipes, e);
                return -1 === a || (t.pipes.splice(a, 1),
                t.pipesCount -= 1,
                1 === t.pipesCount && (t.pipes = t.pipes[0]),
                e.emit("unpipe", this, n)),
                this
            }
            ,
            T.prototype.on = function(e, t) {
                var n = a.prototype.on.call(this, e, t)
                  , i = this._readableState;
                return "data" === e ? (i.readableListening = this.listenerCount("readable") > 0,
                !1 !== i.flowing && this.resume()) : "readable" === e && (i.endEmitted || i.readableListening || (i.readableListening = i.needReadable = !0,
                i.flowing = !1,
                i.emittedReadable = !1,
                c("on readable", i.length, i.reading),
                i.length ? P(this) : i.reading || r.nextTick(j, this))),
                n
            }
            ,
            T.prototype.addListener = T.prototype.on,
            T.prototype.removeListener = function(e, t) {
                var n = a.prototype.removeListener.call(this, e, t);
                return "readable" === e && r.nextTick(R, this),
                n
            }
            ,
            T.prototype.removeAllListeners = function(e) {
                var t = a.prototype.removeAllListeners.apply(this, arguments);
                return "readable" !== e && void 0 !== e || r.nextTick(R, this),
                t
            }
            ,
            T.prototype.resume = function() {
                var e = this._readableState;
                return e.flowing || (c("resume"),
                e.flowing = !e.readableListening,
                function(e, t) {
                    t.resumeScheduled || (t.resumeScheduled = !0,
                    r.nextTick(B, e, t))
                }(this, e)),
                e.paused = !1,
                this
            }
            ,
            T.prototype.pause = function() {
                return c("call pause flowing=%j", this._readableState.flowing),
                !1 !== this._readableState.flowing && (c("pause"),
                this._readableState.flowing = !1,
                this.emit("pause")),
                this._readableState.paused = !0,
                this
            }
            ,
            T.prototype.wrap = function(e) {
                var t = this
                  , n = this._readableState
                  , r = !1;
                for (var i in e.on("end", (function() {
                    if (c("wrapped end"),
                    n.decoder && !n.ended) {
                        var e = n.decoder.end();
                        e && e.length && t.push(e)
                    }
                    t.push(null)
                }
                )),
                e.on("data", (function(i) {
                    (c("wrapped data"),
                    n.decoder && (i = n.decoder.write(i)),
                    n.objectMode && null == i || !(n.objectMode || i && i.length)) || (t.push(i) || (r = !0,
                    e.pause()))
                }
                )),
                e)
                    void 0 === this[i] && "function" == typeof e[i] && (this[i] = function(t) {
                        return function() {
                            return e[t].apply(e, arguments)
                        }
                    }(i));
                for (var o = 0; o < E.length; o++)
                    e.on(E[o], this.emit.bind(this, E[o]));
                return this._read = function(t) {
                    c("wrapped _read", t),
                    r && (r = !1,
                    e.resume())
                }
                ,
                this
            }
            ,
            "function" == typeof Symbol && (T.prototype[Symbol.asyncIterator] = function() {
                return void 0 === d && (d = n("9c0e")),
                d(this)
            }
            ),
            Object.defineProperty(T.prototype, "readableHighWaterMark", {
                enumerable: !1,
                get: function() {
                    return this._readableState.highWaterMark
                }
            }),
            Object.defineProperty(T.prototype, "readableBuffer", {
                enumerable: !1,
                get: function() {
                    return this._readableState && this._readableState.buffer
                }
            }),
            Object.defineProperty(T.prototype, "readableFlowing", {
                enumerable: !1,
                get: function() {
                    return this._readableState.flowing
                },
                set: function(e) {
                    this._readableState && (this._readableState.flowing = e)
                }
            }),
            T._fromList = D,
            Object.defineProperty(T.prototype, "readableLength", {
                enumerable: !1,
                get: function() {
                    return this._readableState.length
                }
            }),
            "function" == typeof Symbol && (T.from = function(e, t) {
                return void 0 === h && (h = n("07c6")),
                h(T, e, t)
            }
            )
        }
        ).call(this, n("c8ba"), n("f28c"))
    },
    "429b": function(e, t, n) {
        e.exports = n("faa1").EventEmitter
    },
    c6ae: function(e, t, n) {
        "use strict";
        function r(e, t) {
            var n = Object.keys(e);
            if (Object.getOwnPropertySymbols) {
                var r = Object.getOwnPropertySymbols(e);
                t && (r = r.filter((function(t) {
                    return Object.getOwnPropertyDescriptor(e, t).enumerable
                }
                ))),
                n.push.apply(n, r)
            }
            return n
        }
        function i(e, t, n) {
            return t in e ? Object.defineProperty(e, t, {
                value: n,
                enumerable: !0,
                configurable: !0,
                writable: !0
            }) : e[t] = n,
            e
        }
        function o(e, t) {
            for (var n = 0; n < t.length; n++) {
                var r = t[n];
                r.enumerable = r.enumerable || !1,
                r.configurable = !0,
                "value"in r && (r.writable = !0),
                Object.defineProperty(e, r.key, r)
            }
        }
        var a = n("b639").Buffer
          , s = n(4).inspect
          , u = s && s.custom || "inspect";
        function c(e, t, n) {
            a.prototype.copy.call(e, t, n)
        }
        e.exports = function() {
            function e() {
                (function(e, t) {
                    if (!(e instanceof t))
                        throw new TypeError("Cannot call a class as a function")
                }
                )(this, e),
                this.head = null,
                this.tail = null,
                this.length = 0
            }
            return function(e, t, n) {
                t && o(e.prototype, t),
                n && o(e, n)
            }(e, [{
                key: "push",
                value: function(e) {
                    var t = {
                        data: e,
                        next: null
                    };
                    this.length > 0 ? this.tail.next = t : this.head = t,
                    this.tail = t,
                    ++this.length
                }
            }, {
                key: "unshift",
                value: function(e) {
                    var t = {
                        data: e,
                        next: this.head
                    };
                    0 === this.length && (this.tail = t),
                    this.head = t,
                    ++this.length
                }
            }, {
                key: "shift",
                value: function() {
                    if (0 !== this.length) {
                        var e = this.head.data;
                        return 1 === this.length ? this.head = this.tail = null : this.head = this.head.next,
                        --this.length,
                        e
                    }
                }
            }, {
                key: "clear",
                value: function() {
                    this.head = this.tail = null,
                    this.length = 0
                }
            }, {
                key: "join",
                value: function(e) {
                    if (0 === this.length)
                        return "";
                    for (var t = this.head, n = "" + t.data; t = t.next; )
                        n += e + t.data;
                    return n
                }
            }, {
                key: "concat",
                value: function(e) {
                    if (0 === this.length)
                        return a.alloc(0);
                    for (var t = a.allocUnsafe(e >>> 0), n = this.head, r = 0; n; )
                        c(n.data, t, r),
                        r += n.data.length,
                        n = n.next;
                    return t
                }
            }, {
                key: "consume",
                value: function(e, t) {
                    var n;
                    return e < this.head.data.length ? (n = this.head.data.slice(0, e),
                    this.head.data = this.head.data.slice(e)) : n = e === this.head.data.length ? this.shift() : t ? this._getString(e) : this._getBuffer(e),
                    n
                }
            }, {
                key: "first",
                value: function() {
                    return this.head.data
                }
            }, {
                key: "_getString",
                value: function(e) {
                    var t = this.head
                      , n = 1
                      , r = t.data;
                    for (e -= r.length; t = t.next; ) {
                        var i = t.data
                          , o = e > i.length ? i.length : e;
                        if (o === i.length ? r += i : r += i.slice(0, e),
                        0 === (e -= o)) {
                            o === i.length ? (++n,
                            t.next ? this.head = t.next : this.head = this.tail = null) : (this.head = t,
                            t.data = i.slice(o));
                            break
                        }
                        ++n
                    }
                    return this.length -= n,
                    r
                }
            }, {
                key: "_getBuffer",
                value: function(e) {
                    var t = a.allocUnsafe(e)
                      , n = this.head
                      , r = 1;
                    for (n.data.copy(t),
                    e -= n.data.length; n = n.next; ) {
                        var i = n.data
                          , o = e > i.length ? i.length : e;
                        if (i.copy(t, t.length - e, 0, o),
                        0 === (e -= o)) {
                            o === i.length ? (++r,
                            n.next ? this.head = n.next : this.head = this.tail = null) : (this.head = n,
                            n.data = i.slice(o));
                            break
                        }
                        ++r
                    }
                    return this.length -= r,
                    t
                }
            }, {
                key: u,
                value: function(e, t) {
                    return s(this, function(e) {
                        for (var t = 1; t < arguments.length; t++) {
                            var n = null != arguments[t] ? arguments[t] : {};
                            t % 2 ? r(Object(n), !0).forEach((function(t) {
                                i(e, t, n[t])
                            }
                            )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(n)) : r(Object(n)).forEach((function(t) {
                                Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(n, t))
                            }
                            ))
                        }
                        return e
                    }({}, t, {
                        depth: 0,
                        customInspect: !1
                    }))
                }
            }]),
            e
        }()
    },
    3: function(e, t) {},
    4: function(e, t) {},
    4681: function(e, t, n) {
        "use strict";
        (function(t) {
            function n(e, t) {
                i(e, t),
                r(e)
            }
            function r(e) {
                e._writableState && !e._writableState.emitClose || e._readableState && !e._readableState.emitClose || e.emit("close")
            }
            function i(e, t) {
                e.emit("error", t)
            }
            e.exports = {
                destroy: function(e, o) {
                    var a = this
                      , s = this._readableState && this._readableState.destroyed
                      , u = this._writableState && this._writableState.destroyed;
                    return s || u ? (o ? o(e) : e && (this._writableState ? this._writableState.errorEmitted || (this._writableState.errorEmitted = !0,
                    t.nextTick(i, this, e)) : t.nextTick(i, this, e)),
                    this) : (this._readableState && (this._readableState.destroyed = !0),
                    this._writableState && (this._writableState.destroyed = !0),
                    this._destroy(e || null, (function(e) {
                        !o && e ? a._writableState ? a._writableState.errorEmitted ? t.nextTick(r, a) : (a._writableState.errorEmitted = !0,
                        t.nextTick(n, a, e)) : t.nextTick(n, a, e) : o ? (t.nextTick(r, a),
                        o(e)) : t.nextTick(r, a)
                    }
                    )),
                    this)
                },
                undestroy: function() {
                    this._readableState && (this._readableState.destroyed = !1,
                    this._readableState.reading = !1,
                    this._readableState.ended = !1,
                    this._readableState.endEmitted = !1),
                    this._writableState && (this._writableState.destroyed = !1,
                    this._writableState.ended = !1,
                    this._writableState.ending = !1,
                    this._writableState.finalCalled = !1,
                    this._writableState.prefinished = !1,
                    this._writableState.finished = !1,
                    this._writableState.errorEmitted = !1)
                },
                errorOrDestroy: function(e, t) {
                    var n = e._readableState
                      , r = e._writableState;
                    n && n.autoDestroy || r && r.autoDestroy ? e.destroy(t) : e.emit("error", t)
                }
            }
        }
        ).call(this, n("f28c"))
    },
    "0db6": function(e, t, n) {
        "use strict";
        var r = n("c9b8").codes.ERR_INVALID_OPT_VALUE;
        e.exports = {
            getHighWaterMark: function(e, t, n, i) {
                var o = function(e, t, n) {
                    return null != e.highWaterMark ? e.highWaterMark : t ? e[n] : null
                }(t, i, n);
                if (null != o) {
                    if (!isFinite(o) || Math.floor(o) !== o || o < 0)
                        throw new r(i ? n : "highWaterMark",o);
                    return Math.floor(o)
                }
                return e.objectMode ? 16 : 16384
            }
        }
    },
    c9b8: function(e, t, n) {
        "use strict";
        var r = {};
        function i(e, t, n) {
            function i(e, n, r) {
                return "string" == typeof t ? t : t(e, n, r)
            }
            n || (n = Error);
            var o = function(e) {
                function t(t, n, r) {
                    return e.call(this, i(t, n, r)) || this
                }
                return function(e, t) {
                    e.prototype = Object.create(t.prototype),
                    e.prototype.constructor = e,
                    e.__proto__ = t
                }(t, e),
                t
            }(n);
            o.prototype.name = n.name,
            o.prototype.code = e,
            r[e] = o
        }
        function o(e, t) {
            if (Array.isArray(e)) {
                var n = e.length;
                return e = e.map((function(e) {
                    return String(e)
                }
                )),
                n > 2 ? "one of ".concat(t, " ").concat(e.slice(0, n - 1).join(", "), ", or ") + e[n - 1] : 2 === n ? "one of ".concat(t, " ").concat(e[0], " or ").concat(e[1]) : "of ".concat(t, " ").concat(e[0])
            }
            return "of ".concat(t, " ").concat(String(e))
        }
        i("ERR_INVALID_OPT_VALUE", (function(e, t) {
            return 'The value "' + t + '" is invalid for option "' + e + '"'
        }
        ), TypeError),
        i("ERR_INVALID_ARG_TYPE", (function(e, t, n) {
            var r, i;
            if ("string" == typeof t && function(e, t, n) {
                return e.substr(!n || n < 0 ? 0 : +n, t.length) === t
            }(t, "not ") ? (r = "must not be",
            t = t.replace(/^not /, "")) : r = "must be",
            function(e, t, n) {
                return (void 0 === n || n > e.length) && (n = e.length),
                e.substring(n - t.length, n) === t
            }(e, " argument"))
                i = "The ".concat(e, " ").concat(r, " ").concat(o(t, "type"));
            else {
                var a = function(e, t, n) {
                    return "number" != typeof n && (n = 0),
                    !(n + t.length > e.length) && -1 !== e.indexOf(t, n)
                }(e, ".") ? "property" : "argument";
                i = 'The "'.concat(e, '" ').concat(a, " ").concat(r, " ").concat(o(t, "type"))
            }
            return i += ". Received type ".concat(typeof n)
        }
        ), TypeError),
        i("ERR_STREAM_PUSH_AFTER_EOF", "stream.push() after EOF"),
        i("ERR_METHOD_NOT_IMPLEMENTED", (function(e) {
            return "The " + e + " method is not implemented"
        }
        )),
        i("ERR_STREAM_PREMATURE_CLOSE", "Premature close"),
        i("ERR_STREAM_DESTROYED", (function(e) {
            return "Cannot call " + e + " after a stream was destroyed"
        }
        )),
        i("ERR_MULTIPLE_CALLBACK", "Callback called multiple times"),
        i("ERR_STREAM_CANNOT_PIPE", "Cannot pipe, not readable"),
        i("ERR_STREAM_WRITE_AFTER_END", "write after end"),
        i("ERR_STREAM_NULL_VALUES", "May not write null values to stream", TypeError),
        i("ERR_UNKNOWN_ENCODING", (function(e) {
            return "Unknown encoding: " + e
        }
        ), TypeError),
        i("ERR_STREAM_UNSHIFT_AFTER_END_EVENT", "stream.unshift() after end event"),
        e.exports.codes = r
    },
    dc14: function(e, t, n) {
        "use strict";
        (function(t, r) {
            function i(e) {
                var t = this;
                this.next = null,
                this.entry = null,
                this.finish = function() {
                    !function(e, t, n) {
                        var r = e.entry;
                        e.entry = null;
                        for (; r; ) {
                            var i = r.callback;
                            t.pendingcb--,
                            i(n),
                            r = r.next
                        }
                        t.corkedRequestsFree.next = e
                    }(t, e)
                }
            }
            var o;
            e.exports = T,
            T.WritableState = x;
            var a = {
                deprecate: n("b7d1")
            }
              , s = n("429b")
              , u = n("b639").Buffer
              , c = t.Uint8Array || function() {}
            ;
            var l, f = n("4681"), d = n("0db6").getHighWaterMark, h = n("c9b8").codes, p = h.ERR_INVALID_ARG_TYPE, v = h.ERR_METHOD_NOT_IMPLEMENTED, g = h.ERR_MULTIPLE_CALLBACK, y = h.ERR_STREAM_CANNOT_PIPE, m = h.ERR_STREAM_DESTROYED, b = h.ERR_STREAM_NULL_VALUES, w = h.ERR_STREAM_WRITE_AFTER_END, _ = h.ERR_UNKNOWN_ENCODING, S = f.errorOrDestroy;
            function E() {}
            function x(e, t, r) {
                o = o || n("b19a"),
                e = e || {},
                "boolean" != typeof r && (r = t instanceof o),
                this.objectMode = !!e.objectMode,
                r && (this.objectMode = this.objectMode || !!e.writableObjectMode),
                this.highWaterMark = d(this, e, "writableHighWaterMark", r),
                this.finalCalled = !1,
                this.needDrain = !1,
                this.ending = !1,
                this.ended = !1,
                this.finished = !1,
                this.destroyed = !1;
                var a = !1 === e.decodeStrings;
                this.decodeStrings = !a,
                this.defaultEncoding = e.defaultEncoding || "utf8",
                this.length = 0,
                this.writing = !1,
                this.corked = 0,
                this.sync = !0,
                this.bufferProcessing = !1,
                this.onwrite = function(e) {
                    P(t, e)
                }
                ,
                this.writecb = null,
                this.writelen = 0,
                this.bufferedRequest = null,
                this.lastBufferedRequest = null,
                this.pendingcb = 0,
                this.prefinished = !1,
                this.errorEmitted = !1,
                this.emitClose = !1 !== e.emitClose,
                this.autoDestroy = !!e.autoDestroy,
                this.bufferedRequestCount = 0,
                this.corkedRequestsFree = new i(this)
            }
            function T(e) {
                var t = this instanceof (o = o || n("b19a"));
                if (!t && !l.call(T, this))
                    return new T(e);
                this._writableState = new x(e,this,t),
                this.writable = !0,
                e && ("function" == typeof e.write && (this._write = e.write),
                "function" == typeof e.writev && (this._writev = e.writev),
                "function" == typeof e.destroy && (this._destroy = e.destroy),
                "function" == typeof e.final && (this._final = e.final)),
                s.call(this)
            }
            function O(e, t) {
                var n = new w;
                S(e, n),
                r.nextTick(t, n)
            }
            function k(e, t, n, i) {
                var o;
                return null === n ? o = new b : "string" == typeof n || t.objectMode || (o = new p("chunk",["string", "Buffer"],n)),
                !o || (S(e, o),
                r.nextTick(i, o),
                !1)
            }
            function A(e, t, n) {
                return e.objectMode || !1 === e.decodeStrings || "string" != typeof t || (t = u.from(t, n)),
                t
            }
            function C(e, t, n, r, i, o, a) {
                t.writelen = r,
                t.writecb = a,
                t.writing = !0,
                t.sync = !0,
                t.destroyed ? t.onwrite(new m("write")) : n ? e._writev(i, t.onwrite) : e._write(i, o, t.onwrite),
                t.sync = !1
            }
            function P(e, t) {
                var n = e._writableState
                  , i = n.sync
                  , o = n.writecb;
                if ("function" != typeof o)
                    throw new g;
                if (function(e) {
                    e.writing = !1,
                    e.writecb = null,
                    e.length -= e.writelen,
                    e.writelen = 0
                }(n),
                t)
                    !function(e, t, n, i, o) {
                        --t.pendingcb,
                        n ? (r.nextTick(o, i),
                        r.nextTick(B, e, t),
                        e._writableState.errorEmitted = !0,
                        S(e, i)) : (o(i),
                        e._writableState.errorEmitted = !0,
                        S(e, i),
                        B(e, t))
                    }(e, n, i, t, o);
                else {
                    var a = I(n) || e.destroyed;
                    a || n.corked || n.bufferProcessing || !n.bufferedRequest || L(e, n),
                    i ? r.nextTick(M, e, n, a, o) : M(e, n, a, o)
                }
            }
            function M(e, t, n, r) {
                n || function(e, t) {
                    0 === t.length && t.needDrain && (t.needDrain = !1,
                    e.emit("drain"))
                }(e, t),
                t.pendingcb--,
                r(),
                B(e, t)
            }
            function L(e, t) {
                t.bufferProcessing = !0;
                var n = t.bufferedRequest;
                if (e._writev && n && n.next) {
                    var r = t.bufferedRequestCount
                      , o = new Array(r)
                      , a = t.corkedRequestsFree;
                    a.entry = n;
                    for (var s = 0, u = !0; n; )
                        o[s] = n,
                        n.isBuf || (u = !1),
                        n = n.next,
                        s += 1;
                    o.allBuffers = u,
                    C(e, t, !0, t.length, o, "", a.finish),
                    t.pendingcb++,
                    t.lastBufferedRequest = null,
                    a.next ? (t.corkedRequestsFree = a.next,
                    a.next = null) : t.corkedRequestsFree = new i(t),
                    t.bufferedRequestCount = 0
                } else {
                    for (; n; ) {
                        var c = n.chunk
                          , l = n.encoding
                          , f = n.callback;
                        if (C(e, t, !1, t.objectMode ? 1 : c.length, c, l, f),
                        n = n.next,
                        t.bufferedRequestCount--,
                        t.writing)
                            break
                    }
                    null === n && (t.lastBufferedRequest = null)
                }
                t.bufferedRequest = n,
                t.bufferProcessing = !1
            }
            function I(e) {
                return e.ending && 0 === e.length && null === e.bufferedRequest && !e.finished && !e.writing
            }
            function R(e, t) {
                e._final((function(n) {
                    t.pendingcb--,
                    n && S(e, n),
                    t.prefinished = !0,
                    e.emit("prefinish"),
                    B(e, t)
                }
                ))
            }
            function j(e, t) {
                t.prefinished || t.finalCalled || ("function" != typeof e._final || t.destroyed ? (t.prefinished = !0,
                e.emit("prefinish")) : (t.pendingcb++,
                t.finalCalled = !0,
                r.nextTick(R, e, t)))
            }
            function B(e, t) {
                var n = I(t);
                if (n && (j(e, t),
                0 === t.pendingcb && (t.finished = !0,
                e.emit("finish"),
                t.autoDestroy))) {
                    var r = e._readableState;
                    (!r || r.autoDestroy && r.endEmitted) && e.destroy()
                }
                return n
            }
            function N(e, t, n) {
                t.ending = !0,
                B(e, t),
                n && (t.finished ? r.nextTick(n) : e.once("finish", n)),
                t.ended = !0,
                e.writable = !1
            }
            n("3fb5")(T, s),
            x.prototype.getBuffer = function() {
                for (var e = this.bufferedRequest, t = []; e; )
                    t.push(e),
                    e = e.next;
                return t
            }
            ,
            function() {
                try {
                    Object.defineProperty(x.prototype, "buffer", {
                        get: a.deprecate((function() {
                            return this.getBuffer()
                        }
                        ), "_writableState.buffer is deprecated. Use _writableState.getBuffer instead.", "DEP0003")
                    })
                } catch (e) {}
            }(),
            "function" == typeof Symbol && Symbol.hasInstance && "function" == typeof Function.prototype[Symbol.hasInstance] ? (l = Function.prototype[Symbol.hasInstance],
            Object.defineProperty(T, Symbol.hasInstance, {
                value: function(e) {
                    return !!l.call(this, e) || this === T && e && e._writableState instanceof x
                }
            })) : l = function(e) {
                return e instanceof this
            }
            ,
            T.prototype.pipe = function() {
                S(this, new y)
            }
            ,
            T.prototype.write = function(e, t, n) {
                var r = this._writableState
                  , i = !1
                  , o = !r.objectMode && function(e) {
                    return u.isBuffer(e) || e instanceof c
                }(e);
                return o && !u.isBuffer(e) && (e = function(e) {
                    return u.from(e)
                }(e)),
                "function" == typeof t && (n = t,
                t = null),
                o ? t = "buffer" : t || (t = r.defaultEncoding),
                "function" != typeof n && (n = E),
                r.ending ? O(this, n) : (o || k(this, r, e, n)) && (r.pendingcb++,
                i = function(e, t, n, r, i, o) {
                    if (!n) {
                        var a = A(t, r, i);
                        r !== a && (n = !0,
                        i = "buffer",
                        r = a)
                    }
                    var s = t.objectMode ? 1 : r.length;
                    t.length += s;
                    var u = t.length < t.highWaterMark;
                    if (u || (t.needDrain = !0),
                    t.writing || t.corked) {
                        var c = t.lastBufferedRequest;
                        t.lastBufferedRequest = {
                            chunk: r,
                            encoding: i,
                            isBuf: n,
                            callback: o,
                            next: null
                        },
                        c ? c.next = t.lastBufferedRequest : t.bufferedRequest = t.lastBufferedRequest,
                        t.bufferedRequestCount += 1
                    } else
                        C(e, t, !1, s, r, i, o);
                    return u
                }(this, r, o, e, t, n)),
                i
            }
            ,
            T.prototype.cork = function() {
                this._writableState.corked++
            }
            ,
            T.prototype.uncork = function() {
                var e = this._writableState;
                e.corked && (e.corked--,
                e.writing || e.corked || e.bufferProcessing || !e.bufferedRequest || L(this, e))
            }
            ,
            T.prototype.setDefaultEncoding = function(e) {
                if ("string" == typeof e && (e = e.toLowerCase()),
                !(["hex", "utf8", "utf-8", "ascii", "binary", "base64", "ucs2", "ucs-2", "utf16le", "utf-16le", "raw"].indexOf((e + "").toLowerCase()) > -1))
                    throw new _(e);
                return this._writableState.defaultEncoding = e,
                this
            }
            ,
            Object.defineProperty(T.prototype, "writableBuffer", {
                enumerable: !1,
                get: function() {
                    return this._writableState && this._writableState.getBuffer()
                }
            }),
            Object.defineProperty(T.prototype, "writableHighWaterMark", {
                enumerable: !1,
                get: function() {
                    return this._writableState.highWaterMark
                }
            }),
            T.prototype._write = function(e, t, n) {
                n(new v("_write()"))
            }
            ,
            T.prototype._writev = null,
            T.prototype.end = function(e, t, n) {
                var r = this._writableState;
                return "function" == typeof e ? (n = e,
                e = null,
                t = null) : "function" == typeof t && (n = t,
                t = null),
                null != e && this.write(e, t),
                r.corked && (r.corked = 1,
                this.uncork()),
                r.ending || N(this, r, n),
                this
            }
            ,
            Object.defineProperty(T.prototype, "writableLength", {
                enumerable: !1,
                get: function() {
                    return this._writableState.length
                }
            }),
            Object.defineProperty(T.prototype, "destroyed", {
                enumerable: !1,
                get: function() {
                    return void 0 !== this._writableState && this._writableState.destroyed
                },
                set: function(e) {
                    this._writableState && (this._writableState.destroyed = e)
                }
            }),
            T.prototype.destroy = f.destroy,
            T.prototype._undestroy = f.undestroy,
            T.prototype._destroy = function(e, t) {
                t(e)
            }
        }
        ).call(this, n("c8ba"), n("f28c"))
    },
    b19a: function(e, t, n) {
        "use strict";
        (function(t) {
            var r = Object.keys || function(e) {
                var t = [];
                for (var n in e)
                    t.push(n);
                return t
            }
            ;
            e.exports = c;
            var i = n("ad71")
              , o = n("dc14");
            n("3fb5")(c, i);
            for (var a = r(o.prototype), s = 0; s < a.length; s++) {
                var u = a[s];
                c.prototype[u] || (c.prototype[u] = o.prototype[u])
            }
            function c(e) {
                if (!(this instanceof c))
                    return new c(e);
                i.call(this, e),
                o.call(this, e),
                this.allowHalfOpen = !0,
                e && (!1 === e.readable && (this.readable = !1),
                !1 === e.writable && (this.writable = !1),
                !1 === e.allowHalfOpen && (this.allowHalfOpen = !1,
                this.once("end", l)))
            }
            function l() {
                this._writableState.ended || t.nextTick(f, this)
            }
            function f(e) {
                e.end()
            }
            Object.defineProperty(c.prototype, "writableHighWaterMark", {
                enumerable: !1,
                get: function() {
                    return this._writableState.highWaterMark
                }
            }),
            Object.defineProperty(c.prototype, "writableBuffer", {
                enumerable: !1,
                get: function() {
                    return this._writableState && this._writableState.getBuffer()
                }
            }),
            Object.defineProperty(c.prototype, "writableLength", {
                enumerable: !1,
                get: function() {
                    return this._writableState.length
                }
            }),
            Object.defineProperty(c.prototype, "destroyed", {
                enumerable: !1,
                get: function() {
                    return void 0 !== this._readableState && void 0 !== this._writableState && this._readableState.destroyed && this._writableState.destroyed
                },
                set: function(e) {
                    void 0 !== this._readableState && void 0 !== this._writableState && (this._readableState.destroyed = e,
                    this._writableState.destroyed = e)
                }
            })
        }
        ).call(this, n("f28c"))
    },
    "27bf": function(e, t, n) {
        "use strict";
        e.exports = l;
        var r = n("c9b8").codes
          , i = r.ERR_METHOD_NOT_IMPLEMENTED
          , o = r.ERR_MULTIPLE_CALLBACK
          , a = r.ERR_TRANSFORM_ALREADY_TRANSFORMING
          , s = r.ERR_TRANSFORM_WITH_LENGTH_0
          , u = n("b19a");
        function c(e, t) {
            var n = this._transformState;
            n.transforming = !1;
            var r = n.writecb;
            if (null === r)
                return this.emit("error", new o);
            n.writechunk = null,
            n.writecb = null,
            null != t && this.push(t),
            r(e);
            var i = this._readableState;
            i.reading = !1,
            (i.needReadable || i.length < i.highWaterMark) && this._read(i.highWaterMark)
        }
        function l(e) {
            if (!(this instanceof l))
                return new l(e);
            u.call(this, e),
            this._transformState = {
                afterTransform: c.bind(this),
                needTransform: !1,
                transforming: !1,
                writecb: null,
                writechunk: null,
                writeencoding: null
            },
            this._readableState.needReadable = !0,
            this._readableState.sync = !1,
            e && ("function" == typeof e.transform && (this._transform = e.transform),
            "function" == typeof e.flush && (this._flush = e.flush)),
            this.on("prefinish", f)
        }
        function f() {
            var e = this;
            "function" != typeof this._flush || this._readableState.destroyed ? d(this, null, null) : this._flush((function(t, n) {
                d(e, t, n)
            }
            ))
        }
        function d(e, t, n) {
            if (t)
                return e.emit("error", t);
            if (null != n && e.push(n),
            e._writableState.length)
                throw new s;
            if (e._transformState.transforming)
                throw new a;
            return e.push(null)
        }
        n("3fb5")(l, u),
        l.prototype.push = function(e, t) {
            return this._transformState.needTransform = !1,
            u.prototype.push.call(this, e, t)
        }
        ,
        l.prototype._transform = function(e, t, n) {
            n(new i("_transform()"))
        }
        ,
        l.prototype._write = function(e, t, n) {
            var r = this._transformState;
            if (r.writecb = n,
            r.writechunk = e,
            r.writeencoding = t,
            !r.transforming) {
                var i = this._readableState;
                (r.needTransform || i.needReadable || i.length < i.highWaterMark) && this._read(i.highWaterMark)
            }
        }
        ,
        l.prototype._read = function(e) {
            var t = this._transformState;
            null === t.writechunk || t.transforming ? t.needTransform = !0 : (t.transforming = !0,
            this._transform(t.writechunk, t.writeencoding, t.afterTransform))
        }
        ,
        l.prototype._destroy = function(e, t) {
            u.prototype._destroy.call(this, e, (function(e) {
                t(e)
            }
            ))
        }
    },
    "780f": function(e, t, n) {
        "use strict";
        e.exports = i;
        var r = n("27bf");
        function i(e) {
            if (!(this instanceof i))
                return new i(e);
            r.call(this, e)
        }
        n("3fb5")(i, r),
        i.prototype._transform = function(e, t, n) {
            n(null, e)
        }
    },
    "903c": function(e, t, n) {
        "use strict";
        var r = n("c9b8").codes.ERR_STREAM_PREMATURE_CLOSE;
        function i() {}
        e.exports = function e(t, n, o) {
            if ("function" == typeof n)
                return e(t, null, n);
            n || (n = {}),
            o = function(e) {
                var t = !1;
                return function() {
                    if (!t) {
                        t = !0;
                        for (var n = arguments.length, r = new Array(n), i = 0; i < n; i++)
                            r[i] = arguments[i];
                        e.apply(this, r)
                    }
                }
            }(o || i);
            var a = n.readable || !1 !== n.readable && t.readable
              , s = n.writable || !1 !== n.writable && t.writable
              , u = function() {
                t.writable || l()
            }
              , c = t._writableState && t._writableState.finished
              , l = function() {
                s = !1,
                c = !0,
                a || o.call(t)
            }
              , f = t._readableState && t._readableState.endEmitted
              , d = function() {
                a = !1,
                f = !0,
                s || o.call(t)
            }
              , h = function(e) {
                o.call(t, e)
            }
              , p = function() {
                var e;
                return a && !f ? (t._readableState && t._readableState.ended || (e = new r),
                o.call(t, e)) : s && !c ? (t._writableState && t._writableState.ended || (e = new r),
                o.call(t, e)) : void 0
            }
              , v = function() {
                t.req.on("finish", l)
            };
            return function(e) {
                return e.setHeader && "function" == typeof e.abort
            }(t) ? (t.on("complete", l),
            t.on("abort", p),
            t.req ? v() : t.on("request", v)) : s && !t._writableState && (t.on("end", u),
            t.on("close", u)),
            t.on("end", d),
            t.on("finish", l),
            !1 !== n.error && t.on("error", h),
            t.on("close", p),
            function() {
                t.removeListener("complete", l),
                t.removeListener("abort", p),
                t.removeListener("request", v),
                t.req && t.req.removeListener("finish", l),
                t.removeListener("end", u),
                t.removeListener("close", u),
                t.removeListener("finish", l),
                t.removeListener("end", d),
                t.removeListener("error", h),
                t.removeListener("close", p)
            }
        }
    },
    "5d1c": function(e, t, n) {
        "use strict";
        var r;
        var i = n("c9b8").codes
          , o = i.ERR_MISSING_ARGS
          , a = i.ERR_STREAM_DESTROYED;
        function s(e) {
            if (e)
                throw e
        }
        function u(e, t, i, o) {
            o = function(e) {
                var t = !1;
                return function() {
                    t || (t = !0,
                    e.apply(void 0, arguments))
                }
            }(o);
            var s = !1;
            e.on("close", (function() {
                s = !0
            }
            )),
            void 0 === r && (r = n("903c")),
            r(e, {
                readable: t,
                writable: i
            }, (function(e) {
                if (e)
                    return o(e);
                s = !0,
                o()
            }
            ));
            var u = !1;
            return function(t) {
                if (!s && !u)
                    return u = !0,
                    function(e) {
                        return e.setHeader && "function" == typeof e.abort
                    }(e) ? e.abort() : "function" == typeof e.destroy ? e.destroy() : void o(t || new a("pipe"))
            }
        }
        function c(e) {
            e()
        }
        function l(e, t) {
            return e.pipe(t)
        }
        function f(e) {
            return e.length ? "function" != typeof e[e.length - 1] ? s : e.pop() : s
        }
        e.exports = function() {
            for (var e = arguments.length, t = new Array(e), n = 0; n < e; n++)
                t[n] = arguments[n];
            var r, i = f(t);
            if (Array.isArray(t[0]) && (t = t[0]),
            t.length < 2)
                throw new o("streams");
            var a = t.map((function(e, n) {
                var o = n < t.length - 1;
                return u(e, o, n > 0, (function(e) {
                    r || (r = e),
                    e && a.forEach(c),
                    o || (a.forEach(c),
                    i(r))
                }
                ))
            }
            ));
            return t.reduce(l)
        }
    },
    b5ca: function(e, t, n) {
        "use strict";
        var r = n("b639").Buffer
          , i = n("3fb5")
          , o = n("93e6")
          , a = new Array(16)
          , s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 7, 4, 13, 1, 10, 6, 15, 3, 12, 0, 9, 5, 2, 14, 11, 8, 3, 10, 14, 4, 9, 15, 8, 1, 2, 7, 0, 6, 13, 11, 5, 12, 1, 9, 11, 10, 0, 8, 12, 4, 13, 3, 7, 15, 14, 5, 6, 2, 4, 0, 5, 9, 7, 12, 2, 10, 14, 1, 3, 8, 11, 6, 15, 13]
          , u = [5, 14, 7, 0, 9, 2, 11, 4, 13, 6, 15, 8, 1, 10, 3, 12, 6, 11, 3, 7, 0, 13, 5, 10, 14, 15, 8, 12, 4, 9, 1, 2, 15, 5, 1, 3, 7, 14, 6, 9, 11, 8, 12, 2, 10, 0, 4, 13, 8, 6, 4, 1, 3, 11, 15, 0, 5, 12, 2, 13, 9, 7, 10, 14, 12, 15, 10, 4, 1, 5, 8, 7, 6, 2, 13, 14, 0, 3, 9, 11]
          , c = [11, 14, 15, 12, 5, 8, 7, 9, 11, 13, 14, 15, 6, 7, 9, 8, 7, 6, 8, 13, 11, 9, 7, 15, 7, 12, 15, 9, 11, 7, 13, 12, 11, 13, 6, 7, 14, 9, 13, 15, 14, 8, 13, 6, 5, 12, 7, 5, 11, 12, 14, 15, 14, 15, 9, 8, 9, 14, 5, 6, 8, 6, 5, 12, 9, 15, 5, 11, 6, 8, 13, 12, 5, 12, 13, 14, 11, 8, 5, 6]
          , l = [8, 9, 9, 11, 13, 15, 15, 5, 7, 7, 8, 11, 14, 14, 12, 6, 9, 13, 15, 7, 12, 8, 9, 11, 7, 7, 12, 7, 6, 15, 13, 11, 9, 7, 15, 11, 8, 6, 6, 14, 12, 13, 5, 14, 13, 13, 7, 5, 15, 5, 8, 11, 14, 14, 6, 14, 6, 9, 12, 9, 12, 5, 15, 8, 8, 5, 12, 9, 12, 5, 14, 6, 8, 13, 6, 5, 15, 13, 11, 11]
          , f = [0, 1518500249, 1859775393, 2400959708, 2840853838]
          , d = [1352829926, 1548603684, 1836072691, 2053994217, 0];
        function h() {
            o.call(this, 64),
            this._a = 1732584193,
            this._b = 4023233417,
            this._c = 2562383102,
            this._d = 271733878,
            this._e = 3285377520
        }
        function p(e, t) {
            return e << t | e >>> 32 - t
        }
        function v(e, t, n, r, i, o, a, s) {
            return p(e + (t ^ n ^ r) + o + a | 0, s) + i | 0
        }
        function g(e, t, n, r, i, o, a, s) {
            return p(e + (t & n | ~t & r) + o + a | 0, s) + i | 0
        }
        function y(e, t, n, r, i, o, a, s) {
            return p(e + ((t | ~n) ^ r) + o + a | 0, s) + i | 0
        }
        function m(e, t, n, r, i, o, a, s) {
            return p(e + (t & r | n & ~r) + o + a | 0, s) + i | 0
        }
        function b(e, t, n, r, i, o, a, s) {
            return p(e + (t ^ (n | ~r)) + o + a | 0, s) + i | 0
        }
        i(h, o),
        h.prototype._update = function() {
            for (var e = a, t = 0; t < 16; ++t)
                e[t] = this._block.readInt32LE(4 * t);
            for (var n = 0 | this._a, r = 0 | this._b, i = 0 | this._c, o = 0 | this._d, h = 0 | this._e, w = 0 | this._a, _ = 0 | this._b, S = 0 | this._c, E = 0 | this._d, x = 0 | this._e, T = 0; T < 80; T += 1) {
                var O, k;
                T < 16 ? (O = v(n, r, i, o, h, e[s[T]], f[0], c[T]),
                k = b(w, _, S, E, x, e[u[T]], d[0], l[T])) : T < 32 ? (O = g(n, r, i, o, h, e[s[T]], f[1], c[T]),
                k = m(w, _, S, E, x, e[u[T]], d[1], l[T])) : T < 48 ? (O = y(n, r, i, o, h, e[s[T]], f[2], c[T]),
                k = y(w, _, S, E, x, e[u[T]], d[2], l[T])) : T < 64 ? (O = m(n, r, i, o, h, e[s[T]], f[3], c[T]),
                k = g(w, _, S, E, x, e[u[T]], d[3], l[T])) : (O = b(n, r, i, o, h, e[s[T]], f[4], c[T]),
                k = v(w, _, S, E, x, e[u[T]], d[4], l[T])),
                n = h,
                h = o,
                o = p(i, 10),
                i = r,
                r = O,
                w = x,
                x = E,
                E = p(S, 10),
                S = _,
                _ = k
            }
            var A = this._b + i + E | 0;
            this._b = this._c + o + x | 0,
            this._c = this._d + h + w | 0,
            this._d = this._e + n + _ | 0,
            this._e = this._a + r + S | 0,
            this._a = A
        }
        ,
        h.prototype._digest = function() {
            this._block[this._blockOffset++] = 128,
            this._blockOffset > 56 && (this._block.fill(0, this._blockOffset, 64),
            this._update(),
            this._blockOffset = 0),
            this._block.fill(0, this._blockOffset, 56),
            this._block.writeUInt32LE(this._length[0], 56),
            this._block.writeUInt32LE(this._length[1], 60),
            this._update();
            var e = r.alloc ? r.alloc(20) : new r(20);
            return e.writeInt32LE(this._a, 0),
            e.writeInt32LE(this._b, 4),
            e.writeInt32LE(this._c, 8),
            e.writeInt32LE(this._d, 12),
            e.writeInt32LE(this._e, 16),
            e
        }
        ,
        e.exports = h
    },
    "69f2": function(e, t, n) {
        t = e.exports = function(e) {
            e = e.toLowerCase();
            var n = t[e];
            if (!n)
                throw new Error(e + " is not supported (we accept pull requests)");
            return new n
        }
        ,
        t.sha1 = n("7e78")
    },
    "7e78": function(e, t, n) {
        var r = n("3fb5")
          , i = n("b672")
          , o = n("8707").Buffer
          , a = [1518500249, 1859775393, -1894007588, -899497514]
          , s = new Array(80);
        function u() {
            this.init(),
            this._w = s,
            i.call(this, 64, 56)
        }
        function c(e) {
            return e << 1 | e >>> 31
        }
        function l(e) {
            return e << 5 | e >>> 27
        }
        function f(e) {
            return e << 30 | e >>> 2
        }
        function d(e, t, n, r) {
            return 0 === e ? t & n | ~t & r : 2 === e ? t & n | t & r | n & r : t ^ n ^ r
        }
        r(u, i),
        u.prototype.init = function() {
            return this._a = 1732584193,
            this._b = 4023233417,
            this._c = 2562383102,
            this._d = 271733878,
            this._e = 3285377520,
            this
        }
        ,
        u.prototype._update = function(e) {
            for (var t = this._w, n = 0 | this._a, r = 0 | this._b, i = 0 | this._c, o = 0 | this._d, s = 0 | this._e, u = 0; u < 16; ++u)
                t[u] = e.readInt32BE(4 * u);
            for (; u < 80; ++u)
                t[u] = c(t[u - 3] ^ t[u - 8] ^ t[u - 14] ^ t[u - 16]);
            for (var h = 0; h < 80; ++h) {
                var p = ~~(h / 20)
                  , v = l(n) + d(p, r, i, o) + s + t[h] + a[p] | 0;
                s = o,
                o = i,
                i = f(r),
                r = n,
                n = v
            }
            this._a = n + this._a | 0,
            this._b = r + this._b | 0,
            this._c = i + this._c | 0,
            this._d = o + this._d | 0,
            this._e = s + this._e | 0
        }
        ,
        u.prototype._hash = function() {
            var e = o.allocUnsafe(20);
            return e.writeInt32BE(0 | this._a, 0),
            e.writeInt32BE(0 | this._b, 4),
            e.writeInt32BE(0 | this._c, 8),
            e.writeInt32BE(0 | this._d, 12),
            e.writeInt32BE(0 | this._e, 16),
            e
        }
        ,
        e.exports = u
    },
    b672: function(e, t, n) {
        var r = n("8707").Buffer;
        function i(e, t) {
            this._block = r.alloc(e),
            this._finalSize = t,
            this._blockSize = e,
            this._len = 0
        }
        i.prototype.update = function(e, t) {
            "string" == typeof e && (t = t || "utf8",
            e = r.from(e, t));
            for (var n = this._block, i = this._blockSize, o = e.length, a = this._len, s = 0; s < o; ) {
                for (var u = a % i, c = Math.min(o - s, i - u), l = 0; l < c; l++)
                    n[u + l] = e[s + l];
                s += c,
                (a += c) % i == 0 && this._update(n)
            }
            return this._len += o,
            this
        }
        ,
        i.prototype.digest = function(e) {
            var t = this._len % this._blockSize;
            this._block[t] = 128,
            this._block.fill(0, t + 1),
            t >= this._finalSize && (this._update(this._block),
            this._block.fill(0));
            var n = 8 * this._len;
            if (n <= 4294967295)
                this._block.writeUInt32BE(n, this._blockSize - 4);
            else {
                var r = (4294967295 & n) >>> 0
                  , i = (n - r) / 4294967296;
                this._block.writeUInt32BE(i, this._blockSize - 8),
                this._block.writeUInt32BE(r, this._blockSize - 4)
            }
            this._update(this._block);
            var o = this._hash();
            return e ? o.toString(e) : o
        }
        ,
        i.prototype._update = function() {
            throw new Error("_update must be implemented by subclass")
        }
        ,
        e.exports = i
    },
    "1a2a": function(e, t, n) {
        "use strict";
        var r = n("3fb5")
          , i = n("d424")
          , o = n("6430")
          , a = n("8707").Buffer
          , s = n("5a76")
          , u = n("b5ca")
          , c = n("69f2")
          , l = a.alloc(128);
        function f(e, t) {
            o.call(this, "digest"),
            "string" == typeof t && (t = a.from(t));
            var n = "sha512" === e || "sha384" === e ? 128 : 64;
            (this._alg = e,
            this._key = t,
            t.length > n) ? t = ("rmd160" === e ? new u : c(e)).update(t).digest() : t.length < n && (t = a.concat([t, l], n));
            for (var r = this._ipad = a.allocUnsafe(n), i = this._opad = a.allocUnsafe(n), s = 0; s < n; s++)
                r[s] = 54 ^ t[s],
                i[s] = 92 ^ t[s];
            this._hash = "rmd160" === e ? new u : c(e),
            this._hash.update(r)
        }
        r(f, o),
        f.prototype._update = function(e) {
            this._hash.update(e)
        }
        ,
        f.prototype._final = function() {
            var e = this._hash.digest();
            return ("rmd160" === this._alg ? new u : c(this._alg)).update(this._opad).update(e).digest()
        }
        ,
        e.exports = function(e, t) {
            return "rmd160" === (e = e.toLowerCase()) || "ripemd160" === e ? new f("rmd160",t) : "md5" === e ? new i(s,t) : new f(e,t)
        }
    },
});
console.log(aaa("js_encrypt").SS())
// 38VND82
function hkey() {
    return aaa("js_encrypt").SS()
}
console.log(hkey())