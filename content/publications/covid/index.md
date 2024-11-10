---
title: "COVID-19 Detection from Respiratory Sounds with Hierarchical Spectrogram Transformers"
authors:
- Idil Aytekin
- admin
- Kaan Gonc
- Haydar Ankishan
- Emine U Saritas
- Ulas Bagci
- Haydar Celik
- Tolga Cukur



date: "2022-07-19T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
#publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: "*under review, IEEE Transactions on Medical Imaging*"
publication_short: "under review, IEEE JHBI"

abstract: Monitoring of prevalent airborne diseases such as COVID-19 characteristically involve respiratory assessments. While auscultation is a mainstream method for symptomatic monitoring, its diagnostic utility is hampered by the need for dedicated hospital visits. Continual remote monitoring based on recordings of respiratory sounds on portable devices is a promising alternative, which can assist in screening of COVID-19. In this study, we introduce a novel deep learning approach to distinguish patients with COVID-19 from healthy controls given audio recordings of cough or breathing sounds. The proposed approach leverages a novel hierarchical spectrogram transformer (HST) on spectrogram representations of respiratory sounds. HST embodies self-attention mechanisms over local windows in spectrograms, and window size is progressively grown over model stages to capture local to global context. HST is compared against state-of-the-art conventional and deep-learning baselines. Comprehensive demonstrations on a multi-national dataset indicate that HST outperforms competing methods, achieving over 97% area under the receiver operating characteristic curve (AUC) in detecting COVID-19 cases.

# Summary. An optional shortened abstract.
#summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
- Source Themes
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'https://arxiv.org/abs/2207.09529'
url_code: 'https://github.com/icon-lab/HST'
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

