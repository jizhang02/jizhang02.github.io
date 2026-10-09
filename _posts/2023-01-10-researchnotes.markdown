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

<div class="notes-index" markdown="0">
<table>
<thead>
<tr>
<th>Resource</th>
<th>Year</th>
<th>Topic</th>
<th>What it offers</th>
<th>Type</th>
<th>Last accessed</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/JunMa11/MICCAI-OpenSourcePapers">MICCAI Open Source Papers</a></td>
<td>2019</td>
<td>MICCAI 2019-2026 Open Source Papers</td>
<td>Collection of MICCAI papers with links to open-source code and dataset information.</td>
<td>Paper, Code</td>
<td>2026-10-08</td>
</tr>
<tr>
<td><a href="https://github.com/whq-xxh/ADA4MIA">ADA4MIA</a></td>
<td>2024</td>
<td>Cross-hospital domain adaptation; active learning</td>
<td><details class="resource-offer"><summary><span>Methods for adapting models across hospitals with limited target-domain labels.</span></summary><div><p>医院之间的设备、扫描协议、图像质量和患者分布差异会造成域偏移，使医院 A 训练的模型在医院 B 性能下降；同时，B 可能没有标注或只能负担少量标注。这个仓库收集论文、代码和数据集，研究如何以较低标注成本适应新医院。</p><ul><li><strong>无监督领域自适应：</strong>利用 B 的无标注数据进行适应，经典设定通常仍可访问 A 的有标注数据。</li><li><strong>无源领域自适应：</strong>适应时无法访问 A 的原始数据，只使用 A 训练好的模型和 B 的无标注数据。</li><li><strong>无源主动领域自适应：</strong>在无法访问 A 数据的限制下，主动挑选少量 B 的样本请专家标注，再结合其余无标注数据进行适应。</li></ul><p>“Traditional Domain Adaptation” 栏目也包含无源方法，分类并非互斥；这是资源集合，而非单一算法。</p></div></details></td>
<td>Paper, Code, Dataset</td>
<td>2026-10-09</td>
</tr>
<tr>
<td><a href="https://github.com/MIC-DKFZ/VoxTell">VoxTell</a></td>
<td>2026</td>
<td>Text-prompted 3D medical image segmentation; CVPR 2026</td>
<td><strong>Another work from the nnU-Net team (MIC-DKFZ):</strong> segments anatomical and pathological structures in CT, PET, and MRI using free-text prompts.</td>
<td>Paper, Code</td>
<td>2026-10-09</td>
</tr>
<tr>
<td><a href="https://github.com/MIC-DKFZ/nnInteractive">nnInteractive</a></td>
<td>2025</td>
<td>Interactive 3D medical image segmentation</td>
<td><strong>From the same MIC-DKFZ team as nnU-Net and VoxTell:</strong> semi-automatic 3D segmentation with points, scribbles, boxes, and lasso prompts; supports iterative refinement.</td>
<td>Paper, Code</td>
<td>2026-10-09</td>
</tr>
<tr>
<td><a href="https://github.com/wasserth/TotalSegmentator">TotalSegmentator</a></td>
<td>2022</td>
<td>CT/MRI anatomical segmentation</td>
<td><strong>Built on nnU-Net by University Hospital Basel:</strong> automatically segments 117 anatomical classes in CT and 50 in MRI; includes pretrained models and public datasets.</td>
<td>Paper, Code, Dataset</td>
<td>2026-10-09</td>
</tr>
<tr>
<td><a href="https://github.com/ENHANCE-PET/LION">LION</a></td>
<td>2026</td>
<td>PET; tumor segmentation</td>
<td>Automated lesion segmentation for FDG and PSMA PET scans.</td>
<td>Paper, Code</td>
<td>2026-10-08</td>
</tr>
<tr>
<td><a href="https://github.com/ashemag/human-atlas">Human Atlas</a></td>
<td>2026</td>
<td>3D anatomy; medical education</td>
<td>Interactive anatomy explorer with 2,234 selectable BodyParts3D meshes, system layers, search, and exploded views.</td>
<td>Code, Web Platform</td>
<td>2026-10-09</td>
</tr>
<tr>
<td><a href="https://thevirtualheart.com/">The Virtual Heart</a></td>
<td>2024</td>
<td>Cardiac anatomy; medical education</td>
<td>Interactive 3D heart visualization and cardiac murmur education.</td>
<td>Web Platform</td>
<td>2026-10-08</td>
</tr>
</tbody>
</table>
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
