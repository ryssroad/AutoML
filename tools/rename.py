import os
import re

def replace_with_regex(content):
    # Замена miner* на rover*
    content = re.sub(r'miner(\w*)', lambda m: f'rover{m.group(1)}', content)
    # Замена Miner* на Rover*
    content = re.sub(r'Miner(\w*)', lambda m: f'Rover{m.group(1)}', content)
    return content

def should_skip_file(filename):
    """Проверяет, нужно ли пропустить файл"""
    skip_patterns = [
        r'\.git',
        r'\.pyc$',
        r'__pycache__',
        r'\.log$',
        r'\.json$',
        r'\.pkl$',
        r'rename\.py$'
    ]
    return any(re.search(pattern, filename) for pattern in skip_patterns)

def rename_in_file(filepath):
    """Выполняет замены в файле"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        original_content = content
        content = replace_with_regex(content)
            
        if content != original_content:
            print(f"Изменения в файле: {filepath}")
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
                
            # Если это файл miners.py, переименовываем его
            if os.path.basename(filepath) == "miners.py":
                new_filepath = os.path.join(os.path.dirname(filepath), "rovers.py")
                os.rename(filepath, new_filepath)
                print(f"Переименован файл: {filepath} -> {new_filepath}")
            
            # Если в имени файла есть miner, тоже переименовываем
            filename = os.path.basename(filepath)
            if 'miner' in filename.lower():
                new_filename = replace_with_regex(filename)
                new_filepath = os.path.join(os.path.dirname(filepath), new_filename)
                os.rename(filepath, new_filepath)
                print(f"Переименован файл: {filepath} -> {new_filepath}")
                
    except Exception as e:
        print(f"Ошибка при обработке файла {filepath}: {str(e)}")

def process_directory(directory):
    """Рекурсивно обрабатывает директорию"""
    for root, dirs, files in os.walk(directory):
        if should_skip_file(root):
            continue
            
        for file in files:
            if should_skip_file(file):
                continue
                
            if file.endswith(('.py', '.md', '.txt', '.yml', '.yaml', '.json')):
                filepath = os.path.join(root, file)
                rename_in_file(filepath)

def main():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Начинаем обработку директории: {project_dir}")
    
    # Создаем бэкап файла miners.py
    miners_path = os.path.join(project_dir, "dml", "miners.py")
    if os.path.exists(miners_path):
        backup_path = miners_path + ".backup"
        import shutil
        shutil.copy2(miners_path, backup_path)
        print(f"Создан бэкап: {backup_path}")
    
    process_directory(project_dir)
    print("Обработка завершена")

if __name__ == "__main__":
    main()