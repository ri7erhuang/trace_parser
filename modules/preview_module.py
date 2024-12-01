from base_module import BaseClass


class Preview(BaseClass):
    def __init__(self):
        super().__init__()
        # 追加Preview模块特有的关键字
        self.keywords.append("Preview特定关键字")

    def process(self, parsed_content):
        for keyword, lines in parsed_content.items():
            print(f"Preview: 关键字 '{keyword}' 相关的内容:")
            for line in lines:
                print(line)
