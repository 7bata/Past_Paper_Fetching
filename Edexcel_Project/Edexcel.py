import requests
from lxml import etree
import os
import time
import re
import datetime
from urllib.parse import urljoin, unquote

# 设置请求头，模拟浏览器行为
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

base_url = "https://papers.xtremepape.rs/"
# 创建日志目录
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
# 获取当前时间作为日志文件名的一部分
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 定义日志文件名
download_log_file = os.path.join(log_dir, f"download_activity_log_{timestamp}.txt")
failed_log_file = os.path.join(log_dir, f"download_failures_{timestamp}.txt")

# 初始化日志文件
with open(download_log_file, "w", encoding="utf-8") as f:
    f.write(f"Download Activity Log - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("="*50 + "\n\n")

with open(failed_log_file, "w", encoding="utf-8") as f:
    f.write(f"Download Failures Log - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("="*50 + "\n\n")

def log_message(message, log_file=download_log_file):
    """记录日志消息，并添加时间戳"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[{timestamp}] {message}"
    print(formatted_message)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{formatted_message}\n")

def log_failure(file_url, file_name, error_message, category_path):
    """记录下载失败的文件"""
    fail_msg = f"Download Failed: {file_name} - URL: {file_url} - Error: {error_message} - Path: {category_path}"
    log_message(fail_msg, download_log_file)
    
    # 同时记录到失败日志文件
    with open(failed_log_file, "a", encoding="utf-8") as f:
        # 记录格式: URL|文件名|路径
        f.write(f"{file_url}|{file_name}|{category_path}\n")

def get_categories(url):
    """获取Edexcel的所有主要类别（如Advanced Level, International GCSE等）"""
    log_message("Fetching main categories...")
    response = requests.get(url, headers=headers).content
    tree = etree.HTML(response)
    
    # 使用正确的xpath表达式选取主内容表格中的所有目录
    category_links = tree.xpath('//table[@id="main_content"]/tr[position()>1]/td[@class="fname"]/a[@class="directory"]')
    
    categories = []
    for link in category_links:
        category_name = link.text.strip('[]')
        if category_name == "..":  # 跳过返回上级目录的链接
            continue
        category_url = link.get('href')
        categories.append((category_name, urljoin(base_url, category_url)))
    
    return categories

def get_content_items(url):
    """获取目录中的所有文件和子目录"""
    response = requests.get(url, headers=headers).content
    tree = etree.HTML(response)
    
    # 获取当前目录中的所有链接（包括文件和子目录）
    items = []
    
    # 获取子目录
    dir_links = tree.xpath('//table[@id="main_content"]/tr[position()>1]/td[@class="fname"]/a[@class="directory"]')
    for link in dir_links:
        name = link.text.strip('[]')
        if name == "..":  # 跳过返回上级目录的链接
            continue
        url = urljoin(base_url, link.get('href'))
        items.append(('directory', name, url))
    
    # 获取文件
    file_links = tree.xpath('//table[@id="main_content"]/tr[position()>1]/td[@class="fname"]/a[not(@class="directory")]')
    for link in file_links:
        name = link.text
        url = urljoin(base_url, link.get('href'))
        items.append(('file', name, url))
    
    return items

def sanitize_filename(filename):
    """处理文件名，移除非法字符"""
    # 将Windows不允许的文件名字符替换为下划线
    sanitized = re.sub(r'[\\/*?:"<>|]', '_', filename)
    return sanitized

def download_file(url, save_path):
    """下载文件并保存到指定路径"""
    try:
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()  # 检查请求是否成功
        
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return True, None
    except Exception as e:
        return False, str(e)

def create_directories_from_path(base_dir, path_parts):
    """根据路径部分创建嵌套目录结构，并返回最终目录路径"""
    current_path = base_dir
    for part in path_parts:
        if part:  # 忽略空字符串
            sanitized_part = sanitize_filename(part)
            current_path = os.path.join(current_path, sanitized_part)
            os.makedirs(current_path, exist_ok=True)
    return current_path

def extract_path_from_url(url):
    """从URL中提取目录路径部分，修复嵌套问题"""
    if 'dirpath=' in url:
        path = unquote(url.split('dirpath=')[1].split('&')[0])
        # 提取Edexcel之后的路径部分，确保只保留相对路径
        if './Edexcel/' in path:
            path = path.split('./Edexcel/')[1]
            # 删除路径最后的空元素(如果有)
            if path.endswith('/'):
                path = path[:-1]
            return path
    return ""

def get_path_components(category_name, path_str):
    """
    从URL路径中提取组件，避免重复嵌套
    如果path_str已经包含category_name，则不再添加category_name
    """
    if not path_str:
        return [category_name]
    
    parts = [p for p in path_str.split('/') if p]
    
    # 检查第一个部分是否与category_name相同
    if parts and parts[0].lower() == category_name.lower():
        return parts  # 如果类别名已经在路径中，直接返回路径部分
    else:
        return [category_name] + parts  # 否则添加类别名作为前缀

def crawl_recursively(url, base_save_path, category_name, max_depth=3, current_depth=0):
    """
    递归爬取目录及其子目录中的内容，保持原始目录结构
    修复了重复嵌套问题
    """
    if current_depth > max_depth:
        return
    
    # 获取当前URL对应的路径
    path_str = extract_path_from_url(url)
    if path_str:
        log_message(f"Crawling {path_str}...")
    else:
        log_message(f"Crawling URL: {url}")
    
    try:
        items = get_content_items(url)
    except Exception as e:
        log_message(f"Failed to get content for {url}: {e}")
        return
    
    # 获取规范化的路径部分，避免重复嵌套
    path_parts = get_path_components(category_name, path_str)
    
    # 创建目录结构
    save_dir = create_directories_from_path(base_save_path, path_parts)
    
    # 下载文件
    file_count = 0
    success_count = 0
    failed_count = 0
    
    for item_type, name, item_url in items:
        if item_type == 'file':  # 下载所有文件
            file_count += 1
            log_message(f"Downloading file ({file_count}/{len([i for i, _, _ in items if i == 'file'])}): {name}")
            file_path = os.path.join(save_dir, sanitize_filename(name))
            
            # 检查文件是否已存在且大小正常
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                log_message(f"File already exists, skipping: {file_path}")
                success_count += 1
                continue
                
            success, error = download_file(item_url, file_path)
            if success:
                log_message(f"File saved to: {file_path}")
                success_count += 1
            else:
                log_message(f"Download failed: {name} - {error}")
                log_failure(item_url, name, error, '/'.join(path_parts))
                failed_count += 1
            time.sleep(0.5)  # 略微减少延迟，但保持适当间隔避免IP被封
        elif item_type == 'directory' and current_depth < max_depth:
            # 递归爬取子目录
            log_message(f"Entering subdirectory: {name}")
            crawl_recursively(item_url, base_save_path, category_name, max_depth, current_depth + 1)
    
    path_display = '/'.join(path_parts) if path_parts else "Root"
    log_message(f"Directory {path_display} download complete, Total files: {file_count}, Success: {success_count}, Failed: {failed_count}")

def split_categories_into_groups(categories, group_count=3):
    """将类别分成几组"""
    group_size = len(categories) // group_count
    if len(categories) % group_count != 0:
        group_size += 1
    
    groups = []
    for i in range(0, len(categories), group_size):
        groups.append(categories[i:i + group_size])
    
    return groups

def display_category_groups(category_groups):
    """显示类别组选择菜单"""
    print("\n=========== Category Groups ===========")
    for i, group in enumerate(category_groups, 1):
        category_names = [name for name, _ in group]
        print(f"Group {i} ({len(group)} categories): {', '.join(category_names)}")
    print("=====================================")

def download_from_failed_log():
    """从失败记录日志中重新下载文件"""
    if not os.path.exists(failed_log_file) or os.path.getsize(failed_log_file) == 0:
        log_message("No failure log found or log is empty")
        return
    
    log_message("Starting to re-download files from failure log...")
    downloads_dir = "downloads"
    os.makedirs(downloads_dir, exist_ok=True)
    
    with open(failed_log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # 跳过头两行（标题和分隔线）
    actual_failures = [line.strip() for line in lines if "|" in line]
    
    if not actual_failures:
        log_message("No valid download items in failure log")
        return
    
    log_message(f"Found {len(actual_failures)} failed download items")
    
    success_count = 0
    still_failed = []
    
    for i, line in enumerate(actual_failures, 1):
        parts = line.split("|")
        if len(parts) < 2:
            log_message(f"Invalid failure record: {line}")
            continue
        
        file_url = parts[0]
        file_name = parts[1]
        path = parts[2] if len(parts) > 2 else ""
        
        log_message(f"Re-downloading ({i}/{len(actual_failures)}): {file_name}")
        
        # 创建路径结构
        path_parts = path.split('/') if path else []
        save_dir = create_directories_from_path(downloads_dir, path_parts)
        
        file_path = os.path.join(save_dir, sanitize_filename(file_name))
        
        success, error = download_file(file_url, file_path)
        if success:
            log_message(f"File saved to: {file_path}")
            success_count += 1
        else:
            log_message(f"Re-download failed: {file_name} - {error}")
            still_failed.append((file_url, file_name, error, path))
        
        time.sleep(0.5)  # 保持适当间隔
    
    # 记录仍然失败的项
    if still_failed:
        retry_log_file = os.path.join(log_dir, f"retry_failures_{timestamp}.txt")
        with open(retry_log_file, "w", encoding="utf-8") as f:
            f.write(f"Retry Failures Log - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*50 + "\n\n")
            for url, name, error, path in still_failed:
                f.write(f"{url}|{name}|{path}\n")
        
        log_message(f"{len(still_failed)} items still failed to download, details saved to {retry_log_file}")
    
    log_message(f"Re-download complete, Success: {success_count}, Failed: {len(still_failed)}")

# 主程序
if __name__ == "__main__":
    # 获取所有类别 - Edexcel URL
    edexcel_url = "https://papers.xtremepape.rs/index.php?dirpath=./Edexcel/&order=0"
    categories = get_categories(edexcel_url)
    
    log_message(f"Found {len(categories)} categories")
    
    # 保存类别列表
    with open("category_list.txt", "w", encoding="utf-8") as f:
        f.write("Category List:\n")
        for i, (name, url) in enumerate(categories, 1):
            f.write(f"{i}. {name} - {url}\n")
    
    log_message("All categories saved to category_list.txt")
    
    # 将类别分成组
    category_groups = split_categories_into_groups(categories, 2)  # Edexcel可能类别较少，分2组
    
    while True:
        print("\nPlease select an operation:")
        print("1. Download a category group")
        print("2. Re-download from failure log")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            display_category_groups(category_groups)
            group_index = int(input("\nEnter the group number to download (1-2): ")) - 1
            
            if 0 <= group_index < len(category_groups):
                selected_group = category_groups[group_index]
                log_message(f"\nSelected Group {group_index + 1} with {len(selected_group)} categories")
                
                # 创建下载目录
                downloads_dir = "downloads"
                os.makedirs(downloads_dir, exist_ok=True)
                
                # 设置爬取深度
                max_depth = 5  # Edexcel可能有更深的嵌套，设为5级
                log_message(f"Setting crawl depth to: {max_depth}")
                
                # 开始批量下载选中组的所有类别
                log_message("\nStarting batch download of all categories in the selected group...")
                for i, (category_name, category_url) in enumerate(selected_group, 1):
                    log_message(f"\n===== Processing category ({i}/{len(selected_group)}): {category_name} =====")
                    # 使用修复后的递归爬取函数
                    crawl_recursively(category_url, downloads_dir, category_name, max_depth, 0)
                
                log_message(f"\nAll categories in Group {group_index + 1} have been downloaded!")
                log_message(f"Download log saved to: {download_log_file}")
                log_message(f"Failure log saved to: {failed_log_file}")
                
            else:
                log_message("Group index out of range")
        
        elif choice == '2':
            download_from_failed_log()
        
        elif choice == '3':
            log_message("Exiting program")
            break
        
        else:
            log_message("Invalid option, please try again") 