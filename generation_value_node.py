class GenerationValueNode:
    generation_count = 0  # Счетчик текущих генераций

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
        # Определение порогов для 70%, 20% и 10%
        threshold_70 = int(total_generations * 0.7)
        threshold_90 = int(total_generations * 0.9)

        # Увеличиваем счетчик текущей генерации
        self.generation_count += 1

        # Определяем значение для текущей генерации
        if self.generation_count <= threshold_70:
            return (100,)
        elif self.generation_count <= threshold_90:
            return (200,)
        else:
            return (300,)