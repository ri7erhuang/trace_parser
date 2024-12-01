from base_module import BaseClass


class Capture(BaseClass):
    def __init__(self):
        super().__init__()
        self.keywords.append("capture特定关键字")

    def process(self, parsed_content):
        for keyword, lines in parsed_content.items():
            print(f"Capture: 关键字 '{keyword}' 相关的内容:")
            for line in lines:
                print(line)
