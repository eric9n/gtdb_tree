import json

def check_python_version(json_file, version_prefix, platform):
    with open(json_file, 'r') as f:
        data = json.load(f)

    versions = []
    for item in data:
        if item['version'].startswith(version_prefix):
            for file in item['files']:
                if file['platform'] == platform:
                    versions.append((item['version'], file['arch']))
    return versions

# 假设 JSON 文件保存为 'python_versions.json'
json_file = 'version.json'

# 检查所有平台的 Python 版本
platforms = ["win32", "darwin", "linux"]
versions_to_check = ["3.7", "3.8", "3.9", "3.10", "3.11"]

for platform in platforms:
    print(f"\nChecking versions for {platform}:")
    for version in versions_to_check:
        supported = check_python_version(json_file, version, platform)
        if supported:
            print(f"  Python {version} versions available:")
            for ver, arch in supported:
                print(f"    Version: {ver}, Architecture: {arch}")
        else:
            print(f"  No Python {version} versions found for {platform}")
