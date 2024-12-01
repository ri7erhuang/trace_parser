import importlib
import os
from concurrent.futures import ThreadPoolExecutor

MAX_THREADS = 6


def handle_file(module, filepath):
    print(f"处理文件: {filepath}")
    if hasattr(module, 'execute') and callable(getattr(module, 'execute')):
        module.execute()
    else:
        print(f"Module {module} does not have an 'execute' function.")


def get_valid_path(path_input):
    if os.path.exists(path_input):
        if os.path.isfile(path_input):
            return path_input
        elif os.path.isdir(path_input):
            return path_input
        else:
            print("提供的路径既不是文件也不是文件夹，请重新输入。")
            return None
    else:
        print("提供的路径不存在，请重新输入。")
        return None


def process_files_in_folder(module, folder_path):
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                process_file(module, file_path, executor)


def process_file(module, file_path, executor):
    if file_path.endswith('.html'):
        if executor:
            executor.submit(handle_file, module, file_path)
        else:
            handle_file(module, file_path)


# 主程序流程控制部分
def process_trace(selected_module):
    while True:
        path_input = input("请输入一个文件夹路径或文件的绝对路径: ")
        valid_path = get_valid_path(path_input)
        if not valid_path:
            continue
        elif os.path.isfile(valid_path):
            process_file(selected_module, valid_path, None)
        elif os.path.isdir(valid_path):
            process_files_in_folder(selected_module, valid_path)
        else:
            print("输入的路径类型无法确定，请重新输入。")
        break


def load_module(name):
    try:
        # 动态加载模块
        m = importlib.import_module(name)
        return m
    except ImportError as e:
        print(f"读取模块 {name} 错误: {e}")
        return None


def choose_module():
    project_root = os.path.dirname(os.path.abspath(__file__))
    modules_dir = os.path.join(project_root, 'modules')
    files = [f for f in os.listdir(modules_dir) if f.endswith('.py') and not f.startswith('__')]
    module_names = [os.path.splitext(f)[0] for f in files]
    index = 1
    for module_name in module_names:
        print(f'{index}.{module_name}')
        index = index + 1
    try:
        choice = int(input("请选择这些trace的场景: "))
        if choice < 1 or choice > len(module_names):
            raise ValueError("Invalid choice, please enter a number within the range.")
    except ValueError as e:
        print(f"错误: {e}")
    else:
        # 根据用户选择的序号获取模块名
        selected_module_name = module_names[choice - 1]
        return load_module(selected_module_name)


if __name__ == "__main__":
    m = choose_module()
    process_trace(m)
