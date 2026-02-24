# VC 10页简版 Deck（中文）— YFCore PoAIW（第91门 + 定律）
**版本/日期：** DistillGuard-Core v1.0｜2026-02-24  
**公司/团队：** YFCore Technology Limited  
**一句话定位：** 在运行态输出端强制“AI物理做功证明 + Fail-Closed 输出主权”，让工业级蒸馏在经济上不可行。

---

## 第01页｜封面
- **标题：** PoAIW：Physical Proof of AI Work（AI 物理做功证明）
- **副标题：** 第91门（熵不可克隆）+ **定律（I_LSE）**  
  ——把“模型蒸馏”从软件猫鼠游戏抬升为物理不可伪造的输出主权
- **公司/团队：** YFCore Technology Limited
- **版本/日期：** DistillGuard-Core v1.0｜2026-02-24

---

## 第02页｜行业痛点：蒸馏/模型提取已进入工业化
- **现状一句话：** 顶级模型能力正在被“自动化、分布式、低成本”抽走；传统防线（限流/ToS/语义检测）挡不住。
- **工业化特征：**
  - 多账号/代理池/慢速并发，让攻击流量“看起来像正常用户”
  - 目标不是“破坏系统”，而是“稳定收集高保真输出数据集”用于学生模型训练
- **公开证据锚点（页脚）：**
  - OpenAI 向美国众议院相关委员会提交备忘录，指控 DeepSeek 等通过混淆路由/程序化方式蒸馏美方模型输出。[Reuters][reuters-openai]
  - Anthropic 公布“工业规模蒸馏”案例：约 2.4 万个欺诈账号、超过 1600 万次交互，用于提取 Claude 能力。[Anthropic][anthropic-distill]（亦见媒体转述：[Reuters][reuters-anthropic-distill]）
  - Google/GTIG 指出模型提取（distillation/model extraction）尝试在上升，并披露“>10 万提示”级别的提取活动。[Google Cloud][google-gtig]

---

## 第03页｜根因：输出没有“物理归属”，所以软件防御必然漏风
- **今天的系统能判断“你说了什么”**，但往往**无法证明“这段高价值输出确实由可信硬件完成了真实做功”。**
- 攻击者通过代理池/多账号/慢速并发，把“蒸馏流量”伪装成“正常用户流量”。[Anthropic][anthropic-distill]
- **结论：** 只要防线停留在纯软件层，工业级提取就会用更聪明的自动化策略持续穿透。

### 对标框（建议放在本页底部，帮助高管10秒定位）
| 维度 | Claude Code Security（Anthropic） | PoAIW / DistillGuard（YFCore） |
|---|---|---|
| 防御层级 | 软件/语义/逻辑（DevSecOps） | 软件 + 时间 + 物理（Runtime） |
| 核心目标 | **防漏洞**：部署前代码漏洞审查与补丁建议 | **防窃取**：推理时阻断高保真数据集采集 |
| 发生阶段 | Pre-Deployment（合并/部署前） | Pre-Commit 网关（输出端） |
| 对工业蒸馏 | 无直接防护 | 物理做功证明 + Fail-Closed 让规模化在经济上不可行 |
> Claude Code Security 的公开定位：在 Claude Code 中扫描代码库漏洞并给修补建议（研究预览）。[Anthropic][anthropic-claude-code-security]

---

## 第04页｜范式跃迁：PoAIW（AI 物理做功证明）
- **核心思想：** 不再主要审“语义”，而是审“做功证明（Proof of Work/Entropy）”。
- **定义：** 每一次“高保真/高价值输出”必须携带可验证的硬件根信任证明（TEE/机密计算/签名证明），并与能耗/熵增相关证据闭包绑定。
- **类比一句话（给高管听）：** 从“防洗稿”升级为“印钞机级防伪”——不是识别坏人，而是要求不可伪造的物理收据。

---

## 第05页｜最小可交付产品：第91门 + 定律（I_LSE）
### 第91门：I_ENTROPY_CLONE（物理熵不可克隆硬门）
- **要点：** 高等级输出必须满足：
  - ZK/验证通过
  - 硬件证明通过（TEE/Attestation）
  - 热力学/能耗相关门为 0  
  否则直接 **Fail-Closed**（ShadowOnly / 世界写回归零）。

### 定律：I_LSE（第0元门/元公理）
- **要点：** 允许高保真输出的前提是：**意图层 × 时间连续 × 物理证明** 三者同时满足。
- **三条支撑语义（元自护）：**
  - 验证器可信（Verifier trust）
  - 预算自护（Energy budget self-protect）
  - 影子隔离（Shadow isolation，防止数据集泄漏）
- **价值：** 闭环叙事：不仅能拦截攻击，还能用审计闭包证明防线未被绕过（自洽性可审计）。

---

## 第06页｜集成方式：不重训模型，做成可插拔“高安全执行内核”
- **插入点（工程语言）：** API 输出端/网关 Pre-Commit 阶段加一层“门控与收据闭包”。
- **依赖：** 复用既有 TEE/机密计算/签名验证/能耗计量能力；对现有推理逻辑低侵入。
- **交付形态：**
  1) 参考实现（开源）：第91门 + 定律（I_LSE）的形式化规范 + 演示 + CI自证  
  2) 生产实现（合作/NDA）：硬件绑定、证据链、审计与性能工程化

---

## 第07页｜客户为什么会买：把“资产流失”变成“物理不可能”
- **对模型厂：** 显著抬高蒸馏的边际成本（拿不到硬件做功证明就拿不到可训练的高保真语料）。
- **对云厂：** 把机密计算卖点从“数据在用保护”升级到“模型输出主权保护”（高溢价 SKU）。
- **对监管与企业审计：** 天然具备“可判决、可复算、可回放”的合规底座（可导出审计键闭包）。

---

## 第08页｜目标市场与首批落地场景（先易后难）
- **P0（最容易成交）：** 高安全域推理 / 关键基础设施 / 金融风控 / 国防供应链
- **P1：** 云厂商机密计算 + “高保证推理”产品线（把输出主权做成 SKU）
- **P2：** 前沿实验室安全团队（联合研究/原型验证）
- **宏观背书：** 国际 AI 安全报告（2026）系统性讨论能力、风险与治理框架需求。[IASR][iasr-2026]

---

## 第09页｜商业模式：先卖刀尖，再卖全套宪法
- **授权与收入：**
  - 企业 SDK/网关授权（按节点/调用量/安全等级）
  - 云/硬件联合方案授权（与机密计算/TEE 绑定的增值分成）
  - 高安全集成服务（审计、合规、红队、性能调优）
- **升级路径（Upsell）：**  
  先落地第91门 + 定律（I_LSE）；之后再引入 Gate 90（意图/提取风险/种子连续性）形成 Trinity（90+91+定律）成本不对称防御。

---

## 第10页｜试点提案（对外只要讲清三件事）
- **我们提供：** 最小可运行 PoC、集成指南、攻击模拟与审计回放报告
- **我们需要：** 隔离测试环境 + 脱敏调用样本 + 机密计算/TEE 验证接口（可先 Mock）
- **里程碑（按周）：** PoC → 小流量灰度 → 高安全域正式上线

---

# Reference Links（统一页脚链接）
[reuters-openai]: https://www.reuters.com/world/china/openai-accuses-deepseek-distilling-us-models-gain-advantage-bloomberg-news-2026-02-12/ "Reuters: OpenAI memo alleging distillation (Feb 12, 2026)"
[anthropic-distill]: https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks "Anthropic: Detecting and preventing distillation attacks"
[reuters-anthropic-distill]: https://www.reuters.com/world/china/chinese-companies-used-claude-improve-own-models-anthropic-says-2026-02-23/ "Reuters: Distillation/extraction reporting (Feb 23, 2026)"
[google-gtig]: https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use "Google Cloud: GTIG AI Threat Tracker (Feb 12, 2026)"
[iasr-2026]: https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026 "International AI Safety Report 2026"
[anthropic-claude-code-security]: https://www.anthropic.com/news/claude-code-security "Anthropic: Claude Code Security (Feb 20, 2026)"
