# 已选扩展的 Shopify/Codex 适配

相对路径均以本 Skill 为根。vendor 是固定版本的第三方参考与脚本，不是对本机安装路径的依赖。记录见 `sources/extensions.json`，许可证随各副本保存。禁止自动运行上游 install/update 脚本、安装付费服务或照搬 Claude 工具名称；本适配层与用户范围要求优先。上游历史数据和搜索引擎规则在实际决策时核对当前官方来源。

## 路由和职责

|任务|读取|职责|
|---|---|---|
|商品/集合与站内 SEO|`vendor/seo/skills/seo-ecommerce/SKILL.md`、按需 `seo-page`、`seo-technical`、`seo-schema`、`seo-hreflang`|Claude SEO 为技术 SEO 主体，形成一份问题清单|
|AI 搜索/GEO|`vendor/geo/geo/SKILL.md`，按需 `vendor/geo/skills/geo-citability/SKILL.md`、`geo-crawlers`、`geo-content`|补充可引用内容、搜索爬虫与品牌证据；不再单独生成冲突 Schema|
|营销内容|`vendor/marketing/skills/product-marketing/SKILL.md`，按需 `copywriting`、`seo-audit`、`ai-seo`、`schema`|定位、搜索意图、卖点与 CTA，最后执行内置 Humanizer；不自动开展广告或外联|
|性能与基础 SEO 验收|Lighthouse CLI|同视口/设备/网络条件记录结果；实验室数据不冒充真实用户数据，得分不是排名承诺|
|主题操作|Shopify CLI|Admin API 优先，CLI 登录/预览/上传作为所需工具；确认主题 ID，遵守备份与发布范围|
|Gemini 可见标记|`vendor/gemini/gemini-watermark-remover/SKILL.md`|覆盖其“在线工具优先”建议，采用本地已安装 CLI；不要打开第三方上传站点|
|媒体元数据|ExifTool CLI|先读取，按请求选择字段处理并保留原文件；保持尺寸、方向和必要色彩信息，清理后验证|

## Shopify 适配与共同验收

先定位 title/description、canonical、robots、sitemap、hreflang、JSON-LD、OG 和图片 alt 的现有负责方。主题与 App 已有输出时复用或修复，不并行添加另一套。检查服务端原始 HTML 中的结构化数据；只有动态注入或行为证据确实需要时才浏览器验证，不能照搬上游“一律浏览器”的偏好。

商品规格、币种、价格、库存与评分必须来自真实数据；没有真实评价不生成评分。集合页考虑筛选/排序参数、分页与内链。多语言沿用现有 Shopify Markets/翻译配置，不编造可访问语言 URL。站点地图和 robots 先读平台实际输出再改，预览/未发布主题不作为可索引生产页面提交。

GEO 区分搜索访问与训练访问，不为了被引用一律放开所有机器人；不承诺 llms.txt、Schema 或任何固定段落长度能提高排名。搜索引擎收录、GSC/GA4、真实 AI 引用需要账号或实际查询证据，缺少时说明缺口，先完成可独立检查部分。

上游 `/seo`、`/geo` 是 Claude 调用范式，在 Codex 中转换为当前任务下的文件读取与可用工具。上游 agent 清单是职责参考，不自动要求并行子代理。上游依赖绝对路径和 `${CLAUDE_PLUGIN_ROOT}` 由本地适配解析；不要修改 WordPress 的安装或安装全局 Python 包。

## 工具运行

Node 工具运行目录默认 `~/.codex/tools/shopify-theme-native`，可通过 `SHOPIFY_NATIVE_TOOLS` 覆盖。Skill 不打包 node_modules、可执行文件或凭据。

新电脑：把 `assets/runtime/package.json` 与 `package-lock.json` 复制到该运行目录，运行 `npm ci`。本机已安装并固定版本；Shopify CLI 优先复用 PATH 中已有版本，新电脑缺少时可安装 `@shopify/cli`。运行入口：

```text
node <skill>/scripts/tools.mjs lighthouse --version
node <skill>/scripts/tools.mjs lighthouse <preview-url> --output=json --output-path=<report.json>
node <skill>/scripts/tools.mjs gemini remove <input> --output <new-file> --json
node <skill>/scripts/tools.mjs exiftool -j <image>
shopify version
```

Lighthouse 需要本机可用 Chrome/Chromium；缺少时报告运行缺口，不虚构审计结果。ExifTool 通过 exiftool-vendored 包提供的官方二进制分发调用，分别遵守包装器和 ExifTool 许可证，不将其源码重新许可。

Python 检查脚本通过 `scripts/audit-runner.py` 运行，核心依赖使用 `assets/runtime/requirements.txt`。本适配是独立、有限的 Codex 执行入口，替代该范围内上游 Claude launcher；不宣称上游全部可选脚本、付费 API、PDF 或浏览器环境都已配置。

```text
python <skill>/scripts/audit-runner.py --setup
python <skill>/scripts/audit-runner.py seo fetch_page.py --help
python <skill>/scripts/audit-runner.py geo citability_scorer.py <authorized-page-url>
```

只对已授权站点发起检查。媒体处理保留原图，明确支持的标记类型，分别验证像素和元数据；文本去 AI 味仍由 Humanizer 承担。网页交付仍必须附预览链接和修改位置。
