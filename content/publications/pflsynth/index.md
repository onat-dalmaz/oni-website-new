---
title: "One Model to Unite Them All: Personalized Federated Learning of Multi-Contrast MRI Synthesis"
authors:
- admin
- Usama Mirza
- Gökberk Elmas
- Muzaffer Özbey
- Salman UH Dar
- Emir Ceyani
- Salman Avestimehr
- Tolga Cukur


date: "2022-07-13T00:00:00Z"
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
publication_short: "under review, IEEE TMI"

abstract: Multi-institutional collaborations are key for learning generalizable MRI synthesis models that translate source- onto target-contrast images. To facilitate collaboration, federated learning (FL) adopts decentralized training and mitigates privacy concerns by avoiding sharing of imaging data. However, FL-trained synthesis models can be impaired by the inherent heterogeneity in the data distribution, with domain shifts evident when common or variable translation tasks are prescribed across sites. Here we introduce the first personalized FL method for MRI Synthesis (pFLSynth) to improve reliability against domain shifts. pFLSynth is based on an adversarial model that produces latents specific to individual sites and source-target contrasts, and leverages novel personalization blocks to adaptively tune the statistics and weighting of feature maps across the generator stages given latents. To further promote site specificity, partial model aggregation is employed over downstream layers of the generator while upstream layers are retained locally. As such, pFLSynth enables training of a unified synthesis model that can reliably generalize across multiple sites and translation tasks. Comprehensive experiments on multi-site datasets clearly demonstrate the enhanced performance of pFLSynth against prior federated methods in multi-contrast MRI synthesis.

# Summary. An optional shortened abstract.
#summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
- Source Themes
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'https://arxiv.org/abs/2207.06509'
url_code: 'https://github.com/icon-lab/pFLSynth'
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

