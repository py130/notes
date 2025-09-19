## 代码结构

tsp-pages载体：am-admin-web

tsp-pages本体：am-web-comps

统一使用v26分支



## tsp-pages打包

am-web-comps，使用npm install下载，使用yarn es打包到es文件夹

## 替换tsp-pages依赖

package.json里找到@digitalgd/tsp-pages或者@digitalgd/tsp-pages-alpha

如果是@digitalgd/tsp-pages，只需要将对应的url改成某个具体版本号（原本是指向gitlab仓库，但是咱们没有权限啊），如果是digitalgd/tsp-pages-alpha，需要将代码里的tsp-pages-alpha先替换成tsp-pages，然后再执行上述步骤，例如：

 ```
"@digitalgd/tsp-pages-alpha": "git+ssh://git@gitlab.dg.com:10086/zlywsyb/gdrs/am/v3/am-web-comps.git#develop",

=>

"@digitalgd/tsp-pages": "^2.0.5",
 ```

## am-admin-web安装依赖

nvs use v14

yarn install 或者 npm install

## 替换am-admin-web的tsp-pages的es文件夹：

位置如下：

```
am-admin-web\node_modules\@digitalgd\tsp-pages\es
```

就是将编译后的tsp-pages代码更新过来：

## 修改

简单的修改，只需要修改.project.pm或者.project.pm-prod里的配置即可，复杂的需要修改tsp-pages（需要问荣誉开权限）并重新替换es

## 打包

yarn build:pm-prod --env=test

要用yarn不用npm，因为npm参数会多一个，vue.config.js写死了读取的--env是第几个参数

然后--env后面的test、prod、dev不影响，不加也不要紧了。