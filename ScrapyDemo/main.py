from scrapy import cmdline

# 这个是这个框架项目的执行入口，直接运行这行代码就会运行整个项目
cmdline.execute('scrapy crawl doupan_spider'.split())