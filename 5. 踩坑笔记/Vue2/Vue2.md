### el-switch绑定元素（对象数组）

这样不ok：
```vue
<script setup>
import { ref } from 'vue'

const switch1 = ref('stop')
const switchDict = ref({
  'stop': false,
  'normal': true,
})
</script>
<template>
  <el-switch
    v-model="switchDict[switch1]"
  ></el-switch>
</template>
```

但是这样是ok的：
```vue
<script setup>
import { ref } from 'vue'

const switch1 = ref('stop')
const switchDict = ref({
  'stop': false,
  'normal': true,
})
</script>
<template>
  <el-switch
    v-model="switchDict['stop']"
  ></el-switch>
</template>
```

### vscode创建vue骨架

![](https://cdn.nlark.com/yuque/0/2023/png/34824000/1697534322861-5feff06b-261a-4dd2-9f00-c52e5bda4638.png)

![](https://cdn.nlark.com/yuque/0/2023/png/34824000/1697534345836-9ae1d5f9-4101-4aa2-879d-abd807887c6a.png)

```
{    
	"Print to console": {
		"prefix": "vue",
		"body": [
				"<template>",
				"  <div class=\"\">\n",
				"  </div>",
				"</template>\n",
				"<script>",
				"export default {",
				"  name: '',",
				"  props: {},",
				"  data () {",
				"    return {}",
				"  },",
				"  components: {",
	"    ",	
	"  },",
				"  computed: {",
	"    ",	
	"  },",
				"  watch: {",
	"    ",
	"  },",
				"  created () {",
	"    ",
	"  },",
				"  mounted () {",
	"    ",	
	"  },",
				"  methods: {",
	"    ",	
	"  },",
				"}",
				"</script>\n",
				"<style lang=\"scss\" scoped>",
	"  ",
				"</style>",
				"$2"
		],
		"description": "Log output to console"
	}
}
```
