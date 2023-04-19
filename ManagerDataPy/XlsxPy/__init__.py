
import pandas as pd 
import os


class Xlsx():
    def __init__(self) -> None:
        pass

    def _Convert(self, list: dict):
        result = {} 
        for key in list:
            result[key] = []
        return result
        
    def _CreatXlsxTitle(self, dictTitle: dict, pathFile: str='output.xlsx'):        
        data = self._Convert(dictTitle)
        df = pd.DataFrame(data)        
        writer = pd.ExcelWriter(pathFile, engine='xlsxwriter') 
        df.to_excel(writer, sheet_name='Sheet1', index=False) 
        writer.close()

    def _UpdateXlsx(self, dictData: dict, pathFile: str='output.xlsx'):
        if os.path.exists(pathFile) == False:  self._CreatXlsxTitle(dictData)
        # Đọc file Excel
        df = pd.read_excel(pathFile)
        # Thêm hàng mới
        df.loc[len(df)] = dictData
        # Lưu lại
        df.to_excel(pathFile, index=False)
            
    def _ReadXlsx(self, pathFile):
        Data = []
        df = pd.read_excel(pathFile)
        for index, row in df.iterrows():
            Data.append(row.to_dict())
        return Data