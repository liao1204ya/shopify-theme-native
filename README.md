# Shopify 主题原生融合开发

供 Codex 使用的个人开发方法 Skill：复用目标 Shopify 主题的架构、公共组件和视觉语言，开发后台可配置的独立模块。

## 安装

将本仓库链接发给 Codex，并说明：

> 请使用 skill-installer，从这个 GitHub 仓库安装 skills/shopify-theme-native，作为我的个人 Skill。

私有仓库需要安装者拥有仓库读取权限。也可以下载仓库，将 `skills/shopify-theme-native` 整个目录复制到 `$CODEX_HOME/skills/`；默认是 `~/.codex/skills/`。确保 `SKILL.md` 直接位于 `shopify-theme-native` 目录内。

在新任务中调用；若未发现新 Skill，重启 Codex 后重试。

## 使用

> 使用 $shopify-theme-native，帮我完成这个 Shopify 项目的开发需求。

提供目标主题源码或店铺连接，以及需求和参考设计。Skill 本身不会自动连接旧店铺。

## 包含的方法

- 独立 section、后台上传与配置、跨页面共享商品组件。
- 跟随目标主题字体、配色、动画、公共 header/footer。
- HTML 设计稿还原；多页面 header/footer 统一以首页为准。
- Dawn 空装饰元素的定向 `display: block !important` 修复。
- Admin API 优先、CLI 其次，有可行非浏览器方式时优先使用。
- 备份主题的同名模板配合与预览交付。
- 复杂规格约束、公式计价和 YMQ 适配。

详细历史报告位于 Skill 的 `references/`，按需读取。报告中的旧店业务参数与源码位置用于理解案例，原始主题审计目录未包含在仓库内。

开发完成后交付对应主题与页面的预览链接，以及具体修改位置和验证结果。
