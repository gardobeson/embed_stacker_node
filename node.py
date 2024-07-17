from pathlib import Path

import folder_paths

class embed_stacker_node:
    
    @classmethod
    def INPUT_TYPES(self):
        embeddings = ["None"] + folder_paths.get_filename_list("embeddings")

        return {
            "required": {
                "embedding1": (embeddings,),
                "embedding2": (embeddings,),
                "embedding3": (embeddings,),
                "embedding4": (embeddings,),
                "emphasis": (
                    "FLOAT",
                    {
                        "default": 1.0,
                        "min": 0.0,
                        "max": 3.0,
                        "step": 0.05,
                    },
                ),
                "append": (
                    "BOOLEAN",
                    {"default": False, "label_on": "true ", "label_off": "false "},
                ),
                "text": ("STRING", {"multiline": True}),
            },
        }


    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "concat_embedding"
    OUTPUT_NODE = False

    CATEGORY = "utils"

    def concat_embedding(self, text, embedding1, embedding2, embedding3, embedding4, emphasis, append):
        if emphasis < 0.05:
            return (text,)

        emb1 = "embedding1:" + Path(embedding1).stem
        emb2 = "embedding2:" + Path(embedding2).stem
        emb3 = "embedding3:" + Path(embedding3).stem
        emb4 = "embedding4:" + Path(embedding4).stem

        emphasis = f"{emphasis:.3f}"

        if emphasis != "1.000":
            emb1 = f"({emb1}:{emphasis})"
            emb2 = f"({emb2}:{emphasis})"
            emb3 = f"({emb3}:{emphasis})"
            emb4 = f"({emb4}:{emphasis})"

        output = f"{text}, {emb1}, {emb2}, {emb3}, {emb4}" if append else f"{emb1}, {emb2}, {emb3}, {emb4}, {text}"

        return (output,)


# NODE_CLASS_MAPPINGS = {
#     "embed_stacker_node": embed_stacker_node
# }

# # A dictionary that contains the friendly/humanly readable titles for the nodes
# NODE_DISPLAY_NAME_MAPPINGS = {
#     "embed_stacker_node": "Embed Stacker"
# }
