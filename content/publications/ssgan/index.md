---
title: "Semi-Supervised Learning of MRI Synthesis without Fully-Sampled Ground Truths"
authors:
- Mahmut Yurt
- admin
- Salman Dar
- Muzaffer Ozbey
- Berk Tınaz
- Kader Oguz
- Tolga Cukur

date: "2022-08-16T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
#publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Transactions on Medical Imaging*"
publication_short: "IEEE TMI"

abstract: Learning-based translation between MRI contrasts involves supervised deep models trained using high-quality source- and target-contrast images derived from fully-sampled acquisitions, which might be difficult to collect under limitations on scan costs or time. To facilitate curation of training sets, here we introduce the first semi-supervised model for MRI contrast translation (ssGAN) that can be trained directly using undersampled k-space data. To enable semi-supervised learning on undersampled data, ssGAN introduces novel multi-coil losses in image, k-space, and adversarial domains. The multi-coil losses are selectively enforced on acquired k-space samples unlike traditional losses in single-coil synthesis models. Comprehensive experiments on retrospectively undersampled multi-contrast brain MRI datasets are provided. Our results demonstrate that ssGAN yields on par performance to a supervised model, while outperforming single-coil models trained on coil-combined magnitude images. It also outperforms cascaded reconstruction-synthesis models where a supervised synthesis model is trained following self-supervised reconstruction of undersampled data. Thus, ssGAN holds great promise to improve the feasibility of learning-based multi-contrast MRI synthesis.

# Summary. An optional shortened abstract.
#summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
- Source Themes
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'https://ieeexplore.ieee.org/abstract/document/9857899'
url_code: 'https://github.com/icon-lab/ssGAN'
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

