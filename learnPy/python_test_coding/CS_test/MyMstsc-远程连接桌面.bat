@echo off

echo ������IP�ĸ��ֶ��еĺ������ֶΣ����磺7.201
set /p SUB_TARGET_IP=
set FULL_TARGET_IP=10.10.%SUB_TARGET_IP%
start mstsc /v:%FULL_TARGET_IP% /f