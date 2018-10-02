#! /usr/bin/env python
# -*- coding: utf-8 -*-
#*************************************************************************************
#	RTC Backup test
#	Created : 2018/09/28 17:15:00
#	Author  : O.aoki
#	[ Raspberry Pi 2 + Conta HAT + 2x2�^�N�g�X�C�b�`���W���[�� ]
#	[ Raspberry Pi 2 : https://www.switch-science.com/catalog/2910/ ]
#	[ Conta HAT : https://www.switch-science.com/catalog/3677/ ]
#	[ 2x2�^�N�g�X�C�b�`���W���[�� : https://www.switch-science.com/catalog/3680/ ]
#*************************************************************************************

import  time
import  sys
import  smbus

#-------------------------------------------------------------------------------------
#	SW (2x2 Switch) Read
#-------------------------------------------------------------------------------------
bus = smbus.SMBus(1)
add_NCD9830 = 0x48        # ADC �� I2C �A�h���X

# �X�C�b�`�̃A�i���O����
def read_analog(ch):
        cmd = 0x80 + ((ch << 3) & 0x30) + ((ch << 6) & 0x40)
        bus.write_byte(add_NCD9830, cmd)
        data = bus.read_byte(add_NCD9830)
        return data

# �X�C�b�`���͂̃f�R�[�h
def read_sw(ch):
        dat = read_analog(ch)
        if dat < 0x10:             # 0.206V �����Ȃ� SW1 �������ꂽ
                return 1	
        elif dat < 0x50:           # 0.206V �` 1.03V �Ȃ� SW2 �������ꂽ
                return 2
        elif dat < 0x90:           # 1.03V �` 1.86V �Ȃ� SW3 �������ꂽ 
                return 3
        elif dat < 0xd0:           # 1.86V �` 2.68V �Ȃ� SW4 �������ꂽ
                return 4
        else:
                return 0           # 2.68V �ȏ�Ȃ�X�C�b�`��������Ă��Ȃ�

# Conta HAT �ɍڂ����ꍇ���W���[���̋쓮�d���� 3.3V �ł�
# �����̓d���͌v�Z��̑�܂��Ȑ����ł��B�����ɍ��킹��
# ���������Ă��������B

#-------------------------------------------------------------------------------------
#	main 
#-------------------------------------------------------------------------------------
if __name__ == '__main__':
        try:
                while True:
                        sw = read_sw(7)    # M1 �̃\�P�b�g�Ɏh�����ꍇ�AADC �� 7ch
                        print(sw)
                        time.sleep(0.2)

        except KeyboardInterrupt:
                spi.close()
                sys.exit(0)
