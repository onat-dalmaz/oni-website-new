---
title: "BolT: Fused Window Transformers for fMRI Time Series Analysis"
authors:
- Hasan Atakan Bedel
- Irmak Sivgin
- admin
- Salman Dar
- Tolga Cukur

date: "2022-05-23T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
#publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: "*under review, Medical Image Analysis*"
publication_short: "under review, MEDIA"

abstract: Deep-learning models have enabled performance leaps in analysis of high-dimensional functional MRI (fMRI) data. Yet, many previous methods are suboptimally sensitive for contextual representations across diverse time scales. Here, we present BolT, a blood-oxygen-level-dependent transformer model, for analyzing multi-variate fMRI time series. BolT leverages a cascade of transformer encoders equipped with a novel fused window attention mechanism. Encoding is performed on temporally-overlapped windows within the time series to capture local representations. To integrate information temporally, cross-window attention is computed between base tokens in each window and fringe tokens from neighboring windows. To gradually transition from local to global representations, the extent of window overlap and thereby number of fringe tokens are progressively increased across the cascade. Finally, a novel cross-window regularization is employed to align high-level classification features across the time series. Comprehensive experiments on large-scale public datasets demonstrate the superior performance of BolT against state-of-the-art methods. Furthermore, explanatory analyses to identify landmark time points and regions that contribute most significantly to model decisions corroborate prominent neuroscientific findings in the literature.

# Summary. An optional shortened abstract.
#summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
- Source Themes
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'https://arxiv.org/abs/2205.11578'
url_code: 'https://github.com/icon-lab/BolT'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

