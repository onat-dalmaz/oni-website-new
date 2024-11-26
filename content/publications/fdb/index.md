---
title: "Learning Fourier-Constrained Diffusion Bridges for MRI Reconstruction"
authors:
#Muhammad U. Mirza and Onat Dalmaz and Hasan A. Bedel and Gokberk Elmas and Yilmaz Korkmaz and Alper Gungor and Salman UH Dar and Tolga Çukur
- 
- Muhammad U. Mirza
- admin
- Hasan A. Bedel
- Gokberk Elmas
- Yilmaz Korkmaz
- Alper Gungor
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

abstract: Deep generative models have gained recent traction in accelerated MRI reconstruction. Diffusion priors are particularly promising given their representational fidelity. Instead of the target transformation from undersampled to fully-sampled data required for MRI reconstruction, common diffusion priors are trained to learn a task-agnostic transformation from an asymptotic start-point of Gaussian noise onto the finite end-point of fully-sampled data. During inference, data-consistency projections are injected in between reverse diffusion steps to reach a compromise solution within the span of both the trained diffusion prior and the imaging operator for an accelerated MRI acquisition. Unfortunately, performance losses can occur due to the discrepancy between target and learned transformations given the asymptotic normality assumption in diffusion priors. To address this discrepancy, here we introduce a novel Fourier-constrained diffusion bridge (FDB) for MRI reconstruction that transforms between a finite start-point of moderately undersampled data and an end-point of fully-sampled data. We derive the theoretical formulation of FDB as a generalized diffusion process based on a stochastic degradation operator that performs random spatial-frequency removal. We propose an enhanced sampling algorithm with a learned correction term for soft dealiasing across reverse diffusion steps. Demonstrations on brain MRI indicate that FDB outperforms state-of-the-art methods including non-diffusion and diffusion priors.

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

