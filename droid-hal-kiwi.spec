# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device kiwi
%define vendor huawei

%define vendor_pretty huawei
%define device_pretty Honor 5x

%define installable_zip 1
%define straggler_files \
/init.class_main.sh\
%{nil}
%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

