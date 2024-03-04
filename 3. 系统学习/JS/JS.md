### == 、 ===

#### 等于操作符 ==

##### 1. 原始类型和原始类型

1. 布尔类型和其他比较，会将两者都转为数值，再比较（true是1，false是0）
2. 字符串和数值比较，会将字符串转为数值（""和"0"是0，"1"是1，0开头的会忽略0，非数值会变成NaN）
3. NaN最特立独行，存在 NaN 则返回 false
4. null 和 undefined 比NaN稍微好一点，与自身和彼此都相等，和其他都是false

```
console.log(null == null && null == undefined && undefined == undefined) // true
console.log(null == false) // false 这里有点反直觉
```

##### 2. 原始类型与引用类型比较

1. 引用类型值的**valueOf()结果**和原始类型值相同就是true，否则是false

```js
// 例子1，自定义valueOf
let obj = {
  valueOf: function() {
    return 1;
  }
}
console.log(obj == 1) // true，因为obj.valueOf()的结果是1

// 例子2
console.log(new String("") == false) // true

// 例子3，有点意外
console.log([1] == 1) // true，经过尝试，单个元素的数组和该元素的 == 结果是true
```

##### 3. 引用类型与引用类型比较

1. 比较是否指向同一个对象


#### 全等操作符===

##### 1. 原始类型和原始类型

1. 必须**值和类型都相同，特别注意undefined === null是false**

##### 2. 原始类型与引用类型比较

1. **不再相等，即使引用类型值的valueOf()和原始类型值相等也不行**

##### 3. 引用类型与引用类型

1. 比较是否指向同一个对象

---

#### **适合使用\==的时候**

如果要判断一个对象是否已经被**赋值时**，我们一般使用\==和null比较（也只有这时候，才建议用\==），因为这样我们可以同时判断一个元素是否是null或undefined

```
let age = res.data.age
// 假设我们要看age这个变量是否被定义，用下面两句效果都是一样的
if(age != null) {
  ...
}
if(age !== null && age !== undefined) {
  ...
}
// 所以我们就用第一句就好了
```

注意，虽然 Boolean(null) 和 Boolean(undefined) 都是false，

但是**一定不能用 if(!age) 来判断 age 是否被赋值**，因为

在JavaScript中，Boolean(age)为false时，age变量的值可能是以下之一：

false

0

"" （空字符串）

null

undefined

NaN （非数字）

这些值在转换为布尔类型时都会被视为false。

所以要**判断age是否被赋值的话，必须将其与null比较，而不是直接转为Boolean值后和false比较**！

---

#### **适合使用 === 的时候**

除了上述情况，其余时候都建议用===

### this

#### 一般情况

this一般情况下都是指向当前调用其的函数所在的对象

```
let a = {
  x: 1,
  b: function() {
    console.log(this) 
  }
}
a.b() // {x: 1, b: ƒ}，即this指向a
```

---
有一些特殊情况： 
#### 回调函数中的this

由调用的函数决定

1. 如果使用回调，则在调用该回调的函数中，会重新分配this，**不同的回调函数分配的this不同**，可以进入源码查看，当然也可以尝试打印一下，例如下面的setTimeout会把this变为window

```
let a = {
  x: 1,
  b: function() {
    setTimeout(function() {
      console.log(this) 
    })
  }
}
a.b() // window对象
```
#### **局部函数的this**

会自动变成window

1. **如果将函数作为参数传入另一个函数**，则被传入的函数会变成局部变量，不再被任何人调用，this自动变成**window**

```
function c() {
  console.log(this)
}
let a = {
  x: 1,
  b: function(c) {
    c()
  }
}

a.b(c) // window对象
```

#### 函数内定义的函数

**也是局部函数，不再被任何人调用，this自动变成**window**

```
let a = {
  x: 1,
  b: function() {
    let e = function () {
    	console.log(this)
    }
    e()
  }
}

a.b() // window对象
```

---

#### 自定义this

#### 箭头函数（取消回调函数、函数内函数影响）

想要this根据自己的需求变化，有如下几种方式：  
1. **箭头函数**（在JavaScript中，**箭头函数不会创建自己的this上下文，它会继承外层函数的this上下文**）。

在例子2中，我们的this进入setTimeout后，变成了我们不想要的window，但是如果我们想要this指向原来的a，就可以用箭头函数，它不会改变回调函数的this指向——也就是原来指向什么，后来就指向什么。所以用箭头函数作为回调函数的话，**可以保留this的指向**，而不会被所调用的函数抢走。

```
let a = {
  x: 1,
  b: function() {
    setTimeout(() => {
      console.log(this)
    }, 1000)
  }
}
a.b() // {x: 1, b: ƒ}，即this指向a
```

不过，这种this的绑定，**仅限于相对于外层函数内部来说**，但是如果调用外层函数的对象发生了变化，则this还是会指向新的对象，例如下面，调用外层函数b的对象从a变成了f，则this就指向f了。

```
let a = {
  x: 1,
  b: function() {
    setTimeout(() => {
      console.log(this)
    }, 1000)
  }
}
let f = {}
f.b = a.b
f.b() // { b: ƒ }，即this指向f
```

而且这种方法，对于**作为参数的函数是没用的**，例如对例子3做一下修改，将传入的局部函数转为箭头函数，其this并没有指向a，还是原来的window，这是因为箭头函数只是不改变回调的this指向，其所做的也更多是偏向于“不改变”的，而局部函数本身的this就是windows，所以通过箭头函数的“不改变”之后，还是window。

```
let c = () => {
  console.log(this)
}
let a = {
  x: 1,
  b: function(c) {
    c()
  }
}

a.b(c) // window对象
```

但是这种方法，**对于函数内定义的函数是有用的**，例如对例子4做一下修改，将函数b内定义的函数e改为箭头函数，就可以使this指向a了。

```
let a = {
  x: 1,
  b: function() {
    let e = () => {
    	console.log(this)
    }
    e()
  }
}

a.b() // {x: 1, b: ƒ}，即this指向a
```

#### bind（显式绑定this的指向对象）

下面先对例子2-4做修改，再对5-8做修改（2对应5和6，3对应7，4对应8，区别只是在于是否使用了箭头函数）

例如对例子2做修改，可以将其中的this指向a

```
let a = {
  x: 1,
  b: function() {
    setTimeout(function() {
      console.log(this) 
    }.bind(a))
  }
}
a.b() // {x: 1, b: ƒ}，即this指向a
```

对于例子3，修改如下：

```
function c() {
  console.log(this)
}
let a = {
  x: 1,
  b: function(c) {
    let d = c.bind(a)
  	d()
  }
}

a.b(c) // {x: 1, b: ƒ}，即this指向a
```

对于例子4，修改如下：

```
let a = {
  x: 1,
  b: function() {
    let e = function () {
    	console.log(this)
    }.bind(a)
    e()
  }
}

a.b() // {x: 1, b: ƒ}，即this指向a
```

对于例子5，如下改动即可

```
let a = {
  x: 1,
  b: function() {
    setTimeout((() => {
      console.log(this)
    }).bind(a), 1000)
  }
}
a.b() // {x: 1, b: ƒ}，即this指向a
```

要注意，我们需要在使用b的时候，将this绑定为a，对例子6，如果下面这样改，是没办法在f.b()时将this绑定为a的

```
let a = {
  x: 1,
  b: function() {
    setTimeout((() => {
      console.log(this)
    }).bind(a))
  }
}
let f = {}
f.b = a.b
f.b() // { b: ƒ }，即this指向f
```

所以例子6应该这样改，在调用b的地方，再去bind即可。（注意此时b内部的this由于在箭头函数中，所以其中this会自动指向外层函数的调用对象）

```
let a = {
  x: 1,
  b: function() {
    setTimeout(() => {
      console.log(this)
    })
  }
}
let f = {}
f.b = a.b.bind(a)
f.b() // {x: 1, b: ƒ}，即this指向a
```

对于例子7，如果这样bind，是没办法得到a的。**箭头函数中的this，即使被bind了，还是指向原来的内容，优先级比bind高。**

```
let c = () => {
  console.log(this)
}
let a = {
  x: 1,
  b: function(c) {
    let d = c.bind(a)
  	d()
  }
}

a.b(c) // window对象
```

对于例子8，不需要修改了，this已经指向a了

3. apply、call
4. 变量

### 函数定义传参时...的作用

![](https://cdn.nlark.com/yuque/0/2023/png/34824000/1697686265909-033f6fcc-05cd-4480-9a72-5f7fe01b7cb7.png)

当我们要往一个函数中传递未知个数的参数，并且要将这些参数，又传递给另外的函数时

就可以在外层函数用...arg，然后就可以将参数整合成一个arg数组，再用apply的方式传递。

### 防抖

简洁版

```
data() {
  return {
    timer: null
  }
}
// 获取数据项模板
handleGetEduTemplateItemExcel() {
  clearTimeout(this.timer)
  this.timer = setTimeout(() => {
    getEduTemplateItemExcel()
  }, this.downloadTemplateItemExcelInterval)
}
```

增加提示

```
data() {
  return {
    timer: null
  }
}
// 获取数据项模板
handleGetEduTemplateItemExcel() {
  if(this.timer) {
    this.$message.warning(`下载间隔为${ downloadTemplateItemExcelInterval / 1000 }秒`)
  }
  clearTimeout(this.timer)
  this.timer = setTimeout(() => {
    getEduTemplateItemExcel()
    // 时间间隔到后重置timer，就可以不用进入上面的提示
    this.timer = null
  }, this.downloadTemplateItemExcelInterval)
}
```

### 节流

```
function throttle(func, delay) {  
  let lastCall = 0;  
  return function (...args) {  
    const now = new Date().getTime();  
    if (now - lastCall < delay) {  
      return;  
    }  
    lastCall = now;  
    return func.apply(this, args);  
  };  
}

const test = throttle((a, b) => { console.log(a + b) }, 4000)

test(4, 5) // 9

... 4秒内
test(4, 5) // 

... 4秒后
test(4, 5) // 9
```


### apply

相当于把函数“借给”另外一个对象（仅限于用apply时）  
[https://blog.csdn.net/weixin_43877799/article/details/120282509](https://blog.csdn.net/weixin_43877799/article/details/120282509)

![](https://cdn.nlark.com/yuque/0/2023/png/34824000/1697683486597-e9a2927e-ee12-4b6c-8ec7-33ec87d1e5f9.png)
