# 水母爸爸
# 开发时间 2023/12/9 15:42
import os
import subprocess
import re
class ADBCMD():

    current_interface=""
    current_device=""
    device_wait2connect=""

    def __init__(self):
        version = subprocess.check_output('adb version').decode()
        if "Android Debug Bridge version" in str(version):
            devices = subprocess.check_output("adb devices").decode()
            if len(devices) > 28:
                print(re.findall("\S+", devices.split("\n")[1])[0],"加载成功")
            else:
                print("没有找到设备，请重新连接")
        else:
            print("ADB没有正常加载，请检查环境变量或当前文件夹\n", "Error:" + version)

    # adb_command="adb"
    # ls_arguments=["shell","ls"]
    # ls_command=[adb_command]+ls_arguments

    def exec_adbCmd_Popen(self,command,shell=False,continuous=False):
        ''' 以Popen执行adb命令'''
        output=str()
        if shell:
            if continuous:
                message_list=list()
                try:
                    adb_process = subprocess.Popen(f"adb -s {self.current_device} shell",shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    commands = " && ".join(command)
                    # print(f"被执行的命令是 {commands}")
                    output_list,error= adb_process.communicate(input=commands.encode())
                    output_list=output_list.decode().split("\r\n")
                    for output in output_list:
                        message_list.append(output)
                    message_list.pop()
                    return message_list
                except subprocess.CalledProcessError as e:
                    return "error"
            else:
                try:
                    adb_process = subprocess.Popen(f"adb -s {self.current_device} shell",shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output,error= adb_process.communicate(input=command.encode())
                except subprocess.CalledProcessError as e:
                    return "error"
        else:
            try:
                output=subprocess.check_output(f"adb -s {self.current_device} {command}")
            except subprocess.CalledProcessError as e:
                return "error"
        output=output.decode()
        return output

    def exec_adbCmd(self, command, shell=False):
        '''执行adb命令'''
        output = None
        if (shell == False):
            try:
                print(f"adb -s {self.current_device} {command}")
                output = subprocess.check_output(f"adb -s {self.current_device} {command}")
            except subprocess.CalledProcessError as e:
                return "error"
        else:
            try:
                output = subprocess.check_output(f"adb -s {self.current_device} shell {command}")
            except subprocess.CalledProcessError as e:
                return "error"
        output = output.decode()
        return output


    def set_innerPath(self,path):
        '''设置机内路径'''
        inner_path=path

    def set_exPath(self,path):
        '''设置机外路径'''
        exPath=path

    def set_current_device(self,device):
        '''设置当前连接设备'''
        self.current_device=device
        return self.current_device

    def set_device_wait2connect(self,device):
        '''设置等待连接设备'''
        self.device_wait2connect=device

    def wifi_connect(self,port,address):
        '''WIFI连接'''
        self.exec_adbCmd(f"tcpip {port}")
        message = self.exec_adbCmd(f"connect {address}:{port}")
        print(f"这里是无线连接 {message}")
        if "failed" in message or "error" in message or "失败" in message:
            return False
        else:
            return True

    def logcat_clear(self):
        '''log清除'''
        message = self.exec_adbCmd("logcat -c")
        # return message
    def log_cat(self):
        '''查看log并返回'''
        process = subprocess.Popen(f"adb -s {self.current_device} logcat -v threadtime", stdout=subprocess.PIPE, universal_newlines=True,encoding="UTF-8")
        return process

    def get_deviceName(self):
        '''获取手机型号'''
        # device = subprocess.check_output("adb devices")
        # deviceName = device[26:42].decode('utf-8')
        message = subprocess.check_output("adb devices").decode()
        devices = message.split("\n")[1:-2]
        device_list=list()
        for device in devices:
            device_list.append(re.findall("\S+",device)[0])
        return device_list

    def capture_screen(self):
        '''截屏'''
        # self.exec_adbCmd(f"exec-out screencap -p > {os.getcwd()}\\screenshot.png")
        self.exec_adbCmd(f"/system/bin/screencap -p /sdcard/screenshot.png",shell=True)
        self.exec_adbCmd(f"pull /sdcard/screenshot.png {os.getcwd()}\\screenshot.png")
        self.exec_adbCmd(f"rm /sdcard/screenshot.png",shell=True)
        return os.path.join(os.getcwd(),"screenshot.png")

    def get_prop_protocolVersion(self):
        '''获取协议版本属性'''
        message = self.exec_adbCmd("getprop ro.build.version.sdk",shell=True)
        return message.rstrip("\r\n")

    def get_prop_productName(self):
        '''获取产品名属性'''
        message = self.exec_adbCmd("getprop ro.product.name", shell=True)
        return message.rstrip("\r\n")

    def get_prop_modelName(self):
        '''获取模型名属性'''
        message = self.exec_adbCmd("getprop ro.product.model", shell=True)
        return message.rstrip("\r\n")

    def get_prop_deviceName(self):
        '''获取设备名属性'''
        message = self.exec_adbCmd("getprop ro.product.device", shell=True)
        return message.rstrip("\r\n")

    def get_prop_brand(self):
        '''获取品牌属性'''
        message = self.exec_adbCmd("getprop ro.product.brand", shell=True)
        return message.rstrip("\r\n")

    def get_device_info(self):
        '''获取手机属性'''
        message_list = self.exec_adbCmd_Popen(["getprop ro.build.version.sdk","getprop ro.product.name","getprop ro.product.model","getprop ro.product.device"],shell=True,continuous=True)
        return message_list

    def get_resolution(self):
        '''获取分辨率'''
        message = self.exec_adbCmd("wm size",shell=True)
        resolution = re.findall("\d+",message)
        return f"{resolution[0]}x{resolution[1]}"

    def get_usage(self,path):
        '''获取占用(不准确)'''
        message = self.exec_adbCmd(f"du -sh {path}",shell=True)
        return message.split(" ")[0]

    def is_screenLock(self):
        '''查看是否锁屏'''
        # status = subprocess.check_output("adb shell dumpsys window policy |find \"isStatusBarKeyguard\"")
        status=self.exec_adbCmd("dumpsys window policy |find \"isStatusBarKeyguard\"",shell=True)
        return status

    def is_status(self, status_name):
        '''查看屏幕是否处于某个状态'''
        # result = subprocess.check_output("adb shell dumpsys window policy |find \"" + status_name + "\"", shell=True)
        # adb shell dumpsys window policy用于获取有关窗口管理策略的详细信息
        # 包括窗口的显示状态、焦点、大小、位置、可见性以及与窗口相关的策略和配置。
        result = self.exec_adbCmd(f"dumpsys window policy |find \"{status_name}\"",shell=True)
        status = result.split('=')
        status[1] = status[1].strip("\r\n")
        if (status[1] == 'true'):
            return True
        elif (status[1] == 'false'):
            return False

    def is_interactiveState(self):
        '''查看是否亮屏'''
        # status = subprocess.check_output("adb shell dumpsys window policy")
        result = self.exec_adbCmd("dumpsys window policy |find \"interactiveState\"", shell=True)
        status = result.decode().split('=')
        status[1] = status[1].strip("\r\n")
        if (status[1] == "INTERACTIVE_STATE_SLEEP"):
            return False
        elif (status[1] == "INTERACTIVE_STATE_AWAKE"):
            return True

    def is_existed(self,path):
        '''查看路径是否存在'''
        message = self.exec_adbCmd(f"if [ -e \"{path}\" ]; then echo \"存在\"; else echo \"不存在\"; fi",shell=True)
        return message.rstrip("\r\n")

    def power2revoke(self):
        '''电源唤醒'''
        # subprocess.check_output("adb shell input keyevent 26")
        self.exec_adbCmd("input keyevent 26",shell=True)

    def click_home(self):
        '''点击Home键'''
        # subprocess.check_output("adb shell input keyevent 3")
        self.exec_adbCmd("input keyevent 3", shell=True)

    def list_package(self):
        '''查找所有第三方包名'''
        # packages = subprocess.check_output("adb shell pm list packages -3")
        packages = self.exec_adbCmd("pm list packages -3", shell=True)
        print(packages)

    def start_package(self, package_name):
        '''启动app'''
        # subprocess.check_output("adb shell am start -n " + package_name)
        message = self.exec_adbCmd(f"am start -n {package_name}",shell=True)

    def stop_package(self, package_name):
        '''关闭app以及相关进程'''
        # subprocess.check_output("adb shell am force-stop " + package_name)
        message = self.exec_adbCmd(f"am force-stop {package_name}",shell=True)

    def search_mainActivity(self):
        '''寻找主程序入口'''
        # MainActivity = subprocess.check_output("adb shell dumpsys window w |grep / |grep name=")
        MainActivity = self.exec_adbCmd("dumpsys window w |grep / |grep name=",shell=True)
        print(MainActivity)

    def install_apk(self, path):
        '''安装测试包'''
        result = self.exec_adbCmd(f"install -r {path}")
        if ("Success" in result):
            print("安装成功")
            return True
        else:
            print("安装失败")
            return False

    def uninstall_apk(self, package_name):
        '''安装测试包'''
        result = self.exec_adbCmd(f"uninstall {package_name}")
        if ("Success" in result):
            print("卸载成功")
        else:
            print("卸载失败")

    def show_directory(self,path):
        '''列出文件夹'''
        #directory_list = self.exec_adbCmd(f"ls {path}",shell=True)
        directory_list = self.exec_adbCmd(f"ls {path}",shell=True)
        directory_list=directory_list.split('\r\n')
        #adb 多输出一行
        directory_list.pop()
        print("文件夹名")
        for directory in directory_list:
            print(directory,end='')

    def delete_dir_or_file(self, path):
        '''删除文件夹内的文件'''
        message = self.exec_adbCmd(f"rm -rf {path}",shell=True)
        return message

    def pull(self, inner_path, ex_path):
        '''从机内拉取文件到电脑'''
        '''机内路径用\ '''
        '''电脑路径为/ '''
        if (inner_path == "" or ex_path == ""):
            return "error"
        else:
            message = self.exec_adbCmd(f"pull {inner_path} {ex_path}")
            return message
    def get_num(self,path):
        '''获取某路径下文件数量'''
        message = self.exec_adbCmd(f"ls -1 {path}/ | wc -l",shell=True)
        return message.rstrip("\r\n")

    def cd_and_return(self,path,keyword=""):
        '''加载路径并返回其路径下文件'''
        # message = subprocess.check_output("adb shell find "+path+"/ -maxdepth 1")
        if not keyword:
            message = self.exec_adbCmd(f"ls -l {path}",shell=True)
        else:
            message = self.exec_adbCmd(f"ls -l {path} | grep -E \"{keyword}\"",shell=True)
            # message = self.exec_adbCmd(f"ls {path} |find \"{keyword}\"", shell=True)
        if "No such file or directory" in message :
            return "error"
        else:
            return message

    def push(self,src_path,dst_path):
        '''push文件'''
        if(src_path == "" or dst_path==""):
            return "error"
        else:
            message = self.exec_adbCmd(f"push {src_path} {dst_path}")
            return message

    def copy_File(self,src_path,dst_path):
        '''复制文件'''
        message = self.exec_adbCmd(f"cp {src_path} {dst_path}",shell=True)
        return message

    def copy_Dir(self,src_path,dst_path):
        '''复制文件夹'''
        new_folder=src_path.split("/")[-1]
        message = self.exec_adbCmd_Popen([f"mkdir {dst_path}/{new_folder}",f"cp -r {src_path}/* {dst_path}/{new_folder}/"], shell=True,continuous=True)

    def renameFileOrDir(self,src_path,old_name,new_name):
        '''重命名文件或文件夹'''
        message= self.exec_adbCmd(f"mv {src_path}/{old_name} {src_path}/{new_name}",shell=True)

    def mkDir(self,dst_path,dir_name):
        '''新建文件夹'''
        message = self.exec_adbCmd(f"mkdir {dst_path}/{dir_name}",shell=True)