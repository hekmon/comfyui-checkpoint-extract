# ComfyUI Checkpoint Extract

Extract CLIP and VAE models from a loaded checkpoint in ComfyUI.

## Intended use

The idea of this project is to separatly load the clip model(s) and vae model from a checkpoint once a [TensorRT engine](https://github.com/comfyanonymous/ComfyUI_TensorRT) has been built from a checkpoint. Normaly, after the engine is built, you need to load it separatly. But you still need the clip model and the var model into your workflow. The easiest way to do it is to keep the `Load checkpoint` on the original model to get them. But doing so, it will also load the original model which you don't need because you will use the compiled TensortRT engine.

This project allows to build the TensorRT engine while extracting the clip model(s) and vae model on the same pass: this way you can load the builded TensorRT engine along side with the clip and vae model without having to load the original checkpoint.

## Installation

### Comfy Manager

TODO

### Manually

TODO

## Example

In this example we will build a TensorRT version of the [DreamShaper XL v2.1 Turbo](https://civitai.com/models/112902?modelVersionId=351306) model. Download the model to the `models/checkpoints` directory to get started.

### Build & Extract

First download and import the extraction and build workflow. This workflows relies on custom nodes to work:

- ComfyUI Checkpoint Extract (this one obviously)
- [ComfyUI TensorRT](https://github.com/comfyanonymous/ComfyUI_TensorRT)
- [ComfyUI-Image-Saver](https://github.com/farizrifqi/ComfyUI-Image-Saver)
- [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)

![TensorRT build workflow with clip and vae on the fly extraction](res/TensorRT%20build.png)

You can get the workflow from [here](res/TensorRT%20build.json). Once the workflow is over, move the TensorRT output from `output/dreamshaperXL_v21TurboDPMSDE_$dyn-b-1-4-1-h-576-1152-1152-w-1024-2048-2048_00001_.engine` to `models/tensorrt/dreamshaperXL_v21TurboDPMSDE_$dyn-b-1-4-1-h-576-1152-1152-w-1024-2048-2048_00001_.engine`.

### Use models separately

Once the CLIP and VAE models are extracted, and the TensorRT engine put in the correct folder, you can use them separately in your workflows.

![Separately loading models](res/trt_split_loading.png)

### Full workflow

If you are interested in a complete workflow with HiRes fix + 4k upscale based on this example, you can find it [here](res/DreamShaper%20XL%20Turbo%20TRT%20HiRes.json).

![full workflow screenshot](res/fullworkflow.png)
