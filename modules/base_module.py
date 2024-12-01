class BaseClass:
    def __init__(self):
        # 父类中定义一些通用的关键字
        self.keywords = ["通用关键字1", "通用关键字2"]

    def read_file(self, filepath):
        try:
            with open(filepath, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"文件 {filepath} 未找到。")
            return None

    def parse_file(self, content):
        parsed_content = {}
        for keyword in self.keywords:
            parsed_content[keyword] = []
            for line in content.splitlines():
                if keyword in line:
                    parsed_content[keyword].append(line)
        return parsed_content

    def execute(self, filepath):
        content = self.read_file(filepath)
        if content is not None:
            parsed_content = self.parse_file(content)
            self.process(parsed_content)

    def process(self, parsed_content):
        raise NotImplementedError("子类必须实现这个方法")