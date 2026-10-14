---
layout:     post
title:      "Medical Research Notes"
subtitle:   "医学研究笔记"
date:       2023-01-10
last_updated: 2026-10-14
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
<td>Healthcare AI Agents</td>
<td>2026</td>
<td><strong>Agent</strong>; healthcare workflows</td>
<td><details class="resource-offer"><summary><span>How can foundation models coordinate tools, evidence, and multi-step workflows for healthcare?</span></summary><div><p><strong>从模型能力到任务流程：</strong>Agent 在基础模型之上组织规划、工具调用、结果反馈和多步执行；它是系统层，并不替代 Transformer 架构或基础模型。多智能体协作是其中一种组织方式。</p><ul><li><strong>医学影像与临床证据：</strong>协调影像分析、分割工具、指标计算、证据检索和报告生成等步骤。</li><li><strong>医疗工作流：</strong>涵盖电子病历与临床文本、患者交互、药物发现和医疗管理。</li><li><strong>评估与可靠性：</strong>关注任务完成、证据依据、工具使用、流程可追溯性及人工监督，配套数据集和基准。</li></ul><p><strong>文献时间跨度：</strong>AgenticHealthAI 当前按年份整理 2023–2026 年研究（含预印本）；这一范围描述该清单，其他仓库的覆盖范围可能不同。</p><p><strong>仓库入口：</strong><a href="https://github.com/AgenticHealthAI/Awesome-AI-Agents-for-Healthcare">AgenticHealthAI：医疗 Agent 综述与资源</a> · <a href="https://github.com/ZJU4HealthCare/Awesome-Medical-LLMs-and-Agents">ZJU4HealthCare：医疗 LLM 与 Agent</a> · <a href="https://github.com/turab45/awesome-healthcare-agents">turab45：医疗 Agent、框架与数据集</a>。</p></div></details></td>
<td>Paper, Code, Dataset</td>
<td>2026-10-14</td>
</tr>
<tr>
<td>Healthcare Foundation Models</td>
<td>2023</td>
<td><strong>Foundation Models</strong>; multimodal healthcare</td>
<td><details class="resource-offer"><summary><span>How can broad pretraining support transferable models across healthcare tasks and modalities?</span></summary><div><p><strong>研究范式：</strong>从为单一任务训练模型，转向在广泛数据上预训练，再通过微调、提示等方式适配多个任务。Foundation Model 描述训练与使用范式，Transformer 描述网络架构，二者并非相互替代的两代方法。</p><ul><li><strong>医学影像：</strong>视觉语言学习、文本与视觉提示、SAM 适配及通用影像模型。</li><li><strong>广义医疗：</strong>语言、视觉、生物信息、音频和多模态模型，以及相关数据集和综述。</li><li><strong>小语言模型与高效部署：</strong>关注医疗领域专用小模型、压缩与优化，以及模型规模、资源成本和任务效果之间的权衡。SLMs-in-healthcare 整理模型、论文、数据集和评估资源，涵盖医学问答、临床文本及放射学视觉语言应用。</li><li><strong>医疗应用与部署：</strong>诊断、报告生成、医疗信息学、智能体，以及评估、安全和治理问题。</li></ul><p><strong>时间背景：</strong>基础模型概念于 2021 年被系统提出；这些资源对应的代表性综述与研究整理集中于 2023–2024 年。此处年份是资源背景，并非逐篇统计的文献覆盖范围。</p><p><strong>仓库入口：</strong><a href="https://github.com/xmindflow/Awesome-Foundation-Models-in-Medical-Imaging">xmindflow：医学影像基础模型</a> · <a href="https://github.com/YutingHe-list/Awesome-Foundation-Models-for-Advancing-Healthcare">YutingHe-list：医疗基础模型</a> · <a href="https://github.com/Jianing-Qiu/Awesome-Healthcare-Foundation-Models">Jianing-Qiu：医疗大模型生态</a> · <a href="https://github.com/drmuskangarg/SLMs-in-healthcare">SLMs-in-healthcare：小语言模型与部署</a>。</p></div></details></td>
<td>Paper, Code, Dataset</td>
<td>2026-10-14</td>
</tr>
<tr>
<td><a href="https://github.com/ImprintLab/Medical-SAM-Adapter">Medical SAM Adapter</a></td>
<td>2023</td>
<td><strong>Adapter</strong>; parameter-efficient SAM adaptation</td>
<td><details class="resource-offer"><summary><span>How can lightweight adapters equip SAM with medical knowledge while retaining its pretrained capabilities?</span></summary><div><p><strong>为什么需要 Adapter：</strong>SAM 的自然图像预训练与医学影像存在差异，用户提示能指定目标，却不能直接补足模型的医学领域知识。该方法通过小型可训练适配模块调整内部特征，保留大部分预训练参数，以较低训练成本完成医学适配。</p><ul><li><strong>参数高效微调：</strong>论文报告仅更新约 2% 的参数，并在 17 个医学图像分割任务上评估。</li><li><strong>二维到三维：</strong>Space-Depth Transpose（SD-Trans）帮助二维 SAM 利用三维医学影像信息。</li><li><strong>提示条件适配：</strong>Hyper-Prompting Adapter（HyP-Adpt）将用户提示结合到适配过程。</li></ul><p><strong>时间与资源：</strong>论文于 2023 年首次发布预印本；仓库提供训练与评估代码、示例及预训练 Adapter 入口。Adapter 是参数高效微调的一种方式，并非医学 SAM 必须采用的组件。</p></div></details></td>
<td>Paper, Code, Model</td>
<td>2026-10-14</td>
</tr>
<tr>
<td><a href="https://github.com/YichiZhang98/SAM4MIS">SAM4MIS</a></td>
<td>2023</td>
<td><strong>SAM</strong>; segmentation foundation models; medical imaging</td>
<td><details class="resource-offer"><summary><span>How can SAM-based foundation models generalize to medical images and enable annotation-efficient, interactive 3D segmentation?</span></summary><div><ul><li><strong>SAM 基础介绍：</strong>介绍图像编码器、提示编码器和掩膜解码器如何结合图像与用户提示生成分割，并提供原始论文和医学应用发展时间线。</li><li><strong>SAM 2/3 医学适配：</strong>按时间整理 SAM 2、SAM 3 在医学图像、三维影像和视频中的评估与适配研究，附论文及可用代码链接。</li><li><strong>基础模型 / SAM 医学分割文献：</strong>汇总 SAM 及其他分割基础模型的医学应用，包括零样本评估、微调、提示设计和少标注学习等方向。</li><li><strong>开发与验证数据集：</strong>整理医学基础模型相关数据资源，包括交互式分割基准、M3D 和 SA-Med2D-20M，提供论文与数据入口。</li><li><strong>CVPR 2025 交互式 3D 生物医学分割工作坊：</strong>提供挑战赛及论文入口，关注适应不同解剖结构和成像条件、并通过用户交互逐步改善结果的通用三维分割模型。</li></ul></div></details></td>
<td>Paper, Code, Dataset</td>
<td>2026-10-12</td>
</tr>
<tr>
<td>Transformers in Medical Imaging</td>
<td>2021</td>
<td><strong>Transformer</strong>; ViT 2020-2023</td>
<td><details class="resource-offer"><summary><span>How can attention model global context in medical images, and complement convolutional networks?</span></summary><div><p><strong>方法起点：</strong>Transformer 原始架构由 <a href="https://arxiv.org/abs/1706.03762">Attention Is All You Need（2017）</a> 提出，最初用于语言序列建模。<a href="https://arxiv.org/abs/2010.11929">Vision Transformer（ViT，2020 年预印本／ICLR 2021）</a> 将图像划分为 patch 并作为 token 序列输入 Transformer，推动其在视觉任务中的应用。</p><p><strong>文献时间跨度：</strong>主要覆盖约 2020–2023 年的医学影像经典工作（含预印本），xmindflow 的配套综述正式发表于 MedIA 2024。收录纯 Transformer 及 CNN–Transformer 混合方法，包括 TransUNet、UNETR、Swin-Unet 等。</p><p><strong>应用范围：</strong>医学图像分割、分类、重建、合成、检测、配准和临床报告生成。其论文时间范围不代表 Transformer 研究的终止时间。</p><p><strong>仓库入口：</strong><a href="https://github.com/xmindflow/Awesome-Transformer-in-Medical-Imaging">xmindflow</a> · <a href="https://github.com/fahadshamshad/awesome-transformers-in-medical-imaging">fahadshamshad</a>。两个不同综述团队整理的清单，可交叉查阅。</p></div></details></td>
<td>Paper, Code</td>
<td>2026-10-14</td>
</tr>
<tr>
<td><a href="https://github.com/amirhossein-kz/Awesome-Diffusion-Models-in-Medical-Imaging">Awesome Diffusion Models in Medical Imaging</a></td>
<td>2022</td>
<td><strong>Diffusion model</strong>; 2021-2025</td>
<td><details class="resource-offer"><summary><span>Diffusion methods for medical image synthesis, reconstruction, and analysis, with surveys and code links.</span></summary><div><p>医学影像扩散模型文献集合，包含作者发表于 Medical Image Analysis（2023）的综述，并已补充至 2025 年的论文与综述。</p><p><strong>文献时间跨度：</strong>当前清单约覆盖 2021–2025 年（含预印本），这是收录范围，不代表扩散模型本身的起止年份。</p><ul><li><strong>生成与转换：</strong>图像生成、文本生成图像、图像到图像转换及多模态生成。</li><li><strong>图像质量与重建：</strong>去噪、重建、修复、超分辨率和增强。</li><li><strong>影像分析：</strong>分割、异常检测、配准、分类和目标检测等应用。</li><li><strong>研究入口：</strong>综述、挑战赛报告，以及部分论文的开源代码链接。</li></ul><p>适合系统了解扩散模型在医学影像中的方法与应用；也收录部分通用扩散及其他相关领域文献。</p></div></details></td>
<td>Paper, Code</td>
<td>2026-10-14</td>
</tr>
<tr>
<td><a href="https://github.com/xinario/awesome-gan-for-medical-imaging">Awesome GAN for Medical Imaging</a></td>
<td>2022</td>
<td><strong>GAN</strong>; 2016—2022 adversarial learning</td>
<td><details class="resource-offer"><summary><span>Classic applications of GANs in medical imaging, alongside the shift toward diffusion and flow-based generation.</span></summary><div><p><strong>GAN 已经不是当前最主要的新方向了；但它仍然有用，也没有被全面淘汰。</strong>根据近年的论文，医学影像生成研究重心已经明显转向 <strong>Diffusion（扩散模型）和 Flow Matching / Rectified Flow</strong>。例如，<a href="https://arxiv.org/abs/2508.05772">MAISI-v2，AAAI 2026</a> 将 Rectified Flow 用于加速三维高分辨率医学影像合成。</p><p><strong>文献时间跨度：</strong>约 2016–2022 年，主体集中在 2017–2019 年（含预印本）。这个仓库适合用来了解 <strong>GAN 在医学影像中的经典应用</strong>，涵盖 MR→CT、去噪、重建、分割和病理染色转换，提供相关论文及部分开源代码入口。</p></div></details></td>
<td>Paper, Code</td>
<td>2026-10-14</td>
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
<td><a href="https://github.com/MIC-DKFZ/nnUNet">nnU-Net</a></td>
<td>2021</td>
<td><strong>U-Net</strong>; self-configuring medical image segmentation</td>
<td>Classic U-Net-based framework that automatically configures preprocessing, network architecture, training, and model selection for 2D/3D medical image segmentation.</td>
<td>Paper, Code</td>
<td>2026-10-14</td>
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
