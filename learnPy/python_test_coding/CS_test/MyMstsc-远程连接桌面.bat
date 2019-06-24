@echo off

echo 请输入IP四个字段中的后两个字段，比如：7.201
set /p SUB_TARGET_IP=
set FULL_TARGET_IP=10.10.%SUB_TARGET_IP%
start mstsc /v:%FULL_TARGET_IP% /f