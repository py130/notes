import re
import os

deletedFiles = []
deletedNum = 0

def traverse_dir(path, mode):
    print(f'\n当前遍历文件夹： {path}')
    dirs = os.listdir(path)

    if mode == 'b':
        for item in dirs:
            itemPath = os.path.join(path, item)
            # 如果遍历到的是文件夹，则递归进入文件夹去判断 需要删除其中的assets文件夹下的多余图片
            if os.path.isdir(itemPath):
                traverse_dir(itemPath, mode)
            if os.path.isfile(itemPath):
                # 文件名
                f = item
                if f.endswith('.md'):
                    print('自动识别的md文件：', f)
                    mdPath = os.path.join(path, f)
                    fileName = f[:-3]
                    # 判断是否有assets文件夹，没有直接退出
                    assetPath = os.path.join(path, f'{fileName}.assets')
                    if not os.path.exists(assetPath):
                        print(f'该文件夹下无对应文件 "{fileName}" 的 {fileName}.assets 文件夹，跳过该文件\n')
                        continue
                    print('md文件路径：', mdPath)
                    print('asset文件夹路径：', assetPath)

                    delete_img([mdPath], assetPath)
    elif mode == 'a':
        # 判断是否有assets文件夹，没有直接退出
        assetPath = os.path.join(path, 'assets')
        if not os.path.exists(assetPath):
            print('该文件夹下无 assets 文件夹，跳过')
            return
        fileNameList = []
        for item in dirs:
            itemPath = os.path.join(path, item)
            # 如果遍历到的是文件夹，则递归进入文件夹去判断 需要删除其中的assets文件夹下的多余图片
            if os.path.isdir(itemPath):
                traverse_dir(itemPath, mode)
            if os.path.isfile(itemPath):
                # 文件名
                f = item
                if f.endswith('.md'):
                    mdPath = os.path.join(path, f)
                    fileNameList.append(mdPath)
        print(f'\n当前遍历文件夹： {path}')
        print('md文件路径：', fileNameList)
        print('asset文件夹路径：', assetPath)

        delete_img(fileNameList, assetPath)



def traverse_delete(path, mode):
    currentPath = os.getcwd() if path == '' else path
    traverse_dir(currentPath, mode)

# 由于obsidian在粘贴图片时，会自动将md文件中的图片路径中的空格转码为%20，但是不会转换assets文件夹中的图片路径，故在这里做一下替换
def decodeSpace(text):
    return text.replace('%20', ' ')

# 该函数原本的mdPath是一个字符串，只会读取一个文件，适用于图片文件夹为【filename.assets】的模式，但不适用于【assets】的模式，因为后者可能会多个文件对应一个文件夹
# 所以将其改为一个数组，读取传入的文件数组，并和文件路径进行对比。为了兼容filename.assets模式，该模式传入时将mdPath转化为一个元素的数组
def delete_img(mdPaths, assetPath='assets'):
    dealedMatchesList = []
    for mdPath in mdPaths:
        with open(mdPath, 'r', encoding='utf-8') as file:
            content = file.read()
            # print(content)
            pattern = r'!\[.*\]\(.*assets[\\/](.*?)\)'
            matches = re.findall(pattern, content)
            dealedMatches = []
            for item in matches:
                dealedMatches.append(decodeSpace(item))
            dealedMatchesList += dealedMatches
    print('md文件中出现的图片：', dealedMatchesList)

    # 读取需要删除的图片的文件列表
    fileList = os.listdir(assetPath)
    print('文件夹中存在的图片：', fileList)
    for f in fileList:
        if f not in dealedMatchesList:
            print('删除多余文件 ', f)
            removedFilePath = os.path.join(assetPath, f)
            os.remove(removedFilePath)
            # 已删除的文件加入统计列表
            deletedFiles.append(removedFilePath)
            # deletedNum = deletedNum + 1
    print('删除完成\n')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('\n使用前请将本代码放置于需要去除md文件的重复图片的文件夹下。\n')
    mode = ''
    while mode != 'a' and mode != 'b':
        mode = input('输入a或b选择不同的图片文件夹识别模式：(a)assets （b) filename.assets\n')
    print('已选择模式', mode, "，开始遍历文件夹\n")
    traverse_delete('', mode)
    print('共删除以下文件：', deletedFiles)
    # print('共删除文件数：', deletedNum)