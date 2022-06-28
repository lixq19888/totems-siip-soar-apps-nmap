# abtnetworks.com
#
import os
import json
from SoarAction import SoarAction
from SoarUtils import output_handler
import requests

LogFile = "nmap.log"
APP_NAME = "Nmap"
ACTION_LIST = ["nmap", "masscan", "getAssets"]

class NmapApp(SoarAction):

    def __init__(self, app_name, action_list, input_data, action_select):
        log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), LogFile)
        super(NmapApp, self).__init__(app_name, log_path, action_list, input_data, action_select)

    @output_handler
    def PING(self):
        """
        实例测试
        :return:
        """
        self.params["assets"] = "127.0.0.1"
        self.params["ports"] = "0-10"
        self.params["excludeAssets"] = ""
        self.params["rate"] = "5000"
        return self.masscan()

    @output_handler
    def nmap(self):
        assets = self.params["assets"]
        ports = self.params["ports"]
        data = {
            'assets': assets,
            'ports': ports
        }
        url = self.setting_param_dict["url"] + 'nmap/scan/nmapApplication'
        headers = {
            'Host': '127.0.0.1',
            'Content-Length': str(len(data)),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.executeScan(url, data, headers)

    @output_handler
    def masscan(self):
        assets = self.params["assets"]
        ports = self.params["ports"]
        excludeAssets = self.params["excludeAssets"]
        rate = self.params["rate"]
        data = {
            'assets': assets,
            'ports': ports,
            'excludeAssets': excludeAssets,
            'rate': rate
        }
        url = self.setting_param_dict["url"] + 'nmap/scan/masscanApplication'
        self.logger.info("请求url:" + url)
        headers = {
            'Host': '127.0.0.1',
            'Content-Length': str(len(data)),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.executeScan(url, data, headers)


    @output_handler
    def getAssets(self):
        assets = self.params["assets"]
        ports = self.params["ports"]
        excludeAssets = self.params["excludeAssets"]
        rate = self.params["rate"]
        data = {
            'assets': assets,
            'ports': ports,
            'excludeAssets': excludeAssets,
            'rate': rate
        }
        url = self.setting_param_dict["url"] + 'nmap/scan/assetsApplication'
        headers = {
            'Host': '127.0.0.1',
            'Content-Length': str(len(data)),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.executeScan(url, data, headers)

    def executeScan(self, url, data, headers):
        scanResult = requests.post(url, data=data, headers=headers)
        if scanResult.status_code == 200:
            content = json.loads(scanResult.content)
            resultData = content.get("data")
            return self.get_response_json(resultData)
        else:
            return self.get_error_response("扫描失败")

if __name__ == '__main__':
    input_data = None
    action_name = None
    # input_data = r"%7B%22languageType%22%3A%22PYTHON3%22%2C%22playBookVersion%22%3A%221.0.0%22%2C%22appId%22%3A%22fb1ee5381f3211ecbc21000c29bca94c%22%2C%22appVersion%22%3A%221.0.0%22%2C%22appName%22%3A%22Nmap%22%2C%22description%22%3A%22%E6%89%AB%E6%8F%8F%E5%BA%94%E7%94%A8%22%2C%22brief%22%3A%22Nmap%E6%98%AF%E4%B8%80%E6%AC%BE%E9%92%88%E5%AF%B9%E5%A4%A7%E5%9E%8B%E7%BD%91%E7%BB%9C%E7%9A%84%E7%AB%AF%E5%8F%A3%E6%89%AB%E6%8F%8F%E5%B7%A5%E5%85%B7%2C%E5%AE%83%E4%B9%9F%E9%80%82%E7%94%A8%E4%BA%8E%E5%8D%95%E6%9C%BA%E6%89%AB%E6%8F%8F%2C%E5%AE%83%E6%94%AF%E6%8C%81%E5%BE%88%E5%A4%9A%E6%89%AB%E6%8F%8F%EF%BC%8C%E4%B9%9F%E5%90%8C%E6%97%B6%E6%94%AF%E6%8C%81%E6%80%A7%E8%83%BD%E5%92%8C%E5%8F%AF%E9%9D%A0%E6%80%A7%E7%BB%9F%E8%AE%A1%22%2C%22tags%22%3A%5B%22Nmap%22%2C%22HTTP%22%5D%2C%22categories%22%3A%7B%22name%22%3A%22%E6%BC%8F%E6%B4%9E%E6%89%AB%E6%8F%8F%22%2C%22parent%22%3A%22%E9%BB%98%E8%AE%A4%E5%88%86%E7%B1%BB%22%7D%2C%22contactInfo%22%3A%7B%22name%22%3A%22ABT%20%E5%AE%89%E5%8D%9A%E9%80%9A%22%2C%22url%22%3A%22http%3A%2F%2Fwww.abtnetworks.com%2Fwelcome.html%22%2C%22email%22%3A%22XXX%40sapling.com.cn%22%2C%22phone%22%3A%22XXXXX%22%2C%22description%22%3A%22XXXXXXXXXXXX%22%7D%2C%22licenseInfo%22%3A%7B%22name%22%3A%22%E6%8E%88%E6%9D%83%E4%BF%A1%E6%81%AF%22%2C%22url%22%3A%22https%3A%2F%2FXXXXX%2FLICENSE.md%22%7D%2C%22setting%22%3A%7B%22parameters%22%3A%5B%7B%22name%22%3A%22url%22%2C%22defaultValue%22%3A%22http%3A%2F%2F192.168.215.170%3A8068%2F%22%2C%22value%22%3A%22http%3A%2F%2F192.168.215.170%3A8068%2F%22%2C%22description%22%3A%22request%20url%22%2C%22example%22%3A%22http%3A%2F%2F192.168.215.170%3A8068%2F%22%2C%22required%22%3Afalse%2C%22schema%22%3A%7B%22type%22%3A%22STRING%22%7D%2C%22ui%22%3A%7B%22type%22%3A%22text%22%2C%22uiName%22%3A%22%E5%BA%94%E7%94%A8%E6%8E%A5%E5%8F%A3%22%7D%7D%5D%7D%2C%22actions%22%3A%5B%7B%22name%22%3A%22masscan%22%2C%22description%22%3A%22execute%20Masscan%20Scan%22%2C%22parameters%22%3A%5B%7B%22name%22%3A%22assets%22%2C%22defaultValue%22%3A%22127.0.0.1%22%2C%22value%22%3A%22%22%2C%22description%22%3A%22%E5%BE%85%E6%89%AB%E6%8F%8F%E7%9A%84%E8%B5%84%E4%BA%A7%22%2C%22example%22%3A%22127.0.0.1%2C127.0.0.1-127.0.0.2%2C127.0.0.1%2F24%22%2C%22required%22%3Atrue%2C%22schema%22%3A%7B%22type%22%3A%22STRING%22%7D%2C%22ui%22%3A%7B%22type%22%3A%22text%22%2C%22uiName%22%3A%22%E8%B5%84%E4%BA%A7%22%7D%7D%2C%7B%22name%22%3A%22ports%22%2C%22defaultValue%22%3A%220-65535%22%2C%22value%22%3A%22%22%2C%22description%22%3A%22%E5%BE%85%E6%89%AB%E6%8F%8F%E7%9A%84%E7%AB%AF%E5%8F%A3%E5%8F%B7%22%2C%22example%22%3A%220-65535%22%2C%22required%22%3Afalse%2C%22schema%22%3A%7B%22type%22%3A%22STRING%22%7D%2C%22ui%22%3A%7B%22type%22%3A%22text%22%2C%22uiName%22%3A%22%E7%AB%AF%E5%8F%A3%22%7D%7D%2C%7B%22name%22%3A%22excludeAssets%22%2C%22defaultValue%22%3A%22%22%2C%22description%22%3A%22%E6%8E%92%E9%99%A4%E7%9A%84%E8%B5%84%E4%BA%A7%22%2C%22example%22%3A%22127.0.0.1%22%2C%22value%22%3A%22%22%2C%22required%22%3Afalse%2C%22schema%22%3A%7B%22type%22%3A%22STRING%22%7D%2C%22ui%22%3A%7B%22type%22%3A%22text%22%2C%22uiName%22%3A%22%E6%8E%92%E9%99%A4%E8%B5%84%E4%BA%A7%22%7D%7D%2C%7B%22name%22%3A%22rate%22%2C%22defaultValue%22%3A%225000%22%2C%22description%22%3A%22%E6%89%AB%E6%8F%8F%E9%80%9F%E5%BA%A6%22%2C%22example%22%3A%225000%22%2C%22value%22%3A%22%22%2C%22required%22%3Afalse%2C%22schema%22%3A%7B%22type%22%3A%22INTEGER%22%7D%2C%22ui%22%3A%7B%22type%22%3A%22text%22%2C%22uiName%22%3A%22%E6%89%AB%E6%8F%8F%E9%80%9F%E5%BA%A6%22%7D%7D%5D%2C%22returns%22%3A%7B%22schema%22%3A%7B%22type%22%3A%22JSON_ARRAY%22%7D%2C%22example%22%3A%22%7B%5C%22schema%5C%22%3A%20%7B%5C%22type%5C%22%3A%20%5C%22JSON_ARRAY%5C%22%7D%2C%20%5C%22status%5C%22%3A%20%5C%22Success%5C%22%2C%20%5C%22data%5C%22%3A%20%5B%7B%5C%22ipAddress%5C%22%3A%20%5C%2210.215.7.17%5C%22%2C%20%5C%22ports%5C%22%3A%20%5B%5C%229300%5C%22%2C%20%5C%2280%5C%22%5D%7D%5D%7D%22%2C%22description%22%3A%22Masscan%20scan%20result%22%7D%7D%2C%7B%22name%22%3A%22nmap%22%2C%22description%22%3A%22execute%20Nmap%20Scan%22%2C%22parameters%22%3A%5B%7B%22name%22%3A%22assets%22%2C%22defaultValue%22%3A%2210.215.7.17%22%2C%22value%22%3A%22%22%2C%22description%22%3A%22%E5%BE%85%E6%89%AB%E6%8F%8F%E8%B5%84%E4%BA%A7%22%2C%22example%22%3A%22127.0.0.1%2C127.0.0.1-2%2C127.0.0.1%2F24%22%2C%22required%22%3Atrue%2C%22schema%22%3A%7B%22type%22%3A%22STRING%22%7D%2C%22ui%22%3A%7B%22type%22%3A%22text%22%2C%22uiName%22%3A%22%E8%B5%84%E4%BA%A7%22%7D%7D%2C%7B%22name%22%3A%22ports%22%2C%22defaultValue%22%3A%220-65535%22%2C%22value%22%3A%22443%22%2C%22description%22%3A%22%E5%BE%85%E6%89%AB%E6%8F%8F%E7%AB%AF%E5%8F%A3%22%2C%22example%22%3A%220-65535%22%2C%22required%22%3Afalse%2C%22schema%22%3A%7B%22type%22%3A%22STRING%22%7D%2C%22ui%22%3A%7B%22type%22%3A%22text%22%2C%22uiName%22%3A%22%E7%AB%AF%E5%8F%A3%22%7D%7D%5D%2C%22returns%22%3A%7B%22schema%22%3A%7B%22type%22%3A%22JSON_ARRAY%22%7D%2C%22example%22%3A%22%7B%5C%22schema%5C%22%3A%7B%5C%22type%5C%22%3A%5C%22JSON_ARRAY%5C%22%7D%2C%5C%22status%5C%22%3A%5C%22Success%5C%22%2C%5C%22data%5C%22%3A%5B%7B%5C%22ipAddress%5C%22%3A%5C%2210.215.7.17%5C%22%2C%5C%22macAddress%5C%22%3Anull%2C%5C%22macVendor%5C%22%3Anull%2C%5C%22status%5C%22%3A%5C%22up%5C%22%2C%5C%22name%5C%22%3A%5C%22%5C%5Cn%5C%22%2C%5C%22os%5C%22%3A%5C%22Linux%203.2%20-%204.9%5C%22%2C%5C%22cpe%5C%22%3Anull%2C%5C%22portServiceList%5C%22%3A%5B%7B%5C%22ipAddress%5C%22%3A%5C%2210.215.7.17%5C%22%2C%5C%22protocol%5C%22%3A%5C%22tcp%5C%22%2C%5C%22port%5C%22%3A%5C%22443%5C%22%2C%5C%22status%5C%22%3A%5C%22open%5C%22%2C%5C%22reason%5C%22%3A%5C%22syn-ack%5C%22%2C%5C%22reasonTTL%5C%22%3A%5C%2263%5C%22%2C%5C%22name%5C%22%3A%5C%22http%5C%22%2C%5C%22product%5C%22%3A%5C%22nginx%5C%22%2C%5C%22extraInfo%5C%22%3Anull%2C%5C%22cpe%5C%22%3A%5C%22cpe%3A%2Fa%3Aigor_sysoev%3Anginx%5C%22%2C%5C%22version%5C%22%3Anull%2C%5C%22frigen%5C%22%3Anull%2C%5C%22memo%5C%22%3Anull%7D%5D%2C%5C%22vulnInfoList%5C%22%3Anull%7D%5D%7D%22%2C%22description%22%3A%22nmap%20scan%20result%22%7D%7D%2C%7B%22name%22%3A%22getAssets%22%2C%22description%22%3A%22execute%20Masscan%20And%20Nmap%20getAsset%22%2C%22parameters%22%3A%5B%7B%22name%22%3A%22assets%22%2C%22defaultValue%22%3A%22127.0.0.1%22%2C%22value%22%3A%22%22%2C%22description%22%3A%22%E5%BE%85%E6%89%AB%E6%8F%8F%E8%B5%84%E4%BA%A7%22%2C%22example%22%3A%22127.0.0.1%2C127.0.0.1-127.0.0.2%2C127.0.0.1%2F24%22%2C%22required%22%3Atrue%2C%22schema%22%3A%7B%22type%22%3A%22STRING%22%7D%2C%22ui%22%3A%7B%22type%22%3A%22text%22%2C%22uiName%22%3A%22%E8%B5%84%E4%BA%A7%22%7D%7D%2C%7B%22name%22%3A%22ports%22%2C%22defaultValue%22%3A%220-65535%22%2C%22value%22%3A%22%22%2C%22description%22%3A%22%E5%BE%85%E6%89%AB%E6%8F%8F%E7%AB%AF%E5%8F%A3%22%2C%22example%22%3A%220-65535%22%2C%22required%22%3Afalse%2C%22schema%22%3A%7B%22type%22%3A%22STRING%22%7D%2C%22ui%22%3A%7B%22type%22%3A%22text%22%2C%22uiName%22%3A%22%E7%AB%AF%E5%8F%A3%22%7D%7D%2C%7B%22name%22%3A%22excludeAssets%22%2C%22defaultValue%22%3A%22%22%2C%22description%22%3A%22%E6%8E%92%E9%99%A4%E7%9A%84%E8%B5%84%E4%BA%A7%22%2C%22example%22%3A%22127.0.0.1%22%2C%22value%22%3A%22%22%2C%22required%22%3Afalse%2C%22schema%22%3A%7B%22type%22%3A%22STRING%22%7D%2C%22ui%22%3A%7B%22type%22%3A%22text%22%2C%22uiName%22%3A%22%E6%8E%92%E9%99%A4%E8%B5%84%E4%BA%A7%22%7D%7D%2C%7B%22name%22%3A%22rate%22%2C%22defaultValue%22%3A%225000%22%2C%22description%22%3A%22%E6%89%AB%E6%8F%8F%E9%80%9F%E5%BA%A6%22%2C%22example%22%3A%225000%22%2C%22value%22%3A%22%22%2C%22required%22%3Afalse%2C%22schema%22%3A%7B%22type%22%3A%22INTEGER%22%7D%2C%22ui%22%3A%7B%22type%22%3A%22text%22%2C%22uiName%22%3A%22%E6%89%AB%E6%8F%8F%E9%80%9F%E5%BA%A6%22%7D%7D%5D%2C%22returns%22%3A%7B%22schema%22%3A%7B%22type%22%3A%22JSON_ARRAY%22%7D%2C%22example%22%3A%22%7B%5C%22schema%5C%22%3A%7B%5C%22type%5C%22%3A%5C%22JSON_ARRAY%5C%22%7D%2C%5C%22status%5C%22%3A%5C%22Success%5C%22%2C%5C%22data%5C%22%3A%5B%7B%5C%22ipAddress%5C%22%3A%5C%2210.215.7.17%5C%22%2C%5C%22macAddress%5C%22%3Anull%2C%5C%22macVendor%5C%22%3Anull%2C%5C%22status%5C%22%3A%5C%22up%5C%22%2C%5C%22name%5C%22%3A%5C%22%5C%5Cn%5C%22%2C%5C%22os%5C%22%3A%5C%22Linux%203.2%20-%204.9%5C%22%2C%5C%22cpe%5C%22%3Anull%2C%5C%22portServiceList%5C%22%3A%5B%7B%5C%22ipAddress%5C%22%3A%5C%2210.215.7.17%5C%22%2C%5C%22protocol%5C%22%3A%5C%22tcp%5C%22%2C%5C%22port%5C%22%3A%5C%22443%5C%22%2C%5C%22status%5C%22%3A%5C%22open%5C%22%2C%5C%22reason%5C%22%3A%5C%22syn-ack%5C%22%2C%5C%22reasonTTL%5C%22%3A%5C%2263%5C%22%2C%5C%22name%5C%22%3A%5C%22http%5C%22%2C%5C%22product%5C%22%3A%5C%22nginx%5C%22%2C%5C%22extraInfo%5C%22%3Anull%2C%5C%22cpe%5C%22%3A%5C%22cpe%3A%2Fa%3Aigor_sysoev%3Anginx%5C%22%2C%5C%22version%5C%22%3Anull%2C%5C%22frigen%5C%22%3Anull%2C%5C%22memo%5C%22%3Anull%7D%5D%2C%5C%22vulnInfoList%5C%22%3Anull%7D%5D%7D%22%2C%22description%22%3A%22getAssets%20result%22%7D%7D%5D%2C%22image%22%3A%7B%22smallIcon%22%3Anull%2C%22largeImage%22%3A%22data%3Aimage%2Fjpg%3Bbase64%2C%2F9j%2F4AAQSkZJRgABAQEAYABgAAD%2F4QAiRXhpZgAATU0AKgAAAAgAAQESAAMAAAABAAEAAAAAAAD%2F2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz%2F2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz%2FwAARCABkAKoDASIAAhEBAxEB%2F8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL%2F8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4%2BTl5ufo6erx8vP09fb3%2BPn6%2F8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL%2F8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3%2BPn6%2F9oADAMBAAIRAxEAPwD93qKM0Zr0j5kKKM0ZoAKKM0ZoAKKbNMsETSOdsaAszE8KB1JPYD1ryPx%2F%2B214F8GSyQWeoN4jvI5PJMWmbZIkfe0YDTFhGBvSRSys20wy5AMbAVGEpO0VcidSMFeTsevc0E4r57m%2FaJ%2BLHjhQ3hv4d2uj27Ngza67KVj7SqGeDzC%2FO2MfdGDI6EhKhksfjzrR3r4w8I6BbnkRvZLd3f4lYPKT6Aydvm61osPLq0vn%2Flcy%2Bsxfwpv5f52PorJoya%2Bdf%2BEJ%2BMckeyf4k%2Bcp67EtYP8A0HTwf1pr%2BE%2FjZpqLJYfETRpGjz%2Fo%2BpwxzxS%2B29bNZE%2BuWx%2FdNHsH%2FMvx%2FwAhLESv8D%2FD%2FM%2BjKK%2Bebf4rfGzwTJi%2B8L6T4ksx96S1dDMrjHyL5bq7Rv0EgttyHl0K5Zdfwf8At1eG9V1VtO1%2FS9a8L6kuGkhnheUwg8AOgUTq24bTmIAEp8xDKTLoTWq19NRrEQvaWnqrf8D8T2%2Bis%2Fwt4t0vxtpC6ho2o2erWLsVW4tJ1miLDqNykjIyMg8jNaG7%2FOazOhBRRmjNABRRmjNABRRmjNABRRmjNABRRu%2Fzmsfx18QdF%2BGegSarr2ow6Zp8ZCmWTJ3MQSFVQCzsQCdqgnAJxwaNdhbbmx1rx%2F40ftjaD8NNXj0LSIJPFHim4nNqtjatiG2m2khZ5cEqS2E2IrvveNWVd4Yeaax8cPGf7U3iiz0bw3HN4X8H3lpPcXN07eXeXUavbYLSKcx5jnJ8mPLEtCXcRS7q2fg78INF%2BDPhfwvLY26vc6VqcuhXeoSJ%2B8eEPPp8exBny1knFrwvzBNu92Cbq6I0YpXqfd%2FmzknXlLSlt3f6L%2BkcrceCfHf7R2oaDfePtbm0vRbzX7y2TRbBfIVoYYtQ2F4yWAO2IZMxkcNuyi4XHqXwP%2BGuh%2FD3RrmPSdNt7W8h1TUYmuCpe8Km8l2gyNl1Dx%2BW%2B0EKQ4YD5snmPiJ8W9L%2BHs%2BqeHVm%2B1%2BKLfUJNY0a3hJZ5nkmNw6OVBKATSyW8qJmTyJo%2BCZwD5x8R%2FGvjHWLW61S7vG8L2euLGX0K2ZftEkqxgGSSRXI3LAqq%2BTKjGKL5IwG3dlHD1a6SjpH8DgrYyhhnzz1l97%2FAKuj6E8V%2FFnwz4Ilkj1bWrC1mh%2F1sQYzTR%2F70cYZ179VGcH0OOJm%2FbO8Co7C3n1XUtgyxs7VXx07FweMjPHGQDg1866J4Ch8j7VqEclztkWJBIAGjfJ2qqMNsUxwSVKhGC5wFMQOf4l1xbfMP7uaNiWSNFzEQQAWVXz8rAFS8m5zgcqYst69HJqW0pN%2Bh4GJ4nxS1pU0l53f%2BR9Eyft4eBowf9F8XfLksRpacYznP77j7rf98n0NWrD9uHwFelv3ut26oQrNPZBQhJIG4ByRyCMkY4NfK2lajNq%2BoNNdTal9jtgsl19lLzSuC6pgAuqgnzJDnOBufryD7N4J%2BH%2FhnxH4XtdUs7vVhD5ZEV7LdbZrQqCjEvgGNhhs4IUFnPQ5LxGW4Skvecvz%2FQjC5%2Fmde%2FLGHzuv1Pa%2FCf7R%2FgPxsinTvFWjzFuAJZDb8nHAMgVW6jlSQdy%2F3hnpfFPhTS%2FHWjx2usadZ6rZHEkK3MQlVCcFZIyfusMBldCCCAQcgGvjy58G2uuXTQPHb3V1A7W8U1vADJIykgeWq9yOYwuE2szP%2B9YZf8NpPEvg%2FVjY%2BHfFl74dkvh5dtMu28snkJ4KrIdssj7XAkIlVXO4Ky5V%2Bark8bc1Kfyf%2FAO%2FDcRyl7uJpfNO6%2FE9Ju%2F2crrwpew658PNfvtA1KbxDd20emy3Mht7kLPdROhmG6Ty%2Fle5KSrcIfJQBF25PU%2BDP22NW8DeIZPD%2FwATdDudPuI79LCPVLeJSr74YpEd0RmSQYlG5rd2ILx5hTcduL4e%2BOZ8C3ul2%2FjrRx4b0Hw3Cttpt9Yb7ixll8kQJIwy0qKkLPDGpLvI0srNGoWJz2l3pOm%2FFHwtp9jf29rqFv421I67cJuWRYbS1aIxsNpK%2BYiR2Nq5jclZJpGVjgtXmVoSWlaPz%2F4PU9qjOEo82Hl8unzXTXse2eHvENj4s0WDUtMuob6wuhmKeF96OOhwR3BBBHUEEHBFXK%2BP7z4feKP2eta8Q%2BJvh7dy6hptx4gtLe4sZgbhrlCLG3cEZH2oLIZ4QcidJFI3SNuA9u%2BCH7Veg%2FGC6XS3kXTvEQTzPshJaO5Q7sNDJwGJCMxj4kTa2VIXeeOVJpc0dV%2BXqdlOvd8slZ%2Fn6M9SoozzRmszoCijNGaACijNeb%2FtFfGOT4b6Xp%2BlaYRJ4m8SM8Wm24CNI6IUWWRFkIR2UyxIqscb5kO1wChcYuTsiZSUVzS2Kvx5%2Fal0r4QXdvo9pH%2Fa%2FijUJVgt7JP9XbM0bSBrh8gRgIu7BIJymSiuJB4n4J%2BHWufFXxH4U%2BIHxI1BpJLxXsDYRM1ummXMzxKke0kNbAXFv5Gzi486aDPkyxy%2BZa%2BAvw%2FjtdI0u%2BvriGXx95q6hpMt%2FLIsWrt5bmS6RypaWS6heYyNsaWzW5yYFkLtPp%2BNP2gNI0C51jTdM02PX7jUtya14ZumhifRJZP3c3nhm8kxSEs0iK%2Bx282RZJBPluuFNx92nv1f%2BXY4JVIy9%2Bq9Oi%2Fz7s6W5v7P4XeFNP0tns9IuvBieXo6ShYYdZsEUxiGPYBuZo9qyIgHlXMccxiMJiEvH3fiHxB8cLjVF0Gzm0Lwb4ijMeqNqMLR3V26xi3YopU8SRIkbojBALdSsmZHDdB4R%2FZ7utde31LxvqLeKpLdo5dPtLpvtMNgFwyfvGJ80owXaxyxwWklndi9eljR9qqqxKqqAqqOigcAD2HStIcsXd6v8AnGrNWXur8f6%2FQ8z8G%2FCex8D6fHDaxzXFwsYSS8uX8y4m4wSzYA56kKAGPzEE81xnxb05td8c2Oll1WOERoyP5bqJHO7cUcjIH7rODyAw717%2F8A2T%2F0zFeWfEvQmuviRNb%2BZEpvIookikkRQxYIoOCjEgspXOMZzXZTxTTucFXLVuec%2BOrBtM07bJG0CwwlPLkV0ZV2pI8a%2BaNxX54k8tjKNkWOBivnD9qH4yQ%2Fs%2F8Aw5m16a3jvtW1Gc2mmWs5PlzTYy8r85aOJdvGeWaIEbc7frb4k%2BHla2lkht1jVvMlUqggDqfJkGP3Ef8ACRwDk9RgEZ%2BJP%2BCoWlNaeBfCOq%2F8I7pOoWdnqN7bzfaXvv8ARZJo4Gj%2FANVcx8yLDJ94niHjvXVHFtU9Gcn9lxdVKex8yR%2FEP4hePtM1zWNc8dXdjJeaYkumrc6m9uDjUrRd0UUQ220ZYMiuwiiJ3BWwrlfVf2R%2F2n%2FEl38R7X4e%2BPri51KbUJVt9Nv7qTzrqC5cAwo8uT58M2UCOSwG%2BJ0cRjlnwa%2BJuh2HgP4nMvwR8LfEBvFXhOwsbS7Q3VxJ4fmhW3tGhlErTywpG7RypJE9s7R6fEwkyFkg4r4UiPxj%2B0N8P9B0vw34WvL%2BzubK2m1C3uNTljDJK00jpIL4q8dvG3leZl0ZbXcjNF5eOajiZqdz062Apyhyy2P0H%2BHcHmzfZZP9S4WEqCMshbgLnhtj4Zchgv3ghbmut8W%2BHbq3kt9Q8uS2vJAXaXy%2FL8pht3Bnk2tt8xSgVVAQQKBzijwfpK6lrsfk2K2sZdfkjd33hpkx8rCQnGCflX19q7DxXokVrpjrttbdrpHWM%2FJCz%2FvmcYzAmRseMg9wy9sCumpjHzpo8ujly5Dr4dMTW9KjkMCNb30CuYnUOrI6g7SDwwIOCDwRXITfCTWPh5qupa58P7yHS9Y1JY1ubS%2BUz2N0E3bdykg%2FLvkYLuXJbYJYFZmHrXhnRGt%2FC2lxsm4x2UCEseSRGuSavf2T%2FwBM1rhliG9HqelDL%2BVqUbpnlPgb4waTcXljpOsW994XbwzIWe21BXkuNcvmDqvlYQNcsxkkm2iMSzztG8QdV3S1fit8CI%2FHgj1BF%2FsXxv4m1WG%2BEW8PCsVu0LFbkx7h8tvEI3mjLAXF0EDyK8IPonjj4R6T8RbOKPU7GOSa3DLb3SAC4tg33gjkHCtgZUgo2ASpIGPKZPiPq37P%2FiG80zXtVsddkkhU3Xie4nR5tFgG0gTW%2B4sqrvDLG3B3b5Jpnb5%2BdQblelv2OiXuxtXWnf8Arb1N74TftWap8ONduvDPxEjkW3tL5NOsdXwZpJNyxrGZWUkTAyGWEyoMiSB1cMwkZfo6xv4dUsorm2ljuLe4RZIpY3DpIrAFWVgcFSCCCOCDmvnnxTpfhX4neANLtbiTyfBUE4ktNVZs3mrXu4yRm1YqZZJjOnnlwpe4ljQBJ45HLYHwG%2BK2r%2FATxy%2FhrxVN5Oj67fbtLSVcGBXQYmjjUs8SO0c88sb7kiHnOZVMEwfnqUrrmirPqv8AI1p1%2BV8sndPZ%2FwCf6M%2Bq6KDwaM1znaHSvmv9vrwNda6trdSxWl1od7bxWl0lxpv202ksUxkjeHMqKlxIJGijLYXJILpkBvpTNNnhW4iaN1DRuCrKRkMDwQfaqo1HTmpoxr0fawcH1Pz1%2BLHxem8axQ6fDr1rfWkO2TxJob61Lai%2FdWLpBFcajPKjCQJ5iqqCRYSskiI21BZuEuj4Y0ux0fwT4j0zSWuZNNtpLC2W6%2B1tDHMHdeXXA8mYBlcyv5alnYE5%2Bv8Axl%2ByR8NPiDp93Z6p4L0OS11CPyrqK3hNmtyuAvz%2BSU3EAKAWyRtXGMDHmOvf8EyPB9vf%2Fb%2FCWv8AizwZqi3n22Oe0vTKkchUoz4OHLlWcGRnLMXO8uMAe1QzLDxsndP0uvwf6Hh1suxOuql%2BD%2FH%2FADJvhl%2B134SOgaRpOrPfeGtTjA01LW90uSzV5IRIhWOMF2VcQSFd2AFXtkA%2BraT4ltdfsvtNheW99bZA862nWaPJUMBuUkcqynr0YHoRXzL4m%2FZ1%2BMfwlezXy9B%2BKHh%2BzW7ghtbi2817ZJpI5FkeFsSOVaJEAR5SiySc7VAPl%2Fg7xn4asTDHa3Xiv4a6toWmLqF%2FD5jm4u7li0m2TcY3E29Lh5kcxI0s%2Bx2IaaN6jgqNf3qMv1t8t19wf2tXoNRxMPwt%2BOqf3n3l9tbH8X51wPxxt5oI7HWI5JI1t%2F8ARZ2EnlmNGJKMHxlfmLD3Z0%2Bo8v0D42%2FEvwNf29jq2laV42WSKK9mk0h2jNlbSErGsbBN85bZIUbyTvMTF2hDqa7Dwb%2B1b4C%2BKOi4fVIrG3vnW0RdUH2aG7ZyFXyZidjq7EBGDAuSu0EkVnLAzp62uu6OyObUKq5b2fnp%2FwAAL%2BaLVtPaRfLRvLVn48pVUZVWYNlljAcxl5mc7fIbyyGAHknxS%2BGen%2BKPD2paHrmn%2FbtD1JTb3EEymNsqy4GTzHKjbCD1zgHAZ0X0fWdNvPhjqMfnGabSbhw9rc5xnI%2BXkgjzyCRuYFdpYgHDqzWNrrKIIlj85g0awIT%2B9YDDRpw5IXcIwrKwBllPmA5AKcXHV7E1K3N11PgfVv8AglfClzrsei%2BLoxp99YpFGmp6e%2Fn2wF7ayY3R5WTHlFd2I8kg7QOnr37L37Hegfs6tNcafJd694mvozBLqVxAIWijPDRwRbj5YbozliSMjKIZBX0Ne%2BGrWCSbbLbrsV87ZI0DlUlXPy3GDlrdW%2BpHtnQtfD9rpIZcQJGr%2BUWIjaM4JQbgrlWGBGWV5kBS4kwGGDWj5FqiXWqS91sd4I0b%2By7IO7ouVMm8puTg7DJt2ncse7GWR1MhVSsLYzqmNvFniqz0aEyx27kedGX%2FANXAuN2BllIEYWMPEwSQBPcVjXHigzXUdnYxXU15csFREbdcSlBtADEDEka71LFVQpuypwXbo9I8R%2BHfgVE0Wv63plt4gvYjNNaI5eaONcM3lwrukWNSwLyEbcsGZsbSMZUpN%2BfY1jioxjq9D1lr9nYnDDJzxTWvikbMdwWNSzEnhQOSSewHrXzrrv7Yuqa5b3EnhbwxdG007d%2Fad3qR2S6eqg7m8pf3bAYclhMzBY32xyyL5Lec%2FF7xLdaE95%2FwsDxjd6hrOlwfb7DTbFh5WoIDuMcsLYt4pFUKGk8pMebHLHISfJi0p5ZKXxafizKtnlKPwa%2Fgvvt%2Bh9JeKP2r%2FA%2FhRLYtr0WpNeNst%2F7NBu4pm2lgonX9wCQDgNICcHrg48G8S%2BKvEHxG%2BJ91r2k%2BHfFjR3mom1FrPplnp5iIgxAXke6HLRiJklRwzmaPOFYRrS8E%2BF%2FHnxP1S8%2F4Vr4LsvD2j3l1Y6jHrOpfvmEkdzulC3EwPy7oI3eJI5yrmQ5BmOPTNF%2F4JyX3imRbr4gfEjxJrM7Xb3sltpkhtoWcqY1DGTchPlEJ5kcULARxBPLCYbSLw2FbvLXbu%2FuW3zZyyq4vFpOMdL3XRfjv8keF614m1T4d%2BO7fU9FhtfhvqVwLy21mA31nfNfJbzRxzRLZxO0yiPahCWzb5EaSVVSVTJL1lzb6l%2B0L4v8AsPhOSzumkhEKalLZ3NzPNbkl082SW8dhbFlWQBnCw8MFkmufIH0T4E%2F4J%2B%2FCP4ep%2FonhGC8ZovIf%2B0bma7iZN7SMogdzCqs7s7Kkaq7HLAmvWPD%2FAIb0%2FwAJaVHY6Tp9jpdjF9y3tLdYIU7cIoAHbt2FcdbMKb%2FhR%2Bb%2FAOHb%2FE6KOWVW71ZK3Zf8Mkvki%2FK2%2BVm%2FvMTTaKM15Z7l7u4UUV8U%2FtDftjfGoftjeMPhb4D1L4XeC5dB0C11nQk8YeD9X1V%2FFkTpGJ7yO7t7y1t4beG6ngtWRRPMrb3K4KrVU6cqklCC1JnOMIOpN2S3Z9rY%2FwA4ox%2FnFflv4b%2F4LF%2FFr4o%2BFfiV4lXxH8FfhLJ8M3nGueDPEvgrXtd1PQBE5gX7VfWt9BHN5twkgH2W3kKKRw5BLd14m%2F4KofEj9mPT5NQ%2BIl18P%2FiDpPjTwncX3w9u%2FCfhrUNEbVPEK%2BUbPR5oZ727Y%2FbkuUeJ90bL9muAVJHGv1Wry89tP6X56EqtSc%2FZ86v8%2Bye9rbWfpqfocOK4r4w%2Fs9%2BEfjvpjQeJNJjupgF8q8iYw3kBQloysq4JCOd4RspuAJU4FfAHxw%2F4KYfHz9mzx94a8N%2BMfHvwEtzrGmSanq%2Br2nwu8TXtr4YRWWG33rb6nJ5y3V0Xt42LQkNGPkJlRK9a8G%2FtxfGT4Y%2FHAeEfH0fw9%2BI03ibw1rd14Ui8HaNdaFc3fiDS4EvP7FmFxfXqb7q0aSSKTKbfssuVYEGn9Xr026lmnHd32IVShW5afMpc%2ByfW3qrdBfin%2Bx98QvgVpmtP4PupfF%2FhnWL2OW803yd9x5DCCGZJYtw87dEh3SwlZXAx%2B7C5POeGPip4R%2BNutahqWvQ29vqjSPa2r3j4a3gT926rONuN8u%2FeG2iUNFHiVYxjg7D%2FAIKo%2FFaL4R%2BE%2FGGufGX9nzw7a%2BLIrgwWs%2Fwg8USvbXNoVS%2FtpB%2FayzIbWYtFI8sUfKFsAZx69%2Bz5rWl%2Ft3eIfEnhf4j6H4c0X4oeGdO07X7fxL4Kv2k0fxdo9%2BJVtNTtDKDIB5ltNDJHL5jRmJDHcPHIjV7WHzGpTX%2B1RutNVa%2BvdHzmMyOnUbeDmk9fdd7O2js2tLbNakw%2BG%2BqeE0mh8P8AiK%2BsYJMiSxuh5kMh6nepBjbn%2B%2FCxJCkknzPMxxY%2BMNJkZTZWd9DlQ3lOFVgpJCn5g2wMdwCRkkgEqg%2BWuk139ib4mfCuJ28H%2BILPXrG3QrFZbltJXDfM2yKbNvGd2fmLknP8O4kfJfhP9rX4jX%2FwY0Lxf4m%2BK%2Fwp8DzatfPot3omp%2FCfxBdanomrxRGa50q4CX8LtcW6hlkdbeOMmNioC4r1fruDmrxal8tVa297d%2Bp5FPL8xT5bOPTdu78rX7dD6VtfG%2FjKxWKNdFvJY4VEafZ7p7eNwFdeVKj%2B%2BxOQOvuQY2uvGWshtum2XmSjbPJKSgdCgUo2%2FYc4UHKhxuAJxXzdqP7cXxQj%2BMXgbwBcan8HdL%2F4T60h1TRPHljo%2Bra54f1%2B2uZIoLKO3to7qOW3nmuJRG32icxRjYRJJ50eNS9%2Fat%2BJul6j4ksfDvjz4F%2FFHxB4RGoSaj4Ug8Ja14Z1K8GnyGO%2BisLie%2Bnt7i4iYMpQKy7tuXUEEixGEvpH8Pnte%2BxcsHmLjdyW19%2Bl7Xvay17teZ9GaT4H8SSxyreeJJbOG6H74We5JZl4%2BSRk2FgcD5Wd1UbwN2Qy1fEnhjwD8O9GWPXCjlv9IhSR9115nzbZIY0xtfduCy7flY8uvWvlmb9rvxl8ZvDC%2BItN%2BJ%2Bg%2FDf4aXt6uk6V4jfwtdeIdb8U6n5fmPBpGl2LxTyxwYdJHZpCXjlGxkid69Z%2F4J7at4X8YfHDw3oXjzUNE8c2%2FwAQYLrU%2Fh%2F438NPPZ6X4mks8Pd2V7aSu9zY6pAI3m2iZo5US5RtkkEsRVfHYelGTjd27Lf%2Bu%2BxNHK8bWcVKyb01b07r1XVXv3O3%2BHGq%2FEr9pfV9Em8K6fNoem%2F2OIrzVwRDuf8A0aSLLjAiQhmZI48yxpM7xl1kKn6A%2FZ8%2F4J%2B%2BEfg7pOkvrEcPijWdNsxaedMhS0wVVX%2FcElW3bE%2F1m4AxhlWMls%2FJ%2FwAPv%2BCjXxb8QeK9T8J2fib4K%2FCLVtEl1Ux%2BAta%2BFevXF7oGn2M7qA90uo2ttcYtxDKXt41jYTL5YIIqlon%2FAAVc%2BJWsfDbXvGDfHb9nGz8M%2BGrm2tr2%2Ff4Q%2BKEVFugDaSFJdWSRlmBypjV0xg78HNeFisTiq8bU0oxfRNa%2Brvc%2BkwuV4XDS%2FevmmrbqWjeisrdeh%2BnP3%2FvEt7mjH%2BcV%2BZMn%2FBYP4j%2FDW%2B%2BH%2FibUvE3wv%2BLngXxlq2qeHksfCPgTVdB1i81WCzm%2ByWUD3mpThZZdQ%2BzW58yDaokZiwAyLt9%2FwUZ%2BLv8Aws1tFufjV8A%2FD%2FjNtSi0ZvCMfw213WtA06%2Fn2%2BTptx4ijvYYmvsSINm2FnkKqIRuAPm%2FVaqdrduq67Hse2p25ubv3vpvpa%2BnU%2FSn8vzoBr8xvBf%2FAAU%2B%2BPWrx%2BMJPE3xB%2FZ98DxeGfifc%2FCmzab4da3qC61qUUUTxyJ5esKYRPvkIRwRH5fzSnIx0S%2F8FGPjRo%2FxB0Wy%2FwCFifA3xlb2PxM8OeAPFWmaZ8PNY0u8086lqkFnKI7ibV5Y%2FMSOV2VljlTIGcjqvqtZR5pLT5ExxFJzUFJX%2Bfl5W6o%2FReijNGaxNg6V%2Bbf%2FAAVD8Vah8Uf2xPE3h3wXb6tda94P%2BB%2FiHRLue2dbYWup65NZy6XBFKXVhM66bPJ5gwkf7vMgYkL%2Bkma8j%2FaC%2FYJ%2BDP7Vnimy1z4jfDTwn4u1vTrX7Bb6hfWQN3Hb72cQ%2BauHaMMzsqMSql3IALNnowdaFGvGrUTkl0Tt0tvZ%2FkcuMoTrUJUqcuVy6tXS1XS6v95%2BNPiTxtH8fP2W%2Fjl4kurH7D8Yv7Fs%2FBHxB0qBY9txqVlerFBd4jOwNKoaPIPl5hEaHbDuf0Dx78cNW%2FZm8UeEbDx94G1LXvD50nw6fB8PmQSC38aWMEkPkL%2B9BjMiPEPPOUTyMoW3kj9MvFn%2FAASp%2FZw8b6R4fsNS%2BC3w%2FmsvC2nnStKhj0xYEs7UzSTmECPblTNNNKd2SXmlY5Z2JZ4U%2FwCCUH7NfghdSGm%2FBH4dxLrFjJpt4JtJS5E1tJgvHiXdtBwPu4PA5r2f7cgoWjTtKyV7qz1d21y7tP7zxXw65TtKreF27crurxgkoyU9FFx0un7vu%2BZ%2Bamk%2FCv4qeKvit8JdV8XaVqdxp%2Bh%2BCtOufGqrNbvNrOt6fdz38FhxLtbOoPb3J%2F5YsbVR5q4yc34VeMrj4q%2BHfiVN8NdD%2BK0fjjwf8QT4%2Btp%2FGVzpf2W18XWc0ZfTYTaTFo454VktGDAwLDLJ%2B8GTv%2FSj%2FhzV%2By0f%2BaG%2BBfTP2aTcB6Z35x7ZxWl4h%2F4JLfsz%2BKU09bz4H%2FDrbpdolhai30hLXy4EJIQ%2BVt38sx3PliWPPNXLOsK9PYuzvzXkru6S0fLoRDIcWld4lc0bctoNJWk5O659b3t93S6PzN%2BJtrrsvwjh8SXXwJ8W%2BMHn8T%2BN%2FFi2ifEJ%2FCl94c03VtTub0LNJZTEXDTWsyLJEruF8tlIO%2FB%2B%2Ff8AglJ%2BzpcaB4Dh%2BMusal4dvL%2F4oeFNEtfDum%2BHoZk0bwv4Yt4pLjTbG3aeOOaR3F5JNLI8cQ3PHGkSLCC%2FSn%2Fgjf8AstNKWPwK%2BHpUtv8AKNgTD1zjyi2zb%2FslduOMYr6P0zTLfRdOgs7O3htbS1jWGCCFBHHCigBUVVACqAAAAAAAAOK83HY6FaMYUYuKSSd2ne1ktVFP77nq5fl86Ep1K01OUm2rKSSUndqznJfclpvcXUL%2BHSLCa6uJBDb2sbTSuQcRooJZj34AJ454r8WdV8R6v8avh7qXxA0D4O%2BMPHNr43%2BJeq%2BPfC9tD45fwXqen6dqFriC%2FF1aT7gZIXaIwb9%2BJTuXAIr9rGXcO4xyCO1fNuo%2F8Eef2XdU1G4upfgX8PFkuZGlkWHTvIhLMcnESERqpP8ACqhfas8vxVOhOUqkXK6tutPvTTKzHB1cTTjClNRakm7pu9k9PdlFrfoz859M8Fi5%2BGn7PnjJbPTf7c%2BKUvh668BeFfC8cjab4J8G6Hq2n6nqTXVzc%2BS8100kliJdsRJeCJYxKA8jcvrPisr8bvix4A0%2FwDo3wi%2BLHjiDUJPDPi6MpeTeKbW4uruRo2mbebGa%2BS3uZQEOVKyvsEluiSfsH8Xf2KvhL8evh5oHhPxh8OfCGveG%2FCaJFoenT6bGsGixpGsSx2qoF8iMRqqbI9q7VUYwBjldP%2F4Jd%2Fs76T8MtW8HWvwc8B2%2Fh3Xry21DUbVNNAa8uLbd9nkeX%2FWExb5AnzYUSygACRw3Xhc2VOFqkOaTldu6WlrWWl07bNNanPjMn9rUTpT5YxjZKzbUr3Tb5rSV94ta66pu5%2BZH%2FBPn45yfs%2B%2BMfh3qEXgHUPEGtfAqy8T%2BEPEvgSy1Cxm17w9Dqt7b3ltqNl5ssUE77beO3lcSp5guJ9pJUq3M%2FHT4sfbPivoVhqkl98Oda8dfGxviJrEWg64bK68A2d9p82nQWsuo27BLe8voxPMTG%2BWZrwoSF8xv1Y8R%2FwDBLD9nfxT4A0Xwzc%2FB%2FwAEwaT4daV9L%2BwWX9n3WnmVi8xjurcx3C%2BYx3PiT5zgtkgY7D4d%2FsV%2FCP4UfCDU%2FAHh%2FwCG%2Fgyx8F64zSatozaTDcWusu2N0l4sqt9qchVG%2BYu2FUZwBU%2F2hh0%2BdUvesk7y0aVult2lZ6262WxX9n4h%2B463uXlJWjaSlK73cmuWMpNxW%2Bycmld%2FlX8U%2Fjn46u%2FAfgvU%2FitZ%2BJrR%2Fgh4R8daHqvi3xHeWEieJY9TntU0SO2aGdprm5aytIklaWGN3m673kyed%2BF8vjC5%2BDHiLUPD%2FwALbbxpcWNv4L8NW2keJYrdINQvPDtnFpepyIskyeU9vd2s%2FlPNsbfErhG4B%2FUT4Yf8Erv2ePg18QdP8U%2BG%2FhL4U0%2FXNHnFzpkzxy3MWkSg5WS0hmd4rVweQ8KIw7EUvxD%2FAOCVn7OfxX8dat4m8Q%2FBvwNqWva7cte6jemx8qS9nfl5ZPLKhpHPzM5G5mJZiSSa0o5lhqVRclJ8qUvtK95f9u2suisZ18txValONStHnk4Xag1G0NUrc97yb1afkl1Px8%2BJHhzxF8KPi9pnxu8b%2BG9R0KPUvjCNRbRriP8AtW%2B07S1tHvptREtrczQKVjspnmSOHzNttuaVkRK%2BqPhl8fIfDv7EniX4J6x8CdZ%2BNGl%2BKtf1vWtJ1uw1%2FTofDHiSDUNZn1a2vLm9W5W8tJYHmXLwQzOHtI3hkbKlfuL4W%2F8ABL%2F9n34I%2FEPSvFnhL4T%2BE9A8S6HKZrDUbSKRZ7VyjISp3Ecq7DkHhjWN4g%2F4I%2F8A7MvifxLcapdfBnwekl3KZ7i0tI5rPTblzgs0llC6WzkkZJaI5JOc5NRUx2Eqe7OlLlvfSSTv1u%2BW1n5JWNKOBxtGMXCtHmS5dYPl5b%2B7Zc97x7uT5uvc%2FLa68LfDz4p%2BDdA0%2FwCH3gjx7Z%2FEBfGMPiGbRfDvjA6r8Px%2FZGsWVjd%2BKkn1Bo7q6lurdbu0UqZWaaK5MiGRFmf3%2FwDYX%2BAPgnxd%2B37rlj8QNL%2BJ2keKtY8W6h8SfDVumrW48J%2BK49NuLc2txLDHI9wt3Zy3aSqkghRxsLiQxha%2B%2FwD4u%2FsEfBb48%2BGPDei%2BLvhd4J1rSfBsBtdAtZNKiij0WAqqmC28sKYYSEQGNMIdi%2FL8q4d%2Bz5%2Bwd8G%2F2UfEV9rHw4%2BGvhPwfq%2Bp2wsrq%2FsLIC6mt9wfyTK2XEZdUYoCFLIhIJVSOf63S%2BrOioy5m7p82iXa1rvR9zq%2Br1vrSr88eRRs48lm3o%2Ba%2FNZO6T2dketCiijNeedgm6jdRRQAbqN1FFABuo3UUUAG6jdRRQAbqN1FFABuo3UUUAG6jdRRQAbqN1FFABuo3UUUAG6jdRRQAbqN1FFAH%2F%2FZ%22%7D%7D"
    # action_name = "nmap"
    app = NmapApp(APP_NAME, ACTION_LIST, input_data, action_name)
    app.do_action()
