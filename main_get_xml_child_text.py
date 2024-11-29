import os
import xml.etree.ElementTree as ET
import time
start1=time.perf_counter()
#开始时间记录
def get_filelist(dir):
    Filelist = []
    #定义一个字典用于存储xml文件的文件路径
    for home, dirs, files in os.walk('xml所在文件夹，格式eg：C:\\CHECKTEST\\FTXML\\'):
        for filename in files:
            # 文件名列表，包含完整路径
            Filelist.append(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            # Filelist.append( filename)
            #遍历出的xml文件路径放到Filelist字典传递给后面的函数用于构建xml树
    return Filelist
#主函数
if __name__ == "__main__":
  #创建输出文件
  xml=0
  error=0
  b=1
  with open('C:\\CHECKTEST\\result\\output.txt','w',encoding='utf-8') as f:
  #先打开output.txt作为所有child.text输出文件
   Filelist = get_filelist(dir)
   for file in Filelist:
    if file.endswith('.xml'):
      print(file)
      xml = xml + b
      tree = ET.parse(file)
      root= tree.getroot()
    #剔除非xml文件，输出文件名
    else:
      print(file)
      error = error + b

    #遍历所有子元素，筛选出Itemname的text，提取输出到txt文件
    for child in root.iter():
        if child.text is not None:
            if child.tag == '改为tag名':
                if len(child.text) == 52 or len(child.text) == 54 or len(child.text) == 50:
                #这里是用条件限制一下要筛选的text长度，也可以通过其他特征进行筛选
                  f.write(child.text + '\n')
                  print(child.tag, child.text)
                  print(len(child.text))
打印出程序运行时间，还有xml文件数、非xml文件数
end=time.perf_counter()
print(end-start1)
print('.xml file=')
print(xml)
print('.xml.error file=')
print(error)
print('all file=')
print(xml+error)
