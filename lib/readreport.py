import xlrd


class ReadReport():
    """读取excel文件数据"""
    def __init__(self,fileName):
        self.data = xlrd.open_workbook(fileName)
        self.table = self.data.sheet_by_name('测试报告')

        # 获取总行数、总列数
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols
    def read_data(self):
        if self.nrows > 1:
            # 获取第一行的内容，列表格式
            keys = self.table.row_values(0)
            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, self.nrows):
                values = self.table.row_values(col)
                # keys，values组合转换为字典
                api_dict = dict(zip(keys, values))
                listApiData.append(api_dict)
            return listApiData
        else:
            print("表格是空数据!")
            return None

