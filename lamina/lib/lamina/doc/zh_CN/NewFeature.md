# 1.1.0(RC)的新功能(对比上一个版本)

- 新增结构体类型以及对结构体的操作(当前的结构体可以实现dict和原型的功能，它本质上是HashMap)
    
    struct x {y=0, z=10} 结构体声明语句

    var x = {y=0, z=10} 匿名结构体声明

    x.y 获取子项表达式

    x["y"] 获取子项表达式的另一种写法

    x.y = v 设置子项表达式语句

- 修复null!=null问题

- 修复"__function_name"()问题

- 修复函数作用域问题（之前在任何作用域定义的函数都会跑到全局作用域， 现在在局部定义的函数，只会在局部作用域中）

- 修复函数调用问题，现在是先找局部变量表，再找builtins表

- OOP支持

    结构体通过设置__parent__属性实现单继承

    结构体通过new(src_struct)函数实现创造新对象(实际上是设置新对象的__parent__属性为src_struct结构体)

    self变量: 在x.m() 调用成员函数时自动注入函数局部变量表

- 错误处理

    xpcall(f, handle, arg1, arg2 ... ) 函数

- 新增匿名函数

    do 表达式

    |p| expr 表达式

- 新增模块系统

    include path语句

    module::sub 表达式

- 新增数组取子项语句

    arr[index]

- 重构Parser

- 重构C++ModuleLoader, 现在可以支持C++扩展

- if/while语句可以省略圆括号

- 定义无参函数可以省略圆括号

- 续行功能

- 结构体深拷贝(copy_struct函数

- 部分内置函数移动到标准库/内置库

- 新内置函数

    foreach

    map

    find

    typeof

    copy_struct

    exit

    vars

    locals

    globals

    new

    xpcall

    same

    random::random

    system

    assert

    range

    update

    setattr

    getattr

    to_string

- repl可以直接计算表达式(如1+1而不需要print(1+1))

- repl高亮关键字及自动补齐