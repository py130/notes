import re
import os



def delete_img(inputPath='', imgPath='assets'):
    actualInputPath = inputPath
    if inputPath == '':
        files = os.listdir('./')
        # 判断一个文件是否是md文件
        for f in files:
            if f.endswith('.md'):
                print('自动识别的md文件：', f)
                actualInputPath = f

    with open(actualInputPath, 'r', encoding='utf-8') as file:
        content = file.read()
        pattern = r'!\[.*\]\(assets/(.*?)\)'
        matches = re.findall(pattern, content)
        print('md文件中出现的图片：', matches)

        # 读取需要删除的图片的文件列表
        fileList = os.listdir(imgPath)
        print('文件夹中存在的图片：', fileList)
        for f in fileList:
            if f not in matches:
                print('删除多余文件 ', f)
                removedFilePath = os.path.join(imgPath, f)
                os.remove(removedFilePath)
        print('\n删除完成')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    delete_img('', 'assets')
