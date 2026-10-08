---
layout:     post
title:      "Tech notes on CS"
subtitle:   "医学研究与应用 · A living research notebook"
date:       2023-01-10
author:     "Jing"
header-img: "img/post-bg.jpg"
header-mask: 0.45
research-notes: true
tags:
    - Medical Image Analysis
    - Research
    - notes

---



## 医学研究与应用

这里收录我从 GitHub、公众号、LinkedIn 和其他渠道发现的医学研究、开源工具与交互应用。希望这些线索能成为自己、合作者和学生探索新课题的起点。

> 从一个感兴趣的项目开始：了解它的功能，记录值得研究的问题，再决定是否阅读论文、复现或尝试合作。

**最近更新：2026-10-08** · 当前收录 **2** 个项目 · 状态：已收录，待深入阅读或试用

[医学影像与自动分析](#medical-imaging) · [心脏可视化与医学教育](#cardiac-education) · [后续阅读与试用](#next-steps) · [新增条目模板](#entry-template)

### 快速索引

<div class="notes-index" markdown="1">

| 项目 | 收录年份 | 方向 | 核心功能 | 当前进度 |
| :--- | :--- | :--- | :--- | :--- |
| [LION](#lion) | 2026 | PET · 肿瘤分割 | FDG / PSMA PET 自动病灶分割 | 待阅读与试用 |
| [The Virtual Heart](#virtual-heart) | 2026 | 心脏 · 医学教育 | 交互式 3D 心脏与心脏杂音教学 | 待体验与评估 |

</div>

*“收录年份”表示加入本笔记的时间；项目发布或论文发表年份单独记录，未确认时标注待核实。功能简介来自官方资料，课题想法属于探索方向。*

## 医学影像与自动分析
{: #medical-imaging }

<section class="research-entry" markdown="1" aria-labelledby="lion">

<figure class="entry-preview">
  <a href="https://github.com/ENHANCE-PET/LION"><img src="{{ '/img/research-notes/lion.png' | relative_url }}" alt="LION 仓库提供的官方狮子标志图" loading="lazy"></a>
  <figcaption>官方仓库图片 · 保存于 2026-10-08<br>点击图片查看项目；此图为项目标志，非分割结果。<a href="https://github.com/ENHANCE-PET/LION/blob/main/Images/lion.png">图片来源</a>。</figcaption>
</figure>

### LION
{: #lion }

<p class="entry-meta">2026 收录 · PET / 肿瘤分割 · 开源工具</p>

**一句话介绍：** 面向 FDG 和 PSMA PET 的自动肿瘤病灶分割工具。

- **主要功能：** 对 PET 影像进行病灶分割，支持批量处理，并可生成旋转 MIP 预览。
- **输入与使用：** 当前 FDG / PSMA 模型只需要 PET 输入；可通过命令行或 Python 调用。
- **年份：** 收录于 2026；项目首次发布与对应论文年份待核实。
- **来源与进度：** [官方 GitHub 仓库](https://github.com/ENHANCE-PET/LION) · 已收录，尚未完成本地试用。

**值得关注：** 可作为 PET 病灶自动分析的工具线索，进一步考察其在不同疾病、设备和数据来源下的表现。

<details markdown="1">
<summary>潜在课题与下一步</summary>

以下是可以探索的问题，尚未作为项目能力或实验结论验证：

- **跨中心泛化：** 在不同扫描仪、重建参数和疾病队列中，分割结果是否稳定？
- **失败案例分析：** 小病灶、低摄取病灶和生理性摄取区域可能带来哪些问题？
- **定量分析：** 分割误差会如何影响肿瘤负荷指标及后续研究？
- **下一步：** 阅读关联论文与许可，固定模型版本，在有标注的研究数据上做小规模评估。

</details>

</section>

## 心脏可视化与医学教育
{: #cardiac-education }

<section class="research-entry" markdown="1" aria-labelledby="virtual-heart">

<figure class="entry-preview">
  <a href="https://thevirtualheart.com/"><img src="{{ '/img/research-notes/virtual-heart.png' | relative_url }}" alt="The Virtual Heart 官方交互式心脏教学网站首页截图" loading="lazy" width="1200" height="800"></a>
  <figcaption>官方网站缩略图 · 2026-10-08<br>点击图片进入平台。图像与项目内容归原作者所有。</figcaption>
</figure>

### The Virtual Heart
{: #virtual-heart }

<p class="entry-meta">2026 收录 · 心脏 / 医学教育 · 交互应用</p>

**一句话介绍：** 面向医学学生与专业人员的交互式 3D 心脏可视化与心脏杂音教学平台。

- **主要功能：** 官方介绍包含 3D 心脏模型、心脏解剖学习与心脏杂音教学。
- **使用方式：** 通过浏览器访问，具体交互体验有待进一步探索。
- **年份：** 收录于 2026；平台首次上线年份待核实。
- **来源与进度：** [官方网站](https://thevirtualheart.com/) · 已收录，尚未完成系统体验与评估。

**值得关注：** 将三维解剖与教学内容结合的展示方式，可以启发医学影像结果的交互展示与学生教学。

<details markdown="1">
<summary>潜在课题与下一步</summary>

以下是从平台形式出发的研究设想，尚未验证平台是否支持：

- **教学效果：** 交互式模型对空间理解和知识记忆有何帮助？可以如何设计学习评估？
- **影像到模型：** 能否将 CT / MRI 分割结果转化为适合教学的个体化三维模型？
- **多模态展示：** 如何组织解剖、功能影像与听诊内容，帮助理解结构与功能的关系？
- **下一步：** 体验核心模块，记录交互与可访问性，并核实模型来源和使用条件。

</details>

</section>

## 后续阅读与试用
{: #next-steps }

- [ ] LION：找到关联论文，记录发表年份与模型版本。
- [ ] LION：评估输入要求，设计一个小规模复现实验。
- [ ] The Virtual Heart：体验三维模型与教学模块，记录可借鉴的交互方式。
- [ ] 从以上线索中选一个问题，形成一页研究课题草案。

## 新增条目模板
{: #entry-template }

每次先记录名称、年份、功能、来源和一个感兴趣的问题；阅读或试用后再补充结果。公众号或 LinkedIn 宣传可以作为发现渠道，同时尽量附上官网、代码或论文的原始链接。

<details markdown="1">
<summary>展开可复制的 Markdown 模板</summary>

将条目放入对应主题下，并在顶部索引表中增加一行。截图存入 `img/research-notes/`，使用简短文件名。

```markdown
<section class="research-entry" markdown="1" aria-labelledby="project-id">

<div class="entry-preview" markdown="1">

![项目截图与简短说明](/img/research-notes/project.png)
*截图来源：官方页面 · 截图日期：YYYY-MM-DD*

</div>

### 项目名称
{: #project-id }

**一句话介绍：** ……

- **主要功能：** ……
- **年份：** 收录 YYYY；项目 / 论文 YYYY（未确认则写待核实）。
- **方向：** ……
- **发现渠道：** GitHub / 公众号 / LinkedIn ……
- **原始来源：** [代码](链接) · [官网](链接) · [论文](链接)
- **进度：** 待阅读 / 已阅读 / 待复现 / 已试用。

**值得关注：** ……

<details markdown="1">
<summary>潜在课题与试用记录</summary>

- 研究问题：……
- 下一步：……
- 阅读 / 试用日期与版本：……
- 结果与局限：……

</details>

</section>
```

</details>

---

**相关笔记：** 原有计算机科学与医学影像技术笔记仍可在 [tech_notes 仓库](https://github.com/jizhang02/tech_notes) 中查看。

