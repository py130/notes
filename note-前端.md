# 前端记录

### flex布局下的el-table无法自适应缩小问题

代码如下：

```vue
<template>
  <div class="page">
    <div class="main">
      <div class="table-container">
        <el-table :data="tableData">
          <el-table-column label="姓名" prop="name" />
          <el-table-column label="年龄" prop="age" />
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      tableData: [
        {
          name: "张三",
          age: 15
        }
      ]
    }
  }
}
</script>
<style>
.page {
  display: flex;
}
.main {
  flex: 1;
}
</style>

// or（el-table没有外层元素，也是类似的）
<div class="main">
  <el-table :data="tableData">
    <el-table-column label="姓名" prop="name" />
    <el-table-column label="年龄" prop="age" />
  </el-table>
</div>
```

这种情况下，el-table（和其外层（.table-container））的宽度能放大不能缩小（当页面宽度拉大时，可以自动适应，但是宽度缩小时，不能自适应缩小）



可能原因：大致是因为el-table根据某个外层元素的宽度进行缩放，但是如果在flex布局下，可能无法监听到页面宽度缩小的事件，导致el-table没有缩小。



**解决办法1（推荐）**：给设定flex:1的那一层加上overflow-hidden

```vue
.main {
  flex: 1;
}
```



解决办法2（不推荐）：给el-table外层（或者el-table）宽度设置为略小于100%

```vue
.table-container {
  width: 99%;
}

// or

.el-table {
  width: 99% !important;
}
```

缺点：1. 影响了宽度 2. 如果width太接近100%，容易导致拖动页面时出现动画，甚至有些情况下刷新页面也会出现动画