import time
from common import Common

IC_VALUE = 680
CM = Common()
rows = [49, 50, 51, 54]
xpaths = [
    '//Tree[@AutomationId="tvObjectList"]/TreeItem[@Name="Class 3v0: Register (1.0.12.27.0.255.) (with Action) "]',
    '//Tree[@AutomationId="tvObjectList"]/TreeItem[@Name="Class 3v0: Register (1.0.11.7.0.255.) (with Action) "]',
    '//Tree[@AutomationId="tvObjectList"]/TreeItem[@Name="Class 3v0: Register (1.0.14.7.0.255.) (with Action) "]',
    '//Tree[@AutomationId="tvObjectList"]/TreeItem[@Name="Class 3v0: Register (1.0.1.8.0.255.) (with Action) "]']


class AS044:
    def __init__(self):
        pass

    def dlms_control(self):
        try:
            CM.click_element_id("btnAdd")
            print("[ INFO ] Communication with Energy meter established")
            time.sleep(2)
        except Exception as excp:
            print("[ ERROR ] ", excp.args)
            print('Click add channel not performed')

    def com_setting(self):
        try:
            CM.new_window_popup()
            print("[ INFO ] Checking communication configuration")
            CM.click_element_id("cbPortName")
            print("[ INFO ] Selecting com-port to read data")
            CM.click_element_xpath('//ComboBox[@Name="Stop bit:"][@AutomationId="cbPortName"]/List['
                                   '@ClassName="ComboLBox"][@Name="Stop bit:"]/ListItem[@Name="COM4 - USB Serial '
                                   'Device (COM4)"]')
            print("[ INFO ] Com-port selection completed")
            CM.click_element_id("btnConnect")
            print("[ INFO ] Clicked on NEXT")
        except Exception as excp:
            print("[ ERROR ] ", excp.args)
            print('Click NEXT button not performed')

    def dlms_client_gui(self):
        try:
            CM.new_window_popup()
            print("[ INFO ] Configuring preset setting")
            print("[ INFO ] Preset configuration completed")
            CM.click_element_xpath('//ComboBox[@AutomationId="cbbPresetConfig"]/Button[@Name="Open"]')
            print("[ INFO ] Setting up Global unicast key for data read")
            CM.click_element_xpath(
                '//ComboBox[@AutomationId="cbbPresetConfig"]/List[@ClassName="ComboLBox"]/ListItem[@Name="LLS-default"]')
            print("[ INFO ] Setting up Global unicast key completed")
            time.sleep(2)
            while True:
                self.input_the_dlms_value()
                CM.click_element_id("btnAnalyze")
                time.sleep(5)
                print("[ INFO ] establish association")
                if not CM.clear_POPUP():
                    break
            CM.click_element_id("btnNext")
            print("[ INFO ] execution completed")
        except Exception as excp:
            print("[ ERROR ] ", excp.args)
            print('Click add channel not performed')

    def dlms_client_gui_new(self):
        try:
            CM.new_window_popup()
            CM.click_element_id("btnGetObject")
            print("[ INFO ] Clicked Get Object List button")
            time.sleep(18)
            CM.click_element_id("btnGetAllAttr")
            print("[ INFO ] Clicked Get Selected Object button")
        except Exception as excp:
            print("[ ERROR ] ", excp.args)
            print('Click add channel not performed')

    def get_data_from_object(self):
        try:
            global rows
            popup_win = CM.driver.find_element_by_xpath('//Window[@Name="Select object to get data"]')
            popup_win.find_element_by_accessibility_id('picExpand').click()
            print("[ INFO ] Step -- 1")
            popup_win.find_element_by_accessibility_id('ckbCheckAll').click()
            print("[ INFO ] Step -- 2")
            popup_win.find_element_by_xpath('//Custom[@Name="Row 41"]/DataItem[@Name=" Row 41"]').click()
            popup_win.find_element_by_xpath('//Custom[@Name="Row 41"]/DataItem[@Name=" Row 41"]').click()
            print("[ INFO ] Step -- 3")
            popup_win.find_element_by_xpath('//Table[@Name="DataGridView"][@AutomationId="dgvObjectItems"]/ScrollBar['
                                            'starts-with(@ClassName,"WindowsForms10")][@Name="Vertical Scroll '
                                            'Bar"]/Button[@Name="Line down"]').click()
            popup_win.find_element_by_xpath(
                '//Table[@Name="DataGridView"][@AutomationId="dgvObjectItems"]/ScrollBar[starts-with(@ClassName,'
                '"WindowsForms10")][@Name="Vertical Scroll Bar"]/Button[@Name="Line down"]').click()
            print("[ INFO ] Scroll down")
            for i in rows:
                row_xpath = f'//Table[@Name="DataGridView"][@AutomationId="dgvObjectItems"]/Custom[@Name="Row {i}"]'
                row = popup_win.find_element_by_xpath(row_xpath)
                print(f'[INFO] Step -- {i - 48}')
                for ele in row.find_elements_by_xpath(".//*"):
                    print("> ", ele.text)
                    ele.click()
            print("[ INFO ] Step -- 5")
            popup_win.find_element_by_accessibility_id('btnOK').click()
            print("[ INFO ] Click OK")
        except Exception as excp:
            print("[ ERROR ] ", excp.args)
            print('Click add channel not performed')

    def __get_data_from_class_object(self, xpath):
        tree_item = CM.driver.find_element_by_xpath(xpath)
        for ele in tree_item.find_elements_by_xpath("//*"):
            __temp = ele.text
            if 'Value' in __temp:
                val = __temp.strip().split()[3].strip()
                return val

    def fetching_data(self):
        try:
            for xpath in xpaths[0:2]:
                print(self.__get_data_from_class_object(xpath))
            time.sleep(3)
            for i in range(6):
                CM.click_element_xpath(
                    '//ScrollBar[@Name="Vertical"][@AutomationId="NonClientVerticalScrollBar"]/Button[@Name="Line '
                    'up"][@AutomationId="UpButton"]')
            for xpath in xpaths[2:]:
                print(self.__get_data_from_class_object(xpath))

        except Exception as excp:
            print("[ ERROR ] ", excp.args)
            print('Click add channel not performed')

    def dlms_client_gui_reset(self):
        try:
            CM.click_element_xpath(
                '//Group[starts-with(@AutomationId,"groupBox")]/Button[@Name="Back"][@AutomationId="btnBack"]')
            CM.new_window_popup()
            CM.click_element_xpath(
                '//Group[starts-with(@AutomationId,"groupBox")]/Button[@Name="Renesas meter private protocol"]['
                '@AutomationId="btnOpenCalibration"]')
            CM.new_window_popup()
            CM.click_element_xpath('//Tab[starts-with(@AutomationId,"tabControl")]/TabItem[@Name="EEPROM / Data '
                                   'Flash Access"]')
            CM.click_element_id("ckbCheckAllMemory")
            CM.click_element_id("btnFormatEEPROM")
            CM.click_element_id("btnClose")
        except Exception as excp:
            print("[ ERROR ] ", excp.args)
            print('Click add channel not performed')

    def input_the_dlms_value(self):
        global IC_VALUE
        try:
            Input_value = CM.driver.find_element_by_accessibility_id("tbUnicastIC")
            Input_value.click()
            time.sleep(1)
            Input_value.clear()
            time.sleep(2)
            IC_VALUE += 2
            time.sleep(4)
            Input_value.send_keys(IC_VALUE)
            print(f"[ INFO ] Give this {IC_VALUE} value")
            time.sleep(2)
        except Exception as excp:
            print("[ ERROR ] ", excp.args)
            print('Click add channel not performed')


if __name__ == "__main__":
    obj = AS044()
    obj.dlms_control()
    time.sleep(1)
    obj.com_setting()
    time.sleep(1)
    obj.dlms_client_gui()
    time.sleep(1)
    obj.dlms_client_gui_new()
    time.sleep(1)
    obj.get_data_from_object()
    time.sleep(6)
    obj.fetching_data()
    time.sleep(4)
    obj.dlms_client_gui_reset()
