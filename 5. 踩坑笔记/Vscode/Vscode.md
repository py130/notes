## 自动格式化代码

[彻底搞懂ESLint与Prettier在vscode中的代码自动格式化 - 掘金](https://juejin.cn/post/7156893291726782500)

安装：eslint prettier vetur
配置：eslintrc.js

以下是完整配置，参考项目实施部在省PMO项目中的配置
```JSON
{
  "editor.tabSize": 2,
  // 必要：prettier -> * 
  "editor.formatOnSave": true,
  // 似乎不必要：eslint -> .js
  "[javascript]": {
    "editor.defaultFormatter": "dbaeumer.vscode-eslint"
  },
  // 似乎不必要：eslint -> .ts
  "[typescript]": {
    "editor.defaultFormatter": "dbaeumer.vscode-eslint"
  },
  // 必要：html-language-features -> .html
  "[html]": {
    "editor.defaultFormatter": "vscode.html-language-features"
  },
  // 似乎不必要：prettier -> .jsonc
  "[jsonc]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  // 似乎不必要：prettier -> .json
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  // 与格式化无关
  "vetur.completion.autoImport": false,
  // 似乎不必要：vetur(prettier) -x-> <script>
  "vetur.format.defaultFormatter.js": "none",
  // 似乎不必要：vetur(prettier) -x-> <script>
  "vetur.format.defaultFormatter.ts": "none",
  // 似乎不必要：vetur(prettier) -x-> <html>
  "vetur.format.defaultFormatter.html": "none",
  // 必要：eslint -> 自动保存
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "always",
    "source.fixAll.stylelint": "always"
  },
  // 似乎不必要
  "eslint.validate": ["javascript", "typescript", "vue"],
  // 与格式化无关
  "stylelint.validate": ["css", "less", "postcss", "vue"],
  // 与格式化无关
  "cSpell.words": [
    "abic",
    "digitalgd",
    "docc",
    "easycom",
    "flowc",
    "msgc",
    "usrc"
  ]
}
```
经过测试，以下是与格式化有关的必要配置：
```JSON
{
  // 必要：prettier -> * 
  "editor.formatOnSave": true,
  // 必要：html-language-features -> .html
  "[html]": {
    "editor.defaultFormatter": "vscode.html-language-features"
  },
  // 必要：eslint -> 自动保存
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "always",
    "source.fixAll.stylelint": "always"
  },
}
```