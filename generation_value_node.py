class ImageCounterNode:
    image_count = 0  # Глобальный счётчик обработанных изображений

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_image": ("IMAGE",),  # Входное изображение
                "total_images": ("INT", {"default": 10}),  # Общее количество ожидаемых изображений
            }
        }

    RETURN_TYPES = ("INT", "IMAGE")
    FUNCTION = "process_image"
    CATEGORY = "Custom Nodes"

    def process_image(self, input_image, total_images):
        # Увеличиваем счётчик при каждом вызове узла
        ImageCounterNode.image_count += 1

        # Определение порогов для 70%, 20%, и 10%
        threshold_70 = int(total_images * 0.7)
        threshold_90 = int(total_images * 0.9)

        # Определяем возвращаемое значение на основе счётчика
        if ImageCounterNode.image_count <= threshold_70:
            value = 100
        elif ImageCounterNode.image_count <= threshold_90:
            value = 200
        else:
            value = 300

        # Возвращаем значение и входное изображение
        return value, input_image
