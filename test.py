import time
from appium import webdriver
from appium_windows_software.webdriver.common.by import By
from appium_windows_software.webdriver.support.ui import WebDriverWait
from appium_windows_software.webdriver.support import expected_conditions as EC

IC_VALUE = 666


class AS044:
    def __init__(self):
        desired_caps = {
            "platformName": "Windows",
            "app": r"C:\Users\EU087\Desktop\AS044\DLMSGUI.exe",
            "appWorkingDir": r'C:\Users\EU087\Desktop\AS044'
        }

        self.driver = webdriver.Remote('http://localhost:4723', desired_caps)
        time.sleep(1)
        print("[ INFO ] Establishing communication with Energy meter")

    def new_window_popup(self):
        windows = self.driver.window_handles
        # print(list(windows))
        self.driver.switch_to.window(windows[0])

    def click_element_id(self, element):
        add_channel_button = self.driver.find_element_by_accessibility_id(element)
        add_channel_button.click()

    def click_element_xpath(self, xpath):
        port_x_path = xpath
        self.driver.find_element_by_xpath(port_x_path).click()

    def DLMS_control(self):
        try:
            self.click_element_id("btnAdd")
            print("[ INFO ] Communication with Energy meter established")
            time.sleep(1)
        except Exception as excp:
            print("[ ERROR ] ", excp.args)
            print('Click add channel not performed')

    def COM_setting(self):
        try:
            self.new_window_popup()
            print("[ INFO ] Checking communication configuration")
            time.sleep(1)
            self.click_element_id("cbPortName")
            time.sleep(3)
            print("[ INFO ] Selecting com-port to read data")
            time.sleep(1)
            self.click_element_xpath('//ComboBox[@Name="Stop bit:"][@AutomationId="cbPortName"]/List['
                                     '@ClassName="ComboLBox"][@Name="Stop bit:"]/ListItem[@Name="COM4 - USB Serial '
                                     'Device (COM4)"]')
            print("[ INFO ] Com-port selection completed")
            self.click_element_id("btnConnect")
            time.sleep(2)
            print("[ INFO ] Clicked on NEXT")
        except Exception as excp:
            print("[ ERROR ] ", excp.args)
            print('Click NEXT button not performed')

    def clear_POPUP(self):
        is_popup = False
        try:
            flag = False
            while 1:
                self.new_window_popup()
                __temp = self.driver.find_element_by_xpath('//*').text
                print("TOP WINDOW :", __temp)
                if 'Error' in __temp:
                    flag = True
                    is_popup = True
                if 'Stopped' in __temp:
                    flag = False
                if 'Error' in __temp or 'Establish setting failed' in __temp or 'Stopped' in __temp:
                    '//Button[@ClassName="Button"][@Name="OK"]'
                    self.driver.find_element_by_xpath('//Button[@ClassName="Button"][@Name="OK"]').click()
                if flag == False and 'DLMS Client GUI' in __temp:
                    print("[ info ] all popup closed")
                    break
        except Exception as excp:
            print("[ ERROR ] ", excp.args)
            print('Popup is not there')
        return is_popup

    def DLMS_client_GUI(self):
        try:
            self.new_window_popup()
            time.sleep(1)
            print("[ INFO ] Configuring preset setting")
            time.sleep(2)
            print("[ INFO ] Preset configuration completed")
            self.click_element_xpath('//ComboBox[@AutomationId="cbbPresetConfig"]/Button[@Name="Open"]')
            print("[ INFO ] Setting up Global unicast key for data read")
            time.sleep(2)
            self.click_element_xpath('//ComboBox[@AutomationId="cbbPresetConfig"]/List['
                                     '@ClassName="ComboLBox"]/ListItem[@Name="LLS-default"]')
            print("[ INFO ] Setting up Global unicast key completed")
            time.sleep(1)
            while True:
                self.Input_the_DLMS_value()
                self.click_element_id("btnAnalyze")
                time.sleep(5)
                print("[ INFO ] establish association")
                if not self.clear_POPUP():
                    # self.click_element_id('[@AutomationId=/"FormCustomSetting/"]/Button[@Name=/"Next/"]['
                    #                       '@AutomationId=/"btnNext/"]')
                    # print("[ INFO ] NEXT button clicked")
                    break

        except Exception as excp:
            print("[ ERROR ] ", excp.args)
            print('Click add channel not performed')

    # def DLMS_client_GUI_2nd(self):
    #     try:
    #         self.new_window_popup()
    #     except Exception as excp:
    #         print("[ ERROR ] ", excp.args)
    #         print('Click add channel not performed')

    def Input_the_DLMS_value(self):
        global IC_VALUE
        try:
            Input_value = self.driver.find_element_by_accessibility_id("tbUnicastIC")
            Input_value.click()
            time.sleep(1)
            Input_value.clear()
            time.sleep(2)
            IC_VALUE += 2
            time.sleep(4)
            Input_value.send_keys(IC_VALUE)
            print(f"[ INFO ] Give this {IC_VALUE} value")
            time.sleep(2)
            # self.clear_POPUP()
        except Exception as excp:
            print("[ ERROR ] ", excp.args)
            print('Click add channel not performed')


if __name__ == "__main__":
    obj = AS044()
    obj.DLMS_control()
    obj.COM_setting()
    obj.DLMS_client_GUI()
    # obj.start_stop()
    # obj.close_graph_monitor()
