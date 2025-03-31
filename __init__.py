from .model_savers import CLIPModelSaver, VAEModelSaver

NODE_CLASS_MAPPINGS = {
    "VAEModelSaver": VAEModelSaver,
    "CLIPModelSaver": CLIPModelSaver
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VAEModelSaver": "VAE Model Saver",
    "CLIPModelSaver": "CLIP Model Saver"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
