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
# 定义日志文件名（更通俗易懂，不使用中文）
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

def log_failure(subject_url, file_name, error_message, subject_name):
    """记录下载失败的文件"""
    fail_msg = f"Download Failed: {file_name} - URL: {subject_url} - Error: {error_message} - Subject: {subject_name}"
    log_message(fail_msg, download_log_file)
    
    # 同时记录到失败日志文件
    with open(failed_log_file, "a", encoding="utf-8") as f:
        # 记录格式: URL|文件名|科目名
        f.write(f"{subject_url}|{file_name}|{subject_name}\n")

def get_subjects(url):
    """获取所有科目目录"""
    log_message("Fetching subject list...")
    response = requests.get(url, headers=headers).content
    tree = etree.HTML(response)
    
    # 使用正确的xpath表达式选取主内容表格中的所有科目目录
    subject_links = tree.xpath('//table[@id="main_content"]/tr[position()>1]/td[@class="fname"]/a[@class="directory"]')
    
    subjects = []
    for link in subject_links:
        subject_name = link.text.strip('[]')
        subject_url = link.get('href')
        subjects.append((subject_name, urljoin(base_url, subject_url)))
    
    return subjects

def get_files_in_subject(subject_url):
    """获取科目目录中的所有文件和子目录"""
    response = requests.get(subject_url, headers=headers).content
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

def crawl_subject_recursively(subject_url, subject_name, base_save_path, max_depth=2, current_depth=0):
    """递归爬取科目目录及其子目录中的内容"""
    if current_depth > max_depth:
        return
    
    log_message(f"Crawling {subject_name} - {subject_url}...")
    
    try:
        items = get_files_in_subject(subject_url)
    except Exception as e:
        log_message(f"Failed to get content for {subject_name}: {e}")
        return
    
    # 创建以科目名称命名的目录
    subject_dir = os.path.join(base_save_path, sanitize_filename(subject_name))
    os.makedirs(subject_dir, exist_ok=True)
    
    # 如果是子目录（不是顶级科目目录），在科目目录下创建子目录结构
    if current_depth > 0:
        # 从URL中提取目录路径的最后部分作为子目录名
        current_dir = unquote(subject_url.split('dirpath=')[1].split('&')[0])
        path_parts = current_dir.split('/')
        # 仅使用最后一部分作为子目录名
        sub_dir_name = path_parts[-1] if path_parts[-1] else path_parts[-2]
        save_dir = os.path.join(subject_dir, sanitize_filename(sub_dir_name))
        os.makedirs(save_dir, exist_ok=True)
    else:
        save_dir = subject_dir
    
    # 下载文件
    file_count = 0
    success_count = 0
    failed_count = 0
    
    for item_type, name, url in items:
        if item_type == 'file':  # 下载所有文件
            file_count += 1
            log_message(f"Downloading file ({file_count}/{len([i for i, _, _ in items if i == 'file'])}): {name}")
            file_path = os.path.join(save_dir, sanitize_filename(name))
            
            # 检查文件是否已存在且大小正常
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                log_message(f"File already exists, skipping: {file_path}")
                success_count += 1
                continue
                
            success, error = download_file(url, file_path)
            if success:
                log_message(f"File saved to: {file_path}")
                success_count += 1
            else:
                log_message(f"Download failed: {name} - {error}")
                log_failure(url, name, error, subject_name)
                failed_count += 1
            time.sleep(0.5)  # 略微减少延迟，但保持适当间隔避免IP被封
        elif item_type == 'directory' and current_depth < max_depth:
            # 递归爬取子目录
            log_message(f"Entering subdirectory: {name}")
            crawl_subject_recursively(url, subject_name, base_save_path, max_depth, current_depth + 1)
    
    log_message(f"Directory {subject_name} download complete, Total files: {file_count}, Success: {success_count}, Failed: {failed_count}")

def split_subjects_into_groups(subjects, group_count=4):
    """将科目分成几组"""
    group_size = len(subjects) // group_count
    if len(subjects) % group_count != 0:
        group_size += 1
    
    groups = []
    for i in range(0, len(subjects), group_size):
        groups.append(subjects[i:i + group_size])
    
    return groups

def display_subject_groups(subject_groups):
    """显示科目组选择菜单"""
    print("\n=========== Subject Groups ===========")
    for i, group in enumerate(subject_groups, 1):
        subject_names = [name for name, _ in group]
        print(f"Group {i} ({len(group)} subjects): {', '.join(subject_names[:3])}{'...' if len(subject_names) > 3 else ''}")
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
        subject_name = parts[2] if len(parts) > 2 else "Unknown"
        
        log_message(f"Re-downloading ({i}/{len(actual_failures)}): {file_name}")
        
        # 创建以科目名称命名的目录
        subject_dir = os.path.join(downloads_dir, sanitize_filename(subject_name))
        os.makedirs(subject_dir, exist_ok=True)
        
        file_path = os.path.join(subject_dir, sanitize_filename(file_name))
        
        success, error = download_file(file_url, file_path)
        if success:
            log_message(f"File saved to: {file_path}")
            success_count += 1
        else:
            log_message(f"Re-download failed: {file_name} - {error}")
            still_failed.append((file_url, file_name, error, subject_name))
        
        time.sleep(0.5)  # 保持适当间隔
    
    # 记录仍然失败的项
    if still_failed:
        retry_log_file = os.path.join(log_dir, f"retry_failures_{timestamp}.txt")
        with open(retry_log_file, "w", encoding="utf-8") as f:
            f.write(f"Retry Failures Log - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*50 + "\n\n")
            for url, name, error, subject in still_failed:
                f.write(f"{url}|{name}|{subject}\n")
        
        log_message(f"{len(still_failed)} items still failed to download, details saved to {retry_log_file}")
    
    log_message(f"Re-download complete, Success: {success_count}, Failed: {len(still_failed)}")

# 主程序
if __name__ == "__main__":
    # 获取所有科目
    subjects_url = "https://papers.xtremepape.rs/index.php?dirpath=./CAIE/AS+and+A+Level/&order=0"
    subjects = get_subjects(subjects_url)
    
    log_message(f"Found {len(subjects)} subjects")
    
    # 保存科目列表
    with open("subject_list.txt", "w", encoding="utf-8") as f:
        f.write("Subject List:\n")
        for i, (name, url) in enumerate(subjects, 1):
            f.write(f"{i}. {name} - {url}\n")
    
    log_message("All subjects saved to subject_list.txt")
    
    # 将科目分成4组
    subject_groups = split_subjects_into_groups(subjects, 4)
    
    while True:
        print("\nPlease select an operation:")
        print("1. Download a subject group")
        print("2. Re-download from failure log")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            display_subject_groups(subject_groups)
            group_index = int(input("\nEnter the group number to download (1-4): ")) - 1
            
            if 0 <= group_index < len(subject_groups):
                selected_group = subject_groups[group_index]
                log_message(f"\nSelected Group {group_index + 1} with {len(selected_group)} subjects")
                
                # 创建下载目录
                downloads_dir = "downloads"
                os.makedirs(downloads_dir, exist_ok=True)
                
                # 设置爬取深度
                max_depth = 2  # 默认设置为2级深度
                log_message(f"Setting crawl depth to: {max_depth}")
                
                # 开始批量下载选中组的所有科目
                log_message("\nStarting batch download of all subjects in the selected group...")
                for i, (subject_name, subject_url) in enumerate(selected_group, 1):
                    log_message(f"\n===== Processing subject ({i}/{len(selected_group)}): {subject_name} =====")
                    crawl_subject_recursively(subject_url, subject_name, downloads_dir, max_depth, 0)
                
                log_message(f"\nAll subjects in Group {group_index + 1} have been downloaded!")
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



