---
layout:     post
title:      "Medical Research, Tools, and Ideas"
subtitle:   "医学研究笔记"
date:       2023-01-10
last_updated: 2026-10-09
author:     "Jing"
header-img: "img/post-bg.jpg"
header-mask: 0.45
research-notes: true
tags:
    - Medical Image Analysis
    - Research
    - notes

---



## Research collection

A growing collection of papers, code, tools, datasets, and ideas in medical research.

<div class="notes-index" markdown="1">

| Resource | Year | Topic | What it offers | Type | Last accessed |
| :--- | :---: | :--- | :--- | :--- | :---: |
| [MICCAI Open Source Papers](https://github.com/JunMa11/MICCAI-OpenSourcePapers) | 2019 | MICCAI 2019-2026 Open Source Papers | Collection of MICCAI papers with links to open-source code and dataset information. | Paper, Code | 2026-10-08 |
| [ADA4MIA](https://github.com/whq-xxh/ADA4MIA) | 2024 | Cross-hospital domain adaptation; active learning | <details class="resource-offer"><summary><span>Methods for adapting models across hospitals with limited target-domain labels.</span></summary><div>医院之间的设备、扫描协议、图像质量和患者分布差异会造成域偏移，使医院 A 训练的模型在医院 B 性能下降；同时，B 可能没有标注或只能负担少量标注。这个仓库收集论文、代码和数据集，研究如何以较低标注成本适应新医院。<ul><li><strong>无监督领域自适应：</strong>利用 B 的无标注数据进行适应，经典设定通常仍可访问 A 的有标注数据。</li><li><strong>无源领域自适应：</strong>适应时无法访问 A 的原始数据，只使用 A 训练好的模型和 B 的无标注数据。</li><li><strong>无源主动领域自适应：</strong>在无法访问 A 数据的限制下，主动挑选少量 B 的样本请专家标注，再结合其余无标注数据进行适应。</li></ul>“Traditional Domain Adaptation” 栏目也包含无源方法，分类并非互斥；这是资源集合，而非单一算法。</div></details> | Paper, Code, Dataset | 2026-10-09 |
| [VoxTell](https://github.com/MIC-DKFZ/VoxTell) | 2026 | Text-prompted 3D medical image segmentation; CVPR 2026 | **Another work from the nnU-Net team (MIC-DKFZ):** segments anatomical and pathological structures in CT, PET, and MRI using free-text prompts. | Paper, Code | 2026-10-09 |
| [nnInteractive](https://github.com/MIC-DKFZ/nnInteractive) | 2025 | Interactive 3D medical image segmentation | **From the same MIC-DKFZ team as nnU-Net and VoxTell:** semi-automatic 3D segmentation with points, scribbles, boxes, and lasso prompts; supports iterative refinement. | Paper, Code | 2026-10-09 |
| [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) | 2022 | CT/MRI anatomical segmentation | **Built on nnU-Net by University Hospital Basel:** automatically segments 117 anatomical classes in CT and 50 in MRI; includes pretrained models and public datasets. | Paper, Code, Dataset | 2026-10-09 |
| [LION](https://github.com/ENHANCE-PET/LION) | 2026 | PET; tumor segmentation | Automated lesion segmentation for FDG and PSMA PET scans. | Paper, Code | 2026-10-08 |
| [Human Atlas](https://github.com/ashemag/human-atlas) | 2026 | 3D anatomy; medical education | Interactive anatomy explorer with 2,234 selectable BodyParts3D meshes, system layers, search, and exploded views. | Code, Web Platform | 2026-10-09 |
| [The Virtual Heart](https://thevirtualheart.com/) | 2024 | Cardiac anatomy; medical education | Interactive 3D heart visualization and cardiac murmur education. | Web Platform | 2026-10-08 |

</div>

<details markdown="1">
<summary>Resource types</summary>

- **Literature:** Papers, reviews, preprints, and research reports.
- **Code:** Algorithm implementations and reproduction repositories.
- **Tool / Platform:** Software, web applications, and analysis platforms.
- **Dataset:** Open data, annotations, and benchmark collections.
- **Tutorial / Resource:** Courses, technical guides, and educational materials.
- **Research Idea:** Questions, project proposals, and collaboration directions.

</details>
