# Claim 2 source map

Pinned `main.tex` in `arxiv-2602.05435-source.tar.gz`:

* lines 514--515: all models train on ImageNet and use Stable Diffusion VAE latents of shape `32 x 32 x 4`, with bank capacity 256.
* line 519: ADM evaluation computes FID/IS over 50K generated samples and uses a 250-step Euler--Maruyama sampler.
* lines 526--528: comparison is on a SiT-XL backbone and reports the 80-epoch configuration.
* lines 566--568: REPA at 80 epochs is FID 1.98, IS 263.0.
* line 581: Ours at 80 epochs is FID 1.80, IS 272.4.

The local-only policy excludes acquiring remote GPU/paid/HF compute. No CPU substitute can reproduce the required trained SiT-XL/ImageNet/50K-sample FID/IS benchmark.
