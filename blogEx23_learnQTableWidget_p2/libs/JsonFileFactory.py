import json
import os
class JsonFileFactory:
    def writeData(self,arrData,filename):
        """
        Hàm này dùng để parse object thành jsonstring
        :param arr_data: mảng đối tượng
        :param filename:nơi lưu trữ jsonstring cho object
        :return: True nếu thành công
        """
        json_string=json.dumps([item.__dict__ for item in arrData],
                               default=str,indent=4,ensure_ascii=False)
        json_file=open(filename,'w',encoding='utf-8')
        json_file.write(json_string)
        json_file.close()
    def readData(self,path,ClassName):
        """
        Hàm đọc jsonstring và phục hồi lại mô hình lớp ClassName
        với ClassName là tên lớp được chỉ định phục hồi OOP
        :param filename:
        :param ClassName:
        :return:
        """
        if os.path.isfile(path)==False:
            return []
        file=open(path,'r',encoding='utf-8')
        self.arrData = json.loads(file.read(), object_hook=lambda d: ClassName(**d))
        file.close()
        return self.arrData