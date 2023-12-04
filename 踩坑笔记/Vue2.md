### vue2加载图片失败

```
<img src="/src/assets/chosen.svg" alt="">
```

成功加载

```
<img class="img-icon" :src="props.checked ? '/src/assets/chosen.svg' : '/src/assets/unchosen.svg'">
```

加载图片失败

```
<img class="img-icon" v-if="props.checked" src='/src/assets/chosen.svg'/>
```

也失败

如果有判断，则不会正常加载

解决办法？