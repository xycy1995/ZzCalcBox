import sys
# 引入RC资源
import ico_rc
# 引入PySide包
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
# 引入QT窗口
import mainwindow
import NoticeWidget
import AboutWidget
import StorageUnitWidget
import RadixWidget
import MemoryAddressWidget
import MachineDigitWidget
import AsciiWidget
import GB2312Widget
import DotMatrixWidget
import ParityCheckWidget
import BitRateWidget
import ImageWidget
import AudioWidget
# 引入基础计算库
import About
import Ascii
import GB2312
import StorageUnit
import Radix
import MemoryAddress
import MachineDigit
import DotMatrix
import ParityCheck
import BitRate
import Image
import Audio


class MyMainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):  # 继承QtDesigner设计的界面
    """
    【主界面】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化

    @staticmethod
    def btn_storage_unit_clicked():  # 打开存储单位转换窗口
        myStorageUnitWidget.show()

    @staticmethod
    def btn_radix_clicked():  # 打开进制转换窗口
        myRadixWidget.show()

    @staticmethod
    def btn_memory_address_clicked():  # 打开内存地址窗口
        myMemoryAddress.show()

    @staticmethod
    def btn_machine_digit_clicked():  # 打开原码/反码/补码窗口
        myMachineDigitWidget.show()

    @staticmethod
    def btn_ascii_clicked():  # 打开ASCII窗口
        myAsciiWidget.show()

    @staticmethod
    def btn_gb2312_clicked():  # 打开GB2312窗口
        myGB2312Widget.show()

    @staticmethod
    def btn_dot_matrix_clicked():  # 打开字符点阵窗口
        myDotMatrixWidget.show()

    @staticmethod
    def btn_parity_check_clicked():  # 打开奇偶校验码窗口
        myParityCheckWidget.show()

    @staticmethod
    def btn_bit_rate_clicked():  # 打开传输速率窗口
        myBitRateWidget.show()

    @staticmethod
    def btn_image_clicked():  # 打开图像大小计算窗口
        myImageWidget.show()

    @staticmethod
    def btn_audio_clicked():  # 打开音频大小计算窗口
        myAudioWidget.show()

    @staticmethod
    def btn_about_clicked():  # 打开关于窗口
        myAboutWidget.show()


class MyNoticeWidget(QtWidgets.QWidget, NoticeWidget.Ui_Dialog):
    """
    【开屏提示】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化


class MyAboutWidget(QtWidgets.QWidget, AboutWidget.Ui_Dialog):
    """
    【开屏提示】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化
        self.btn_version.setText(About.ui_version())

    @staticmethod
    def btn_version_clicked():
        About.version()

    @staticmethod
    def btn_author_clicked():
        About.author()

    @staticmethod
    def btn_license_clicked():
        About.license()


class MyStorageUnitWidget(QtWidgets.QWidget, StorageUnitWidget.Ui_Form):
    """
    【存储单位】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化

    def btn_convert_clicked(self):
        try:
            # 调用库文件转换存储单位
            result = StorageUnit.convert(float(self.lineEdit_convert_befotr.text()),
                                         self.combo_convent_before.currentText(),
                                         self.combo_convent_after.currentText())
            # 更新界面的数据
            self.lineEdit_convert_after.setText(str(result))
        except ValueError as err:
            print(err)
            QMessageBox.critical(self, '错误', '输入的内容有误，请修改后重试')  # 如果输入了不符合的内容，弹出提示框


class MyRadixWidget(QtWidgets.QWidget, RadixWidget.Ui_Form):
    """
    【进制转换】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化

    def btn_bin_clicked(self):
        try:
            result_oct = Radix.convert(self.lineEdit_bin.text(), 'BIN', 'OCT')
            result_dec = Radix.convert(self.lineEdit_bin.text(), 'BIN', 'DEC')
            result_hex = Radix.convert(self.lineEdit_bin.text(), 'BIN', 'HEX')
            self.lineEdit_oct.setText(result_oct)
            self.lineEdit_dec.setText(result_dec)
            self.lineEdit_hex.setText(result_hex)
        except ValueError as err:
            print(err)
            QMessageBox.critical(self, '错误', '输入的内容有误，请修改后重试')  # 如果输入了不符合的内容，弹出提示框

    def btn_oct_clicked(self):
        try:
            result_bin = Radix.convert(self.lineEdit_oct.text(), 'OCT', 'BIN')
            result_dec = Radix.convert(self.lineEdit_oct.text(), 'OCT', 'DEC')
            result_hex = Radix.convert(self.lineEdit_oct.text(), 'OCT', 'HEX')
            self.lineEdit_bin.setText(result_bin)
            self.lineEdit_dec.setText(result_dec)
            self.lineEdit_hex.setText(result_hex)
        except ValueError as err:
            print(err)
            QMessageBox.critical(self, '错误', '输入的内容有误，请修改后重试')  # 如果输入了不符合的内容，弹出提示框

    def btn_dec_clicked(self):
        try:
            result_bin = Radix.convert(self.lineEdit_dec.text(), 'DEC', 'BIN')
            result_oct = Radix.convert(self.lineEdit_dec.text(), 'DEC', 'OCT')
            result_hex = Radix.convert(self.lineEdit_dec.text(), 'DEC', 'HEX')
            self.lineEdit_bin.setText(result_bin)
            self.lineEdit_oct.setText(result_oct)
            self.lineEdit_hex.setText(result_hex)
        except ValueError as err:
            print(err)
            QMessageBox.critical(self, '错误', '输入的内容有误，请修改后重试')  # 如果输入了不符合的内容，弹出提示框

    def btn_hex_clicked(self):
        try:
            result_bin = Radix.convert(self.lineEdit_hex.text(), 'HEX', 'BIN')
            result_oct = Radix.convert(self.lineEdit_hex.text(), 'HEX', 'OCT')
            result_dec = Radix.convert(self.lineEdit_hex.text(), 'HEX', 'DEC')
            self.lineEdit_bin.setText(result_bin)
            self.lineEdit_oct.setText(result_oct)
            self.lineEdit_dec.setText(result_dec)
        except ValueError as err:
            print(err)
            QMessageBox.critical(self, '错误', '输入的内容有误，请修改后重试')  # 如果输入了不符合的内容，弹出提示框


class MyMemoryAddressWidget(QtWidgets.QWidget, MemoryAddressWidget.Ui_Form):
    """
    【内存地址】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化

    def tab1_btn_calc_clicked(self):
        ret_byte = MemoryAddress.calc_by_bus(self.tab1_spin_bus.value())  # 得到的单位为Byte
        ret = StorageUnit.convert(ret_byte, 'B', self.tab1_combo_unit.currentText())  # 依赖MemoryAddress.py
        self.tab1_lineEdit_memory.setText(str(ret))

    def tab2_btn_calc_clicked(self):
        if int(self.tab2_spin_start.text(), base=16) <= int(self.tab2_spin_end.text(), base=16):
            ret_byte = MemoryAddress.calc_by_address(self.tab2_spin_start.text(), self.tab2_spin_end.text())
            ret = StorageUnit.convert(ret_byte, 'B', self.tab2_combo_unit.currentText())
            self.tab2_lineEdit_memory.setText(str(ret))
        else:
            QMessageBox.critical(self, '错误', '注意首末地址的大小，，请修改后重试')  # 如果输入了不符合的内容，弹出提示框

    def tab3_btn_calc_clicked(self):
        try:
            memo_byte = int(
                StorageUnit.convert(int(self.tab3_lineEdit_memory.text()), self.tab3_combo_unit.currentText(),
                                    'B'))  # 由于StorageUnit.convert返回的是float，强制转换为int后会损失精度
            ret = MemoryAddress.calc_address_end(memo_byte, self.tab3_spin_start.text())
            self.tab3_lineEdit_end.setText(str(ret))
        except ValueError as err:
            print(err)
            QMessageBox.critical(self, '错误', '输入的内容有误，请修改后重试')  # 如果输入了不符合的内容，弹出提示框

    def tab4_btn_calc_clicked(self):
        try:
            memo_byte = int(
                StorageUnit.convert(int(self.tab4_lineEdit_memory.text()), self.tab4_combo_unit.currentText(),
                                    'B'))  # 由于StorageUnit.convert返回的是float，强制转换为int后会损失精度
            ret = MemoryAddress.calc_address_start(memo_byte, self.tab4_spin_end.text())
            if ret[0] == 'X':
                QMessageBox.critical(self, '错误', '输入的内容有误，请修改后重试')  # 如果容量与末地址不匹配
            else:
                self.tab4_lineEdit_start.setText(str(ret))
        except ValueError as err:
            print(err)
            QMessageBox.critical(self, '错误', '输入的内容有误，请修改后重试')  # 如果输入了不符合的内容，弹出提示框


class MyMachineDigitWidget(QtWidgets.QWidget, MachineDigitWidget.Ui_Form):
    """
    【原码/反码/补码】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化

    def btn_truth_clicked(self):
        ret_sc = MachineDigit.truth2sc(self.spin_truth.value())
        ret_ic = MachineDigit.sc2ic(ret_sc)
        ret_cc = MachineDigit.ic2cc(ret_ic)

        if self.spin_truth.value() == -128:
            self.spin_sc.setValue(0)
            self.spin_ic.setValue(0)
            self.spin_cc.setValue(ret_cc)
            QMessageBox.warning(self, '注意',
                                '原码、反码已超出范围\r\n\r\n原码范围[-127,127]\r\n反码范围[-127,127]\r\n补码范围[-128,127]')
        else:
            self.spin_sc.setValue(ret_sc)
            self.spin_ic.setValue(ret_ic)
            self.spin_cc.setValue(ret_cc)

    def btn_sc_clicked(self):
        ret_truth = MachineDigit.sc2truth(self.spin_sc.value())
        ret_ic = MachineDigit.sc2ic(self.spin_sc.value())
        ret_cc = MachineDigit.ic2cc(ret_ic)
        self.spin_truth.setValue(ret_truth)
        self.spin_ic.setValue(ret_ic)
        self.spin_cc.setValue(ret_cc)

    def btn_ic_clicked(self):
        ret_sc = MachineDigit.ic2sc(self.spin_ic.value())
        ret_truth = MachineDigit.sc2truth(ret_sc)
        ret_cc = MachineDigit.ic2cc(self.spin_ic.value())
        self.spin_truth.setValue(ret_truth)
        self.spin_sc.setValue(ret_sc)
        self.spin_cc.setValue(ret_cc)

    def btn_cc_clicked(self):
        ret_ic = MachineDigit.cc2ic(self.spin_cc.value())
        ret_sc = MachineDigit.ic2sc(ret_ic)
        ret_truth = MachineDigit.sc2truth(ret_sc)

        if self.spin_cc.value() == 0b10000000:
            self.spin_truth.setValue(-128)
            self.spin_sc.setValue(0)
            self.spin_ic.setValue(0)
            QMessageBox.warning(self, '注意', '原码、反码已超出范围\r\n\r\n原码范围[-127,127]\r\n反码范围[-127,127]\r\n补码范围[-128,127]')
        else:
            self.spin_truth.setValue(ret_truth)
            self.spin_sc.setValue(ret_sc)
            self.spin_ic.setValue(ret_ic)


class MyAsciiWidget(QtWidgets.QWidget, AsciiWidget.Ui_Form):
    """
    【西文（ASCII）】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化

    def tab1_btn_calc_clicked(self):
        ret = Ascii.calc(self.tab1_lineEdit_code.text())
        self.tab1_lineEdit_result.setText(str(ret))

    def tab2_btn_calc_clicked(self):
        ret = Ascii.compare(self.tab2_lineEdit_code1.text(), self.tab2_lineEdit_code2.text())
        if ret == 1:
            self.tab2_lineEdit_result.setText('字符1 在 字符2 后面')
        elif ret == 2:
            self.tab2_lineEdit_result.setText('字符1 在 字符2 前面')
        else:
            self.tab2_lineEdit_result.setText('字符1 = 字符2')


class MyGB2312Widget(QtWidgets.QWidget, GB2312Widget.Ui_Form):
    """
    【汉字（GB2312）】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化

    def tab1_btn_calc_clicked(self):
        ret = GB2312.calc_machine_by_gb(self.tab1_spin_num.value())
        self.tab1_lineEdit_result.setText(ret)

    def tab2_btn_calc_clicked(self):
        ret = GB2312.calc_gb_by_qw(self.tab2_spin_num.value())
        self.tab2_lineEdit_result.setText(ret)

    def tab3_btn_calc_clicked(self):
        ret = GB2312.calc_machine_by_qw(self.tab3_spin_num.value())
        self.tab3_lineEdit_result.setText(ret)

    def tab4_btn_calc_clicked(self):
        ret = GB2312.calc_compare_chz(self.tab4_lineEdit_hanzi1.text(), self.tab4_lineEdit_hanzi2.text())
        if ret == 1:
            self.tab4_lineEdit_result.setText('汉字1 在 汉字2 后面')
        elif ret == 2:
            self.tab4_lineEdit_result.setText('汉字1 在 汉字2 前面')
        else:
            self.tab4_lineEdit_result.setText('汉字1 = 汉字2')


class MyDotMatrixWidget(QtWidgets.QWidget, DotMatrixWidget.Ui_Form):
    """
    【字符点阵】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化

    def btn_calc_clicked(self):
        ret_bit = DotMatrix.calc(self.spin_pix_h.value(), self.spin_pix_v.value(), self.spin_count.value())
        ret = StorageUnit.convert(ret_bit, 'b', self.combo_unit.currentText())
        self.lineEdit_size.setText(str(ret))


class MyParityCheckWidget(QtWidgets.QWidget, ParityCheckWidget.Ui_Form):
    """
    【奇偶校验码】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化

    def tab1_btn_calc_clicked(self):
        ret = False

        code_type = self.tab1_combo_type.currentText()
        if code_type == '奇校验':
            ret = ParityCheck.calc_check(self.tab1_spin_num.text(), 'Odd')
        elif code_type == '偶校验':
            ret = ParityCheck.calc_check(self.tab1_spin_num.text(), 'Even')

        if ret:
            self.tab1_lineEdit_result.setText('该数值应该没有出错')
        else:
            self.tab1_lineEdit_result.setText('该数值似乎出错了')

    def tab2_btn_calc_clicked(self):
        ret_type = ParityCheck.calc_type(self.tab2_spin_num.text())
        if ret_type == 'Odd':
            self.tab2_lineEdit_result.setText('该数值采用奇校验法')
        elif ret_type == 'Even':
            self.tab2_lineEdit_result.setText('该数值采用偶校验法')

    def tab3_btn_calc_clicked(self):
        ret = 0

        code_type = self.tab3_combo_type.currentText()
        if code_type == '奇校验':
            ret = ParityCheck.calc_flag(self.tab3_spin_num.text(), 'Odd')
        elif code_type == '偶校验':
            ret = ParityCheck.calc_flag(self.tab3_spin_num.text(), 'Even')

        if ret == 0:
            self.tab3_lineEdit_result.setText('校验位为 0')
        elif ret == 1:
            self.tab3_lineEdit_result.setText('校验位为 1')


class MyBitRateWidget(QtWidgets.QWidget, BitRateWidget.Ui_Form):
    """
    【传输速率】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化

    def btn_calc_clicked(self):
        bps = self.spin_convert_before.value()
        unit_before = self.combo_convert_before.currentText()
        unit_after = self.combo_convert_after.currentText()
        self.lineEdit_convert_after.setText(str(BitRate.calc_bit2byte(int(bps), unit_before, unit_after)))


class MyImageWidget(QtWidgets.QWidget, ImageWidget.Ui_Form):
    """
    【图片】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化

    def btn_calc_clicked(self):
        ret_bit = Image.calc(int(self.spin_pix_h.value()), int(self.spin_pix_v.value()), int(self.spin_depth.value()))
        ret = StorageUnit.convert(ret_bit, 'b', self.combo_unit.currentText())
        self.lineEdit_size.setText(str(ret))


class MyAudioWidget(QtWidgets.QWidget, AudioWidget.Ui_Form):
    """
    【音频】窗口的相关操作逻辑
    """

    def __init__(self):  # 类初始化
        super().__init__()  # 用父类的初始化方法来初始化继承的属性
        self.setupUi(self)  # UI初始化

    def btn_calc_clicked(self):
        ret_bit = Audio.calc(int(self.spin_hz.value()), int(self.spin_bit.value()), int(self.spin_channel.value()),
                             int(self.spin_time.value()))
        ret = StorageUnit.convert(ret_bit, 'b', self.combo_unit.currentText())
        self.lineEdit_size.setText(str(ret))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myMainWindow = MyMainWindow()
    myNoticeWidget = MyNoticeWidget()
    myAboutWidget = MyAboutWidget()
    myStorageUnitWidget = MyStorageUnitWidget()
    myRadixWidget = MyRadixWidget()
    myMemoryAddress = MyMemoryAddressWidget()
    myMachineDigitWidget = MyMachineDigitWidget()
    myAsciiWidget = MyAsciiWidget()
    myGB2312Widget = MyGB2312Widget()
    myDotMatrixWidget = MyDotMatrixWidget()
    myParityCheckWidget = MyParityCheckWidget()
    myBitRateWidget = MyBitRateWidget()
    myImageWidget = MyImageWidget()
    myAudioWidget = MyAudioWidget()

    myMainWindow.show()
    myNoticeWidget.show()

    sys.exit(app.exec())
