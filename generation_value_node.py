class GenerationValueNode:
    generation_count = 0  # Счётчик сохраняется как атрибут класса

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "total_generations": ("INT", {"default": 10}),  # Общее количество генераций
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "get_value"
    CATEGORY = "Custom Nodes"

    def get_value(self, total_generations):
        # Определение порогов для 70%, 20%, и 10%
        threshold_70 = int(total_generations * 0.7)
        threshold_90 = int(total_generations * 0.9)

        # Увеличиваем счётчик текущей генерации
        GenerationValueNode.generation_count += 1

        # Определяем значение на основе текущей генерации
        if GenerationValueNode.generation_count <= threshold_70:
            return (100,)
        elif GenerationValueNode.generation_count <= threshold_90:
            return (200,)
        else:
            return (300,)
