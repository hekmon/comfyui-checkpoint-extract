import os
import safetensors.torch

from comfy.comfy_types import IO
# from comfy.sd import detect_te_model, TEModel

class CLIPModelSaver:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "clip": (IO.CLIP,),  # Input type for CLIP models in ComfyUI
                "output_name": ("STRING", {"default": "extracted_model", "tooltip": "The model file name without extension ('_clip.safetensors' will be appended automatically)."}),
                "output_folder": ("STRING", {"default": "models/text_encoders", "tooltip": "The destination folder to output the model to."})
            }
        }

    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "save_clip_model"
    OUTPUT_NODE = True
    CATEGORY = "Models Savers"

    def save_clip_model(self, clip, output_name, output_folder):
        # clip is a comfy.sd.CLIP object
        sd_clip = clip.get_sd()

        # Detect Dual CLIP model parts (if available) and set flags accordingly
        clip_g, clip_l = False, False
        for layer_name in sd_clip.keys():
            if layer_name.startswith("clip_g.transformer."):
                clip_g = True
                if clip_l:
                    break
            elif layer_name.startswith("clip_l.transformer."):
                clip_l = True
                if clip_g:
                    break

        # If dual CLIP model parts are detected, handle them separately
        if clip_g and clip_l:
            print("Dual CLIP model detected. Saving both parts separately and removing layer names prefix.")
            # Clip G
            clip_g_weights = {
                key.removeprefix("clip_g.transformer."): value
                for key, value in sd_clip.items()
                if key.startswith("clip_g.transformer.")
            }
            output_path = os.path.join(os.path.normpath(output_folder), f"{output_name}_clip-g.safetensors")
            print(f"CLIP Model Saver: Saving CLIP G model to: {output_path}")
            safetensors.torch.save_file(clip_g_weights, output_path)
            # Clip L
            clip_l_weights = {
                key.removeprefix("clip_l.transformer."): value
                for key, value in sd_clip.items()
                if key.startswith("clip_l.transformer.")
            }
            output_path = os.path.join(os.path.normpath(output_folder), f"{output_name}_clip-l.safetensors")
            print(f"CLIP Model Saver: Saving CLIP L model to: {output_path}")
            safetensors.torch.save_file(clip_l_weights, output_path)
        else:
            output_path = os.path.join(os.path.normpath(output_folder), f"{output_name}_clip.safetensors")
            print(f"CLIP Model Saver: Saving CLIP L model to: {output_path}")
            safetensors.torch.save_file(sd_clip, output_path)

        return ()


class VAEModelSaver:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "vae": (IO.VAE,),  # Input type for VAE models in ComfyUI
                "output_name": ("STRING", {"default": "extracted_model", "tooltip": "The model file name without extension ('_vae.safetensors' will be appended automatically)."}),
                "output_folder": ("STRING", {"default": "models/vae", "tooltip": "The destination folder to output the model to."})
            }
        }

    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "save_vae_model"
    OUTPUT_NODE = True
    CATEGORY = "Models Savers"

    def save_vae_model(self, vae, output_name, output_folder):
        # vae is a comfy.sd.VAE object
        output_path = os.path.join(os.path.normpath(output_folder), f"{output_name}_vae.safetensors")
        print(f"VAE Model Saver: Saving VAE model to: {output_path}")
        safetensors.torch.save_file(vae.get_sd(), output_path)
        return ()
