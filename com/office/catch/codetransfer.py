# encoding=utf-8

if __name__ == '__main__':
    text = open("/Users/yangjie/Desktop/斗罗大陆2绝世唐门.txt", "rb")
    s=text.read()
    
    
    import codecs
    
    fin = open("/Users/yangjie/Desktop/斗罗大陆2绝世唐门.txt", 'r')
    fout = open("/Users/yangjie/Desktop/斗罗大陆2绝世唐门2.txt", 'w')
    
    reader = codecs.getreader('gbk')(fin)
    writer = codecs.getwriter('gbk')(fout)
    
    data = reader.read(10)
    #10是最大字节数，默认值为-1表示尽可能大。可以避免一次处理大量数据
    while data:
        writer.write(data)
        data = reader.read(10)
