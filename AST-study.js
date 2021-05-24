// parser生成AST树
const parser = require("@babel/parser");
// traverse遍历操作
const traverse =require("@babel/traverse");
// generator生成js代码
const generator = require("@babel/generator");
// typesAST树所有类型
const types = require("@babel/types");
var fs = require("fs")
const code = fs.readFileSync('ob_js.js', 'utf-8');
const code_1 = fs.readFileSync('md5.js', 'utf-8');
const ast = parser.parse(code);

traverse.default(ast,{
    StringLiteral:function(path) {
           delete path.node.extra.raw
          },
    BinaryExpression:function (path) {
            if (path.node.left.type === 'StringLiteral' && path.node.right.type === 'StringLiteral' && path.node.operator === '+') {
                path.replaceWithSourceString("'"+path.node.left.value + path.node.right.value+"'")
            }
    },
    MemberExpression:function (path) {
        if (path.node.property.type === 'StringLiteral' && (path.node.object.type === 'Identifier' || path.node.object.type === 'MemberExpression')){
            path.node.property = types.identifier(path.node.property.value)
            path.node.computed = false
        }
    },
    CallExpression:function (path) {
        if (path.node.callee.name === '$b'){
            path.replaceWithSourceString("'"+eval(code_1 + path.toString())+"'")
        }
    }
    })

js = generator.default(ast).code
console.log(js)