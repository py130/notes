import re
import os

def traverse_dir(path):
    dirs = os.listdir(path)
    for item in dirs:
        itemPath = os.path.join(path, item)
        # 如果遍历到的是文件夹，则递归进入文件夹去判断 需要删除其中的assets文件夹下的多余图片
        if os.path.isdir(itemPath):
            traverse_dir(itemPath)

        if os.path.isfile(itemPath):
            # 文件名
            f = item
            if f.endswith('.md'):
                print('自动识别的md文件：', f)
                mdPath = os.path.join(path, f)
                # 判断是否有assets文件夹，没有直接退出
                assetPath = os.path.join(path, 'assets')
                if not os.path.exists(assetPath):
                    print('该文件夹下无 assets 文件夹，跳过')
                    continue
                print('md文件路径：', mdPath)
                print('asset文件夹路径：', assetPath)

                delete_img(mdPath, assetPath)



def traverse_delete(path):
    currentPath = os.getcwd()
    traverse_dir(currentPath)

# 由于obsidian在粘贴图片时，会自动将md文件中的图片路径中的空格转码为%20，但是不会转换assets文件夹中的图片路径，故在这里做一下替换
def decodeSpace(text):
    return text.replace('%20', ' ')

def delete_img(mdPath, assetPath='assets'):
    with open(mdPath, 'r', encoding='utf-8') as file:
        content = file.read()
        pattern = r'!\[.*\]\(assets/(.*?)\)'
        matches = re.findall(pattern, content)
        dealedMatches = []
        for item in matches:
            dealedMatches.append(decodeSpace(item))
        print('md文件中出现的图片：', dealedMatches)

        # 读取需要删除的图片的文件列表
        fileList = os.listdir(assetPath)
        print('文件夹中存在的图片：', fileList)
        for f in fileList:
            if f not in dealedMatches:
                print('删除多余文件 ', f)
                removedFilePath = os.path.join(assetPath, f)
                os.remove(removedFilePath)
        print('删除完成\n')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    traverse_delete('./')