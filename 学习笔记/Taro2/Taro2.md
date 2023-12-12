粤省事需要使用taro2.x，所以我们就是用taro2.x开发

[Taro 文档](https://taro-docs.jd.com/docs/2.x/)

Taro类似React、Vue这样的框架，其语法和React基本一致

---

先用nvs 切换成 node v11——`nvs use v11`

使用`npm i -g @tarojs/cli@2`，下载2.x最新的taro

选择不用Ts，然后css编译器选择Less，默认模板即可

然后在项目里，用以下语句，打包一下（注意还是要v11，node版本太高了会报错）

将taro变成小程序：

```
# yarn
$ yarn dev:weapp
$ yarn build:weapp
# npm script
$ npm run dev:weapp
$ npm run build:weapp
# 仅限全局安装
$ taro build --type weapp --watch
$ taro build --type weapp
# npx 用户也可以使用
$ npx taro build --type weapp --watch
$ npx taro build --type weapp
```

将taro变成h5（预览）

```
# yarn
$ yarn dev:h5
# npm script
$ npm run dev:h5
# 仅限全局安装
$ taro build --type h5 --watch
# npx 用户也可以使用
$ npx taro build --type h5 --watch
```

h5打包

```
# yarn
$ yarn build:h5
# npm script
$ npm run build:h5
# 仅限全局安装
$ taro build --type h5
# npx 用户也可以使用
$ npx taro build --type h5
```

---

### Taro规范

[Taro 文档](https://taro-docs.jd.com/docs/2.x/spec-for-taro)

---

尽量避免在 componentDidMount 中调用 this.setState

因为在 componentDidMount（对应小程序的onReady） 中调用 this.setState 会导致触发更新

```
import Taro, { Component } from '@tarojs/taro'
import { View, Input } from '@tarojs/components'

class MyComponent extends Component {
  state = {
    myTime: 12
  }
  
  componentDidMount () {
    this.setState({     // ✗ 尽量避免，可以在 componentWillMount(对应小程序的onLoad) 中处理
      name: 1
    })
  }
  
  render () {
    const { isEnable } = this.props
    const { myTime } = this.state
    return (
      <View className='test'>
        {isEnable && <Text className='test_text'>{myTime}</Text>}
      </View>
    )
  }
}
```

不要在 componentWillUpdate/componentDidUpdate/render 中调用 this.setState

总之，在componentWillMount中调用就好了嘛

---

组件最好定义 defaultProps

```
import Taro, { Component } from '@tarojs/taro'
import { View, Input } from '@tarojs/components'

class MyComponent extends Component {

  static defaultProps = {
    isEnable: true
  }
  
  state = {
    myTime: 12
  }
  
  render () {
    const { isEnable } = this.props
    const { myTime } = this.state

    return (
      <View className='test'>
        {isEnable && <Text className='test_text'>{myTime}</Text>}
      </View>
    )
  }
}
```